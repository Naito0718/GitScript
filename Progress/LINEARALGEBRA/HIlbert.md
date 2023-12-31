- [基本的な用語、性質](#基本的な用語性質)
        - [ノルム空間](#ノルム空間)
        - [総和](#総和)
        - [ノルム環$X$（多元環かつ積の不等式、$X$はノルム空間）（resp.Banach）](#ノルム環x多元環かつ積の不等式xはノルム空間respbanach)
        - [商ノルム](#商ノルム)
        - [イデアル](#イデアル)
- [セミノルム](#セミノルム)
        - [セミノルム位相](#セミノルム位相)
- [Banach空間論](#banach空間論)
        - [コーシー列](#コーシー列)
        - [有限次元](#有限次元)
        - [商空間](#商空間)
- [Hilbert空間](#hilbert空間)
        - [用語](#用語)
        - [CONS](#cons)
- [Frechet空間](#frechet空間)
        - [Frechet空間 $V$](#frechet空間-v)
- [Sovolev空間　](#sovolev空間)


# 基本的な用語、性質

##### ノルム空間

・和、スカラー倍（スカラーも点列）、ノルムは連続

→任意の開球 $B(a,r)$ 閉球 $\overline{B(a,r)}$は凸集合、したがって弧状連結

- 任意の部分空間も凸集合

---

##### 総和 

$$\sum_{j\in J}x_j$$

・定義：ノルム空間 $X$,集合 $J$、対応 $x_j$、$J$ の有限部分集合に包含順序を入れた有向集合 $\mathcal{F}_J$に対して、
ネット列 $(\sum_{j\in F}x_j)_{F\in\mathcal{F}_J}$が収束すること
$$\sum_{j\in J}x_j=\lim_{F\to J}\sum_{j\in F}x_j$$

    ・極大集合J'とか存在するのかな？

---

・性質

→総和が収束すれば、$\{j∊J|x_j≠0\}$ は高々可算

→$Σ_{\bm{N}} x_n$が収束すれば$Σ_{n\ge0} x_n$も収束する。（eventually性）
    
    ・逆は一般に成り立たない

・収束値を持てば一意的

---
    
・絶対収束$\sum_{j\in J}\|x_j\|<\infty$（非負実数値のネット）

→Banach空間で総和が絶対収束すれば、元の総和 $\sum_{j\in J}x_j$ も収束する

---

・$$\sum_{n=1}^{\infty} \|u_n-u_{n-1}\|<\infty$$ ならば、$u_n$ はCauchy列 

---

##### ノルム環 $X$（多元環かつ積の不等式、$X$ はノルム空間）（resp.Banach）

・ノルム環 $X\quad(X{は多元環かつノルム空間})$：
$\|xy\|\le\|x\|\|y\|$

    ・多元環に単位元は要請しない
    ・Banach環も同様

・$*$-環：$\ *:X\to X$（$X$は多元環）
$(x+y)^*=x^*+y^*\\
(\alpha x)^*=\bar{\alpha}x^*\\
(xy)^*=y^*x^*\\
x^{**}=x$

    ・係数体はRかC
    

・ノルム*-環$\ *:X\to X\quad(X{は}*{-環かつノルム環})$
$\|x^*\|=\|x\|$

    ・Banach*-環も同様

・$C^*$-環 $X\quad(X{はBanach環かつ}*{-環})$
$\|x^*x\|=\|x\|^2$


- $C^*$-環ならばBanach$*$-環

---

##### 商ノルム

・ノルム空間 $X$、閉部分空間 $M\subset X$、商空間 $X/M$、商写像 $x\mapsto[x]$ に対して、
$$\|[x]\|=\inf\{\|x-y\| \ |\ y\in M\}$$　と定める

→
$X/M$はノルム空間

---

##### イデアル

・$\bm{C(R)}$上多元環 $X$ のイデアル$I$：
$I\subset X$が$\bm{C(R)}$ベクトル空間かつ、$\forall x\in X,\forall y\in I$ に対して $xy,yx\in I$

・$\bm{C(R)}$上 $*$-環 $X$ の $*$- イデアル $I$：
$I\subset X$が$\bm{C(R)}$ベクトル空間かつ、$\forall x\in X,\forall y\in I$ に対して $xy,yx,y^*\in I$

---
---
---

# セミノルム 

##### セミノルム位相

$$(p_a:X\to[0,\infty))_{(p,a)\in\mathcal{P}\times X}$$

・ベクトル空間 $V$ に対して、セミノルム：$p:V\to [0,\infty),\quad p(x+y)\le p(x)+p(y),p(\alpha x)=|\alpha|p(x)$

    ・p(x)=0→x=0がない、逆は言えてる

- セミノルムの分離族 $\mathcal{P}$：$\{x\in V\ |\ p(x)=0\ (\forall p\in \mathcal{P})\}=\{0\}$

- セミノルム位相：$$(p_a:V\to[0,\infty))_{(p,a)\in\mathcal{P}\times X},\quad p_a(x)=p(x-a)$$から誘導される始位相

        ・ノルム空間はセミノルム空間

・絶対凸$C$：$C$ は凸集合かつ $|\alpha|\le1,x\in C\Rightarrow\alpha x\in C$

---

・ネット $x_{\lambda}$ に対して、
$x_{\lambda}\to x\iff p(x_{\lambda}-x)\to0\ (\forall p)$

- $V$ はセミノルム位相について位相線形空間

- $$V(p_1,...,p_n:\epsilon)=\bigcap p_k^{-1}([0,\epsilon)),\ (\epsilon>0)$$は開近傍かつ絶対凸

- $$\{V(p_1,...p_n:\epsilon)\ |\ n\in\bm{N},p_i\in\mathcal{P},\epsilon>0\}$$は $0\in V$ の基本近傍系

---
---
---

# Banach空間論

##### コーシー列

・$X$をノルム空間、$x_n$をコーシー列とするとき、
$x_n$ が $x$ に収束する部分列を持てば、$x_n$ は $x$ に収束する

---

##### 有限次元

・有限次元ノルム空間はBanach空間

→線形同型写像 $\Phi:\bm{C^n,R}^n\to X,\Phi(x)=x_iu_i$に対して、$\Phi,\Phi^{-1}$は共に有界線形作用素

---

##### 商空間

・Banach空間 $X$ の商空間 $M$ はBanach空間

---
---
---

# Hilbert空間 

##### 用語

・ノルム $\|v\|=\sqrt{(v,v)}$

- $|(u,v)|\le\|u\|\|v\|$

- 中線定理：$\|u+v\|^2+\|u-v\|^2=2(\|u\|^2+\|v\|^2)$

<br>

・$\bm{C}$ 上ベクトル空間 $V,W$、準双線形写像 $\Psi:V\times V\to W$ とする。
このとき、$$\Psi(u,v)=\frac{1}{4}\sum_{i=1}^3i^k\Psi(i^ku+v,i^ku+v)$$  

    ・偏極恒等式

- ユニタリ作用素は内積を保つ：$(Uv_1,Uv_2)=(v_1,v_2)$


---

・ヒルベルト空間 $\mathcal{H}$、閉凸集合 $C$ 、$u\in\mathcal{H}$ に対して、ある $u_0\in C$ であって 
$$\|u-u_0\|=d(u,C)$$

    ・最適近似
    ・d(u,C)はinfのこと

---

##### 準双線形写像

・反線形写像：
$$T(u+v)=Tu+Tv,\quad T(\alpha u)=\bar{\alpha}Tu$$
<br>

・準双線形写像：$\Phi(u,v)$で、第一引数で反線形、第二引数で線形

- 有界双線形：$\|\Phi\|<\infty$
$$\|\Phi\|=\sup\{\|\Phi(u,v)\|\  |\ \|u\|,\|v\|\le1\}=\sup\{\|\Phi(u,v)\ |\ \|u\|,\|v\|=1\}$$

・$\|\Phi(u,v)\|\le\|\Phi|\|u\|\|v\|$

- 双線形写像は、有界ならば連続

      ・準双線形も同様

- 内積 $(\cdot)$ は直積位相で連続で、ノルムは $\|(\cdot)\|\le 1$

---

・ヒルベルト空間 $\mathcal{H}$、双対空間 $\mathcal{H}^*$に対して、
$\mathcal{H}\ni \mapsto (v,\cdot)\in\mathcal{H}^*$
は全単射反線形写像で、　$\|v\|=\|(v,\cdot)\|$

    ・別に0でも成り立つ

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
このとき、$$\sum_{j\in J}|(e_j,v)|^2\le\|v\|^2$$特に、$$(e_j,v)\in l^2(J),\\\ \\ \|v-\sum_{j\in F}(e_j,v)e_j\|^2=\|v\|^2-\sum_{j\in F}|(e_j,v)|^2$$。

        ・Besselの不等式

---

・Hilbert空間　$\mathcal{H}$ のCONS：ONS $B_0$ であって、$\overline{\mathrm{span}(B)}=\mathcal{H}$ を満たすもの。

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

##### 直和Hilbert空間

・空でない集合 $J$、$\bm{C}$ 上Banach空間 $X_j$、$(x_j)\in\Pi_{j\in J}X_j$ に対して、
このとき、$$\|(x_j)_{j\in J}\|_p=\left(\sum_{j\in J} \|x_j\|_j^p\right)^{\frac{1}{p}}\\\ \\
\|(x_j)_{j\in J}\|_{\infty}=\sup_{j\in J}\|x_j\|_j$$と定める。

- $j\mapsto \|x_{j}\|$ は、数え上げ速度空間 $(J,2^J,\mu)$ に対する非負値可測関数
<br>

- $\|(x_j)_{j\in J}\|_p$ は、数え上げ速度空間 $(J,2^J,\mu)$ の $L^p(J)$ における $L^p$ ノルム

- $$\bigoplus_{j\in J}^{(p)}X_j=\{(x_j)_{j\in J}\in\Pi_{j\in J}X_j\ |\ \|(x_j)_{j\in J}\|<\infty\}$$はBanach空間で、直積線形空間 $\Pi X_j$ の部分空間

        ・l^p直和Banach空間

---

・空でない集合 $J$、$\bm{C}$ 上Hilbert空間 $\mathcal{H}_j$、$l^2$ 直和Banach空間 $\oplus_{j\in J}\mathcal{H}_j$ 、$u,v\in\oplus_{j\in J}\mathcal{H}_j$とする。
このとき、$$(u,v)=\sum_{j\in J}(u_j,v_j)_j$$と定める。

- $\sum_{j\in J}|(u_j,v_j)|\le\|u\|\|v\|$、特に、$(u_j,v_j)_{j\in J}\in l^1(J)$
<br>

- $\oplus_{j\in J}\mathcal{H}_j$ はHilbert空間

---
---
---

# Frechet空間

##### Frechet空間 $V$

・$\bm{C,R}$ 上セミノルム空間 $V$ であって、セミノルム分離族が高々可算で、 $V$ の任意のCauchy列が収束する

    ・Banach空間はFrechet空間

- ベクトル空間におけるCauchy列：$n,m\ge\exist n_0\Rightarrow x_n-x_m\in N(0)$

---
  

---
---
---

# Sovolev空間　