
- [基本的な用語、性質](#基本的な用語性質)
        - [総和](#総和)
        - [ノルム環 $X$（多元環かつ積の不等式、$X$ はノルム空間）（resp.Banach）](#ノルム環-x多元環かつ積の不等式x-はノルム空間respbanach)
        - [イデアル](#イデアル)
- [セミノルム](#セミノルム)
  - [セミノルム位相](#セミノルム位相)
        - [セミノルム位相の性質](#セミノルム位相の性質)
  - [汎弱位相](#汎弱位相)
        - [汎弱位相の性質](#汎弱位相の性質)
  - [HahnｰBanachの拡張定理](#hahnｰbanachの拡張定理)
        - [Minkowski汎関数](#minkowski汎関数)
        - [HahnｰBanachの拡張定理](#hahnｰbanachの拡張定理-1)
- [Banach空間](#banach空間)
  - [等長写像](#等長写像)
        - [値域](#値域)
- [Hilbert空間](#hilbert空間)
        - [基本的な性質](#基本的な性質)
        - [準双線形写像](#準双線形写像)
        - [直交：$(u,v)=0$](#直交uv0)
        - [CONS](#cons)
- [Frechet空間](#frechet空間)
        - [Frechet空間 $V$](#frechet空間-v)
        - [平行移動不変距離](#平行移動不変距離)
        - [一様有界性定理](#一様有界性定理)
        - [開写像定理](#開写像定理)
        - [閉グラフ定理](#閉グラフ定理)
- [Sovolev空間　](#sovolev空間)






# 基本的な用語、性質

## 総和 

$$\sum_{j\in J}x_j$$

・定義：ノルム空間 $X$,集合 $J$、対応 $x_j$、$J$ の有限部分集合に包含順序を入れた有向集合 $\mathcal{F}_J$に対して、
ネット列 $(\sum_{j\in F}x_j)_{F\in\mathcal{F}_J}$が収束すること
$$\sum_{j\in J}x_j=\lim_{F\to J}\sum_{j\in F}x_j$$

    ・極大集合J'とか存在するのかな？

---

・総和 $\sum_{j\in J}x_j$ が収束すれば、$\{j∊J|x_j≠0\}$ は高々可算

- $$\sum_{n\in\bm{N}} x_n$$が収束すれば
$$\sum_{n\ge0} x_n$$も収束する。
    
        ・逆は一般に成り立たない

- ノルム空間において、任意のネットは収束値を持てば一意的


---
    
・絶対収束$\sum_{j\in J}\|x_j\|<\infty$

    ・非負実数値のネット

- Banach空間で総和が絶対収束すれば、元の総和 $\sum_{j\in J}x_j$ も収束する

---

・ノルム空間において、$$\sum_{n=1}^{\infty} \|u_n-u_{n-1}\|<\infty$$ ならば、$u_n$ はCauchy列 

---

## ノルム環、Banach環

・多元環かつノルム空間である $X$ に対するノルム環：
$$\|xy\|\le\|x\|\|y\|$$

    ・多元環に単位元は要請しない
    ・Banach環も同様
    ・ノルム環において積は連続。

・$*$-環：$\ *:X\to X$（$X$は多元環）
$(x+y)^*=x^*+y^*\\
(\alpha x)^*=\bar{\alpha}x^*\\
(xy)^*=y^*x^*\\
x^{**}=x$

    ・係数体はRかC
    

・ノルム*-環：$\ *:X\to X\quad(X{は}*{-環かつノルム環})$
$\|x^*\|=\|x\|$

    ・Banach*-環も同様

・$C^*$-環 $X\quad(X{はBanach環かつ}*{-環})$
$\|x^*x\|=\|x\|^2$


- $C^*$-環ならばBanach$*$-環

---

## イデアル

・$\bm{C,R}$ 上多元環 $X$ のイデアル $I$ ：
$I\subset X$ が $\bm{C,R}$ ベクトル空間かつ、$\forall x\in X,\forall y\in I$ に対して $xy,yx\in I$

・$\bm{C,R,}$ 上 $*$-環 $X$ の $*$- イデアル $I$：
$I\subset X$ が $\bm{C,R}$ ベクトル空間かつ、$\forall x\in X,\forall y\in I$ に対して $xy,yx,y^*\in I$

---
---
---

# セミノルム 

## セミノルム位相

$$(p_a:X\to[0,\infty))_{(p,a)\in\mathcal{P}\times X}$$

・ベクトル空間 $V$ に対して、セミノルム：
$$p:V\to [0,\infty),\quad p(x+y)\le p(x)+p(y),p(\alpha x)=|\alpha|p(x)$$

    ・p(x)=0→x=0がない、逆は言えてる

- セミノルムの分離族 $\mathcal{P}$：
$$\{x\in V\ |\ p(x)=0\ (\forall p\in \mathcal{P})\}=\{0\}$$を満たすセミノルムの集合 $\mathcal{P}$
<br>

- セミノルム位相：$$(p_a:V\to[0,\infty))_{(p,a)\in\mathcal{P}\times X},\quad p_a(x)=p(x-a)$$から誘導される始位相

        ・ノルム空間はセミノルム空間：（分離族は||・||だけ）、このとき始位相とノルム空間の位相は一致する。

<br>

・絶対凸 $C$：$C$ は凸集合かつ $|\alpha|\le1,x\in C\Rightarrow\alpha x\in C$

---

##### セミノルム位相の性質

・ネット $x_{\lambda}$ に対して、
$$x_{\lambda}\to x\iff p(x_{\lambda}-x)\to0\ (\forall p\in\mathcal{P})$$したがって、$p\in\mathcal{P}$ はセミノルム位相で連続。

- $V$ はセミノルム位相について位相線形空間

- $x\neq y\in V$ に対して、$\exist(p,a)\in\mathcal{P}\times V$ であって、 $p_a(x)\neq p_a(y)$

- $V$ はセミノルム位相についてHausdorff空間。

- $$V(p_1,...,p_n:\epsilon)=\bigcap_{k=1}^n p_k^{-1}([0,\epsilon)),\ (\epsilon>0)$$は開近傍かつ絶対凸

- $$\{V(p_1,...p_n:\epsilon)\ |\ n\in\bm{N},p_i\in\mathcal{P},\epsilon>0\}$$は $0\in V$ の基本近傍系

- $$\{x+V(p_1,...p_n:\epsilon)\ |\ x\in X,\ n\in\bm{N},p_i\in\mathcal{P},\epsilon>0\}$$は $V$ の基本近傍系。

      ・これがセミノルム空間の位相を定める。

---

## 汎弱位相

・$\bm{C,R}$ 上ベクトル空間 $V$ に対して、
線形汎関数の分離族 $\mathcal{F}$：
$$\{x\in V\ |\ \phi(x)=0\ (\forall \phi\in \mathcal{F})\}=\{0\}$$を満たす線形汎関数の集合 $\mathcal{F}\subset X^*$
<br>

- $\bm{C,R}$ 上ベクトル空間 $V$、線形汎関数の分離族 $\mathcal{F}$ に対して、
$$\mathcal{P}=\{|\phi|\ |\ \phi\in\mathcal{F}\}$$はセミノルムの分離族。
よって、この $\mathcal{P}$ が誘導する $V$ のセミノルム位相を、$\mathcal{F}$ が誘導する $V$ の汎弱位相という。
<br>

- 汎弱位相において、$\phi\in\mathcal{F}$ は連続。

##### 汎弱位相の性質

・

- $\bm{C,R}$ 上ベクトル空間 $V$、線形汎関数の分離族 $\mathcal{F}$、$\phi\in V^*$ に対して、
$\phi\text{ は汎弱位相で連続}\iff\phi\in\mathrm{span}\mathcal{F}$

      ・span Fは汎弱位相で連続な線形汎関数全体

---

## HahnｰBanachの拡張定理

##### Minkowski汎関数

・$\bm{C,R}$ 上ベクトル空間 $V$ とする。 
このとき、Minkowski汎関数 $m:V\to\bm{R}$：
$$m(x+y)\le m(x)+m(y)\\\ \\
\forall\alpha\in[0,\infty)\text{ に対して }m(\alpha x)=\alpha m(x)$$

- セミノルムはMinkowski汎関数

---

##### HahnｰBanachの拡張定理

・$\bm{R}$ 上ベクトル空間 $V$、Minkowski汎関数 $m:V\to\bm{R}$、部分空間 $M\subset V$、線形汎関数 $\phi:M\to\bm{R}$ とする。
このとき、$\phi(x)\le m(x)\ (\forall x\in M)$ ならば、
$$\tilde{\phi}|_M=\phi,\quad\tilde{\phi}(x)\le m(x)\ (\forall x\in X)$$を満たす線形汎関数 $\tilde{\phi}:V\to\bm{R}$ が存在する。

    ・ただ一つではない

- $\bm{C,R}$ 上ベクトル空間 $V$、セミノルム $p:V\to[0,\infty)$、部分空間 $M\subset V$、線形汎関数 $\phi:M\to\bm{R,C}$ とする。
このとき、$|\phi(x)|\le p(x)\ (\forall x\in M)$ ならば、
$$\tilde{\phi}|_M=\phi,\quad\tilde{\phi}(x)\le p(x)\ (\forall x\in X)$$を満たす線形汎関数 $\tilde{\phi}:V\to\bm{R}$ が存在する。

      ・φ(-x)≦p(-x)

- $\bm{C,R}$ 上ノルム空間 $V$、部分空間 $M\subset V$、$\phi\in M^{*}$ とする。
このとき、
$$\tilde{\phi}|_M=\phi,\quad\|\tilde{\phi}\|=\|\phi\|$$を満たす $\tilde{\phi}\in V^*$ が存在する。

      ・今回はノルム空間だから、ちゃんと有界線形汎関数。
      ・M上で制限してノルム取ってる。

- $\bm{C,R}$ 上ノルム空間 $V$、$x_0\in V-\{0\}$ とする。
このとき、
$$\phi(x_0)=\|x_0\|,\quad\|\phi\|=1$$を満たす $\phi\in V^*$ が存在する。

---
---
---

# Banach空間

## 等長写像

・ノルム空間 $V,W$、線形写像 $f:V\to W$ とする。
このとき、等長写像 $f$：
$$\|f(v)\|_2=\|v\|_1$$

---

##### 値域

・Banach空間 $V,W$、等長写像 $f:V\to W$ とする。
このとき、$f(V)$ はBanach空間。

---

# Hilbert空間 

##### 基本的な性質

・ノルム $\|v\|=\sqrt{(v,v)}$

- $|(u,v)|\le\|u\|\|v\|$

- 中線定理：$\|u+v\|^2+\|u-v\|^2=2(\|u\|^2+\|v\|^2)$

<br>

・$\bm{C}$ 上ベクトル空間 $V,W$、準双線形写像 $\Psi:V\times V\to W$ とする。
このとき、$$\Psi(u,v)=\frac{1}{4}\sum_{i=1}^3i^k\Psi(i^ku+v,i^ku+v)$$  

    ・偏極恒等式

- ユニタリ作用素は内積を保つ：$(Uv_1,Uv_2)=(v_1,v_2)$
<br>

- $\bm{R}$ 上ベクトル空間 $V,W$、内積 $\Psi:V\times V\to W$ とする。
このとき、$$\Psi(u,v)=\frac{1}{4}(\Psi(u+v,u+v)-\Psi(u-v,u-v))$$  

      ・双線形写像じゃ無理。
      ・等長作用素は内積を保つ。
  

---

##### 準双線形写像

・反線形写像：
$$T(u+v)=Tu+Tv,\quad T(\alpha u)=\bar{\alpha}Tu$$

・準双線形写像：$\Phi(u,v)$で、第一引数で反線形、第二引数で線形

- 有界双線形：$\|\Phi\|<\infty$
$$\|\Phi\|=\sup\{\|\Phi(u,v)\|\  |\ \|u\|,\|v\|\le1\}=\sup\{\|\Phi(u,v)\ |\ \|u\|,\|v\|=1\}$$

・$\|\Phi(u,v)\|\le\|\Phi|\|u\|\|v\|$

- 双線形写像は、有界ならば連続

      ・準双線形も同様

- 内積 $(\cdot)$ は直積位相で連続で、ノルムは $\|(\cdot)\|\le 1$


---

##### 直交：$(u,v)=0$


- 集合の直交 $(u,v)=0\quad (\forall u\in E,\forall v\in F)$

- 互いに直交する部分空間 $W\perp M$ に対して、和は直和：$W\oplus M$

・直交補空間 $E^{\perp}=\{v\in \mathcal{H}\|\ (u,v)=0,\forall u\in E\}$

- 直交補空間 $E^{\perp}$ は $\mathcal{H}$ の閉部分空間

- $M^{\perp}=(\overline{M})^{\perp}$

- 部分空間 $M$ に対して、$M^{\perp\perp}=\overline{M}$

・閉部分空間 $M$ に対して、
$\mathcal{H}=M\oplus M^{\perp}$

---

##### CONS

・内積空間　$V$ のONS $B_0$：互いに直交する単位ベクトルの集合 $B$。$e_j$　が単射なら添え字付けられているという。

- 内積空間 $V$、$J$ によって添え字付けられた $V$ のONS $e_j$、$v\in V$ とする。
このとき、$$\sum_{j\in J}|(e_j,v)|^2\le\|v\|^2$$特に、$$(e_j,v)\in l^2(J),\\\ \\ \|v-\sum_{j\in F}(e_j,v)e_j\|^2=\|v\|^2-\sum_{j\in F}|(e_j,v)|^2$$

        ・Besselの不等式

---

・Hilbert空間 $\mathcal{H}$ のCONS：ONS $B_0$ であって、$\overline{\mathrm{span}(B)}=\mathcal{H}$ を満たすもの。

- Hilbert空間 $\mathcal{H}$、$J$ によって添え字付けられた $\mathcal{H}$ のONS $e_j\in B_0$、$v\in \overline{\mathrm{span}B_0}$ とする。
このとき、$$\|v\|^2=\sum_{j\in J}|(e_j,v)|^2,\quad v=\sum_{j\in J}(e_j,v)e_j$$が成り立つ。さらに、$$U:\overline{\mathrm{span}B_0}\to l^2(J),\quad U(v)=(e_j,v)_{j\in J}$$はユニタリ作用素。

        ・ユニタリ作用素はノルムを保存する線形同型写像

- $J$ によって添え字付けられた CONS を持つHilbert空間 $\mathcal{H}$ に対して、
$\mathcal{H}\cong l^2(J)$

---

・Hilbert空間 $\mathcal{H}$、$\mathcal{H}$ のONS $B_0$ に対して、
$B_0\subset B$ なる $\mathcal{H}$ のCONS $B$ が存在する。

    ・B_0を含むONS全体の集合は帰納的順序集合

- Hilbert空間 $\mathcal{H}$、$\mathcal{H}$ のCONS $B_1,B_2$ に対して、
$B_1$ と $B_2$ の濃度は等しい。
<br>

- Hilbert空間 $\mathcal{H}$ に対して、
$\mathcal{H}{は可分}\iff \mathcal{H}{のCONSは可算}$

---
---
---

# Frechet空間

##### Frechet空間 $V$

・$\bm{C,R}$ 上セミノルム空間 $V$ とする。
このとき、Frechet空間 $V$：
セミノルム位相を誘導するセミノルムの分離族として高々可算なものが存在し、$V$ の任意のCauchy列が収束する。

- Banach空間はFrechet空間

---

##### 平行移動不変距離

・$\bm{C,R}$ 上Frechet空間 $V$、高々可算なセミノルム分離族 $\mathcal{P}$ とする。
このとき、$$d:V\times V\to [0,\infty)\\\ \\
d(x,y)=\max_{n\in\bm{N}}\frac{1}{n}\frac{p_n(x-y)}{1+p_n(x-y)}$$と定める。

---

- $$\forall x,y,z\in V\text{ に対して、}d(x+z,y+z)=d(x,y)$$

      ・平行移動不変。

- $d$ は $V$ 上の距離。

      ・t/(1+t) は狭義単調増加。

<br>

- 開球 $B(0,r)=\{x\in V\ |\ d(0,x)<r\}$ はFrechet空間において絶対凸な開集合。
<br>

- 距離 $d$ による距離位相はFrechet空間における位相と一致する。したがって、$V$ は $d$ に関して完備である。 

- $$B(x,r)=\{y\in X\ |\ d(y,x)<r\}=\{y'+x\in X\ |\ d(y',0)<r\}$$であって、$$\{B(x,r)\ |\ x\in X,\ r>0\}$$はセミノルム位相についても基本近傍系。

      ・距離位相では基本近傍系。

---

##### 一様有界性定理

・$\bm{C,R}$ 上セミノルム空間 $V$、$B\subset X$ とする。
このとき、$B$ の有界性：$$\forall \text{ 絶対凸な開集合 }U\subset  V\text{ に対して、}\exist r>0\text{ であって、}\\\ \\
B\subset rU=\{rx\ |\ x\in U\}$$

- $\bm{C,R}$ 上セミノルム空間 $X$、$B\subset X$ に対して、
$$B\text{ が有界}\iff\\\ \\
\forall\text{セミノルム位相を与える} p\text{ に対して、}\exist r>0\text{ であって、}\\\ \\
B\subset \{x\in X\ |\ p(x)<r\}$$

      ・後半の集合はr{p(x)<ε}のこと

---

<dl>
<dt>

$\bm{C,R}$ 上セミノルム空間 $X$、$0$ の開近傍 $0\in U\subset\mathcal{N}(0)$ とする。</dt>



<dd>

- $0\in W_0+W_0\subset U$ を満たす絶対凸な $0$ の開近傍 $W_0$ が存在する。
<br>


- $\overline{W}\subset U$ を満たす絶対凸な開集合 $W$ が存在する。

</dd>
</dl>

---

・$\bm{C,R}$ 上Frechet空間 $V$、$\bm{C,R}$ 上セミノルム空間 $W$、添え字付けられた連続線形写像 $f_j:X\to Y$ とする。
このとき、$\forall x\in X\text{ に対して }\{f_j(x)\}\subset Y$ が有界集合ならば、
$$\forall U_2\in\mathcal{N}_W(0_W)\text{ に対して }\exist U_1\in\mathcal{N}_V(0_V)\text{ であって、}\\\ \\f_j(U_1)\subset U_2\ (\forall j)$$

    ・一様有界性定理

- $\bm{C,R}$ 上Frechet空間 $V$、$\bm{C,R}$ 上ノルム空間 $W$、連続線形写像列 $f_n:X\to Y$ とする。
このとき、$\forall x\in X\text{ に対して }\lim f_n(x)\in Y$ ならば、
$$f(x)=\lim_{n\to\infty}f_n(x)$$は連続線形写像。

---

##### 開写像定理

・$\bm{C,R}$ 上Frechet空間 $V,W$、全射連続線形写像 $f:X\to Y$ とする。
このとき、$f$ は開写像。

    ・開写像定理。

- $\bm{C,R}$ 上Frechet空間 $V,W$、連続線形同型写像 $f:X\to Y$ とする。
このとき、$f^{-1}$ は連続。

---

##### 閉グラフ定理

・$\bm{C,R}$ 上Frechet空間 $V,W$、線形写像 $f:V\to W$、グラフ $G(f)=\{(x,f(x))\in V\times W\ |\ x\in V\}$ とする。
このとき、
$$f\text{ は連続}\iff G(f)\text{ は閉集合}$$



---
---
---

# Sovolev空間　