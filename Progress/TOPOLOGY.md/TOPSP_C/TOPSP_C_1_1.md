
- [集合](#集合)
  - [演算](#演算)
  - [極限集合](#極限集合)
- [写像](#写像)
  - [演算](#演算-1)
    - [直積](#直積)
  - [連続性](#連続性)
    - [連続写像の連結](#連続写像の連結)
    - [直積と連続性](#直積と連続性)
- [同値関係](#同値関係)
  - [射影と断面](#射影と断面)
  - [誘導された写像](#誘導された写像)
  - [等化空間](#等化空間)
    - [連続性](#連続性-1)
    - [位相的性質の継承](#位相的性質の継承)
  - [種々の同値関係](#種々の同値関係)
    - [直積と射影](#直積と射影)
    - [部分集合を点とみなす](#部分集合を点とみなす)
- [集積点](#集積点)
  - [$T1$ 空間と集積点](#t1-空間と集積点)


# 集合

## 演算

<dl><dt>

・全体集合 $X$、部分集合族 $A_{\lambda}\sub X$、部分集合 $B\sub X$ とする。
このとき、$$\left(\bigcup_{\lambda}A_{\lambda}\right)\cap B=\bigcup_{\lambda}(A_{\lambda}\cap B)\\\ \\
\left(\bigcap_{\lambda}A_{\lambda}\right)\cup B=\bigcap_{\lambda}(A_{\lambda}\cup B)\\\ \\
\left(\bigcap_{\lambda}A_{\lambda}\right)^c=\bigcup_{\lambda}A_{\lambda}^c\\\ \\
\left(\bigcup_{\lambda}A_{\lambda}\right)^c=\bigcap_{\lambda}A_{\lambda}^c\\\ \\$$

</dt><dd>

- 全体集合 $X$、部分集合 $A,B\sub X$ とする。
このとき、$$A\cup B=A\cup (B\cap A^c)\\\ \\$$

- 全体集合 $X,Y$、部分集合 $A_1,A_2\sub X,\ B_1,B_2\sub Y$ とする。
このとき、
$$(A_1\times B_1)^C=(A_1^C\times Y)\cup(X\times B_1^C)\\\ \\
(A_1\times A_2)\cap(B_1\times B_2)=(A_1\cap B_1)\times(A_2\cap B_2)\\\ \\
(A_1\cup A_2)\times(B_1\cup B_2)=(A_1\times B_1)\cup(A_1\times B_2)\cup(A_2\times B_1)\cup(A_2\times B_2)\\\ \\$$

</dd></dl>


---

## 極限集合

・全体集合 $X$、集合列 $A_n\sub X$ とする。
このとき、上極限集合 $\overline{\lim}A_n$、下極限集合 $\underline{\lim}A_n$：
$$\overline{\lim}A_n=\bigcap_{n=1}^{\infty}\bigcup_{k=n}^{\infty}A_k\\\ \\
\underline{\lim}A_n=\bigcup_{n=1}^{\infty}\bigcap_{k=n}^{\infty}A_k$$
明らかに、$\underline{\lim}A_n\sub \overline{\lim}A_n$。また、$\underline{\lim}A_n=\overline{\lim}A_n$ の時、集合列 $A_n$ は収束するという。
<br>

- 全体集合 $X$、単調増加列 $A_n\sub X$、単調減少列 $B_n\sub X$ とする。
このとき、
$$\overline{\lim}A_n=\underline{\lim}A_n=\bigcup_{n=1}^{\infty} A_n\\\ \\
\overline{\lim}B_n=\underline{\lim}B_n=\bigcap_{n=1}^{\infty} B_n\\\ \\$$

- 全体集合 $X$、集合列 $A_n\sub X$ とする。
このとき、
$$(\overline{\lim}A_n)^c=\underline{\lim}(A_n)^c\\\ \\
(\underline{\lim}A_n)^c=\overline{\lim}(A_n)^c$$

---

# 写像

## 演算

・集合 $X,Y$、写像 $f:X\to Y,\ g:Y\to X$ とする。
このとき、$g\circ f=1_X$ ならば、$f$ は単射で $g$ は全射。

- $$f\left(\bigcup A_{\lambda}\right)=\bigcup f(A_{\lambda})$$

---

### 直積

・集合 $X$、集合族 $Y_{\lambda}$、部分集合族 $A_{\lambda}\sub X_{\lambda}$、関数族 $f_{\lambda}:X\to Y_{\lambda}$ とする。
このとき、
$$F:X\to\Pi_{\lambda\in\Lambda} Y_{\lambda}\\\ \\
F(x)=(...,f_{\lambda}(x),...)$$
と定めると、
$$F^{-1}(\Pi_{\lambda\in\Lambda}A_{\lambda})=\bigcap_{\lambda\in\Lambda} f_{\lambda}^{-1}(A_{\lambda})$$

---

## 連続性

・位相空間 $X,Y$、$y_0\in Y$ に対して、
$f(x)=y_0$ は連続写像

- 位相空間 $X,Y$、$f:X\to Y$ に対して、
$$f(\overline{A})\subset \overline{f(A)}\iff f\text{ は連続}$$

---

### 連続写像の連結

・位相空間 $X,Y$、有限閉被覆 $X=\bigcup_{i=1}^n F_i$、連続写像 $f_i:F_i\to Y$ とする。
このとき、$$f_i|_{F_i\cap F_j}=f_j|_{F_i\cap F_j}$$を満たすならば、
$$f:X\to Y\\\ \\
x\in F_i\text{ のとき }f(x)=f_i(x)$$ はwell-definedで連続。
さらに、$$f^{-1}(A)=\bigcup_{i=1}^nf_i^{-1}(A)$$

    ・最後のは定義域に注意。
    ・弧状連結当たりのやつの正当化。

---

### 直積と連続性

    ・関数定義域直積空間への別の関数の部分的代入みたいなやつは、定数関数との有限直積化とみるべき。

・位相空間 $X,Y_1,...,Y_n$、連続写像 $f_i:X\to Y_i$ とする。
このとき、
$$F:X\to\Pi_{i=1}^nY_i\\\ \\
F(x)=(f_1(x),...,f_n(x))$$
と定めると、$F$ は連続写像。
<br>

    ・可算個だと言えない。
    


---
---
---

# 同値関係

## 射影と断面

<dl><dt>

・集合 $X$、同値関係 $\sim$ とする。
このとき、
$$\pi:X\to X/\sim,\quad \pi(x)=[x]\\\ \\
s:X/\sim\to X,\quad s([x])=x\ (x{は代表元})$$
と定めると、$\pi$ は全射で $s$ は単射。
<br>

</dt><dd>

- 集合 $X$、同値関係 $\sim$ とする。
このとき、$$s\text{ は断面}\iff p\circ s=1_{X/\sim}$$

</dd></dl> 


---

## 誘導された写像

<dl><dt>

・集合 $X,Y$、同値関係 $\sim_X$、$x\sim x'\Rightarrow f(x)=f(x')$ なる写像 $f:X\to Y$ とする。
このとき、$$\tilde{f}:X/\sim\ \to Y,\quad \tilde{f}([x])=f(x)$$はwell-defined。
ここで、$\tilde{f}$ を誘導された写像という。
<br>

</dt><dd>

 - $f=\tilde{f}\circ \pi$ 
 <br>

- $f$ が全射ならば、誘導された写像 $\tilde{f}$ は全射
 <br>

- 集合 $X,Y$、写像 $f:X\to Y$ に対して、
$$x\sim x'\iff f(x)=f(x')$$は $X$ の同値関係であって、誘導された写像 $\tilde{f}$ は単射。

</dd></dl> 

---

## 等化空間

・位相空間 $X$、同値関係 $\sim_X$ とする。
このとき、
$$\mathcal{O}_{\sim}=\{O\sub X/\sim\ |\ \pi^{-1}(O)\text{ は }X\text{ の開集合}\}$$
と定めると、これは位相。
ここで、位相空間 $X/\sim$ を等化空間という。
<br>

- $\pi:X\to X/\sim$ は明らかに連続。

### 連続性

・位相空間 $X,Y$、$X$ の同値関係 $\sim_X$、$f:X\to Y,\ g:X/\sim_X\to Y$ とする。
このとき、$f=g\circ \pi$ ならば、
$$f\text{ が連続}\iff g\text{ が連続}$$

  
---

### 位相的性質の継承

<dl><dt>

・位相空間 $X$、同値関係 $\sim$ とする。

</dt><dd>

- $X$ がコンパクトならば、$X/\sim$ はコンパクト。
        
       ・連続像であることによる。
<br>

- $X$ が弧状連結ならば、$X/\sim$ は弧状連結。


</dd></dl> 

---

## 種々の同値関係

### 直積と射影

 ・直積集合 $X\times Y$ に対して、
 $$(x,y)\sim(x',y')\iff x=x'$$は同値関係。

 - 射影：$\pi(x,y)=x\times Y$、断面：$s(x\times Y)=(x,y_0)\ (y_0\in Y)$

 - $X/\sim\ \cong X,\quad(x\times Y)\leftrightarrow x\ ({濃度})$

 - 断面は包含写像 $i:X\to X\times Y,\ i(x)=(x,y_0)$ とみなせる。
  また、射影は $\pi':X\times Y\to X,\ \pi'(x,y)=x$ とみなせる。

---

### 部分集合を点とみなす

・位相空間 $X$、$A\sub X$ とする。
このとき、
$$x\sim y\iff x=y\text{ または }x,y\in A$$は同値関係。

---
---
---

# 集積点

<dl><dt>

・位相空間 $X$、部分集合 $M\sub X$、$x\in X$ とする。
このとき、$M$ の集積点 $x$：
$$x\in\overline{M-\{x\}}\\\ \\$$
ここで、$M$ の集積点全体を $M^a$ と書く。

    ・集積点でないなら孤立点。
<br>

</dt><dd>

- $x\in X-M$ とする。
このとき、
$$x\text{ が }M\text{ の集積点}\iff x\in\overline{M}-M\\\ \\$$
特に、$$\overline{M}=M\cup M^a$$

</dd></dl>

---

## $T1$ 空間と集積点

・$T_1$ 空間 $X$、部分集合 $A\sub X$、$x\in X$ とする。
このとき、
$$x\text{ は }A\text{ の集積点}\iff\forall U\in\mathcal{N}(x)\text{ に対して、}U\text{ は }A\text{ の要素を無限に含む}\\\ \\$$

    ・U∩(U∩A-{x})^cを考えればよい。

