
- [位相線形空間](#位相線形空間)
  - [コーシー列](#コーシー列)
  - [開集合](#開集合)
  - [閉包](#閉包)
  - [線形写像](#線形写像)
- [ノルム空間](#ノルム空間)
  - [性質](#性質)
    - [同値なノルム](#同値なノルム)
  - [コーシー列](#コーシー列-1)
  - [凸集合](#凸集合)
    - [絶対凸](#絶対凸)
    - [Hahn-Banachの分離定理](#hahn-banachの分離定理)
      - [部分閉空間と分離定理](#部分閉空間と分離定理)
    - [Krein-Milmanの端点定理](#krein-milmanの端点定理)




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

