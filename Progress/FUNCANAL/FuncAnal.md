- [一章](#一章)
  - [連続関数環](#連続関数環)
        - [連続関数環 $C(X)$](#連続関数環-cx)
        - [局所コンパクトHausdorff空間 $X$ 上の連続関数環](#局所コンパクトhausdorff空間-x-上の連続関数環)
- [二章](#二章)
  - [作用素](#作用素)
        - [有界作用素](#有界作用素)
    - [Banach空間上の有界線形作用素](#banach空間上の有界線形作用素)
        - [有限次元ノルム空間 $X$](#有限次元ノルム空間-x)
    - [Hilbert空間上の有界線形作用素](#hilbert空間上の有界線形作用素)
        - [共役作用素](#共役作用素)
- [三章](#三章)
  - [$L^p$空間](#lp空間)
        - [Holderの不等式、Minkowskiの不等式](#holderの不等式minkowskiの不等式)
        - [$L^p$空間](#lp空間-1)
        - [$L^p$関数の可測単関数近似](#lp関数の可測単関数近似)
        - [$L^p-L^q$ ペアリング](#lp-lq-ペアリング)
- [四章](#四章)
  - [$l^p$空間](#lp空間-2)
        - [数え上げ測度と $l^p$ 空間](#数え上げ測度と-lp-空間)


# 一章

## 連続関数環 

・$\{f:X\to\bm{C}\ |\ \sup |f|\in[0,\infty)\}$は$\bm{C}$上ベクトル空間

→ $\|f\|=\sup |f|\in[0,\infty)$ はノルム
 
    ・supノルム

---

##### 連続関数環 $C(X)$

・位相空間$X$に対して、
$$C(X)=\{X{上の連続複素数値関数全体}\}$$ は$\bm{C}$上可換単位的$*$-環

・位相空間$X$に対して、
$$C_b(X)=\{f\in C(X)\ |\ f{は有界}\}$$は$C^*$-環で、$C(X)$の部分$*$-環

・位相空間$X$に対して、
$$C_0(X)=\{f\in C(X)\ |\ \forall\epsilon>0{に対して}(|f|>\epsilon){はコンパクト}\}$$は$C_b(X)$の閉集合かつ $*$-イデアル

    ・補集合を考えるとよい！

- そもそも $(|f|>\epsilon)$ は閉集合

・位相空間$X$に対して、 
$$C_c(X)=\{f\in C(X)\ |\ suppf{はコンパクト}\}$$は$*$-イデアル

- $C_c(X)\subset C_0(X)$
- $f\in C_{c}(X)$ に対して、$|f|\in C_c(X)$
- $f,g\in C_{c,\bm{R}}(X)$ に対して、$\max\{f,g\}\in C_{c,\bm{R}}(X)$

---

##### 局所コンパクトHausdorff空間 $X$ 上の連続関数環

・ $0$拡張：$\tilde{f}:\tilde{X}\to\bm{C}$
$f:X\to\bm{C}$ と一点コンパクト化 $\tilde{X}$ に対して、
$$\tilde{f}(x)=f(x)\ (x\in X),\quad\tilde{f}(x)=0\ (x\in\tilde{X}-X)\\\ \\$$

- $\overline{C_c(X)}=C_0(X)$

- $\tilde{X}$を一点コンパクト化、$\tilde{f}$を$f:X\to\bm{C}$の$0$拡張とすると、
$$f\in C_0(X)\iff \tilde{f}\in C(\tilde{X})$$


---

# 二章

## 作用素

---

##### 有界作用素

・$\bm{C,R}$上ノルム空間 $X,Y$に対して、
$$L(X,Y)=\{f:X\to Y\ |\ f{は線形作用素}\}$$はベクトル空間

- 有界線形作用素のなす空間：
 $B(X,Y)=\{T\in L(X,Y)\ |\ \|T\|<\infty\}\\\ \\ 
\|T\|=\sup\{\|T(x)\|_Y\ |\ x\in X,\ \|x\|_X\le1\}=\sup\{\|T(x)\|\ |\ x\in X,\ \|x\|=1\}$
<br>

- $B(X,Y)$はノルム空間かつ $L(X,Y)$の部分空間
<br>

- $T\in L(X,Y)$に対して、
$T\in B(X,Y)\iff T{は一様連続}\iff T{は}\ 0\in X{で連続}$
<br>

- 有界線形性は合成 $T\circ S$ で保たれる

---

・$\bm{C,R}$上ノルム空間 $X$に対して、
$$L(X)=\{f:X\to X\ |\ f{は線形作用素}\}$$は合成によって$\bm{C,R}$上多元環

- 有界線形作用素のなす空間：
$$B(X)=\{T\in L(X)\ |\ \|T\|<\infty\}\\\ \\ 
\|T\|=\sup\{\|T(x)\|\ |\ x\in X,\ \|x\|\le1\}=\sup\{\|T(x)\|\ |\ x\in X,\ \|x\|=1\}$$

-  $B(X)$はノルム環かつ $L(X)$の部分空間

- $\|ST\|\le \|S\|\|T\|$



---

・ノルム空間 $X$ 、Banach空間 $Y$ に対して、 $B(X,Y)$ はBanach空間

・$\bm{C,R}$上ノルム空間 $X$ の双対空間：$$X^*=B(X,\bm{C,R})$$はBanach空間

---

・ノルム空間 $X$、Banach空間 $Y$、部分空間 $M\subset X$、$T\in B(X,Y)$とする。
このとき、$\overline{T}|_M=T,\ \|\overline{T}\|=\|T\|$ を満たす $\overline{T}:\overline{M}\to Y$がただ一つ存在する 

---

・$T:X\to Y$が有界線形作用素ならば、$\ker T,Im T$ は閉部分空間

---

### Banach空間上の有界線形作用素

##### 有限次元ノルム空間 $X$

・$X$を $\bm{C,R}$上有限次元ノルム空間、 $Y$ を $\bm{C,R}$ 上ノルム空間、 $T:X\to Y$ を線形作用素とする。
このとき、 $T$ は有界線形

---

### Hilbert空間上の有界線形作用素

---

##### 共役作用素



・Hilbert空間$\mathcal{H_1,H_2}$、$T\in B(\mathcal{H_1,H_2})$ に対して、
$$\|T\|=\|T^*\|,\quad (Tu,v)_{2}=(u,T^*v)_1$$であって$T^{*}\in B(\mathcal{H_2,H_1})$ であるものがただ一つ存在する


    ・u,vは同じ元

- Hilbert空間$\mathcal{H_1,H_2}$、$T\in B(\mathcal{H_1,H_2})$ に対して、$$\Phi(u,v)=(Tu,v)_2$$は $\|\Phi\|=\|T\|$ を満たす有界準双線形汎関数
<br>

- Hilbert空間$\mathcal{H_1,H_2}$、有界準双線形汎関数 $\Phi:\mathcal{H_1\times H_2}\to\bm{C,R}$ に対して、 
$$\Phi(u,v)=(u,T^* v),\quad \|\Phi\|=\|T^*\|$$を満たす $T^*\in B(\mathcal{H_2,H_1})$ がただ一つ存在する

---

・$\bm{C,R}$ 上Hilbert空間 $\mathcal{H}$ に対して、Banach環 $B(\mathcal{H})$ は共役演算に対して $C^*$-環

- $(Im T)^{\perp}=\ker T^*$

  
---
---
---

# 三章

## $L^p$空間

##### Holderの不等式、Minkowskiの不等式

・共役指数：$\frac{1}{p}+\frac{1}{q}=1\quad (p,q\in(1,\infty))$

    ・(1,∞)の場合も含めてよい

- $$x^{1-t}y^t≦(1-t)x+ty \quad(t∊[0,1],x,y∊(0,∞))$$

- $(p-1)q=p$

---

・測度空間 $(X,\mathfrak{M},\mu)$、共役指数 $p,q$、可測関数 $f,g:X\to[0,\infty]$ とする。
このとき、$$\int_X fgd\mu\le\left(\int_Xf^pd\mu\right)^{\frac{1}{p}}\left(\int_Xg^qd\mu\right)^{\frac{1}{q}}$$

    ・Holderの不等式
    ・可積分関数ではない

・測度空間 $(X,\mathfrak{M},\mu),\quad p\in(1,\infty)$、可測関数 $f,g:X\to[0,\infty]$とする。
このとき、$$\left(\int_X(f+g)^pd\mu\right)^{\frac{1}{p}}\le\left(\int_Xf^pd\mu\right)^{\frac{1}{p}}+\left(\int_Xg^pd\mu\right)^{\frac{1}{p}}$$ 

    ・(Minkowski不等式)
    ・可積分関数ではない
    ・三角不等式のこと

---

##### $L^p$空間

・複素数値可測関数のなすベクトル空間　$\mathcal{L}(X,\mathfrak{M},\mu)$　から構成される同値類の集合 ：
$$L(X,\mathfrak{M},\mu)$$

- $f\sim g\iff f=g \quad (\mu-a.e.)$

- $\bm{C}$ 上ベクトル空間
- $[f]+[g]=[f+g],\quad\alpha[f]=[\alpha f],\quad \overline{[f]}=[\overline{f}]$

- $f\sim g\Rightarrow f^p\sim g^p$

---

・$$L^p(X,\mathfrak{M},\mu)=\left\{\left(\int_X|f|^pd\mu\right)^{\frac{1}{p}}<\infty\right\}\quad (p\in[1,\infty))$$

- $L^p(X)$ はBanach空間
- $f\in L^p(X)\Rightarrow f\in L^1(x)$

<br>

・$$L^{\infty}(X,\mathfrak{M},\mu)=\{\inf\{\alpha\in[0,\infty)\ |\ \mu((\alpha<|f|))=0\}<\infty\}\\\ \\
{ただし、}\inf\{\sim\}{の中身が空ならば}\ \infty\ {とする}$$

    ・本質的上限のこと、任意の実数より大きくなる点が零集合

- $\mu((\|f\|_{L^{\infty}}<|f|))=0$
- $L^∞(X)$ はBanach空間
  
---

##### $L^p$関数の可測単関数近似

・測度空間 $(X,\mathfrak{M},\mu),\quad p\in[1,\infty]$、$f\in\mathcal{L}^p(X,\mathfrak{M},\mu) $ とする。
このとき、$$|s_n(x)|<|f(x)|\quad(\forall x,\forall n),\quad\lim_{n\to\infty}\|f-s_n\|_{L^p}=0$$を満たす可測単関数列 $s_n$ が存在する 

- 可測空間 $(X,\mathfrak{M})$、有界な可測関数 $f:X\to\bm{C}$ とする。
このとき、$f$ に一様収束する可測単関数列 $s_n$ が存在する

---

##### $L^p-L^q$ ペアリング

・測度空間 $(X,\mathfrak{M},\mu)$、共役指数 $p,q\in[1,\infty]$、$f\in L^p,\ g\in L^q$ とする。
このとき、$$\|fg\|_{L^1}\le \|f\|_{L^p}\|g\|_{L^q}$$

    ・(1,∞)でもよい

- 測度空間 $(X,\mathfrak{M},\mu)$、共役指数 $p,q\in[1,\infty]$ とする。
このとき、$$\Psi:L^p\times L^q\to\bm{C},\quad\Psi(f,g)=\int fgd\mu$$は有界双線形汎関数

      ・ノルムは1以下
      ・手前で共役取ったら準双線形

<br>

- 測度空間 $(X,\mathfrak{M},\mu)$ とする。
このとき、$f,g\in L^2(X)$に対して、
$$(f,g)=\int \overline{f}gd\mu$$は内積

---
---
---


# 四章

## $l^p$空間

##### 数え上げ測度と $l^p$ 空間

・空でない集合 $X$ 、数え上げ測度 $\mu:2^X\to[0,\infty]$ に対して、
$$l^p(X)=L^p(X)=\mathcal{L}^p(X)\quad(p\in[0,\infty])$$

- $$\|(u_x)_{x\in X}\|_{L^p}=\left(\sum_{x\in X}|u_x|^p\right)^{\frac{1}{p}}\quad(p\in[1,\infty))$$

        ・これらは非負値可測関数

- $$\|(u_x)_{x\in X}\|_{L^p}=\sup_{x\in X}|u_x|$$

        ・零集合が空だから、本質的上限とか持ち出さなくてよい
    
---

・空でない集合 $X$ 、数え上げ測度 $\mu:2^X\to[0,\infty]$、$(u_x)_{x\in X}\in l^1(X)$  に対して、
$$\int ud\mu=\sum_{x\in X}u_x$$

- 空でない集合 $X$ 、数え上げ測度 $\mu:2^X\to[0,\infty]$ とする。
このとき、可測単関数の台は有限集合。
<br>

- 空でない集合 $X$ 、$p\in[1,\infty)$、$f\in l^p(X)$  とする。
このとき、$$|s_n(x)|<|f(x)|\quad(\forall x,\forall n),\quad\lim_{n\to\infty}\|f-s_n\|_{l^p}=0$$を満たす可測単関数列 $s_n$ が存在する 。


---





---

