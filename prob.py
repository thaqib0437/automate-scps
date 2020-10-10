import sys
import os

foldername = ''
if(len(sys.argv)<2):
	print("Please Enter FNAME")
	foldername = input("Enter FNAME:")
else:
	foldername = str(sys.argv[1])

ide = 'subl'

if(len(sys.argv)>2):
	ide = sys.argv[2]

path = os.getcwd()
os.chdir(path)



text = '''#include <bits/stdc++.h>\n
using namespace std;\n
 
int main() {\n
    //REMOVE THEM BEFORE SUBMISSION
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

// solution comes here\n
}\n'''


try:
	f= open(foldername + ".cpp","w+")
	f.write(text) 
	os.system(ide +' '+ foldername + '.cpp')

except:
	print("create <project_name> l")
