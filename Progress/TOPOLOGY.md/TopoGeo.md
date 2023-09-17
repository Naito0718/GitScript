
- [基本群](#基本群)
  - [弧状連結](#弧状連結)
    - [単連結](#単連結)
    - [弧状連結空間と基本群](#弧状連結空間と基本群)
  - [ホモトープと基本群](#ホモトープと基本群)
    - [可縮空間](#可縮空間)
- [ホモトピー](#ホモトピー)
  - [ホモトピー同値](#ホモトピー同値)
    - [ホモトピー同値と基本群](#ホモトピー同値と基本群)
- [ファイバー空間](#ファイバー空間)
  - [リフト](#リフト)
  - [弧状連結なファイバー](#弧状連結なファイバー)
  - [被覆ホモトピー定理](#被覆ホモトピー定理)



# 基本群

## 弧状連結

・位相空間 $X$ に対する「道」： 連続写像 $k:[0,1]\to X$

    ・始点、終点：k(0),k(1)
    ・k(0)=k(1)なら閉じた道

- $x_0\in X$ に対して、$k(t)=x_0$ は道

      ・定値の道

- 道 $k$ に対して、$$k^{-1}(t)=k(1-t)$$ は道であって、$$k^{-1}(0)=k(1),\ k^{-1}(1)=k(0)\\\ \\
(k^{-1})^{-1}=k$$

      ・逆の道

- $k(1)=l(0)$ なる道 $k,l$ に対して、$$k\vee l(t)=\begin{cases}
k(2t)  & (0\le t\le1/2)  \\
l(2t-1) & (1/2\le t\le1) \\
\end{cases}$$ は道。

      ・逆に、任意の道は途中の点で分割できる → 途中の点からホモトープな道に分岐したものは、元の道にホモトープ。

---

・弧状連結成分：同値関係 $$x\sim y\iff \exist\ {道}\ k\ {であって、}\ k(0)=x,\ k(1)=y$$

- $k(I)$ は連結。
  <br>

- 位相空間 $X$ が弧状連結ならば、$X$ は連結。
  <br>

- 弧状連結空間 $X$、位相空間 $Y$、連続写像 $f:X\to Y$ とする。
このとき、$f(X)$ は弧状連結。

---

### 単連結

<dl><dt>

・弧状連結空間 $X$ に対して、
単連結空間 $X$：$$\pi(X,x)=[0_x]\quad(\forall x\in X)$$

</dt><dd>

- $$X\text{ が単連結}\iff \forall x,y\in X,\ \forall x\to y\text{ への道 }k,l\text{ に対して、}k\sim l\ \ (\text{ホモトープ})$$

- 単連結空間と同相な位相空間は単連結。

</dd></dl>

---

### 弧状連結空間と基本群

・弧状連結空間 $X$ に対して、
$$\pi(X,x_1)\cong\pi(X,x_2)\ \ (\text{群同型})\\\ \\
\phi:\pi(X,x_1)\to\pi(X,x_2),\quad\phi(k)=h^{-1}kh\\\ \\
(h\text{ は弧状連結性によって取れる $x_1\to x_2$ の道})$$

    ・弧状連結でなくても道が繋がってる点については基本群が同型。

---
## ホモトープと基本群

・$X$ の道 $k,l$ に対して、
ホモトープ $$k\sim l\iff \exist\text{ 連続写像 }\phi:I\times I\to X\\\ \\
\phi(t,0)=k(t),\quad\phi(t,1)=l(t)\\\ \\
\phi(0,s)=k(0)=l(0)\\\ \\
\phi(1,s)=k(1)=l(1)$$と定めると、始点、終点を $x,y$ とする道全体の集合 $\Omega(X,x,y)$ における同値関係。

    ・始点と終点を共有する。
    ・閉じた道全体 Ω(X,x) の同値類 [k] をkのホモトピー類という。



<dl><dt>

・位相空間 $X$、道 $k_1,k_2,l_1,l_2,m$ とする。

</dt><dd>

- $$k_1\sim k_2,\ l_1\sim l_2,\ k(1)=l(0)\Rightarrow k_1\vee l_1\sim k_2\vee l_2\\\ \\
k_1\sim k_2\Rightarrow k_1^{-1}\sim k_2^{-1}\\\ \\
0_{k_1(0)}\vee k_1\sim k_1,\quad k_1\vee 0_{k(1)}\sim k_1\\\ \\
k_1(1)=l_1(0),\ l_1(1)=m(0)\Rightarrow (k_1\vee l_1)\vee m=k_1\vee(l_1\vee m)\\\ \\
k_1\vee k_1^{-1}\sim 0_{k(0)}\\\ \\
k_1\sim l_1\iff k_1\vee l_1^{-1}\sim 0_{k(0)}\\\ \\$$

- $\Omega(X,x)/\sim$ は演算 $[k]\vee[l]=[k\vee l]$ について群をなす。これを基本群 $\pi(X,x)$ という。

      ・閉じてないと単位元が定まらない。
      ・弧状連結が基本。

</dd></dl>


---

### 可縮空間

・位相空間 $X$ に対して、
可縮空間 $X$：
$$\forall x_0\in X,\ \exist\text{ 連続写像 }\Phi:X\times I\to X\text{ であって、}\\\ \\
\Phi(x,0)=x,\quad\Phi(x,1)=x_0$$

<dl><dt>

・位相空間 $X$ に対して、
可縮空間 $X$：
$$\forall x_0\in X,\ \exist\text{ 連続写像 }\Phi:X\times I\to X\text{ であって、}\\\ \\
\Phi(x,0)=x,\quad\Phi(x,1)=x_0$$

</dt><dd>

- $$X\text{が可縮}\iff\text{ 任意の一点集合 }\{a\}\text{ に対して、}\{a\}\cong X\ \ (\text{ ホモトピー同値})$$

- 可縮$\Rightarrow$弧状連結かつ単連結。

</dd></dl>

---
---
---

# ホモトピー

・位相空間 $X\to Y$、連続写像 $f,g:X\to Y$ に対して、
ホモトピック 
$$f\sim g\iff \exist \text{ 連続写像 }H:X\times I\to Y\text{ であって、}\\\ \\
H(x,0)=f(x),\quad H(x,1)=g(x)$$は連続写像 $f:X\to Y$ 全体の集合についての同値関係。

    ・H：ホモトピー

- 連続写像 $f_1,f_2:X\to Y,\ g_1,g_2: Y\to Z$ が $f_1\sim f_2,\ g_1\sim g_2$ を満たすならば、
$$g_1\circ f_1\sim g_2\circ f_2$$

---

## ホモトピー同値

・位相空間 $X,Y$ とする。
このとき、ホモトピー同値：
$$X\sim Y\iff\exist\text{ 連続写像 }f:X\to Y,\ g:Y\to X\text{ であって、}\\\ \\
f\circ g\sim_{hom}1_Y,\quad g\circ f\sim_{hom}1_X\quad(\text{ホモトピック})$$は同値関係。

---

### ホモトピー同値と基本群

<dl><dt>

・位相空間 $X,Y$、$x_0\in X$、連続写像 $\phi:X\to Y$ とする。
このとき、
$$\phi_*:\pi(X,x_0)\to \pi(Y,\phi(x_0))\\\ \\
\phi_*([f])=[\phi\circ f]$$はwell-definedな群準同型写像。すなわち
$$\phi_*([f]\vee[g])=\phi_*([f])\vee\phi_*([g])\\\ \\$$

</dt><dd>

- $(\psi\circ\phi)_*=\psi_*\circ\phi_*$
- $(1_{X})_*=1_{\pi(X,x_0)}$
<br>

- 同相写像 $\phi:X\to Y$ に対して、
$$\phi_*:\pi(X,x_0)\to\pi(Y,\phi(x_0))$$は群同型写像。
<br>

- $X\cong Y\ \ (\text{ホモトピー同値})$、$x_0\in X$、ホモトピー同値写像  $\phi:X\to Y$ とする。
このとき、$$\phi_*:\pi(X,x_0)\to\pi(Y,\phi(x_0))$$は群同型写像。

      ・道の合成とホモトープを示す！

</dd></dl>


---
---
---

# ファイバー空間

<dl><dt>

・位相空間 $(A,B)$、連続な全射：$p:A\to B$、開集合 $U\subset X$ とする。
このとき、$(A,B,p)$ が $U$ 上で自明：
$$\exist\text{ 位相空間 }F_U,\ \exist\text{ 同相写像 }\phi_U:U\times F_U\to p^{-1}(U)\text{ であって、}\\\ \\
p\circ\phi_U=p_U\quad(p_U:U\times F_U\to U,\ p(u,f)=u)$$

    ・F_U:ファイバー、φ_U:自明化写像

・ファイバー空間 $(A,B,p,F)$：

$$A,B\text{ は位相空間}\\\ \\ p:A\to B\text{ は連続な全射}\\\ \\ \exist\text{ 開被覆 }X=\bigcup U_{\lambda}\text{ であって、}U_{\lambda}\text{ 上で自明化が与えられていて、}F_{\lambda}\cong F\ \ (\text{同相})$$

    ・A:全空間、B:底空間、p:射影、F：ファイバー。
    ・自明化写像の定義域は、ファイバーFで置き換えてよい。

</dt><dd>

- $p^{-1}(x)\cong F\ (\text{同相})$

- ファイバー空間の射影は開写像。



</dd></dl>

---

## リフト

・ファイバー空間 $(A,B,p,F)$、$B$ の道 $k$ とする。
このとき、リフト：
$$A\text{ の道 }\tilde{k}:I\to A\text{ であって、}\\\ \\
p\circ\tilde{k}=k$$

- ファイバー空間 $(A,B,p,F)$、$y\in B$、$p(x)=y$ とする。
このとき、
$$\forall B\text{ の道 }k,\ k(0)=y\text{ に対して、}\\\ \\
\exist\text{ リフト }\tilde{k}\text{ であって、}\tilde{k}(0)=x$$

---

## 弧状連結なファイバー

<dl><dt>

・ファイバー空間 $(A,B,p,F)$ において、弧状連結なファイバー $F$ とする。
このとき、
$$p_{*}:\pi(A,x)\to\pi(B,p(x))$$は全射群準同型。

    ・p_*は誘導された写像

</dt><dd>



- ファイバー空間 $(A,B,p,F)$、$y\in B$、同相写像 $i:F\to p^{-1}(y),\quad i(z)=\phi_U(y,z)$、$z_0\in F$、誘導される準同型 $i_{*,z_0}:\pi(F,z_0)\to\pi(A,i(z_0))$ とする。
このとき、
$$p_{*,i(z_0)}:\pi(A,i(z_0))\to\pi(B,y)\text{ に対して、}\\\ \\
\ker p_{*,i(z_0)}=\mathrm{Im}\ i_{*,z_0}\\\ \\$$

- ファイバー空間 $(A,B,p,F)$ において、弧状連結なファイバー $F$ とする。
さらに、$y\in B$、同相写像 $i:F\to p^{-1}(y)$、$z_0\in F$ とする。
このとき、以下の群の完全系列が成り立つ。
$$(e)\xrightarrow{}\pi(F,z_0)\xrightarrow{i_*}\pi(A,i(z_0))\xrightarrow{p_*}\pi(B,y)\xrightarrow{}(e)$$特に、
$$\pi(B,y)\cong\pi(A,i(z_0))/i_*(\pi(F,z_0))\quad(\text{群同型})$$

      ・(e) は任意の単位元からなる群、それぞれIm=ker

</dd></dl>



---

## 被覆ホモトピー定理

・ファイバー空間 $(A,B,p,F)$、$y\in B$、$\phi:I^2\to B$ でホモトープな $y$ を始点とする道 $k,l$、$k$ のリフト $\tilde{k}$ とする。
このとき、
$$\psi:I^2\to A\\\ \\
p\circ\psi=\phi\\\ \\
\psi(t,0)=\tilde{k}(t),\quad\psi(0,s)=\tilde{k}(0)$$ を満たす連続写像が存在する。特に、 $\tilde{l}(t)=\psi(t,1)$ は $l$ のリフト。
<br>

- 長方形 $S=[t_0,t_1]\times[s_0,s_1]\sub\bm{R}^2$、位相空間 $X$、連続写像 $f:[t_0,t_1]\times\{s_0\}\cup\{t_0\}\times[s_0,s_1]\to X$ とする。
このとき、$f$ は連続写像 $S\to X$ に拡張できる。

      ・左下の二辺で定義されてるとした。
