import sys
import os
import os.path
from os import path
import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication, QMessageBox
from UI.maingui import Ui_Form  # importing our generated file


class MyApp(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        ##### my Set Var ####        
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
            os.chdir(file_path)
            my_files = os.listdir(file_path)
            self.vid_sub_list(my_files)
            self.ui.start_btn.setEnabled(True)
            self.ui.search_output_btn.setEnabled(True)
            self.ui.output_path_LE.setEnabled(True)
        except OSError:
           pass

    def vid_sub_list(self, my_files):
        self.video_file = []
        self.sub_file = []        
        for a_file in my_files:
            split_name = a_file.split(".")
            # name.ext
            if len(split_name) == 2 :                
                ext = split_name[1]
            # name.order.ext
            elif len(split_name) == 3 :               
                ext = split_name[2]
            # name.order.team.ext
            elif len(split_name) == 4:                
                ext = split_name[3]
            # name.order.team.lang.ext
            elif len(split_name) == 5 :
                ext = split_name[4]
            else:
                # it is no file or file with no ext
                ext = None

            if ext in self.video_ext:
                self.video_file.append(a_file)
            elif ext in self.sub_ext:
                self.sub_file.append(a_file)

    def start_mux(self):
        # read the options from the Ui_Form or ui
        option_forced_track = str(self.ui.forced_cbox.currentText())
        option_default_track = str(self.ui.default_cbox.currentText())
        option_track_name = str(self.ui.name_LE.text())
        option_language = str(self.ui.language_cbox.currentText())
        option_delay = str(self.ui.delay_LE.text())
        
        # set the output Folder        
        if len(self.ui.output_path_LE.text()) == 0:
            try:
                os.makedirs("Done")
            except FileExistsError:
                # directory already exists
                # i need a massageBox warrning
                pass
            dest_vid_path = "Done/"
        else:
            if path.isdir(self.ui.output_path_LE.text()):
                dest_vid_path = self.ui.output_path_LE.text() + "/"
            else:
                self.showdialog()
                return

        # set video with there subs in 2D list
        vidsub_lst = []        
        for vid in self.video_file:
            subs_for_vid = []
            subs_for_vid.append(vid)
            for sub in self.sub_file:
                if vid.split(".")[0] == sub.split(".")[0]:
                    subs_for_vid.append(sub)
            # check if the video has any sub(s)
            if len(subs_for_vid) > 1 :
                vidsub_lst.append(subs_for_vid)
            else:
                print("no sub for this video!")      
        ###################################################################################
        ####   here start the main mux LOOP by making the vid_name and it's sub_name   ####
        ###################################################################################
        # select the sub(s) name for every video and but it in one lst 
        for a_vidsub in vidsub_lst:
            subs_vid_lst  = []
            for i in range(len(a_vidsub)-1) :
                subs_vid_lst.append(a_vidsub[i+1])
            
            # maybe i will call a func 
            # use the sub(s) name in subs_vid_lst and make a one singel name to use in the subprocess
            ##############################            
            sub_name = ""
            for a_sub in subs_vid_lst :
                a_sub_split = a_sub.split(".") 
                # name.ext               
                if len(a_sub_split) == 2 :
                    sub_name = '"'+a_sub+'"'
                # name.order.ext
                elif len(a_sub_split) == 3 :
                    if len(sub_name) == 0 :
                        sub_name = '--language "0:'+option_language+'" "'+a_sub+'"'
                    else:
                        sub_name = sub_name +" "+ ' --language "0:'+option_language+'" "'+a_sub+'"'
                # name.order.team.ext
                elif len(a_sub_split) == 4 :
                    if len(sub_name) == 0 :
                        sub_name = '--language "0:'+option_language+'" --track-name "0:'+a_sub_split[2]+'" "'+a_sub+'"'
                    else:
                        sub_name = sub_name +" "+ ' --language "0:'+option_language+'" --track-name "0:'+a_sub_split[2]+'" "'+a_sub+'"'
                # name.order.team.lang.ext
                elif len(a_sub_split) == 5 :
                    if len(sub_name) == 0 :
                        sub_name = '--language "0:'+a_sub_split[3].lower()+'" --track-name "0:'+a_sub_split[2]+'" "'+a_sub+'"'
                    else:
                        sub_name = sub_name +" "+ ' --language "0:'+a_sub_split[3].lower()+'" --track-name "0:'+a_sub_split[2]+'" "'+a_sub+'"'
           
            vid_name = a_vidsub [0]
            full_dest_vid_path = dest_vid_path + vid_name            
            ####### new change 03:49am 09-10-2019 ######
            if len(subs_vid_lst) == 1 :
                option_code = '" --forced-track "0:'+option_forced_track+'" --default-track "0:'+option_default_track+'" --track-name "0:'+option_track_name+'" --language "0:'+option_language+'" --sync "0:'+option_delay+'" '
            else:
                option_code = '" --forced-track "0:'+option_forced_track+'" --default-track "0:'+option_default_track+'" --track-name "0:'+option_track_name+'" --sync "0:'+option_delay+'" '
            print(self.mkvmerge_path +' -o "'+ full_dest_vid_path +'" "' + vid_name + option_code + sub_name)
            returncode = subprocess.Popen(self.mkvmerge_path +' -o "'+ full_dest_vid_path +'" "' + vid_name + option_code + sub_name, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            ############################################            
            # the index 0 is to read only the stdout info
            stdout_value = returncode.communicate()[0]
            self.ui.output_PTE.setPlainText(
                "vidsub_lst len :" + str(len(vidsub_lst)))
            self.ui.output_PTE.setPlainText(stdout_value)
            QApplication.processEvents()

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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
