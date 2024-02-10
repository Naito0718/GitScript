\RequirePackage{plautopatch}
\RequirePackage[l2tabu, orthodox]{nag}

\documentclass[platex,dvipdfmx]{jlreq}			% for platex
% \documentclass[uplatex,dvipdfmx]{jlreq}		% for uplatex
\usepackage{graphicx}
\usepackage{bxtexlogo}
\usepackage{amsmath,amssymb}
\usepackage{okumacro}
\usepackage{mathtools}
\usepackage{physics} 
\usepackage{bm}
\usepackage{color}
\usepackage{here}
\usepackage{caption}
\usepackage{listings,jlisting} %日本語のコメントアウトをする場合jlisting（もしくはjvlisting）が必要
%ここからソースコードの表示に関する設定
\lstset{
  basicstyle={\ttfamily},
  identifierstyle={\small},
  commentstyle={\smallitshape},
  keywordstyle={\small\bfseries},
  ndkeywordstyle={\small},
  stringstyle={\small\ttfamily},
  frame={tb},
  breaklines=true,
  columns=[l]{fullflexible},
  numbers=left,
  xrightmargin=0zw,
  xleftmargin=3zw,
  numberstyle={\scriptsize},
  stepnumber=1,
  numbersep=1zw,
  lineskip=-0.5ex
}
%ここまでソースコードの表示に関する設定

\title{実験Aレポート：連成振動}

\author{内藤大智}
\date{\today}
\newtheorem{dfn}{定義}
\newtheorem{thm}{定理}
\newtheorem{Q}{問}

\numberwithin{equation}{section}
\numberwithin{dfn}{section}
\numberwithin{Q}{subsection}

\begin{document}
\maketitle



\tableofcontents
\input{contents/chapter1.tex}

\input{contents/chapter2.tex}

\input{contents/chapter3.tex}

\input{contents/chapter4.tex}

\input{contents/chapter5.tex}

\input{contents/chapter6.tex}



\end{document}