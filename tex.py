import sys
import os

foldername = ''
if(len(sys.argv)<2):
	print("Please Enter FNAME")
	foldername = input("Enter FNAME:")
else:
	foldername = str(sys.argv[1])


path = os.getcwd()
os.chdir(path)
os.mkdir(foldername)
os.chdir(foldername)

os.mkdir('figs')


text1 = """
\documentclass[16pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{amsthm}

\usepackage{setspace}
\setstretch{1.7}
\usepackage{graphicx}
\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}

\usepackage{listings}
\usepackage{color}
\definecolor{dkgreen}{rgb}{0,0.6,0}
\definecolor{gray}{rgb}{0.5,0.5,0.5}
\definecolor{mauve}{rgb}{0.58,0,0.82}

\definecolor{deepblue}{rgb}{0,0,0.5}
\definecolor{deepred}{rgb}{0.6,0,0}
\definecolor{deepgreen}{rgb}{0,0.5,0}
\lstset{frame=tb,
  language=python,
  aboveskip=2mm,
  belowskip=2mm,
  showstringspaces=false,
  columns=flexible,
  basicstyle={\linespread{0.9}\small\ttfamily},
  numbers=none,
  numberstyle=\tiny\color{gray},
  keywordstyle=\color{blue},
  commentstyle=\color{dkgreen},
  stringstyle=\color{deepred},
  breaklines=true,
  breakatwhitespace=true,
  tabsize=4
}

\\theoremstyle{definition}
\\newtheorem{definition}{Definition}[section]

\\newtheorem{theorem}{Theorem}[section]
\\newtheorem{corollary}{Corollary}[theorem]
\\newtheorem{lemma}[theorem]{Lemma}


\\newcommand{\OR}{\\vee}

\\newcommand{\AND}{\wedge}

"""
textA = """\\author{Thaqib Mo.}"""

text2 = """
\\title"""
text2f = text2+"{ "+foldername +" }"

text3 = """
\\begin{document}
\maketitle
\\newpage
\section{Q1}
\end{document}
"""
textFinal = text1 +textA+ text2f + text3


try:
	f= open(foldername + ".tex","w+")
	f.write(textFinal)
	os.system('explorer.exe .')

except:
	print("create <project_name> l")
