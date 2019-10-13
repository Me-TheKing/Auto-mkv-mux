import sys
import os
import os.path
from os import path
import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QApplication, QMessageBox
from UI.maingui import Ui_Form  # importing our generated file


class External(QThread):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(str)
    signal_cmd = list()

    def run(self):
        #print(self.signal_cmd)
        #########################################
        #########################################
        for cmd in self.signal_cmd :
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, text = True)
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    #self.ui.output_PTE.appendPlainText(output.strip())
                    self.countChanged.emit(output.strip())

        #self.complete_dialog(vidsub_lst)

class MyApp(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        ##### my set var ####        
        self.video_ext = ["mp4", "mkv", "avi"]
        self.sub_ext = ["srt", "ass", "txt", "ssa", "sub"]
        self.mkvmerge_path = "C:\\Program Files\\MKVToolNix\\mkvmerge.exe"

        self.btn_handler()

    def btn_handler(self):
        self.ui.search_btn.clicked.connect(self.btnClicked)
        self.ui.start_btn.clicked.connect(self.start_mux)
        self.ui.search_output_btn.clicked.connect(self.out_btnClicked)

    def out_btnClicked(self):
        try:
            out_path = str(QFileDialog.getExistingDirectory(self, "Select Directory", options=QFileDialog.DontUseNativeDialog))
            self.ui.output_path_LE.setText(out_path)
        except OSError:
            pass

    def btnClicked(self):
        try:
            file_path = str(QFileDialog.getExistingDirectory(self, "Select Directory", options=QFileDialog.DontUseNativeDialog))
            self.ui.folder_path_LE.setText(file_path)
            self.ui.output_PTE.setPlainText("")
            os.chdir(file_path)            
            self.ui.start_btn.setEnabled(True)
            self.ui.search_output_btn.setEnabled(True)
            self.ui.output_path_LE.setEnabled(True)
        except OSError:
           pass

    def vid_sub_list(self, my_files):
        videos = []        
        subs = []        
        for a_file in my_files:
            ext = a_file[-3:]

            if ext in self.video_ext:
                videos.append(a_file)
            elif ext in self.sub_ext:
                subs.append(a_file)

        # see if there is a sub file match the name of a video file 
        # and then set a list with the video name and there sub(s) in 2D list
        vidsub_lst = []        
        for vid in videos:
            subs_for_vid = []
            subs_for_vid.append(vid)
            for sub in subs:
                if vid.split(".")[0] == sub.split(".")[0]:
                    subs_for_vid.append(sub)
            # check if the video has any sub(s)
            if len(subs_for_vid) > 1 :
                vidsub_lst.append(subs_for_vid)
            else:
                print("no sub for this video!")
        
        return (vidsub_lst)

    def start_mux(self):
        self.ui.output_PTE.setPlainText("")       
        # read the options from the Ui_Form or ui
        option_forced_track = str(self.ui.forced_cbox.currentText())
        option_default_track = str(self.ui.default_cbox.currentText())
        option_track_name = str(self.ui.name_LE.text())
        option_language = str(self.ui.language_cbox.currentText())
        option_delay = str(self.ui.delay_LE.text())        

        # the output folder
        dest_vid_path = self.output_directory()
        
        # get the name of the video(s) and sub(s)
        my_current_dic = os.getcwd()
        my_files = os.listdir(my_current_dic)
        # get a list for a video and it related sub(s) [[vid01,sub01a,sub01.b,...], [vid02,,sub02.a,sub02.b,...]]
        vidsub_lst = self.vid_sub_list(my_files)
        ###################################################################################
        ####   here start the main mux LOOP by making the vid_name and it's sub_name   ####
        ###################################################################################
        # select the sub(s) name for every video and but it in one lst
        cmds = []
        for a_vidsub in vidsub_lst:
            # set the name of "vid_name" and make a list of it sub(s) name
            vid_name, *subs_vid_lst = a_vidsub             
            # use the sub(s) name in subs_vid_lst and make a one singel name "sub_name" to use in the subprocess
            ##############################            
            sub_name = []
            for a_sub in subs_vid_lst :
                sub_name = self.sub_name_lst(a_sub, sub_name, option_language)

            sub_name = " ".join(sub_name)
            full_dest_vid_path = self.add_quote(dest_vid_path + vid_name)
            vid_name = self.add_quote(vid_name)            
            ####### new change 03:49am 09-10-2019 ######
            option_code = f"--forced-track 0:{option_forced_track} --default-track 0:{option_default_track} --track-name 0:{option_track_name} --sync 0:{option_delay}"

            cmds.append(f"{self.mkvmerge_path} -o {full_dest_vid_path} {vid_name} {option_code} {sub_name}")
        print(cmds)
        self.calc = External()
        #self.calc.countChanged.connect(lambda: self.onCountChanged(cmd))
        self.calc.signal_cmd = cmds
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

        #self.calc.wait()
        #returncode = subprocess.Popen(f"{self.mkvmerge_path} -o {full_dest_vid_path} {vid_name} {option_code} {sub_name}")
        #returncode = subprocess.Popen('"'+self.mkvmerge_path +'" -o "'+ full_dest_vid_path +'" "' + vid_name + option_code + sub_name, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, shell=True)
        ############################################
        # the index 0 is to read only the stdout info
        #stdout_value = returncode.communicate()[0]
        #print(returncode.stdout)
        #self.ui.output_PTE.appendPlainText("vidsub_lst len :" + str(len(vidsub_lst)))
        #self.ui.output_PTE.appendPlainText(stdout_value)
        #QApplication.processEvents()

        #self.complete_dialog(vidsub_lst)

    def onCountChanged(self, value):
        self.ui.output_PTE.appendPlainText(value)

    def add_quote(self, str_name):
        return f'"{str_name}"'

    def sub_name_lst(self, a_sub, sub_name, option_language):
        # see why the add_quote not working with a_sub????
        #self.add_quote(a_sub)
        a_sub_split = a_sub.split(".")                
        # name.ext OR name.order.ext          
        if len(a_sub_split) in (2, 3):
            sub_name.append(f'--language 0:{option_language} "{a_sub}"')
        # name.order.team.ext
        elif len(a_sub_split) == 4 :
            sub_name.append(f'--language 0:{option_language} --track-name 0:{a_sub_split[2]} "{a_sub}"')
        # name.order.team.delay.ext
        elif len(a_sub_split) == 5:
            sync_val = 0 if a_sub_split[3]== "" else sync_val == a_sub_split[3]
            sub_name.append(f'--track-name 0:{a_sub_split[2]} --sync 0:{sync_val} "{a_sub}"')
        # name.order.team.delay.lang.ext
        elif len(a_sub_split) == 6:
            sync_val = 0 if a_sub_split[3]== "" else sync_val == a_sub_split[3]
            sub_name.append(f'--language 0:{a_sub_split[4].lower()} --track-name 0:{a_sub_split[2]} --sync 0:{sync_val} "{a_sub}"')

        return sub_name

    def output_directory(self):
        # set the output Folder        
        if len(self.ui.output_path_LE.text()) == 0:
            try:
                os.makedirs("Done")
            except FileExistsError:
                # directory already exists
                # i need a massageBox warrning
                pass

            output_path = "Done/"
        else:
            if path.isdir(self.ui.output_path_LE.text()):
                output_path = self.ui.output_path_LE.text() + "/"
            else:
                self.showdialog()
                return

        return output_path

    def showdialog(self):        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText("You have Entered a wrong Path!")
        msg.setInformativeText("your path: " + self.ui.output_path_LE.text())
        msg.setWindowTitle("Path directory Error")
        msg.setDetailedText("Please check your Path Folder again. and for Better Result use the Search button.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)

        msg.exec_()

    def complete_dialog(self, total_vid_lst):        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet("QLabel{min-width: 200px;}")

        msg.setText("Tha Mux Has Completed.")
        msg.setInformativeText(f"You Have Mux {len(total_vid_lst)} mkv file.")
        msg.setWindowTitle("Complete Massage")
        video_names = "\n".join(t[0] for t in total_vid_lst)
        msg.setDetailedText(video_names)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)

        msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
