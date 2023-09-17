
- [$C^∞$ 級多様体](#c-級多様体)
  - [基本的な性質](#基本的な性質)
- [$C^∞$ 写像 $F:M→N$](#c-写像-fmn)
  - [多様体の間の $C^∞$ 写像](#多様体の間の-c-写像)
    - [$R^n$ への帰着](#rn-への帰着)
      - [$R$ への $C^∞$ 写像](#r-への-c-写像)
      - [$R^n$ への $C^∞$ 写像](#rn-への-c-写像)
      - [ベクトル値関数の言葉による $C^∞$](#ベクトル値関数の言葉による-c)
      - [成分の言葉による $C^∞$](#成分の言葉による-c)
    - [偏微分](#偏微分)
  - [逆関数定理](#逆関数定理)
- [接空間](#接空間)
  - [接空間の定義](#接空間の定義)
    - [微分 $F$\*](#微分-f)
  - [曲線と速度ベクトル](#曲線と速度ベクトル)
  - [はめ込みと沈め込み](#はめ込みと沈め込み)
- [ベクトル束と接束](#ベクトル束と接束)
- [$1$ の分割](#1-の分割)
- [外微分](#外微分)
  - [微分 $k$ 形式](#微分-k-形式)
- [積分](#積分)
  - [向き](#向き)
- [ドラーム理論](#ドラーム理論)

# $C^∞$ 級多様体

## 基本的な性質

・定義：$C^{\infty}$ 級多様体 $M$

- $M$ はハウスドルフ空間
 
- $M$ は第二可算空間

- $M$ は極大 $C^{\infty}$ アトラスを持つ。
<br>

- $n$ 次元局所ユークリッド空間 $M$：
位相空間 $M$ であって、$\forall x\in M$ に対して、$U\cong \phi(U)\subset \bm{R}^n\ \{同相\}$ であるような開近傍 $x\in U$ を持つ。

---

・$C^{\infty}$ アトラス：$\{(U,\phi)\ |\ \phi:U\to\bm{R}^n{は同相写像},\quad\phi^{-1}\circ\psi\ {は}\ C^{\infty}\}$ であって、$M=\bigcup {アトラス}$

    ・次元はただ一つに定まると仮定する。
    ・多様体 M が連結ならば次元は一意的。
    ・両立性は、反射、対称だが推移的ではない。

- $n$ 次元局所ユークリッド空間 $M$ 上のアトラス $\{(U,\phi)\}$、$(V_1\psi_1),(V_2,\psi_2)$ を チャートとする。
このとき、 $(V_1,\psi_1),(V_2,\psi_2)$ が共にアトラス $(U,\phi)$ と両立するならば、$(V_i,\psi_i)$ は両立する。
<br>

- $n$ 次元局所ユークリッド空間 $M$ 上のアトラス $\{(U,\phi)\}$ に対して、
極大アトラスがただ一つ存在する
  
      ・アトラスの存在を示せば多様体になる
<br>

- $C^{\infty}$ 多様体 $M$、極大アトラス $\{U_{\alpha},\phi_{\alpha}\}$ とする。
このとき、$\{U_{\alpha}\}$ は開基である。

---

# $C^∞$ 写像 $F:M→N$

## 多様体の間の $C^∞$ 写像

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、連続写像 $F:M\to N$、$p\in M$ とする。
このとき、$F$ が $p\in M$ で $C^{\infty}$：
$$p,F(p)\text{ を含むチャート }p\in (U_p,\phi_p),\ F(p)\in (V_{F(p)},\psi_{F(p)})\ {であって、}\\\ \\
\psi\circ F\circ\phi^{-1}:\phi(U_p\cap F^{-1}(V_{F(p)}))\to\bm{R}^n\\\ \\
{が}\ \phi(p)\ {で}\ C^{\infty}$$を満たすものが存在する。

    ・この定義はチャートによらない。
    ・逆写像も C^∞ なら微分同相。

- $m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、連続写像 $F:M\to N$ とする。
このとき、
$$F\text{ は }C^{\infty}\\\ \\
\iff\exist\text{ アトラス }\mathcal{U}_M\subset M,\ \mathcal{U}_N\subset N\text{ であって、}\forall\text{ チャート }(U_M,\phi)\in \mathcal{U}_M,\ (U_N,\psi)\in\mathcal{U}_N\text{ に対して、}\\
\psi\circ F\circ \phi^{-1}\text{ が }C^{\infty}\\\ \\
\iff \forall\text{ チャート }(U_M,\phi)\subset M,\ (U_N,\psi)\sub N\text{ に対して、}\\
\psi\circ F\circ \phi^{-1}\text{ は }C^{\infty}$$

- $C^\infty$ 多様体 $N,M,P$、$C^{\infty}$ 写像 $F:N\to M,\ G:M\to P$ とする。
このとき、合成 $G\circ F:N\to P$ は $C^\infty$ とする。

---

### $R^n$ への帰着

#### $R$ への $C^∞$ 写像

・$m$ 次元 $C^{\infty}$ 多様体 $M$、$f:M\to\bm{R}$、$p\in M$ とする。
このとき、$f$ が $p$ で $C^{\infty}$：
$$p\text{ を含むチャート }p\in (U_p,\phi_p)\ {であって、}\\\ \\
F\circ\phi^{-1}:\phi(U_p)\to\bm{R}\\\ \\
{が}\ \phi(p)\ {で}\ C^{\infty}$$を満たすものが存在する。

    ・このとき、ｆは連続。
    ・この定義はチャートによらない。
    ・この定義は一般の多様体の時の定義と整合する。
    ・逆写像も C^∞ なら微分同相。

- $m$ 次元 $C^{\infty}$ 多様体 $M$、$f:M\to\bm{R}$ とする。
このとき、
$$f\text{ は }C^{\infty}\\\ \\
\iff\exist\text{ アトラス }\mathcal{U}_M\subset M\text{ であって、}\forall\text{ チャート }(U_M,\phi)\in \mathcal{U}_M\text{ に対して、}\\
f\circ \phi^{-1}\text{ が }C^{\infty}\\\ \\
\iff \forall\text{ チャート }(U_M,\phi)\subset M\text{ に対して、}\\
f\circ \phi^{-1}\text{ は }C^{\infty}$$

---

・集合 $N,M$、$F:N\to M$、$h:M\to\bm{R}$ とする。
このとき、引き戻し：$$F^*h=h\circ F:N\to\bm{R}$$

- $f:M\to \bm{R}\text{ がチャート }(U,\phi)\text{ 上で }C^{\infty}\iff\text{ 引き戻し }(\phi^{-1})^*f\text{ が }\phi(U)\text{ 上で }C^{\infty}$ 

#### $R^n$ への $C^∞$ 写像

・$m$ 次元 $C^{\infty}$ 多様体 $M$、連続写像 $F:N\to\bm{R}^m$ とする。
このとき、$$F\text{ が }C^{\infty}\iff F^i=r^i\circ F\text{ がすべて }C^{\infty}$

    ・r^i：成分への射影

#### ベクトル値関数の言葉による $C^∞$

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、連続写像 $F:M\to N$ とする。このとき、
$$F\text{ は }C^{\infty}\\\ \\
\iff\exist\text{ アトラス }\mathcal{U}_N\subset N\text{ であって、}\forall\text{ チャート }(U_N,\psi)\in \mathcal{U}_N\text{ に対して、}\\
\psi\circ F:F^{-1}(V)\to\bm{R}^n\text{ が }C^{\infty}\\\ \\
\iff \forall\text{ チャート }(U_N,\psi)\subset N\text{ に対して、}\\
\psi\circ F:F^{-1}(V)\to\bm{R}^n\text{ は }C^{\infty}$$

---

#### 成分の言葉による $C^∞$

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、連続写像 $F:M\to N$ とする。このとき、
$$F\text{ は }C^{\infty}\\\ \\
\iff\exist\text{ アトラス }\mathcal{U}_N\subset N\text{ であって、}\forall\text{ チャート }(U_N,\psi)\in \mathcal{U}_N\text{ に対して、}\\
\psi^i\circ F:F^{-1}(V)\to\bm{R}\text{ はすべて }C^{\infty}\\\ \\
\iff \forall\text{ チャート }(U_N,\psi)\subset N\text{ に対して、}\\
\psi^i\circ F:F^{-1}(V)\to\bm{R}\text{ はすべて }C^{\infty}$$

---

### 偏微分

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$F:M\to N$、$p,F(p)$ 周りのチャート $(U,x^1,...,x^m),\ (V,y^1,...,y^n)$ とする。
このとき、$p$ での偏微分：
$$\left.\frac{\partial F^i}{\partial x^j}\right|_p=\left.\frac{\partial}{\partial r^j}\right|_{\phi(p)}(y^i\circ F\circ \phi^{-1})$$

    ・並べたやつはヤコビアン
    ・この定義はR^nのときと整合する。

- $$\frac{\partial F^i}{\partial x^j}\circ\phi^{-1}=\frac{\partial}{\partial r^j}(y^i\circ F\circ \phi^{-1})$$
よって、偏微分 $\frac{\partial F^i}{\partial x^j}:M\to \bm{R}$ は $C^{\infty}$

---

## 逆関数定理

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$F:M\to N$、$p\in M$ とする。
このとき、$p$ で $F$ が局所微分同相：
$$\exist U\in\mathcal{N}(p)\text{ であって }F|_U:U\to F(U)\text{ が微分同相}$$

- $m$ 次元 $C^{\infty}$ 多様体 $M_1,M_2$、$C^{\infty}$ 写像 $F:M_1\to M_2$、$p\in M_1$ とする。
ここで、$p,F(p)$ 周りのチャート $U,V$ で $F(U)\sub V$ が成り立つとする。
このとき、
$$F\text{ が }p\text{ で局所微分同相}\iff\det\frac{\partial F^i}{\partial x^j}(p)\neq0\\\ \\$$

- $m$ 次元 $C^{\infty}$ 多様体 $M$、、$p\in M$ 周りのチャート $(U,x^1,...,x^m)$、$C^{\infty}$ 写像 $F_i:U\to\bm{R}\ \ (i=1,...,m)$ とする。
このとき、
$$\det\frac{\partial F^i}{\partial x^j}\neq0\\\ \\
\iff \exist V\in\mathcal{N}(p)\text{ であって、}(V,F^1,...,F^m)\text{ は $p$ 周りのチャート}$$

      ・R^nでの局所座標となるかどうかの判定で使える。

---

# 接空間

## 接空間の定義

<dl><dt>

・$m$ 次元 $C^{\infty}$ 多様体 $M$ とする。

</dt><dd>

- $C^{\infty}$ 写像 $f,g:M\to\bm{R}$ に対して、
$$f\sim g\iff\exist p\in U\in\mathcal{N}(p)\text{ であって、}f(x)=g(x)\ \ (\forall x\in U)$$は同値関係。
<br>

- $$C_p^{\infty}(M)=\{[f]\ |\ C^{\infty}\text{ 写像 }f:M\to\bm{R}\}$$は $\bm{R}-$単位的代数。
<br>

- $p$ の接空間：
$$T_pM=\{D:C_p^{\infty}\to\bm{R}\ |\ D\text{ は線形で、}D(fg)=D(f)g(p)+f(p)D(g)\}$$は $\bm{R}$ 上ベクトル空間。

      ・点導分全体

- $$\left.\frac{\partial}{\partial x^i}\right|_p\in T_p(M),\quad\phi_{*}\left(\left.\frac{\partial}{\partial x^i}\right|_p\right)=\left.\frac{\partial}{\partial r^i}\right|_{\phi(p)}$$したがって、$\left.\frac{\partial}{\partial x^i}\right|_p$ は $T_pM$ の基底で、$\dim T_pM=m$
<br>

- 異なる $p$ 周りのチャート $(U,x^i),(V,y^i)$ に対して、
$$\frac{\partial}{\partial x^i}=\sum_j\frac{\partial y^j}{\partial x^i}\frac{\partial}{\partial y^j}\ \ (\forall p\in U\cap V)$$

</dd></dl>

---

### 微分 $F$*

<dl><dt>

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $F:M\to N$ とする。

</dt><dd>

- $f\in C_{F(p)}^{\infty}(N)$ に対して、
$$f\circ F\in C_p^{\infty}(M)$$

      ・任意の f に対して同じ値（同値類）を返す。

- 
$$F_*:T_pM\to T_{F(p)}N\\\ \\
F_*(X_p)(f)=X_p(f\circ F)$$と定めると、これは線形写像。

    ・F*X_p は導分
    ・ユークリッド空間の間のC^∞写像 F について、微分 F* の基底∂/∂x^i,∂/∂y^i についての表現行列は p でのヤコビ行列

- $C^{\infty}$ 写像の合成について、
$$(G\circ F)_{*,p}=G_{*,F(p)}\circ F_{*,p}$$特に、$1_{M}:M\to M$ に対して、
$$(1_{M})_{*,p}=1_{T_p(M)}$$

- $F$ が微分同相ならば、
微分 $F_*:T_p(M)\to T_{F(p)}N$ は同型写像。
<br>

- $$F_*\left(\left.\frac{\partial}{\partial x^i}\right|_p\right)=\sum_j\frac{\partial F^j}{\partial x^i}(p)\left.\frac{\partial}{\partial y^j}\right|_{F(p)}$$

      ・逆関数定理⇔微分F_*が線形同型。

</dd></dl>

---

## 曲線と速度ベクトル

・$m$ 次元 $C^{\infty}$ 多様体 $M$、$p\in M$ に対して、
$p$ を始点とする滑らかな曲線 $c$：
$$c:(a,b)\to M,\quad c(0)=p\quad(C^{\infty}\text{ 写像})$$

- 速度ベクトル：
$$c'(t)=c_{*}\left(\left.\frac{d}{dt}\right|_p\right)\in T_{c(t)}M$$

      ・R^nへの曲線ならば、c'(t)=dc^i/dt(t) ∂/∂x^i|_(c(t))

- $\forall p\in M,\ \forall X_p\in T_pM$ に対して、$\exist\epsilon >0$ と滑らかな曲線 $c:(-\epsilon,\epsilon)\to M$ であって、
$$c(0)=p,\ c'(0)=X_p$$さらに、この滑らかな曲線は
$$X_p(f)=\left.\frac{d}{dt}\right|_0(f\circ c)\quad (\forall f\in C_p^{\infty}(M))\\\ \\
F_{*,p}(X_p)=\left.\frac{d}{dt}\right|_0(F\circ c)(t)\quad(\forall C^{\infty}\text{ 写像 }F:M\to N)$$を満たす。

      ・X_p は与えられてる。

---

## はめ込みと沈め込み



<dl><dt>

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$p\in M$、$C^{\infty}$ 写像 $F:M\to N$ に対して、
点 $p$ におけるはめ込み、沈め込み：
$$F_{*,p}:T_pM\to T_{F(p)}N$$がそれぞれ単射、全射。

    ・pで沈め込みになるとき、pを正則点という。正則点でなければ臨界点。
    ・臨界点の像：臨界値、それ以外：正則値

</dt><dd>

- $$F\text{ がはめ込み}\Rightarrow m\le n\\\ \\
F\text{ が沈め込み}\Rightarrow m\ge n\\\ \\$$

- $$q\text{ が臨界値}\iff \exist p\in F^{-1}(q)\text{ であって、}p\text{ は臨界点}\\\ \\
q\text{ が正則値}\iff \forall p\in F^{-1}(q)\text{ が正則点}\\\ \\$$

      ・実数値関数なら、pが臨界点⇔∂f/∂x^i(p)=0 (i=1,...,m)

</dd></dl>


---

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$p\in M$、$C^{\infty}$ 写像 $F:M\to N$ に対して、
$p$ における $F$ の階数：
$$\dim F_{*,p}(T_pM)=\mathrm{rank}\frac{\partial F^i}{\partial x^j}(p)\\\ \\
$$


---

# ベクトル束と接束

---

# $1$ の分割

---

# 外微分

## 微分 $k$ 形式

---

# 積分

## 向き

---

# ドラーム理論