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

\usepackage[many]{tcolorbox}
\tcbuselibrary{skins,breakable}


\newtcbtheorem{defn}{Definition}{
    width=\textwidth,
    colback=white!20,
    colframe=orange,
    colbacktitle=orange,
    fonttitle=\bfseries,
    sharp corners,
    boxrule=1pt,
    breakable,
    enhanced,
    boxed title style={sharp corners},
    attach boxed title to top left
}{def}


\newtcbtheorem{axm}{Axiom}{
    width=\textwidth,
    colback=white!20,
    colframe=black,
    colbacktitle=black,
    fonttitle=\bfseries,
    sharp corners,
    boxrule=1pt,
    breakable,
    enhanced jigsaw,
    boxed title style={sharp corners},
    attach boxed title to top left
}{axm}


\newtcbtheorem{thm}{Theorem}{
    width=\textwidth,
    colback=blue!10,
    colframe=blue,
    colbacktitle=blue,
    fonttitle=\bfseries,
    sharp corners,
    boxrule=1pt,
    breakable,
    enhanced,
    boxed title style={sharp corners},
    attach boxed title to top left
}{thm}




\newtcbtheorem{coll}{Corollary}{
    width=\textwidth,
    colback=white!20,
    colframe=red,
    colbacktitle=red,
    fonttitle=\bfseries,
    sharp corners,
    boxrule=1pt,
    breakable,
    enhanced,
    boxed title style={sharp corners},
    attach boxed title to top left
}{coll}




\usepackage{setspace}
\setstretch{1.7}
\usepackage{graphicx}
\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}

\usepackage{listings}
\usepackage{color}
\definecolor{dkgreen}{rgb}{0,0.6,0}
\definecolor{gray}{rgb}{0.5,0.5,0.5}

\definecolor{deepblue}{rgb}{0,0,0.5}
\definecolor{deepred}{rgb}{0.6,0,0}
\definecolor{deepgreen}{rgb}{0,0.5,0}
\definecolor{lorange}{HTML}{FF9F40}

\lstset{frame=tb,
  language=python,
  aboveskip=2mm,
  belowskip=2mm,
  showstringspaces=false,
  columns=flexible,
  basicstyle={\linespread{0.9}\small	tfamily},
  numbers=none,
  numberstyle=	iny\color{gray},
  keywordstyle=\color{blue},
  commentstyle=\color{dkgreen},
  stringstyle=\color{deepred},
  breaklines=true,
  breakatwhitespace=true,
  tabsize=4
}

\theoremstyle{definition}
\newtheorem{definition}{Definition}

\newtheorem{Axiom}{Axiom}

\newtheorem{theorem}{Theorem}
\newtheorem{corollary}{Corollary}[theorem]
\newtheorem{lemma}[theorem]{Lemma}


\newcommand{\OR}{\vee}

\newcommand{\AND}{\wedge}

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
