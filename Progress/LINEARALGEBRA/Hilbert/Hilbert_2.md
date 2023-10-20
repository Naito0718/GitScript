
- [基本的な用語、性質](#基本的な用語性質)
  - [総和](#総和)
    - [絶対収束](#絶対収束)
    - [なんかよく出るやつ](#なんかよく出るやつ)
  - [ノルム環、Banach環](#ノルム環banach環)
  - [イデアル](#イデアル)
- [Banach空間](#banach空間)
  - [等長写像](#等長写像)
        - [値域](#値域)
- [Hilbert空間](#hilbert空間)
  - [準双線形写像](#準双線形写像)
    - [有界性](#有界性)
  - [基本的な性質](#基本的な性質)
    - [ノルム](#ノルム)
  - [直交：$(u,v)=0$](#直交uv0)
  - [CONS](#cons)
      - [可算なCONS](#可算なcons)



# 基本的な用語、性質

## 総和 

$$\sum_{j\in J}x_j$$

・ノルム空間 $X$、集合 $J$、対応 $x_j$、$J$ の有限部分集合に包含順序を入れた有向集合 $\mathcal{F}_J$ とする。
このとき、総和 $\sum_{j\in J}x_j$：
$$\text{ネット列 }\left(\sum_{j\in F}x_j\right)_{F\in\mathcal{F}_J}\text{ が収束すること}\\\ \\
\sum_{j\in J}x_j=\lim_{F\to J}\sum_{j\in F}x_j$$

    ・x_jはネットではない。
    ・実数の時の二重級数と同じ。
    

---

・総和 $\sum_{j\in J}x_j$ が収束すれば、$\{j∊J|x_j≠0\}$ は高々可算。

    ・結局、収束するならNのときと同じとしてよい。
<br>

- $$\sum_{n\in\bm{N}} x_n$$が収束すれば
$$\sum_{n\ge0} x_n$$も収束する。
    
        ・逆は一般に成り立たない

- ノルム空間 $X$ において、任意のネットは収束値を持てば一意的。


---

### 絶対収束
    
・絶対収束$\sum_{j\in J}\|x_j\|<\infty$

    ・非負実数値のネット

- Banach空間で総和が絶対収束すれば、元の総和 $\sum_{j\in J}x_j$ も収束する。

---

### なんかよく出るやつ

・ノルム空間において、$$\sum_{n=1}^{\infty} \|u_n-u_{n-1}\|<\infty$$ ならば、$u_n$ はCauchy列。

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
---
---

# Hilbert空間 

## 準双線形写像

<dl><dt>

・反線形写像：
$$T(u+v)=Tu+Tv,\quad T(\alpha u)=\bar{\alpha}Tu\\\ \\$$

- 準双線形写像：$\Phi(u,v)$で、第一引数で反線形、第二引数で線形
<br>

</dt><dd>

- $\bm{C}$ 上ベクトル空間 $V,W$、準双線形写像 $\Psi:V\times V\to W$ とする。
このとき、$$\Psi(u,v)=\frac{1}{4}\sum_{i=1}^3i^k\Psi(i^ku+v,i^ku+v)$$  

      ・偏極恒等式

</dd></dl>

---

### 有界性

<dl><dt>

- 有界双線形：
$$\|\Phi\|<\infty\\\ \\
\|\Phi\|=\sup\{\|\Phi(u,v)\|\  |\ \|u\|,\|v\|\le1\}=\sup\{\|\Phi(u,v)\ |\ \|u\|,\|v\|=1\}\\\ \\$$

・$\|\Phi(u,v)\|\le\|\Phi|\|u\|\|v\|$

    ・全部ノルム空間。

</dt><dd>

- 双線形写像は、有界ならば連続

      ・準双線形も同様。
      ・逆は知らない。
<br>


- 内積空間 $V$ とする。
このとき、内積 $(\cdot)$ は直積位相で連続で、ノルム $\|(\cdot)\|\le 1$

</dd></dl>

---

## 基本的な性質

### ノルム

・ノルム $\|v\|=\sqrt{(v,v)}$

- $|(u,v)|\le\|u\|\|v\|$

- 中線定理：$\|u+v\|^2+\|u-v\|^2=2(\|u\|^2+\|v\|^2)$

---

- ユニタリ作用素は内積を保つ：$(Uv_1,Uv_2)=(v_1,v_2)$
<br>

- $\bm{R}$ 上ベクトル空間 $V,W$、内積 $\Psi:V\times V\to \bm{C}$ とする。
このとき、$$\Psi(u,v)=\frac{1}{4}(\Psi(u+v,u+v)-\Psi(u-v,u-v)+i\Psi(u+iv,u+iv)-i\Psi(u-iv,u-iv))$$  

      ・実内積なら前二項でよい。
      ・等長作用素は内積を保つ。

---

## 直交：$(u,v)=0$

・内積空間 $V$、$E,F\sub V$ とする。
このとき、$E,F$ が直交する：
$$(u,v)=0\quad (\forall u\in E,\forall v\in F)\\\ \\$$

- 内積空間 $V$、互いに直交する部分空間 $W\perp M$ とする。
このとき、和は直和：$W\oplus M$

---

<dl><dt>

・内積空間 $V$、部分集合 $E\sub V$ とする。
このとき、直交補空間：
$$E^{\perp}=\{v\in \mathcal{H}\|\ (u,v)=0,\forall u\in E\}$$
と定めると、これは $V$ の閉部分空間。
<br>

</dt><dd>

- ヒルベルト空間 $V$、部分空間 $M,N\sub V$ とする。
このとき、
$$M^{\perp}=(\overline{M})^{\perp}\\\ \\
M^{\perp\perp}=\overline{M}\\\ \\
V=N\oplus M\text{ かつ }M\perp N\\
\Rightarrow M,N\text{ は閉部分空間}$$

- ヒルベルト空間 $V$、閉部分空間 $M,N\sub V$ とする。
このとき、
$$V=M\oplus M^{\perp}\\\ \\
M\neq V\text{ ならば、}M^{\perp}\neq\{0\}\\\ \\
V=N\oplus M\text{ かつ }M\perp N\\
\Rightarrow M=N^{\perp}$$

</dd></dl>

---

## CONS

・内積空間 $V$ のONS $B_0$：互いに直交する単位ベクトルの集合 $B$。$e_j$ が単射なら添え字付けられているという。

    ・無限個でも添え字付けられることもある。

- 内積空間 $V$、$J$ によって添え字付けられた $V$ のONS $e_j$、$v\in V$ とする。
このとき、$$\sum_{j\in J}|(e_j,v)|^2\le\|v\|^2$$特に、$$((e_j,v))_{j\in J}\in l^2(J),\\\ \\ \|v-\sum_{j\in F}(e_j,v)e_j\|^2=\|v\|^2-\sum_{j\in F}|(e_j,v)|^2$$
正射影 $P:V\to\overline{\mathrm{span}B_0}$ として、
$$Pu=\sum (u,e_k)e_k\\\ \\
(Pu,Pv)=\sum(u,e_k)\overline{(v,e_k)}$$
ここで、最下段の右の和は絶対収束する。

      ・Besselの不等式

---

・Hilbert空間 $\mathcal{H}$ のCONS：ONS $B$ であって、$\overline{\mathrm{span}(B)}=\mathcal{H}$ を満たすもの。

- Hilbert空間 $\mathcal{H}$、$J$ によって添え字付けられた $\mathcal{H}$ のONS $e_j\in B_0$、$v\in \overline{\mathrm{span}B_0}$ とする。
このとき、$$\|v\|^2=\sum_{j\in J}|(e_j,v)|^2,\quad v=\sum_{j\in J}(e_j,v)e_j\\\ \\
(u,v)=\sum (u,e_k)\overline{(v,e_k)}$$が成り立つ。さらに、$$U:\overline{\mathrm{span}B_0}\to l^2(J),\quad U(v)=(e_j,v)_{j\in J}$$はユニタリ作用素。

      ・ユニタリ作用素：全射な等長写像。

- $J$ によって添え字付けられた CONS を持つHilbert空間 $\mathcal{H}$ に対して、
$$\mathcal{H}\cong l^2(J)\quad(\text{ユニタリ同型})$$

---

・Hilbert空間 $\mathcal{H}$、$\mathcal{H}$ のONS $B_0$ とする。
このとき、$$\exist\text{ CONS } B\sub\mathcal{H}\text{ であって、}B_0\subset B$$

    ・B_0を含むONS全体の集合は帰納的順序集合

- Hilbert空間 $\mathcal{H}$、$\mathcal{H}$ のCONS $B_1,B_2$ に対して、
$B_1$ と $B_2$ の濃度は等しい。
<br>

- Hilbert空間 $\mathcal{H}$ に対して、
$$\mathcal{H}{は可分}\iff \mathcal{H}{のCONSは可算}$$

---

#### 可算なCONS



    ・級数のコーシー列使いたいから可算じゃないと無理っぽい。

