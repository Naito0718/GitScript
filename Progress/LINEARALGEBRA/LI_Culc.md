- [ベクトル空間 $V$](#ベクトル空間-v)
        - [基底の存在](#基底の存在)
        - [セミノルム](#セミノルム)
        - [凸集合 $C$](#凸集合-c)
        - [$C$ 上ベクトル空間を $R$ 上ベクトル空間とみる](#c-上ベクトル空間を-r-上ベクトル空間とみる)
- [位相線形空間](#位相線形空間)
        - [コーシー列](#コーシー列)
        - [開集合](#開集合)
        - [線形写像](#線形写像)
- [ノルム空間](#ノルム空間)
  - [性質](#性質)
        - [同値なノルム](#同値なノルム)
  - [コーシー列](#コーシー列-1)
  - [凸集合](#凸集合)
        - [絶対凸](#絶対凸)
        - [Hahn-Banachの分離定理](#hahn-banachの分離定理)
        - [Krein-Milmanの端点定理](#krein-milmanの端点定理)
  - [有限次元](#有限次元)
- [Hilbert空間](#hilbert空間)
        - [最適近似](#最適近似)
- [ベクトル空間から生成されるベクトル空間](#ベクトル空間から生成されるベクトル空間)
  - [生成される部分空間](#生成される部分空間)
  - [双対空間 $V$\*](#双対空間-v)
        - [基本的な性質](#基本的な性質)
        - [第二双対空間への埋め込み](#第二双対空間への埋め込み)
  - [商空間](#商空間)
  - [テンソル積](#テンソル積)
        - [線形独立性](#線形独立性)
        - [普遍性](#普遍性)
        - [有限次元](#有限次元-1)
        - [テンソル積写像](#テンソル積写像)
        - [テンソル積のテンソル積](#テンソル積のテンソル積)
  - [反対称テンソル](#反対称テンソル)
- [ノルム空間から生成されるベクトル空間](#ノルム空間から生成されるベクトル空間)
        - [商ノルム空間](#商ノルム空間)
  - [双対空間 $X$\*](#双対空間-x)
        - [作用素ノルム](#作用素ノルム)
        - [弱\*-位相](#弱-位相)
        - [Alaogluの定理](#alaogluの定理)
        - [第二双対空間への埋め込み](#第二双対空間への埋め込み-1)
        - [弱位相](#弱位相)
- [Banach空間から生成されるベクトル空間](#banach空間から生成されるベクトル空間)
        - [商Banach空間](#商banach空間)
        - [$l^p$ 直和Banach空間](#lp-直和banach空間)
- [Hilbert空間から生成されるベクトル空間](#hilbert空間から生成されるベクトル空間)
        - [双対空間 $X$\*](#双対空間-x-1)
        - [直和Hilbert空間](#直和hilbert空間)
        - [閉区間上の複素数値連続関数](#閉区間上の複素数値連続関数)
  - [有限次元](#有限次元-2)
- [Frechet空間から生成されるFrechet空間](#frechet空間から生成されるfrechet空間)
        - [閉部分空間](#閉部分空間)
        - [直積空間](#直積空間)








# ベクトル空間 $V$

##### 基底の存在

・$\bm{C,R}$ 上ベクトル空間 $V$、部分集合 $D\subset V$ が $D\backslash\{0\}\neq\phi$ を満たすとする。
このとき、$$\mathrm{span}(D_0)=\mathrm{span}(D)$$を満たす線形独立な $D_0\subset D$ が存在する。

- $\bm{C,R}$ 上ベクトル空間 $V$、線形独立な部分集合 $B,C$ とする。
このとき、$\mathrm{span}(B)=\mathrm{span}(C)$ ならば、
$B,C$ の濃度は等しい。
<br>

- $\bm{C,R}$ 上ベクトル空間 $V$、線形独立な部分集合 $B\subset V$ とする。
このとき、$B\subset C$ を満たす $V$ の基底 $C$ が存在する。

---

##### セミノルム

・$\phi\in V^*$ に対して、
$$|\phi|:V\to[0,\infty),\quad|\phi|(x)=|\phi(x)|$$はセミノルム。

---

##### 凸集合 $C$

・凸集合の共通部分は凸集合。

- 部分空間は凸集合。
<br>

- $\bm{C,R}$ 上ベクトル空間 $V$、$x\in V$ に対して、
$\{x\}$ は凸集合。
<br>

- $\bm{C,R}$ 上ベクトル空間 $V$、凸集合 $A,B\subset V$、$\alpha\in\bm{C,R}$ に対して、
$A+B,\alpha A$ は凸集合。

---

##### $C$ 上ベクトル空間を $R$ 上ベクトル空間とみる

・実数上の線形写像 $\phi:V_{\bm{R}}\to\bm{R}$ に対して、
$$\psi(x)=\phi(x)-i\phi(ix)$$は $\bm{C}$ 上の線形写像。

---

# 位相線形空間

    ・T_1なら位相群

## コーシー列

・$\bm{C,R}$ 上の位相線形空間 $V$、点列 $x_n\subset V$ とする。
このとき、コーシー列 $x_n$：
$$\forall N\in\mathcal{N}(0)\text{ に対して、}\exist n_0\in\bm{N}\text{ であって、}\\\ \\
n,m\ge n_0\Rightarrow x_n-x_m\in N$$ 

---

## 開集合

・$\bm{C,R}$ 上位相線形空間 $V$、開集合 $O\subset V$、$x\in O$ とする。
このとき、$$\exist \mu\in(0,1)\text{ であって、}\frac{1}{\mu}x\in O\\\ \\
\forall w\in V\text{ に対して、}\exist\delta>0\text{ であって、}x+\epsilon w\in O$$

- $\bm{C,R}$ 上位相線形空間 $V$、$0$ の開近傍 $0\in N(0)\in\mathcal{N}(0) V$、$x\in V$ とする。
このとき、$$\exist\delta>0\text{ であって、}\epsilon x\in N(0)$$

---

## 閉包

・$\bm{C,R}$ 上位相線形空間 $V$、部分空間 $M\subset V$ に対して、
$$\overline{M}\subset V$$は部分空間


---

## 線形写像

・$\bm{C,R}$ 上位相線形空間 $V,W$、線形写像 $f:V\to W$、$x\in V$、$f(x)\in N_W(f(x))\in\mathcal{N}_W(f(x))$ とする。
このとき、$$f^{-1}(N_W(f(x)))=f^{-1}(N_V(0_V))+x$$となる $0_V\in N_V(0_V)\in\mathcal{N}_V(0_V)$ が存在する。

- $\bm{C,R}$ 上位相線形空間 $V,W$、線形写像 $f:V\to W$、$x\in V$ とする。
このとき、$f$ が $0_V\in V$ で連続ならば、$f$ は連続。
<br>



---

# ノルム空間

## 性質

・和 $u+v$ 、スカラー倍 $\alpha u$ （スカラーも点列）、ノルム $\|u\|$ は連続

---

・ 任意の開球 $B(a,r)$ 閉球 $\overline{B(a,r)}$は凸集合

- 任意の部分空間も凸集合

・凸集合は弧状連結

---

### 同値なノルム

・ベクトル空間 $V$、$V$ 上のノルム $\|\cdot\|_1,\|\cdot\|_2$ とする。
このとき、同値なノルム：
$$\exist a_1,a_2>0\text{ であって、}\\\ \\
a_1\|u\|_1\le \|u\|_2\le a_2\|u\|_1$$

    ・これは対称な条件。

- 同値なノルムについて、一方のノルムについての収束列は、他方のノルムでも収束列。

- 同値なノルムについて、一方のノルムについての完備ならば、他方のノルムでも完備。

- 同値なノルムについて、一方のノルムについての位相は、もう一方のノルムの位相と一致する。

---

## コーシー列

・$X$をノルム空間、$x_n$をコーシー列とするとき、
$x_n$ が $x$ に収束する部分列を持てば、$x_n$ は $x$ に収束する

---

## 凸集合

### 絶対凸

・$\bm{C,R}$ 上のベクトル空間 $V$ に対して、
絶対凸 $C$：$C$ は凸集合かつ $x\in C,\ |\alpha|\le1$ に対して、$\alpha x\in C$

- 絶対凸の共通部分は絶対凸。

---

### Hahn-Banachの分離定理

・$\bm{C,R}$ 上の位相線形空間、$0\in C\subset V$ を $0$ の凸開近傍とする。
このとき、$$m:V\to[0,\infty)\\\ \\
m(x)=\inf\{\lambda\in(0,\infty)\ |\ \frac{1}{\lambda}x\in C\}$$と定める。

- $m:X\to[0,\infty)$ はMinkowski汎関数。

- $C=\{x\in V\ |\ m(x)<1\}$

---

・$\bm{C,R}$ 上の位相線形空間 $V$、凸集合 $A,B\subset V$ であって、$A$ は開集合かつ $A\cap B=\phi$ とする。
このとき、
$$\mathrm{Re}(\phi(x))< t\le\mathrm{Re}(\phi(y))\quad(\forall x\in A,\forall y\in B)$$を満たす $V$ 上の連続な線形汎関数 $\phi$、$t\in\bm{R}$ が存在する。

    ・Hahn-Banachの分離定理
    ・左側は真の不等式
    ・このとき、Reφ は実数上の線形写像。

- $2$ つのセミノルム位相 $\mathcal{O}_1,\mathcal{O}_2$ を持つ $\bm{C,R}$ 上のベクトル空間 $V$ とする。
このとき、$\mathcal{O}_1$ に関して連続な線形汎関数全体と $\mathcal{O}_2$ に関して連続な線形汎関数全体が一致するならば、
$$\forall \text{ 凸集合 }C\subset V\text{ に対して、 }\\\ \\
C\ {が}\ \mathcal{O}_1\text{ について閉}\iff C\ {が}\ \mathcal{O}_2\text{ について閉}$$

      ・凸集合は位相関係ない。

- セミノルム位相を持つ $\bm{C,R}$ 上のベクトル空間 $V$、閉凸集合 $C\subset V$ とする。
このとき、
$$\forall x\in V-C\text{ に対して、}x\in C'\text{ かつ }C\cap C'=\phi$$ を満たす絶対凸な開近傍 $C'$ が存在する。
<br>

- $\bm{C,R}$ 上ノルム空間、凸集合 $C\subset V$ とする。
このとき、$$C\text{ がノルム位相で閉}\iff C\text{ が弱位相で閉}$$

---

#### 部分閉空間と分離定理

・$\bm{C,R}$ 上ノルム空間 $V$、閉部分空間 $W$、$b\notin W$ とする。
このとき、$$\phi(x)=0\quad(x\in W),\quad \phi(b)\neq0$$を満たす連続線形汎関数 $\phi:V\to \bm{C,R}$ が存在する。

---

### Krein-Milmanの端点定理

・$\bm{C,R}$ 上ベクトル空間 $V$、凸集合 $C\subset V$ に対して、
$C$ のフェイス $F\subset C$：
$$F\text{ は凸集合}\\\ \\
\{(x,y)\in C\times C\ |\ \exist t\in(0,1)\text{ であって、}(1-t)x+ty\in F \}\subset F\times F\\\ \\$$

- $\bm{C,R}$ 上ベクトル空間 $V$、凸集合 $C\subset V$ に対して、
$C$ の端点 $x\in C$：$$\{x\}\ {が}\ C\ {のフェイス}$$
ここで、$C$ の端点全体を $\mathrm{ext}(C)$ と書く。
<br>

- $\bm{C,R}$ 上ベクトル空間 $V$、$E\subset V$ に対して、
凸包 $$\mathrm{conv}(E)=\{\sum_{j=1}^n t_j x_j\ |\ n\in\bm{N},\ t_j\ge0,\ \sum_{j=1}^nt_j=1,\ x_j\in E\}$$は $E$ を含む最小の凸集合。

---

・$\bm{C,R}$ 上セミノルム空間 $V$、$C\subset X$ を空でないコンパクト凸集合とする。
このとき、
$$\mathrm{ext}(C)\neq\phi\\\ \\
C=\overline{\mathrm{conv}(\mathrm{ext}(C))}$$

    ・Krein-Milmanの端点定理

---

## 有限次元

・有限次元ノルム空間はBanach空間

- 線形同型写像 $\Phi:\bm{C^n,R}^n\to X,\Phi(x)=x_iu_i$ に対して、
$\Phi,\Phi^{-1}$ は共に有界線形作用素

---
---
---


# Hilbert空間

##### 最適近似

・ヒルベルト空間 $\mathcal{H}$、閉凸集合 $C$ 、$u\in\mathcal{H}$ に対して、ある $u_0\in C$ であって 
$$\|u-u_0\|=d(u,C)$$

    ・d(u,C)はCとのinf距離のこと

---

# ベクトル空間から生成されるベクトル空間

## 生成される部分空間

・ベクトル空間 $V$、部分集合　$E\subset V$ とする。
このとき、$$\mathrm{span}(E)=\{E{の元の線形結合全体}\}$$はベクトル空間

---

## 双対空間 $V$*

##### 基本的な性質

・$\bm{C,R}$ 上ベクトル空間 $V$、$\phi,\phi_1,...,\phi_n\in V^*$ に対して、
$$\bigcap_{i=1}^n\ker\phi_i\subset\ker\phi$$が成り立つならば、
$$\phi=\sum c_i\phi_i$$と書ける。

---

・$\bm{C,R}$ 上ベクトル空間 $V$、線形独立な族 $e_j\subset V$ とする。
このとき、$$\phi_i(e_j)=\begin{cases}
1  & (i=j)  \\
0  & (i\neq j) \\
\end{cases}$$を満たす線形独立な族 $\phi_j\subset V^*$ が存在する。

---

##### 第二双対空間への埋め込み

・$\bm{C,R}$ 上ベクトル空間 $V$ とする。
このとき、第二双対空間への埋め込み：
$$\iota:V\to V^{**}\\\ \\
\iota(v)(\phi)=\phi(x)$$

- $\iota$ は単射。

---

## 商空間

・$\bm{C,R}$ 上ベクトル空間 $V$、部分空間 $M\subset V$ とする。
このとき、同値関係：
$$x\sim y\iff x-y\in M$$による同値類全体は $\bm{C,R}$ 上ベクトル空間。

    ・多元環、*-環に対してはイデアルを考えれば、再び多元環、*-環になる。
    ・商写像は全射で、線形、多元環準同型、*-環準同型。

---

・$\bm{C,R}$ 上ベクトル空間 $V$、部分空間 $M\subset V$ とする。
このとき、$$\dim(V)=\dim(M)+\dim(V/M)$$

    ・基底の要素数に厳密に一致する。（無限集合でも）

---

## テンソル積

・$\bm{C,R}$ 上ベクトル空間 $V_1,...,V_n$ に対して、
$n$ 重線形写像のなす空間：$ML(\Pi^n V^*_i,\bm{C,R})$ は $\bm{C,R}$ 上ベクトル空間。

    ・双対空間上

- $\bm{C,R}$ 上ベクトル空間 $V_1,...,V_n$、$v_i\in V_i$ に対して、
$$v_1\otimes...\otimes v_n:\Pi_{i=1}^n V^*_i\to \bm{F}\\\ \\
v_1\otimes...\otimes v_n(\phi_1,...,\phi_n)=\phi_1(v_1)...\phi_n(v_n)$$は $ML(\Pi^n V^*_i,\bm{C,R})$ の要素。
<br>

- $\bm{C,R}$ 上ベクトル空間 $V_1,...,V_n$ に対して、
$$V_1\otimes...\otimes V_n=\mathrm{span}\{v_1\otimes...\otimes v_n\ |\ v_i\in V_i\}$$はベクトル空間。
<br>

- $\bm{C,R}$ 上ベクトル空間 $V_1,...,V_n$ に対して、
$$V_1\times...\times V_n\ni (v_1,...,v_n)\mapsto v_1\otimes...\otimes v_n\in V_1\otimes...\otimes V_n$$は $n$ 重線形写像。

---

##### 線形独立性

・$\bm{C,R}$ 上ベクトル空間 $V_1,...,V_n$、線形独立な族 $e_{i,j}\in V_i$ とする。
このとき、$$e_{1,j_1}\otimes...\otimes e_{n,j_n}\in V_1\otimes...\otimes V_n$$は線形独立な族。

---

##### 普遍性

・$\bm{C,R}$ 上ベクトル空間 $V_1,...,V_n,W$、$n$ 重線形写像 $\Phi:V_1\times...\times V_n\to W$ とする。
このとき、
$$\Psi:V_1\otimes...\otimes V_n\to W\\\ \\
\Psi(v_1\otimes...\otimes v_n)=\Phi(v_1,...,v_n)$$を満たすものがただ一つ存在する。

---

##### 有限次元

・$\bm{C,R}$ 上有限次元ベクトル空間 $V_1,...,V_n$、$v_i\in V_i$ に対して、
$$V_1\otimes...\otimes V_n=ML(\Pi^n V^*_i,\bm{C,R})$$

---

##### テンソル積写像

---

##### テンソル積のテンソル積


---

## 反対称テンソル

---
---
---

# ノルム空間から生成されるベクトル空間

## 商ノルム空間

 ・ノルム空間 $X$、閉部分空間 $M\subset X$、商空間 $X/M$、商写像 $x\mapsto[x]$ に対して、
 $$\|[x]\|=\inf\{\|x-y\| \ |\ y\in M\}$$　と定める

 - $X/M$はノルム空間

 ---

## 双対空間 $X$*

##### 作用素ノルム

 ・$\bm{C,R}$上ノルム空間 $X$ の双対空間：$$X^*=B(X,\bm{C,R})$$はBanach空間

    ・線形写像 f:X→C,R に対して、一様連続⇔双対空間の元

---

##### 弱*-位相

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

・$\bm{C,R}$ 上Banach空間 $V$、部分空間 $M\subset V$ とする。
このとき、
$$M\text{ が }V\text{ のノルムでBanach空間}\iff\overline{M}=M$$

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

・$\bm{C,R}$ 上Hilbert空間 $V$、部分空間 $M\subset V$ とする。
このとき、
$$M\text{ が }V\text{ の内積でHilbert空間}\iff\overline{M}=M$$

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

# Frechet空間から生成されるFrechet空間

##### 閉部分空間

・Frechet空間 $V$、閉部分空間 $M\subset V$ とする。
このとき、$M$ は自然にFrechet空間。

- セミノルムの分離族：$\mathcal{P}=\{p_n|_M\ |\ n\in\bm{N}\}$

- $M$ のセミノルム位相は、相対位相と一致する。

##### 直積空間

・Frechet空間 $V,W$ とする。
このとき、$V\times W$ は自然にFrechet空間。

- セミノルムの分離族：$\mathcal{P}=\{p_{V,n}+p_{W,n}\ |\ n\in\bm{N}\}$

- $M$ のセミノルム位相は、直積位相と一致する。