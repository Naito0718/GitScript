
- [ノルム空間から生成されるベクトル空間](#ノルム空間から生成されるベクトル空間)
  - [部分空間](#部分空間)
  - [商ノルム空間](#商ノルム空間)
  - [双対空間 $X$\*](#双対空間-x)
    - [作用素ノルム](#作用素ノルム)
      - [弱\*-位相](#弱-位相)
        - [Alaogluの定理](#alaogluの定理)
        - [第二双対空間への埋め込み](#第二双対空間への埋め込み)
        - [弱位相](#弱位相)
- [Banach空間から生成されるベクトル空間](#banach空間から生成されるベクトル空間)
  - [閉部分空間](#閉部分空間)
  - [商Banach空間](#商banach空間)
  - [$l^p$ 直和Banach空間](#lp-直和banach空間)
- [Hilbert空間から生成されるベクトル空間](#hilbert空間から生成されるベクトル空間)
  - [閉部分空間](#閉部分空間-1)
  - [双対空間 $X$\*](#双対空間-x-1)
  - [直和Hilbert空間](#直和hilbert空間)
- [閉区間上の複素数値連続関数](#閉区間上の複素数値連続関数)
  - [有限次元](#有限次元)




# ノルム空間から生成されるベクトル空間

## 部分空間

・$\bm{R,C}$ 上ノルム空間 $V$、部分空間 $M\sub V$ とする。
このとき、$\overline{M}$ は $V$ の閉部分空間。

---

## 商ノルム空間

 ・ノルム空間 $X$、閉部分空間 $M\subset X$、商空間 $X/M$、商写像 $x\mapsto[x]$ に対して、
 $$\|[x]\|=\inf\{\|x-y\| \ |\ y\in M\}$$　と定める

 - $X/M$はノルム空間

 ---

## 双対空間 $X$*

### 作用素ノルム

・$\bm{R,C}$上ノルム空間 $V$ とする。
このとき、
$$V^*=B(X,\bm{C,R})\\\ \\
\|T\|=\sup\{\|T(x)\|_Y\ |\ x\in X,\ \|x\|_X\le1\}\\\ \\
=\sup\{\|T(x)\|\ |\ x\in X,\ \|x\|=1\}$$
は $\bm{R,C}$ 上Banach空間

    ・線形写像 f:X→C,R に対して、一様連続⇔双対空間の元

---

#### 弱*-位相

    ・作用素ノルムとは違う？
    ・結局V^*は有界作用素全体だと思うけど

・$\bm{C,R}$ 上ノルム空間 $V$、$x\in V$ に対して、
$$\iota(x):V^*\to\bm{F},\quad\iota(x)(\phi)=\phi(x)$$は $V^*$ 上線形汎関数。

- $\|\iota(x)\|\le\|\phi\|\|x\|$、よって、$\iota(x)\in V^{**}$
<br>

- $\bm{C,R}$ 上ノルム空間 $V$ に対して、
$$\iota(X)=\{\iota(x)\ |\ x\in V\}$$は $V^*$ 上の線形汎関数の分離族。
そこで、$\iota(X)$ が誘導する $V^*$ 上の汎弱位相を弱$*$-位相という。

---

・ $\iota(c_1x_1+c_2x_2)=c_1\iota(x_1)+c_2\iota(x_2)$
<br>

- $\bm{C,R}$ 上ノルム空間 $V$、ネット $\phi_{\lambda}\in V^*$、$\phi\in V^*$ に対して、
$$\text{弱*-位相において }\phi_{\lambda}\to\phi\iff\forall x\in V\text{ に対して }\phi_{\lambda}(x)\to\phi(x)$$

- $\iota(X)={弱}^*-{位相において連続な}\ V^*\ {上の線形汎関数全体}$

--- 

##### Alaogluの定理

・$\bm{C,R}$ 上ノルム空間 $V$ に対して、
単位ノルム開球$$(V^*)_1=\{\phi\in V^*\ |\ \|\phi\|\le1\}$$は弱*-位相でコンパクト。

    ・ι(x)!

---

##### 第二双対空間への埋め込み

・$\bm{C,R}$ 上ノルム空間 $V$、$$\iota(x):V^*\to\bm{C,R},\quad\iota(x)(\phi)=\phi(x)$$とする。
このとき、$$\iota:V\to V^{**},\quad x\mapsto\iota(x)$$と定める。

    ・第二双対空間への埋め込み

- $\iota$ は単射線形写像。

- $\|x\|=\|\iota(x)\|$

      ・作用素ノルム

---

・$\bm{C,R}$ 上Banach空間 $V$ とする。
このとき、$\iota(B)\subset B^{**}$はBanach空間。

---

##### 弱位相

・$\bm{C,R}$ 上ノルム空間 $V$ とする。
このとき、$V^*$ は $V$ 上の線形汎関数の分離族。
よって、$V^*$ が誘導する $V$ 上の汎弱位相を、$V$ の弱位相という。

- $\bm{C,R}$ 上ノルム空間 $V$、ネット $x_{\lambda}\subset V$、$x\in X$ に対して、
$$x_{\lambda}\to x\iff \forall\phi\in V^{*}\text{ に対して }\phi(x_{\lambda})\to\phi(x)$$

- $\bm{C,R}$ 上ノルム空間 $V$ に対して、
弱位相に関して連続な線形汎関数全体は $V^*$ に一致する。


---


# Banach空間から生成されるベクトル空間

## 閉部分空間

・$\bm{R,C}$ 上Banach空間 $V$、部分空間 $M\subset V$ とする。
このとき、
$$M\text{ が }V\text{ のノルムでBanach空間}\iff\overline{M}=M$$

---

## 商Banach空間

・Banach空間 $X$ の商空間 $M$ はBanach空間

---

## $l^p$ 直和Banach空間

・空でない集合 $J$、$\bm{C}$ 上Banach空間 $X_j$、$(x_j)\in\Pi_{j\in J}X_j$ に対して、
このとき、$$\|(x_j)_{j\in J}\|_p=\left(\sum_{j\in J} \|x_j\|_j^p\right)^{\frac{1}{p}}\\\ \\
\|(x_j)_{j\in J}\|_{\infty}=\sup_{j\in J}\|x_j\|_j$$と定める。

    ・別に実数上でもいい。

- $j\mapsto \|x_{j}\|$ は、数え上げ速度空間 $(J,2^J,\mu)$ に対する非負値可測関数
<br>

- $\|(x_j)_{j\in J}\|_p$ は、数え上げ速度空間 $(J,2^J,\mu)$ の $L^p(J)$ における $L^p$ ノルム

- $$\bigoplus_{j\in J}^{(p)}X_j=\{(x_j)_{j\in J}\in\Pi_{j\in J}X_j\ |\ \|(x_j)_{j\in J}\|<\infty\}$$はBanach空間で、直積線形空間 $\Pi X_j$ の部分空間

        ・l^p直和Banach空間

---
---
---

# Hilbert空間から生成されるベクトル空間

## 閉部分空間

・$\bm{R,C}$ 上Hilbert空間 $V$、部分空間 $M\subset V$ とする。
このとき、
$$M\text{ が }V\text{ の内積でHilbert空間}\iff\overline{M}=M$$

---

## 双対空間 $X$*

・$\bm{C}$ 上ヒルベルト空間 $\mathcal{H}$、双対空間 $\mathcal{H}^*$に対して、
$\mathcal{H}\ni \mapsto (v,\cdot)\in\mathcal{H}^*$
は全単射反線形写像で、　$\|v\|=\|(v,\cdot)\|$

    ・別に0でも成り立つ
    ・実数上なら線形写像。

---

## 直和Hilbert空間

・空でない集合 $J$、$\bm{C}$ 上Hilbert空間 $\mathcal{H}_j$、$l^2$ 直和Banach空間 $\oplus_{j\in J}\mathcal{H}_j$ 、$u,v\in\oplus_{j\in J}\mathcal{H}_j$とする。
このとき、$$(u,v)=\sum_{j\in J}(u_j,v_j)_j$$と定める。

    ・別に実数上でもいい。

- $\sum_{j\in J}|(u_j,v_j)|\le\|u\|\|v\|$、特に、$(u_j,v_j)_{j\in J}\in l^1(J)$
<br>

- $\oplus_{j\in J}\mathcal{H}_j$ はHilbert空間

---


# 閉区間上の複素数値連続関数
$C[a,b]$$

・ノルム$\|u\|=\sup|u(x)|$

    ・点列（関数列）の収束は一様収束と同値
    ・このノルムではBanach空間

---

・ノルム$\|u\|=\int|u(x)|$

    ・このノルムではBanach空間でない


## 有限次元

・$\bm{C}^n$

    ・|u|=sup|u_k|$もノルム

・$n$次多項式全体$\bm{C}_n[x]$

    ・n+1次元

---
---
---



