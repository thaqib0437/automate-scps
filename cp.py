import sys
import os

foldername = ''
if(len(sys.argv)<2):
	print("Please Enter FNAME")
	foldername = input("Enter FNAME:")
else:
	foldername = str(sys.argv[1])

ide = 'code'

if(len(sys.argv)>2):
	ide = sys.argv[2]

path = os.getcwd()
os.chdir(path)
os.mkdir(foldername)
os.chdir(foldername)



text = '''#include <bits/stdc++.h>\n
using namespace std;\n
 
int main() {\n
    //REMOVE THEM BEFORE SUBMISSION
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

// solution comes here\n
}\n'''


try:
	f= open(foldername + "_code.cpp","w+")
	f.write(text) 
	f2 = open("input.txt", "w+")
	
	f3 = open("output.txt", "w+")
	
	os.system(ide +' '+ foldername + '_code.cpp')

except:
	print("create <project_name> l")
