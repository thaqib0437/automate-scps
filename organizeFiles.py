import sys
import shutil
import os

from os import listdir
from os.path import isfile, join



def ogn(path):
    try:
        os.chdir(path)
        print(os.getcwd())
    except OSError:
        print('invalid path')
    folder_dict = {
	"IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
			".heif", ".psd"],
	"VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
			".qt", ".mpg", ".mpeg", ".3gp",".mkv"],
	"DOCUMENTS": [".doc", ".pptx", ".pdf", ".docx", ".doc", ".xla",],
	"AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
			".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
	"PLAINTEXT": [".txt", ".in", ".out"],
	"PDF": [".pdf"],
	"PYTHON": [".py"],
	"XML": [".xml"],
	"EXE": [".exe"]

            }
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(folder_dict.keys())
    
    
ogn("FILE-DIR")
