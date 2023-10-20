
- [$L^p$ 空間](#lp-空間)
  - [一般の測度空間に対する $L^p$ 空間](#一般の測度空間に対する-lp-空間)
    - [Holderの不等式,Minkowskiの不等式](#holderの不等式minkowskiの不等式)
    - [$L^p$空間](#lp空間)
      - [包含関係](#包含関係)
    - [$L^p$関数の可測単関数近似](#lp関数の可測単関数近似)
        - [$L^p-L^q$ ペアリング](#lp-lq-ペアリング)
  - [局所コンパクトHausdorff空間のRadon測度と $L^p$ 空間](#局所コンパクトhausdorff空間のradon測度と-lp-空間)
- [$l^p$空間](#lp空間-1)
  - [数え上げ測度](#数え上げ測度)
  - [$l^p$ 空間](#lp-空間-1)



# $L^p$ 空間

## 一般の測度空間に対する $L^p$ 空間

### Holderの不等式,Minkowskiの不等式

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

    ・Minkowski不等式
    ・可積分関数ではない
    ・三角不等式のこと

 ---

### $L^p$空間

・複素数値可測関数のなすベクトル空間　$\mathcal{L}(X,\mathfrak{M},\mu)$　から構成される同値類の集合 ：
 $$L(X,\mathfrak{M},\mu)$$

- $f\sim g\iff f=g \quad (\mu-a.e.)$

- $\bm{C}$ 上ベクトル空間
- $[f]+[g]=[f+g],\quad\alpha[f]=[\alpha f],\quad \overline{[f]}=[\overline{f}]$

- $f\sim g\Rightarrow f^p\sim g^p$

---

・$$L^p(X,\mathfrak{M},\mu)=\left\{\left(\int_X|f|^pd\mu\right)^{\frac{1}{p}}<\infty\right\}\quad (p\in[1,\infty))$$

- $L^p(X)$ は $\bm{C}$ 上Banach空間

---

・$$L^{\infty}(X,\mathfrak{M},\mu)=\{\inf\{\alpha\in[0,\infty)\ |\ \mu((\alpha<|f|))=0\}<\infty\}\\\ \\
{ただし、}\inf\{\sim\}{の中身が空ならば}\ \infty\ {とする}$$

    ・本質的上限のこと、任意の実数より大きくなる点が零集合

- $\mu((\|f\|_{L^{\infty}}<|f|))=0$
- $L^∞(X)$ は $\bm{C}$ 上Banach空間
  
---

#### 包含関係

・$p_1<p_2<\infty$ とし、$\mu(X)<\infty$ とする。
このとき、$L^{p_2}\sub L^{p_1}$ であって、
$$\|f\|_{L^{p_1}}\le\mu(X)^{(p_2-p_1)/p_1p_2}\|f\|_{L^{p_2}}$$

    ・有限測度空間。

・$p\in[1,\infty)$、$\mu(X)<\infty$ とする。
このとき、$L^{\infty}\sub L^{p}$ であって、
$$\|f\|_{L^{p}}\le\mu(X)^{1/p}\|f\|_{L^{\infty}}$$

---

### $L^p$関数の可測単関数近似

・測度空間 $(X,\mathfrak{M},\mu),\quad p\in[1,\infty]$、$f\in\mathcal{L}^p(X,\mathfrak{M},\mu) $ とする。
このとき、$$|s_n(x)|<|f(x)|\quad(\forall x,\forall n),\quad\lim_{n\to\infty}\|f-s_n\|_{L^p}=0$$を満たす可測単関数列 $s_n$ が存在する。

    ・このとき、s_n は L^p空間の元。

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
 $$(f,g)=\int \overline{f}gd\mu$$は内積。

---

## 局所コンパクトHausdorff空間のRadon測度と $L^p$ 空間

・局所コンパクトHausdorff空間 $X$、Radon測度 $\mu$、$p\in[1,\infty)$、$f\in\mathcal{L}^p(X,\mu)$ とする。
このとき、
$$\exist f_n\subset C_c(X)\text{ であって、}\\\ \\
\lim_{n\to\infty}\|f-f_n\|_{p}=0$$

---
---
---

# $l^p$空間

## 数え上げ測度

    ・数え上げ測度：φなら0、有限要素ならその数、無限集合なら∞。これは測度。

・空でない集合 $X$、有限部分集合 $F\sub X$、数え上げ測度 $\mu:2^X\to[0,\infty]$、$f:X\to[0,\infty]$ とする。
このとき、$$\int_F fd\mu=\sum_{j\in F}f(j)$$

---

## $l^p$ 空間

・空でない集合 $X$、数え上げ測度 $\mu:2^X\to[0,\infty]$ に対して、
$$l^p(X)=L^p(X)=\mathcal{L}^p(X)\quad(p\in[0,\infty])$$

    ・零集合がφしかない。

- $$\|(u_x)_{x\in X}\|_{L^p}=\left(\sum_{x\in X}|u_x|^p\right)^{\frac{1}{p}}\quad(p\in[1,\infty))$$

      ・これらは非負値可測関数の積分になるので、和でよい。

- $$\|(u_x)_{x\in X}\|_{L^{\infty}}=\sup_{x\in X}|u_x|$$

      ・零集合が空だから、本質的上限とか持ち出さなくてよい
    
 ---

・空でない集合 $X$ 、数え上げ測度 $\mu:2^X\to[0,\infty]$、$(u_x)_{x\in X}\in l^1(X)$  に対して、
$$\int ud\mu=\sum_{x\in X}u_x$$

    ・任意の関数で可測。

- 空でない集合 $X$ 、数え上げ測度 $\mu:2^X\to[0,\infty]$ とする。
 このとき、可測単関数の台は有限集合。
 <br>

- 空でない集合 $X$ 、$p\in[1,\infty)$、$f\in l^p(X)$  とする。
 このとき、$$|s_n(x)|<|f(x)|\quad(\forall x,\forall n),\quad\lim_{n\to\infty}\|f-s_n\|_{l^p}=0$$を満たす可測単関数列 $s_n$ が存在する 。


---