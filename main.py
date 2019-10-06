from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication
from UI.maingui import Ui_Form  # importing our generated file 
import sys
import os
import subprocess
 
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
        self.ui.search_btn.clicked.connect(self.btnClicked) # connecting the clicked signal with btnClicked slot
        self.ui.start_btn.clicked.connect(self.start_mux)

    def btnClicked(self):
        file_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.lineEdit.setText(file_path)
        os.chdir(file_path)
        my_files = os.listdir(file_path)
        self.vid_sub_list(my_files)
        #self.ui.output_txt.setPlainText(str(self.my_files))

    def vid_sub_list(self, my_files):
        self.video_file = []
        self.sub_file = []
        for file in my_files :
            ext = file[-3:]
            name = file[:-4]

            if ext in self.video_ext :
                self.video_file.append([name, ext])
            elif ext in self.sub_ext :
                self.sub_file.append([name, ext])

    def start_mux(self):
        for vid in self.video_file :
            for sub in self.sub_file :
                if vid[0] == sub[0] :
                    original_file = vid[0]+"."+vid[1]
                    dest_file_path = "New_"+ original_file
                    full_sub_name = sub[0]+"."+sub[1]

                    returncode = subprocess.Popen(self.mkvmerge_path +' -o "'+ dest_file_path +'" "'+ original_file +'" --forced-track "0:yes" --default-track "0:yes" --track-name "0:Arabic" --language "0:ara" "'+ full_sub_name +'"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                    stdout_value = returncode.communicate()[0]                    
                    self.ui.output_txt.setPlainText(stdout_value)
                    QApplication.processEvents()
 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())