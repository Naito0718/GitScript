
- [多様体の向き](#多様体の向き)
  - [有限次元ベクトル空間の向き](#有限次元ベクトル空間の向き)
  - [多様体の向き](#多様体の向き-1)
    - [連結性と向き](#連結性と向き)
      - [向き形式](#向き形式)
    - [微分形式と向き](#微分形式と向き)
      - [一般の向き形式](#一般の向き形式)
    - [アトラスと向き](#アトラスと向き)
      - [アトラス形式](#アトラス形式)
- [境界を持つ多様体](#境界を持つ多様体)
  - [向きの付いたベクトル場](#向きの付いたベクトル場)
  - [境界 $∂M$](#境界-m)
    - [ベクトル場](#ベクトル場)
    - [向き](#向き)
- [多様体上の積分](#多様体上の積分)




# 多様体の向き

## 有限次元ベクトル空間の向き

<dl><dt>

・$\bm{R}$ 上有限次元ベクトル空間 $V$、順序付けられた基底 $(v_i),(u_i)$、基底変換行列 $v_i=\sum A^j_{i}u_j$ とする。
このとき、
$$(v_i)\sim (u_i)\iff\det A>0$$
と定めると、これは同値関係。これを有限次元ベクトル空間 $V$ の向きという。
<br>

    ・向きは2通り。R^nじゃないとどっちが正とかはない。
    ・0次元は適当に+,-としておく。
    ・実数上でないと意味ない。
<br>

- $\bm{R}$ 上 $N$ 次元ベクトル空間 $V$、$\xi\in(\Lambda^N(V))^{\vee}$、$v_1,...,v_N,u_1,...,u_N\in V$ とし、$v_i=\sum A^j_{i}u_j$ が成り立つとする。
このとき、
$$\xi(v_1\wedge...\wedge v_N)=(\det A)\xi(u_1\wedge...\wedge u_N)$$
特に、順序付けられた基底 $(v_i),(u_i)$、基底変換行列 $v_i=\sum A^j_{i}u_j$ とすると、
$$0\neq\xi\in(\Lambda^N(V))^{\vee}\text{ に対して、} \xi(v_1\wedge...\wedge v_N)\text{ と }\xi(u_1\wedge...\wedge u_N)\text{ が同符号}\\\ \\
\iff(v_i)\sim(u_i)$$
ここで、$\xi(v_1\wedge...\wedge v_N)>0$ なら、$\xi$ は順序付けられた基底 $(v_i)$ の向きを定めるという。
<br>

      ・ξは0でないなら何でもよい。0でないなら、Λ^rVの0でない元に対して0を返すことはない。

<br>

</dt><dd>

- $\bm{R}$ 上 $N$ 次元ベクトル空間 $V$、$\xi,\eta\in(\Lambda^N(V))^{\vee}-\{0\}$ とする。
このとき、
$$\xi\sim\eta\iff\exist\alpha>0\text{ であって、}\xi=\alpha\eta$$
と定めると、これは同値関係。これを有限次元ベクトル空間 $V$ の向きという。

      ・向きは2通り。

</dd></dl>

---

## 多様体の向き

・$m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、点ごとの向き $\mu$：
$$\mu:M\to(\text{向き})\\\ \\
\mu(p)=(T_pM\text{ の向き})$$
と定める。
ここで、$p\in M$ で $\mu$ が連続：
$$\exist\text{ 開近傍 }p\in U\text{ であって、}\\\forall q\in 
U\text{ に対して }\exist U\text{ 上連続なベクトル場の枠 } Y_{1,q},...,Y_{m,q}\text{ であって、}\\\ \\
\mu(q)=[(Y_{1,q},...,Y_{m,q})]\quad (\forall q\in U)$$
と定義し、$\forall p\in M$ で連続ならば、$\mu$ を連続な向きまたは $M$ の向きといい、このとき $M$ は向き付け可能であるという。
ただし、$U$ 上のベクトル場の枠の同値関係：
$$(X_i)\sim(Y_i)\iff\forall p\in U\text{ に対して、}(X_{i,p})\sim (Y_{i,p})\\\ \\$$

    ・U上のベクトル場の枠は、常にそれで展開できるってことなので、変換行列A(p)の行列式が常に正ってこと。
    ・ホントはC^∞写像って連続性も見ないといけなかったのか！！！→確認できた！いつもの∂/∂xは連続！

---

### 連結性と向き

・向き付け可能な連結 $m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、$M$ は二つの向き $\mu,\nu$ しか持たず、
$$\mu=-\nu$$

---

#### 向き形式

・連結 $m$ 次元 $C^{\infty}$ 多様体 $M$、$\omega_1,\omega_2\in\Omega^m(M)-\{0\}$ とする。
このとき、
$$\omega_1\sim\omega_2\\\ \\
\iff\exist C^{\infty}\text{ 写像 }:M\to (0,\infty)\text{ であって、}\omega_1=f\omega_2$$
と定めると、これは同値関係であって、同値類は $2$ つ。特に、$[\omega]$ に対しては $[-\omega]$ が対応する。
<br>

・向き付け可能な連結 $m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、
$$f:\{M\text{ の向き}\}\to \{\Omega^m(M)-\{0\}\text{ の、上記の同値関係による同値類}\}\\\ \\
f(\mu)=\sum_{\alpha}\rho_{\alpha}dx^{1}\wedge...\wedge dx^m\quad(\text{トゥー多様体の証明で構成したやつ})$$
と定めると、これは全単射であって、
$$f^{-1}([\omega])=\forall p\in M\text{ に対して }\omega(X_1,...,X_n)>0\text{ となるような枠 }[X_{1,p},...,X_{2,p}]\\\ \\
(\text{これもトゥー多様体の証明で構成したやつ})$$

---

### 微分形式と向き

<dl><dt>

・$m$ 次元 $C^{\infty}$ 多様体 $M$、向き $\mu$ とする。
このとき、
$$\mu\text{ が連続}\iff\\\ \\
\forall p\in M\text{ に対して、}\exist\text{ チャート }(U,\phi)\text{ であって、}\mu(p)=[X_{1,p},...,X_{m,p}]\text{ とすると、}\\\ \\
(dx^1\wedge...\wedge dx^n)(X_{1},...,X_{m})(p)>0\quad (\forall p\in U)\\\ \\$$

- $m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、
$$M\text{ が向き付け可能}\iff\exist \omega\in \Omega^m(M)\text{ であって、}\omega\neq0\\\ \\$$

</dt><dd>

・向き付け可能な $m,n$ 次元 $C^{\infty}$ 多様体 $(M,[\omega_M]),\ (N,[\omega_N])$、微分同相写像 $F:N\to M$ とする。
このとき、$F$ が向きを保つ：
$$[F^*\omega_M]=[\omega_N]$$
ここで、$[F*\omega_N]=[-\omega_M]$ ならば、向きを逆にするという。
<br>

    ・一般の多様体では向きは2通りではない。
    ・F^*は引き戻し。

</dd></dl>

---

#### 一般の向き形式

・向き付け可能な $m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、$M$ の向きと $\Omega^m(M)-\{0\}$ の、各連結成分における同値類を $M$ の各連結成分ごとに向き形式として定めると、これは全単射。
よって、$\omega$ は $M$ の向きを定め、特に、$\omega(X_1,...,X_m)>0$ ならば、$\omega$ は向き $[X_1,...,X_m]$ を定める。
<br>

    ・多様体の連結成分は開集合。
    ・常にω(X_1,...,X_m)なるベクトル場は存在するし、このとき、[X_1,...,X_n]は連続な向き。

---


### アトラスと向き

・$m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、
$$M\text{ は向き付け可能}\\\ \\
\iff\exist\text{ アトラス }\{(U_{\alpha},\phi_{\alpha})\}\text{ であって、}U_{\alpha}\cap U_{\beta}\neq\phi\text{ ならば、}\forall p\in U\cap V\text{ に対して、}\det\frac{\partial y^i}{\partial x^j}>0$$
ここで、上記の条件を満たすアトラスを向き付けられたアトラスという。
<br>

- 向き付け可能な $m$ 次元 $C^{\infty}$ 多様体 $M$、向き付けられたアトラス $\{U_{\alpha},\phi_{\alpha}\}, \{V_{\beta},\psi_{\beta}\}$ とする。
このとき、
$$\{U_{\alpha},\phi_{\alpha}\}\sim\{V_{\beta},\psi_{\beta}\}\\\ \\
\iff\forall\alpha,\beta\text{ に対して、}\phi_{\alpha}\circ\psi_{\beta}^{-1}:\psi_{\beta}(U_{\alpha}\cap V_{\beta})\to\phi_{\alpha}(U_{\alpha\cap V_{\beta}})\text{ のヤコビ行列 }\det\frac{\partial \phi_{\alpha}\circ\psi_{\beta}^{-1}}{\partial r^j}>0$$
と定めると、これは同値関係。
<br>

      ・微分同相だから、ヤコビ行列の逆行列は逆関数のヤコビ行列。

---

#### アトラス形式

・向き付け可能な $m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、
$$f:\{M\text{ 上の向き }\}\to\{M\text{ 上の向き付けられたアトラスの同値類}\}\\\ \\
f(\mu)=\{\text{ 各点 }p\in M\text{ に対して }dx^1\wedge...\wedge dx^m(X_1,...,X_m)>0\text{ となるような }(U_{\alpha},\phi_{\alpha})\}\\\ \\
(\text{トゥー多様体の証明で構成したやつ})$$
と定めると、これはwell-definedな全単射であって、
$$f^{-1}(\{U_{\alpha},x^1,...,x^m\})=\text{ 各点 }p\in M\text{ に対して }\left[\left.\frac{\partial}{\partial x^1}\right|_p,...,\left.\frac{\partial}{\partial x^m}\right|_p\right]\\\ \\
(\text{これもトゥー多様体の証明で構成したやつ})$$
よって、向き付けられたアトラスは $M$ に向きを定める。
<br>

・向き付け可能な $m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、$M$ に対して逆の向きを定めたものを $-M$ とすると、$M$ の向きを定める向き付けられたアトラスは $\{(U_{\alpha},-x^1,x^2...,x^m)\}$ となる。

---
---
---

# 境界を持つ多様体

    ・接空間とか向きとかは全部普通の多様体と同じ。
<br>

・境界を持つ $m$ 次元位相多様体 $M$、$M$ を被覆するチャートの族 $\{(U_{\alpha},\phi_{\alpha})\}$ とする。
このとき、$C^{\infty}$ アトラス $\{(U_{\alpha},V_{\alpha})\}$：
$$\forall(U_{\alpha},\phi_{\alpha}),(U_{\beta},\phi_{\beta})\sub\{(U_{\gamma},\phi_{\gamma})\}\text{ に対して、}\\\ \\
\phi_{\beta}\circ\phi_{\alpha}^{-1}:\phi_{\alpha}(U_{\alpha}\cap U_{\beta})\to\phi_{\beta}(U_{\alpha}\cap U_{\beta})\sub\mathcal{H}^m\ \ \text{が微分同相写像}$$
ここで、$M$ が極大な $C^{\infty}$ アトラスを持つならば、$M$ を境界を持つ $m$ 次元 $C^{\infty}$ 多様体という。
<br>

    ・結局定義をちょっと拡張しただけだから、今までのは問題なく成り立つ。
<br>

- 境界を持つ $m$ 次元 $C^{\infty}$ 多様体 $M$、$p\in M$ とする。
このとき、内点 $p$：
$$\exist p\text{ を含むチャート }(U,\phi)\sub M\text{ であって、}\\\ \\
\phi(p)\in(\mathcal{H}^m)^i$$
ここで、定義を $\phi(p)\in(\mathcal{H}^m)^f$ に変更したものを境界点といい、内点全体の集合を $in(M)$ 境界点全体の集合を $\partial M$ と書く。さらに、この定義はチャートによらずwell-defined。

---

## 向きの付いたベクトル場

・境界を持つ $m$ 次元 $C^{\infty}$ 多様体 $M$、境界点 $p\in\partial M$、$X_p\in T_pM$ とする。
このとき、内向きベクトル場 $X_p$：
$$\exist C^{\infty}\text{ 曲線 }c:[0,\epsilon]\to M\text{ であって、}\\\ \\
c(0)=p,\ c((0,\epsilon))\sub \mathrm{in}(M),\ c'(0)=X_p$$
ここで、$-X_p$ が内向きベクトル場であるとき、$X_p$ を外向きベクトル場という。

---

## 境界 $∂M$

・境界を持つ $m$ 次元 $C^{\infty}$ 多様体 $M$、境界 $\partial M$ とする。
このとき、$\partial M$ は $m-1$ 次元 $C^{\infty}$ 多様体で、$\{(U_{\alpha}\cap\partial M,\ \phi_{\alpha}|_{U_{\alpha\cap\partial M}})\}$ はアトラス。
さらに、$\partial M$ は境界を持たない。

---

### ベクトル場

・境界を持つ $m$ 次元 $C^{\infty}$ 多様体 $M$、境界 $\partial M$ とする。
このとき、
$$X:\partial M\to TM\\\ \\
X(p)=X_p\in T_pM\text{ となる関数}$$
と定めると、$p$ を含むチャート $(U,\phi)$ 上において、
$$X(q)=\sum_{i=1}^ma^i(q)\left.\frac{\partial}{\partial x^i}\right|_{q}\quad(\forall q\in U\cap\partial M)$$
と書ける。ここで、$X$ を $\partial M$ に沿ったベクトル場といい、すべての $a^i(q)$ があるチャート $(U,\phi)$ が存在して $U\cap\partial M$ 上で $C^{\infty}$ であるとき、$X$ は $C^{\infty}$ であるという。
<br>

    ・T(∂M)への写像ではない。

---

### 向き






# 多様体上の積分