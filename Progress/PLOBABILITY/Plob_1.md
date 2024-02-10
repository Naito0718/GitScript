
- [確率の性質](#確率の性質)
  - [有限加法族と有限加法的確率](#有限加法族と有限加法的確率)
  - [$P-a.s.$ 集合](#p-as-集合)
- [確率変数](#確率変数)
  - [分布の性質](#分布の性質)
    - [可算集合](#可算集合)
- [離散型分布](#離散型分布)
  - [ディラック測度から定まる確率](#ディラック測度から定まる確率)
  - [離散型分布](#離散型分布-1)
    - [離散型分布の性質](#離散型分布の性質)
  - [確率変数と離散型分布](#確率変数と離散型分布)
- [絶対連続型分布と密度関数](#絶対連続型分布と密度関数)
- [分布関数](#分布関数)
  - [分布関数の性質](#分布関数の性質)
  - [ルベーグ-スティルチェス測度](#ルベーグ-スティルチェス測度)



# 確率の性質

<dl><dt>

・測度空間 $(\Omega,\mathfrak{M},P)$ とする。
このとき、確率空間 $(\Omega,\mathfrak{M},P)$：$P(\Omega)=1$

    ・全部が起きることは起こりうる。Aでないことも起こりうる。AまたはBまたは...も起こりうる。
    ・まず興味のある事柄が必ず入っている集合 Ω を決定し、その後細かさに応じて σ-加法族 を決定する。
<br>

</dt><dd>

- $$P(A)+P(A^c)=1\\\ \\
P(A\cup B)=P(A)+P(B)-P(A\cap B)\\\ \\
P(S)=1\text{ なる }S\in\mathfrak{M},\ \forall A\in\mathfrak{M}\text{ に対して、}P(A\cap S^c)=0$$

</dd></dl>

---

## 有限加法族と有限加法的確率

- 有限加法族 $\mathcal{F}\sub2^\Omega$、有限加法的確率 $P:\mathfrak{M}\to[0,1]$ とする。
このとき、
$$P\text{ は }\sigma(\mathcal{F})\text{ 上の確率に一意拡張できる}\\\ \\
\iff\forall\text{ 非交叉列 }A_n\sub\mathcal{F},\ \bigcup A_n\in\mathcal{F}\text{ に対して、}P(\bigcup A_n)=\sum P(A_n)\\\ \\$$

- 可測空間 $(\Omega,\mathfrak{M})$、有限加法的確率 $P:\mathfrak{M}\to[0,1]$ とする。
このとき、
$$P\text{ は確率 }\\\ \\
\iff\forall\text{ 単調増加列 }(E_n)\subset\mathfrak{M}\text{ に対し、}P\left(\bigcup E_n\right)=\lim P(E_n)\\\ \\
\iff\forall\text{ 単調減少列 }(E_n)\sub\mathfrak{M}\text{ に対し、}P\left(\bigcap E_n\right)=\lim P(E_n)$$

      ・一般の測度空間上でもμ(E_1)<∞にすれば成り立つ。

---

## $P-a.s.$ 集合

<dl><dt>

・確率空間 $(\Omega,\mathfrak{M},P)$、$A\in\mathfrak{M}$ とする。
このとき、$P-a.s.$ 集合 $A$：
$$P(A)=1\iff\exist P\text{-零集合 }N\in\mathfrak{M}\text{ であって、}A^c\sub N\\\ \\$$

</dt><dd>

- $P-a.s.$ な集合列 $(A_n)\sub\mathfrak{M}$ とする。
このとき、$\bigcap A_n$ は $P-a.s.$ 集合、すなわち、
$$P\left(\bigcap A_n\right)=1$$

</dd></dl>

---

# 確率変数

     ・d次元確率変数：R^d値可測関数
     ・d次元分布：R^dにおけるBorel集合上の確率測度
<br>

<dl><dt>


- $P:\mathfrak{B}_{\bm{R}^d}\to[0,1]$ とする。
このとき、$d$ 次元分布 $P$：
$$P\text{ は確率測度}\\\ \\$$

</dt><dd>

- 確率空間 $(\Omega,\mathfrak{M},P)$、$d$ 次元確率変数 $X:\Omega\to\bm{R}^d$ とする。
このとき、
$$X_*P:\mathfrak{B}_{\bm{R}^d}\to[0,1]\\\ \\
X_*P(B)=P(X^{-1}(B))$$
と定めると、これは $(\bm{R}^d,\mathfrak{B}_{\bm{R}^d})$ 上の確率測度。特に、$X_*P$ は $d$ 次元分布。
<br>

      ・押し出し？
<br>

- $d$ 次元確率変数 $X,Y:\Omega\to\bm{R}^d$ とする。
このとき、
$$\{\omega\ |\ X(\omega)=Y(\omega)\}\in\mathfrak{M}$$ であって、
$$X=Y\ (a.e.)\Rightarrow X_*P=Y_*P$$
ここで、$d$ 次元確率変数 $X,Y;\Omega\to\bm{R}^d$ が $X_*P=Y_*P$ を満たすとき、$X,Y$ は同分布に従うという。

</dd></dl>

---

## 分布の性質

### 可算集合

・分布 $\mu,\nu:\mathfrak{B}_{\bm{R}^d}\to[0,1]$、可算集合 $S\sub\bm{R}^d$、$\mu(S)=1$ とする。
このとき、
$$\mu(x)=\nu(x)\ \ (\forall x\in S)\Rightarrow\mu=\nu\\\ \\$$

- 分布 $\mu,\nu:\mathfrak{B}_{\bm{R}^d}\to[0,1]$、可算集合 $S\sub\bm{R}^d$、$\mu(S)=\nu(S)=1$ とする。
このとき、
$$\mu((-\infty,x_1]\times...\times(-\infty,x_d])=\nu((-\infty,x_1]\times...\times(-\infty,x_d])\ \ (\forall x\in S)\\\ \\
\Rightarrow\mu=\nu$$

---

# 離散型分布

## ディラック測度から定まる確率

<dl><dt>

・可測空間 $(\Omega,\mathfrak{M})$、可算集合 $\Gamma\sub\Omega$、$p:\Gamma\to[0,1],\ \ \sum_{x\in\Gamma} p(x)=1$ とする。
<br>

    ・別に有限集合でもよいし、その時はほとんど0で定めてもよい。
<br>

</dt><dd>

- 
$$P:\mathfrak{M}\to[0,\infty]\\\ \\
P(B)=\sum_{x\in\Gamma}p(x)\delta_x(B)$$
と定めると、これは確率測度であって、
$$P(B)=\sum_{x\in B\cap \Gamma}p(x)$$
ただし、$\delta_x$ はディラック測度。
<br>

- 非負値可測関数 $f:\Omega\to[0,\infty]$ とする。
このとき、
$$\int_{\omega}fdP=\sum_{x\in\Gamma}p(x)f(x)$$

</dd></dl>

---

## 離散型分布

・$d$ 次元分布 $P:\mathfrak{B}_{\bm{R}^d}\to[0,1]$ とする。
このとき、離散型分布 $P$：
$$\exist\text{ 可算集合 }\Gamma\sub\bm{R}^d,\ \exist p:\Gamma\to[0,1],\ \ \sum_{x\in\Gamma} p(x)=1\text{ であって、}\\\ \\
P=\sum_{x\in\Gamma}p(x)\delta_x$$

---

### 離散型分布の性質

・$d$ 次元分布 $P:\mathfrak{B}_{\bm{R}^d}\to[0,1]$ とする。
このとき、
$$P\text{ は離散型}\iff\exist\text{ 可算集合 }\Gamma\sub\bm{R}^d\text{ であって、}P(\Gamma)=1$$

---

## 確率変数と離散型分布

・確率空間 $(\Omega,\mathfrak{M},P)$、$d$ 次元確率変数 $X:\Omega\to\bm{R}^d$ とする。
このとき、$X(\Omega)$ が可算集合ならば、$X$ の分布 $X_*P$ は離散型であって、
$$X_*P=\sum_{x\in X(\Omega)}X_*P(x)\delta_x$$
と定めると、これは $(\bm{R}^d,\mathfrak{B}_{\bm{R}^d})$ 上の確率測度。特に、$X_*P$ は $d$ 次元分布。

---

# 絶対連続型分布と密度関数

・$d$ 次元分布 $P:\mathfrak{B}_{\bm{R}^d}\to[0,1]$ とする。
このとき、絶対連続型分布 $P$：
$$\exist\text{ 非負値可測関数 }\rho:[0,1]\to[0,\infty]\text{ であって、}\\\ \\
P_{[0,1]}=m_{\rho}$$
ただし、$m$ はLebesgue測度。


・確率空間 $(\Omega,\mathfrak{M},P)$、$d$ 次元確率変数 $X:\Omega\to\bm{R}^d$、$X$ の分布関数 $F:\bm{R}^d\to[0,1]$ とする。
このとき、$X$ が離散型、連続型、絶対連続型：
$$\exist\text{ 高々可算 }A\sub\bm{R}^d\text{ であって、}P(X^{-1}(A))=1\\\ \\
F\text{ が }\bm{R}^d\text{ 上連続}\\\ \\
\exist f\in\mathcal{L}^1_{\bm{R_+}}(\bm{R}^d),\ \int_{\bm{R}^d}f(x)dx=1\text{ であって、}\\F(x)=\int_{(-\infty,x_1]\times...\times[-\infty,x_d)} f(y)dy$$

    ・Xが絶対連続型のときに存在する f をXの密度関数という。

---

# 分布関数

・確率空間 $(\Omega,\mathfrak{M},P)$、$1$ 次元確率変数 $X:\Omega\to\bm{R}$ とする。
このとき、$X$ の分布関数 $F$：
$$F:\bm{R}^d\to[0,1]\\\ \\
F(x)=(X_*P)((-\infty,x])\\\ \\$$

・有限測度 $\mu:\mathfrak{B}_{\bm{R}}\to[0,\infty)$ とする。
このとき、$\mu$ の分布関数 $F$：
$$F:\bm{R}\to\bm{R}\\\ \\
F(x)=\mu((-\infty,x])\\\ \\$$

    ・Xの分布関数とは少し違う。

---

## 分布関数の性質

<dl><dt>

・有限測度 $\mu:\mathfrak{B}_{\bm{R}}\to[0,\infty)$、$\mu$ の分布関数 $F$ とする。

</dt><dd>

- $F$ は単調増加で右連続、すなわち、
$$x\le y\Rightarrow F(x)\le F(y),\quad\lim_{y\to+x} F(y)=F(x)\\\ \\$$

- 
$$\lim_{x\to\infty} F(x)=\mu(X),\quad \lim_{x\to-\infty} F(x)=0\\\ \\$$

- $$\lim_{y\to-x}F(y)=\mu((-\infty,x))$$
特に、$$F\text{ が }x\in\bm{R}\text{ で連続}\iff\mu(\{x\})=0$$


</dd></dl>

---

## ルベーグ-スティルチェス測度



・$f:\bm{R}\to\bm{R}$ とする。
このとき、総変動、有界変動、局所有界変動：
$$V(f)=\sup_{I\sub\bm{R}}\sup_{\Delta}\sum_{i\in\Delta}|f(x_i)-f(x_{i-1})|\\\ \\
V(f)<\infty\\\ \\
\forall\text{ 有界閉区間 }I\text{ で有界変動}$$

    ・閉区間では左端のsupは消せる。
    ・開区間、半開区間なども同様。
    ・閉区間上の関数なら、有界変動⇔局所有界変動


<dl><dt>

・確率変数 $X:\Omega\to\bm{R}$、$X$ の分布 $\mu$、分布関数 $F$ とする。

</dt><dd>

- 単調増加な有界関数は、有界変動関数。特に、分布関数は有界変動。
- 有界変動関数は有界関数。
- 有界変動関数 $f,g:\bm{R}\to\bm{R}$、$\alpha\in\bm{R}$ とする。このとき、
$$f+g,\ \alpha f,\ fg$$は有界変動関数。
- $f:\bm{R}\to\bm{R}$ とする。
このとき、
$$f\text{ は有界変動}\iff f_i\text{ は有界変動}\\\ \\$$

- $f:\bm{R}\to\bm{R}$ とする。
このとき、
$f\text{ は有界変動 }\iff\exist\text{ 有界単調増加関数 }\phi,\psi\text{ }$

</dd></dl>

---