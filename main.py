import tkinter as tk
from tkinter import filedialog
import os
import subprocess


video_ext = ["mp4", "mkv", "avi"]
sub_ext = ["srt", "ass", "txt", "ssa", "sub"]
mkvmerge_path = "C:\\Program Files\\MKVToolNix\\mkvmerge.exe"

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()
os.chdir(file_path)
my_files = os.listdir(file_path)

video_file = []
sub_file = []
for file in my_files :
	ext = file[-3:]
	name = file[:-4]

	if ext in video_ext :
		video_file.append([name, ext])
	elif ext in sub_ext :
		sub_file.append([name, ext])


#"B:\OneDrive\Portable applications\mkvtoolnix\mkvmerge.exe" -o "remux-%%~nxA" "%%~A" --forced-track "0:yes" --default-track "0:yes" --track-name "0:English" --language "0:eng" "%%~nA.srt" )

for vid in video_file :
	for sub in sub_file :
		if vid[0] == sub[0] :
			original_file = vid[0]+"."+vid[1]
			dest_file_path = "New_"+ original_file
			full_sub_name = sub[0]+"."+sub[1]

			returncode = subprocess.run(mkvmerge_path +' -o "'+ dest_file_path +'" "'+ original_file +'" --forced-track "0:yes" --default-track "0:yes" --track-name "0:Arabic" --language "0:ara" "'+ full_sub_name +'"')
