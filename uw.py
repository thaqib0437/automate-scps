import sys
import os

foldername = ''
if(len(sys.argv)<2):
	print("Please Enter COURSE NAME")
	foldername = input("COURSE NAME:")
else:
	foldername = str(sys.argv[1])


#c = """C:\Users\thaqi\Desktop\UW\"""
#os.chdir(c)

path = "Desktop\UW"
os.chdir(path)

print(path)


os.mkdir(foldername)
os.chdir(foldername)
os.mkdir('PSETS')
os.mkdir('Res')
os.mkdir('Vids')
os.mkdir('BOOK')
os.mkdir('IMP')


os.chdir('PSETS')

os.mkdir('Written')
os.mkdir('Electronic')


os.chdir('..')
os.system('explorer.exe .')
