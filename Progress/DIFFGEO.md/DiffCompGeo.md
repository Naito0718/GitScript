
     複素幾何（小林）

- [多変数複素関数と正則性](#多変数複素関数と正則性)
  - [共役偏微分](#共役偏微分)
  - [$f:C^n→C$](#fcnc)
  - [$f:C^n→C^m$](#fcncm)
    - [逆写像定理](#逆写像定理)
    - [陰関数定理](#陰関数定理)
  - [正則関数列](#正則関数列)
- [複素多様体](#複素多様体)
- [層とコホモロジー](#層とコホモロジー)
- [接続とChern類](#接続とchern類)
- [Kaler多様体](#kaler多様体)
- [調和積分](#調和積分)
- [消滅定理と埋蔵定理](#消滅定理と埋蔵定理)
- [複素トーラスとAbel多様体](#複素トーラスとabel多様体)
- [Riemann面](#riemann面)
- [](#)




# 多変数複素関数と正則性

## 共役偏微分

<dl><dt>

・
$$\frac{\partial}{\partial z^k}=\frac{1}{2}\left(\frac{\partial}{\partial x^k}-i\frac{\partial}{\partial y^k}\right),\quad\frac{\partial}{\partial \overline{z}^k}=\frac{1}{2}\left(\frac{\partial}{\partial x^k}+i\frac{\partial}{\partial y^k}\right)\\\ \\
dz^k=dx^k+idy^k,\quad d\overline{z}^k=dx^k-idy^k$$
とする。
このとき、
$$df(\bm{z})=d(u(\bm{x,y})+iv(\bm{x,y}))\\\ \\
=d'f+d''f\\\ \\
d'f=\sum\frac{\partial f}{\partial z^k}dz^k,\quad d''f=\sum\frac{\partial f}{\partial\overline{z}^k}d\overline{z}^k$$

    ・別にfのままでも成り立つし、f=u+ivに直しても成り立つ。
    ・(∂f/∂x)dyとか出てきちゃうけど、どうせ消える。
<br>

</dt><dd>

- $g:\bm{C}^n\to\bm{C}^m$、$f:\bm{C}^m\to\bm{C}$ とし、$z^1=x^1+iy^1,\ w^1=p^1+iq^1$ とする。
このとき、合成関数の微分において、
$$\frac{\partial}{\partial z^1}(f\circ g)(z)=\\\ \\
\sum\frac{\partial f}{\partial w^k}(g(z))\frac{\partial g^k}{\partial z^1}(z)+\sum\frac{\partial f}{\partial \overline{w}^k}(g(z))\frac{\partial \overline{g}^k}{\partial z^1}(z)\\\ \\
\frac{\partial}{\partial \overline{z}^1}(f\circ g)(z)=\\\ \\
\sum\frac{\partial f}{\partial w^k}(g(z))\frac{\partial g^k}{\partial \overline{z}^1}(z)+\sum\frac{\partial f}{\partial \overline{w}^k}(g(z))\frac{\partial \overline{g}^k}{\partial \overline{z}^1}(z)$$

      ・共役偏微分の意味！
<br>


- 連続関数 $f:\bm{C}^n\supset U\to\bm{C}$ とする。
このとき、
$$f\text{ は }U\text{ 上正則}\iff d''f=0$$

      ・微分形式的には、係数∂f/∂z*が0。現状は任意のdz*に対して0。

</dd></dl>

---

## $f:C^n→C$

・領域 $U\subset \bm{C}^n$、$f:U\to \bm{C}$ とする。
このとき、
$$\forall a\in U\ {に対して、}\\\ \\f(z)=\sum a_I(z-a)^I\ \ (z\in{a\text{ の近傍}})\\\ \\
\iff f\ {は}\ U\ {上連続で、各変数}\ z^i\ {に対して正則}$$
さらに、
$$a_{k_1,...,k_n}=\\\ \\
\left(\frac{1}{2\pi i}\right)^n\int_{|w^1-a^1|=r_1}...\int_{|w^n-a^n|=r_n}\frac{f(w^1,...,w-n)dw^1...dw^n}{(w^1-a^1)^{k_1+1}...(w^n-a^n)^{k_n+1}}$$
であって、$M=\sup\{|f(w)|\ |\ |w^k-a^k|\le r_k \}$ とすると、
$$|a_{k_1,...,k_n}|\le \frac{M}{r_1^{k_1}...r_n^{k_n}}$$
ここで、上記のいずれかを満たす関数 $f$ を $U$ 上正則という。
    
    ・後半のfの連続性は各変数の正則性から導けるらしい。（各成分が連続でも全体が連続とは限らない）Hartogs、複素幾何 p.2
    ・⇒は明らか。
    ・ここって各積分領域って領域？⇒円板内だからいっか。

---

## $f:C^n→C^m$

・領域 $U\sub\bm{C}^n$、$f:U\to\bm{C}^m$ とする。
このとき、$f$ が正則：各 $f^k$ が正則。

    ・∂f^k/∂z*^l=0

- 領域 $U\sub\bm{C}^n$、正則関数 $f:U\to\bm{C}^n$ とする。
このとき、ヤコビアン $J(f)=\det(\frac{\partial f}{\partial z})$ に対して、
$$\begin{pmatrix}
1 & i & \cdots \\
i & 1 & \cdots \\   
0 & 0 & 1 & i & \cdots \\
0 & 0 & i & 1 & \cdots \\   
\vdots
\end{pmatrix}\left[\frac{\partial(u_1,v_1,...,u_n,v_n)}{\partial(x^1,y^1,...,x^n,y^n)}\right]\begin{pmatrix}
1 & -i & \cdots \\
-i & 1 & \cdots \\   
0 & 0 & 1 & -i & \cdots \\
0 & 0 & -i & 1 & \cdots \\   
\vdots 
\end{pmatrix}\\\ \\
=2\begin{pmatrix}
\frac{\partial f^1}{\partial z^1} & -i\frac{\partial f^1}{\partial \overline{z}^1} & \frac{\partial f^1}{\partial z^2} & \cdots \\\ \\
\overline{-i\frac{\partial f}{\partial \overline{z}^1}} & \overline{\frac{\partial f}{\partial z^1}} & \overline{-i\frac{\partial f}{\partial \overline{z}^2}} & \cdots\\\ \\
\frac{\partial f^2}{\partial z^1} & -i\frac{\partial f^2}{\partial \overline{z}^1} & \frac{\partial f^2}{\partial z^2} & \cdots \\\ \\
\vdots \\
\end{pmatrix}$$
したがって、$$|J(f)|^2=\det\left[\frac{\partial(u_1,v_1,...,u_n,v_n)}{\partial(x^1,y^1,...,x^n,y^n)}\right]$$
   

---

### 逆写像定理

・領域 $U\sub \bm{C}^n$、正則関数 $f:U\to \bm{C}^n$、ヤコビアン $J(f)$、$a\in U$ とする。
このとき、$J(f)(a)\neq0$ ならば、
$$\exist\text{ 開近傍 }V\in\mathcal{N}(a)\text{ であって、}\\\ \\
\begin{cases}
f:V\to f(V)\text{ は全単射}   \\
f(V)\sub\bm{C}^n\text{ は開集合}   \\
f^{-1}:f(V)\to V\text{ は正則}   \\
\end{cases}$$

    ・逆関数定理。
    ・正則性以外は実数における逆関数定理から従う。

---


### 陰関数定理

・領域 $U\sub \bm{C}^n$、正則関数 $f_1,...,f_r:U\to \bm{C}$、$a\in U$ とする。
このとき、
$$f_1(a)=...=f_r(a)=0\\\ \\
\det\left[\left(\frac{\partial f^{\alpha}}{\partial z^{\beta}}\right)_{1\le\alpha,\beta\le r}\right]\neq0$$
ならば、
$$\exist\text{ 開集合 }V\sub\bm{C}^{n-r},W\sub\bm{C}^r,\ a\in V\times W,\\
\phi:V\to W\text{ であって、}\\\ \\
\begin{cases}
(a^{n-r+1},...,a^n)=\phi(a^{1},...,a^{n-r})   \\\ \\
\phi\text{ は }V{ 上正則}   \\\ \\
(x,y)\in V\times W\text{ に対して、}\\(f_1,...,f_r)(x,y)=0\iff y=\phi(x)   \\
\end{cases}$$
また、この条件を満たす $\phi$ は一意的に定まる。

    ・左上のk×k小行列式が0でない。
    ・陰関数定理。
    ・正則性以外は実数における陰関数定理から確かに従う。適当な全単射考えればよい。

---

## 正則関数列

・領域 $U\sub\bm{C}^n$、正則関数列 $f_n:D\to\bm{C}$ とする。
このとき、$f_n$ が $f$ に $U$ 上広義一様収束するならば、$f$ は正則関数。

   ・fの定義域は？


---

# 複素多様体

# 層とコホモロジー

# 接続とChern類

# Kaler多様体

# 調和積分

# 消滅定理と埋蔵定理

# 複素トーラスとAbel多様体

# Riemann面

# 