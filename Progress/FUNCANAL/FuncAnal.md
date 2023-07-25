- [関数解析](#関数解析)
  - [連続関数環](#連続関数環)
        - [連続関数環 $C(X)$](#連続関数環-cx)
        - [局所コンパクトHausdorff空間 $X$ 上の連続関数環](#局所コンパクトhausdorff空間-x-上の連続関数環)
  - [作用素](#作用素)
        - [有界作用素](#有界作用素)
    - [Banach空間上の有界線形作用素](#banach空間上の有界線形作用素)
        - [有限次元ノルム空間 $X$](#有限次元ノルム空間-x)
    - [Hilbert空間上の有界線形作用素](#hilbert空間上の有界線形作用素)
        - [共役作用素](#共役作用素)
  - [$L^p$空間](#lp空間)
        - [Holderの不等式、Minkowskiの不等式](#holderの不等式minkowskiの不等式)
        - [$L^p$空間](#lp空間-1)
  - [$l^p$空間](#lp空間-2)


# 関数解析


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
$$C_0(X)=\{f\in C(X)\ |\ \forall\epsilon>0{に対して}(|f|>\epsilon){はコンパクト}\}$$は$C_b(X)$の閉集合

    ・これ和で閉じる？スカラー倍、イデアル積、対合では閉じてる

- そもそも $(|f|>\epsilon)$ は閉集合

・位相空間$X$に対して、 
$$C_c(X)=\{f\in C(X)\ |\ suppf{はコンパクト}\}$$

    ・イデアル積、スカラー倍では閉じてる


- $C_c(X)\subset C_0(X)$

---

##### 局所コンパクトHausdorff空間 $X$ 上の連続関数環

・ $0$拡張：$\tilde{f}:\tilde{X}\to\bm{C}$
$f:X\to\bm{C}$ と一点コンパクト化 $\tilde{X}$ に対して、
$$\tilde{f}(x)=f(x)\ (x\in X),\quad\tilde{f}(x)=0\ (x\in\tilde{X}-X)\\\ \\$$

- $\overline{C_c(X)}=C_0(X)$

- $\tilde{X}$を一点コンパクト化、$\tilde{f}$を$f:X\to\bm{C}$の$0$拡張とすると、
$$f\in C_0(X)\iff \tilde{f}\in C(\tilde{X})$$


---

## 作用素

---

##### 有界作用素

・$\bm{C,R}$上ノルム空間 $X,Y$に対して、
$$L(X,Y)=\{f:X\to Y\ |\ f{は線形作用素}\}$$はベクトル空間

→有界線形作用素のなす空間：
 $B(X,Y)=\{T\in L(X,Y)\ |\ \|T\|<\infty\}\\\ \\ 
\|T\|=\sup\{\|T(x)\|_Y\ |\ x\in X,\ \|x\|_X\le1\}=\sup\{\|T(x)\|\ |\ x\in X,\ \|x\|=1\}$

→ 
$B(X,Y)$はノルム空間かつ $L(X,Y)$の部分空間

→
$T\in L(X,Y)$に対して、
$T\in B(X,Y)\iff T{は一様連続}\iff T{は}\ 0\in X{で連続}$

→有界線形性は合成 $T\circ S$ で保たれる

---

・$\bm{C,R}$上ノルム空間 $X$に対して、
$$L(X)=\{f:X\to X\ |\ f{は線形作用素}\}$$は合成によって$\bm{C,R}$上多元環

→有界線形作用素のなす空間：
 $B(X)=\{T\in L(X)\ |\ \|T\|<\infty\}\\\ \\ 
\|T\|=\sup\{\|T(x)\|\ |\ x\in X,\ \|x\|\le1\}=\sup\{\|T(x)\|\ |\ x\in X,\ \|x\|=1\}$

-  $B(X)$はノルム環かつ $L(X)$の部分空間

- $\|ST\|\le \|S\|\|T\|$



---

・ノルム空間 $X$ 、Banach空間 $Y$ に対して、 $B(X,Y)$ はBanach空間

・$\bm{C,R}$上ノルム空間 $X$ の双対空間：$X^*=B(X,\bm{C,R})$

→これはBanach空間

---

・ノルム空間 $X$、Banach空間 $Y$、部分空間 $M\subset X$、$T\in B(X,Y)$とする。
このとき、$\overline{T}|_M=T,\ \|\overline{T}\|=\|T\|$ を満たす $\overline{T}:\overline{M}\to Y$がただ一つ存在する 

---

・$T:X\to Y$が有界線形作用素ならば、$\ker T,Im T$ は閉部分空間

---

### Banach空間上の有界線形作用素

##### 有限次元ノルム空間 $X$

・$X$を $\bm{C,R}$上有限次元ノルム空間、 $Y$ を $\bm{C,R}$ 上ノルム空間、 $T:X\to Y$ を線形作用素とすると、 $T$ は有界線形

---

### Hilbert空間上の有界線形作用素

##### 共役作用素

---

・Hilbert空間$\mathcal{H_1,H_2}$、$T\in B(\mathcal{H_1,H_2})$ に対して、
$$\|T\|=\|T^*\|,\quad (Tu,v)_{2}=(u,T^*v)_1$$であって$T^{*}\in B(\mathcal{H_2,H_1})$ であるものがただ一つ存在する


    ・u,vは同じ元

- Hilbert空間$\mathcal{H_1,H_2}$、$T\in B(\mathcal{H_1,H_2})$ に対して、$$\Phi(u,v)=(Tu,v)_2$$は $\|\Phi\|=\|T\|$ を満たす有界準双線形汎関数

- Hilbert空間$\mathcal{H_1,H_2}$、有界準双線形汎関数 $\Phi:\mathcal{H_1\times H_2}\to\bm{C,R}$ に対して、 
$$\Phi(u,v)=(u,T^* v),\quad \|\Phi\|=\|T^*\|$$を満たす $T^*\in B(\mathcal{H_2,H_1})$ がただ一つ存在する

---

・$\bm{C,R}$ 上Hilbert空間 $\mathcal{H}$ に対して、Banach環 $B(\mathcal{H})$ は共役演算に対して $C^*$-環

- $(Im T)^{\perp}=\ker T^*$

  
---


## $L^p$空間

##### Holderの不等式、Minkowskiの不等式

・共役指数$1/p+1/q=1\ (p,q\in(1,\infty))$

    ・(1,∞)の場合も含めてよい
    ・x^{1-t}y^t≦(1-t)x+ty (t∊[0,1],x,y∊(0,∞))
    ・(p-1)q=p

・$(X,\mathfrak{M},\mu)$を測度空間、$p,q$を共役指数、$f,g:X\to[0,\infty]$を可測関数とすると、$\int_X fgd\mu\le(\int_Xf^pd\mu)^{\frac{1}{p}}(\int_Xg^qd\mu)^{\frac{1}{q}}$ （Holder不等式）

    ・可積分関数ではない

・$(X,\mathfrak{M},\mu)$を測度空間、$p\in(1,\infty)$、$f,g:X\to[0,\infty]$を可測関数とすると、$(\int_X(f+g)^pd\mu)^{\frac{1}{p}}\le(\int_Xf^pd\mu)^{\frac{1}{p}}+(\int_Xg^pd\mu)^{\frac{1}{p}}$ (Minkowski不等式)

    ・可積分関数ではない

---

##### $L^p$空間

・複素数値可測関数$\mathcal{L}(X,\mathfrak{M},\mu)$から構成される同値類$L(X,\mathfrak{M},\mu)$

    ・f~g⇔a.e.f=g
    ・複素数C上ベクトル空間で、積、複素共役がwell-defined

・$L^p(X,\mathfrak{M},\mu)=\{(\int_X|f|^pd\mu)^{\frac{1}{p}}<\infty\}\ (p\in[1,\infty))$

    ・L^pはノルム空間かつベクトル空間

・$L^{\infty}(X,\mathfrak{M},\mu)=\{\inf\{\alpha\ge0\ |\ \mu((\alpha<|f|))=0\}<\infty\}$

    ・本質的上限のこと、任意の実数より大きくなる点が零集合
    ・L^∞はノルム空間かつベクトル空間

---

## $l^p$空間



---





---

