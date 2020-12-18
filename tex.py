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
\\documentclass[16pt,a4paper]{article}
\\usepackage[utf8]{inputenc}
\\usepackage{amsmath}
\\usepackage{amsfonts}
\\usepackage{amssymb}
\\usepackage{amsthm}
\\usepackage{physics}


\\usepackage[many]{tcolorbox}
\\tcbuselibrary{skins,breakable}
\\usepackage{hyperref}
\\usepackage{mathtools}

\\usepackage{dsfont}

\\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,      
    urlcolor=cyan,
    bookmarks=true,
    pdfauthor=Thaqib,
    bookmarksopen=true
}


\\newtcbtheorem[number within=subsection]{algo}{Algorithm}{
    width=\textwidth,
    colback=white!20,
    colframe=mauve,
    colbacktitle=mauve,
    fonttitle=\\bfseries,
    sharp corners,
    boxrule=1pt,
    breakable,
    enhanced jigsaw,
    boxed title style={sharp corners},
    attach boxed title to top left
}{algo}


\\newtcbtheorem[number within=section]{axm}{Axiom}{
    width=\textwidth,
    colback=white!20,
    colframe=black,
    colbacktitle=black,
    fonttitle=\\bfseries,
    sharp corners,
    boxrule=1pt,
    breakable,
    enhanced jigsaw,
    boxed title style={sharp corners},
    attach boxed title to top left
}{axm}


\\newtcbtheorem[number within=section]{thm}{Theorem}{
    width=\textwidth,
    colback=deepblue!2,
    colframe=deepblue,
    colbacktitle=deepblue,
    fonttitle=\\bfseries,
    sharp corners,
    boxrule=1pt,
    breakable,
    enhanced,
    boxed title style={sharp corners},
    attach boxed title to top left
}{thm}
\\newtcbtheorem[use counter from=thm, number within=section]{prop}{Proposition}{
    width=\textwidth,
    colback=white!20,
    colframe=black,
    colbacktitle=black,
    fonttitle=\\bfseries,
    sharp corners,
    boxrule=1pt,
    breakable,
    enhanced jigsaw,
    boxed title style={sharp corners},
    attach boxed title to top left
}{prop}


\\newtcbtheorem[number within=section]{defn}{Definition}{
    width=\\textwidth,
    colback=white!20,
    colframe=orange,
    colbacktitle=orange,
    fonttitle=\\bfseries,
    sharp corners,
    boxrule=1pt,
    breakable,
    enhanced,
    boxed title style={sharp corners},
    attach boxed title to top left
}{defn}


\\newtcbtheorem[use counter from=thm, number within=section]{lemm}{Lemma}{
    width=\\textwidth,
    colback=deepred!0,
    colframe=deepred,
    colbacktitle=deepred,
    fonttitle=\\bfseries,
    sharp corners,
    boxrule=1pt,
    breakable,
    enhanced,
    boxed title style={sharp corners},
    attach boxed title to top left
}{lemm}



\\newtcbtheorem[number within=subsection]{coll}{Corollary}{
    width=\\textwidth,
    colback=white!20,
    colframe=dkgreen,
    colbacktitle=dkgreen,
    fonttitle=\\bfseries,
    sharp corners,
    boxrule=1pt,
    breakable,
    enhanced,
    boxed title style={sharp corners},
    attach boxed title to top left
}{thm}




\\usepackage{setspace}
\\setstretch{1.7}
\\usepackage{graphicx}

\\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}

\\usepackage{listings}
\\usepackage{color}
\\definecolor{dkgreen}{rgb}{0,0.3,0}
\\definecolor{gray}{rgb}{0.5,0.5,0.5}
\\definecolor{mauve}{HTML}{6a1b9a}

\\definecolor{deepblue}{rgb}{0,0,0.5}
\\definecolor{deepred}{rgb}{0.6,0,0}
\\definecolor{deepgreen}{rgb}{0,0.5,0}
\\lstset{frame=tb,
  language=python,
  aboveskip=2mm,
  belowskip=2mm,
  showstringspaces=false,
  columns=flexible,
  basicstyle={\\linespread{0.9}\\small	tfamily},
  numbers=none,
  numberstyle= tiny\\color{gray},
  keywordstyle=\\color{blue},
  commentstyle=\\color{dkgreen},
  stringstyle=\\color{deepred},
  breaklines=true,
  breakatwhitespace=true,
  tabsize=4
}
\\theoremstyle{definition}

\\newtheorem{example}{Example}[subsection]
\\newtheorem{remark}{Remark}[subsection]
\\newtheorem{note}{Note}[subsection]


\\newcommand{\\ang}[1]{\langle #1 \rangle}

\\newcommand{\OR}{\\vee}
\\newcommand{\Z}{\mathbf{Z}}
\\newcommand{\C}{\mathbf{C}}
\\newcommand{\R}{\mathbf{R}}
\\newcommand{\Q}{\mathbf{Q}}
\\newcommand{\AND}{\wedge}

\\newcommand{\\fig}[2]{\\begin{figure}[hbtp] 
 \\centering
 \\includegraphics[scale=#2]{figs/#1.png}
 \\end{figure}
}

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
