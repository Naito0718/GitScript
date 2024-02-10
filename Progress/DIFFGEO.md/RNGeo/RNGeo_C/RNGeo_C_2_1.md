
- [$R^n$ 内の曲線](#rn-内の曲線)
  - [変動量](#変動量)
  - [有界変動関数の性質](#有界変動関数の性質)
    - [右連続関数](#右連続関数)
    - [リプシッツ連続性](#リプシッツ連続性)
  - [絶対連続関数](#絶対連続関数)
  - [スチルチェス積分](#スチルチェス積分)
- [$R^n$ 内の連続曲線](#rn-内の連続曲線)
  - [弧長](#弧長)
- [$R^n$ 内の $C^1$ 曲線](#rn-内の-c1-曲線)
  - [弧長](#弧長-1)
  - [向きと $C^1$ 同値](#向きと-c1-同値)
  - [区分的 $C^1$ 曲線](#区分的-c1-曲線)




# $R^n$ 内の曲線

## 変動量

・区間 $I=[a,b]$、$f:I\to\bm{R}^n$ とする。
このとき、変動量 $v(\Delta)$、総変動 $V$：
$$v(\Delta)=\sum_{i=1}^n|f(t_{i})-f(t_{i-1})|\quad(\Delta\text{ は } I \text{ の分割})\\\ \\
V=\sup_{\Delta\in\mathcal{D}} v(\Delta)$$
ここで、$V$ は $\infty$ も含めて一意的で、
$$\Delta_1\sub\Delta_2\Rightarrow l(\Delta_1)\le l(\Delta_2)\\\ \\$$
また、$V\in[0,\infty)$ ならば、$f$ は有界変動であるといい、
$$f\text{ が有界変動}\iff f_i\text{ がすべて有界変動}$$
が成り立つ。
<br>

    ・結局実数値関数で考えればよい。

---

## 有界変動関数の性質

<dl><dt>

・区間 $I=[a,b]$、有界変動関数 $f:I\to\bm{R}^n$ とする。
このとき、$f$ は有界。
<br>

</dt><dd>

- 実数値有界変動関数 $f,g:I\to\bm{R}$、$\alpha\in\bm{R}$ とする。
このとき、$f+g,\ \alpha f,fg:I\to\bm{R}$ は有界変動。
<br>

- $f:[a,b]\to\bm{R}$ とする。
このとき、
$$f\text{ は有界変動関数 }\\\ \\
\iff\forall c\in [a,b]\text{ に対して、}f\text{ は }[a,c],\ [c,b]\text{ 上で有界変動 }$$
さらに、有界変動関数 $f$ の $[a,b]$ 上の変動量を $V(a,b;f)$ とすると、
$$V(a,b;f)=V(a,c;f)+V(c,b;f)\\\ \\$$ 

- 単調増加または単調減少関数 $f:[a,b]\to\bm{R}$ とする。
このとき、$f$ は有界変動であって、変動量 $V=|f(b)-f(a)|$
<br>

- $f:[a,b]\to\bm{R}$ とする。
このとき、
$$f\text{ は有界変動}\\\ \\
\iff\exist\text{ 単調増加関数 }\phi,\psi:[a,b]\to\bm{R}\text{ であって、}\forall x\in[a,b]\text{ に対して、}f(x)=\phi(x)-\psi(x)$$
特に、有界変動関数 $f$ に対して、
$$\phi(a)=0,\forall x\in(a,b]\text{ に対して、}\quad\phi(x)=V(a,x;f)\\\ \\
\psi=\phi-f$$
と与えることができる。

</dd></dl>

---

### 右連続関数

    ・f(x)=xで、X=0でf(x)=1なら右連続でない。
<br>

・$f:[a,b]\to\bm{R}$ とする。
このとき、
$$f\text{ は右連続で有界変動}\\\ \\
\iff\exist\text{ 右連続な単調増加関数 }\phi,\psi:[a,b]\to\bm{R}\text{ であって、}\forall x\in[a,b]\text{ に対して、}f(x)=\phi(x)-\psi(x)$$
特に、右連続な有界変動関数 $f$ に対して、
$$\phi(a)=0,\forall x\in(a,b]\text{ に対して、}\quad\phi(x)=V(a,x;f)\\\ \\
\psi=\phi-f$$
と与えることができる。

---

### リプシッツ連続性

・区間 $I=[a,b]$、リプシッツ連続関数 $f:I\to\bm{R}^n$ とする。
このとき、$f$ は $I$ で有界変動。

---

## 絶対連続関数

<dl><dt>

・区間 $I=[a,b]$、$f:I\to\bm{R}^n$ とする。
このとき、絶対連続関数 $f$：
$$f\text{ は }I\text{ 上有界であって、}\\\ \\
\forall\epsilon>0\text{ に対して、}\exist\delta>0\text{ であって、}\forall\text{ 非交叉な区間 }I_1=[a_1,b_1],...,I_k=[a_k,b_k]\sub I\text{ に対して、}\\
\sum_{i=1}^kv(I_i)<\delta\Rightarrow\sum_{i=1}^k|f(b_i)-f(a_i)|<\epsilon$$
明らかに、$f$ は $I$ 上一様連続。
<br>

    ・リプシッツ連続性とは関係なさそう？
<br>

</dt><dd>

- $$f\text{ は }I\text{ 上絶対連続}\Rightarrow f\text{ は }I\text{ 上有界変動}\\\ \\$$

- 
$$f\text{ は }I\text{ 上絶対連続}\\\ \\
\iff \forall\epsilon>0\text{ に対して、}\exist\delta>0\text{ であって、}\forall\text{ 非交叉な区間列 }I_n=[a_n,b_n]\sub I I\text{ に対して、}\\
\sum_{n=1}^{\infty}v(I_n)<\delta\Rightarrow\sum_{n=1}^{\infty}|f(b_n)-f(a_n)|<\epsilon\\\ \\$$

    ・可算個で考えても同値。単調増加列と、ε/2とかで考えればよい。
<br>




</dd></dl>

## スチルチェス積分

---
---
---

# $R^n$ 内の連続曲線

・$I_1=[a_1,b_1],\ I_2=[a_2,b_2]\sub \bm{R}$、$c:I\to\bm{R}^n$、連続関数 $f_i:I_i\to\bm{R}^n$ とする。
このとき、
$$f_1\sim f_2\iff\\\ \\
\exist\text{ 狭義単調増加連続関数 }\phi:I_1\to I_2\text{ であって、}\\\ \\
f_1=f_2\circ \phi$$
と定めると、これはある区間から $R^n$ への連続写像全体の上での同値関係。
ここで、$f_1\sim f_2$ ならば、
$$f_1(a_1)=f_2(a_2),\quad f_1(b_1)=f_2(b_2),\quad f_1(I_1)=f_2(I_2)$$
であって、同値類 $C(f)$ を $f$ で径数付けられる連続曲線という。

---

## 弧長

<dl><dt>

・$R^n$ 内の連続曲線 $C$、径数表示 $f:I\to \bm{R}^n$、変動量 $l(\Delta)$、総変動 $l$とする。
このとき、$l(\Delta),l$ は共にwell-defined、すなわち径数表示によらない。
ここで、$l$ を $C$ の弧長という。
<br>

</dt><dd>

- $l<\infty$ ならば、
$$\lim_{d(\Delta)\to0}=l\\\ \\$$

      ・ダルブーの定理と同様。


</dd></dl>

---

# $R^n$ 内の $C^1$ 曲線

    ・径数表示にC^1が存在するだけでいい時もある。

## 弧長

<dl><dt>

・$I=[a,b]$、$f:I\to\bm{R}^n$ は $I$ 上微分可能で、$f'$ が $I$ 上有界とする。
このとき、$f$ は $I$ 上リプシッツ連続。
特に、$f$ は有界変動である。また、$f$ が $C^1$ ならば定理の条件は満たされる。
<br>

</dt><dd>

- $\bm{R}^n$ 内の連続曲線 $C$、$C^1$ 径数表示 $f:I\to\bm{R}^n$ とする。
このとき、
$$l=\int_a^b|f(x)|dx$$


</dd></dl>

---

## 向きと $C^1$ 同値

    ・C^n曲線と言えば多様体ではないが、正則曲線だと言えば多様体。
<br>

・$C^1$ 写像 $f:I\to\bm{R}^n$、$g:J\to \bm{R}^n$ とする。
このとき、
$$f\sim_0 g\iff\\\ \\
\exist C^1\text{ 同相写像 }\phi:I\to J\text{ であって、}f=g\circ\phi$$
と定めると、これは同値関係。
さらに、
$$f\sim g\iff\\\ \\
\exist C^1\text{ 同相写像 }\phi:I\to J,\ \phi'(t)>0\ \ (\forall t\in I)\text{ であって、}f=g\circ\phi$$
と定めると、これも同値関係。
ここで、$f\sim g$ ならば、$f,g$ は向きを込めて同値といい、同値類 $(f)$ を向きの付いた $C^1$ 曲線という。

---

## 区分的 $C^1$ 曲線

<dl><dt>

・連続関数 $f:I\to \bm{R^n}$ とする。
このとき、区分的 $C^1$ 曲線 $f$：
ある有限個の点 $a<t_1<...<t_m<b\in I$ が存在して、各 $[t_{k-1},t_k]$ 上で $C^1$ かつ、両側からの導値 $f'(t_{k}-0),f'(t_k+0)\in\bm{R}^n$ 
<br>

- 区分的 $C^1$ 曲線 $f:I\to \bm{R}^n$、$g:J\to\bm{R}^n$ とする。
このとき、
$$f\sim g\iff\\\ \\
\exist \text{ 狭義単調増加な区分的 }C^1\text{ 曲線 }\phi:I\to J,\ \phi'(t)>0\ \ \left(t\in\bigcup_{k=1}^m (t_{k-1},t_k)\right)\text{ で、片側からの導値は }0 \text{でないものであって、}\\\ \\
f=g\circ\phi$$
と定めると、これは同値関係。
<br>

      ・各区間で向きを込めてC^1同値ってこと。
<br>

</dt><dd>

- 区分的 $C^1$ 曲線 $f$ とする。
このとき、
$$f^{inv}:[-b,-a]:\bm{R}^n\\\ \\
f^{inv}(t)=f(-t)$$
と定めると、これは区分的 $C^1$ 曲線であって、$f\sim g\Rightarrow f^{inv}\sim g^{inv}$
ここで、$-C=(f^{inv})$ と書く。


</dd></dl>



