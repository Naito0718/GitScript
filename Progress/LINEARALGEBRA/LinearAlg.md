# 有限次元ベクトル空間

・基底と次元

    ・次元がnであることと基底がn個であることは同値

---

# $K$-右加群

## 定義

・加群 $V$、斜体 $K$ に対して、
$K$-右加群 $V$：
$$x\lambda\in V\\\ \\
x(\lambda\mu)=(x\lambda)\mu\\\ \\
x(\lambda+\mu)=x\lambda+x\mu\\\ \\
(x+y)\lambda=x\lambda+y\lambda\\\ \\
x1=x$$

    ・スカラー倍が逆なら左K-加群。

- 可換体 $K$ 上ベクトル空間 $V$：
$$x\lambda=\lambda x\in V\text{ であって、}V\text{ は右 }K\text{-加群}$$

      ・このとき、明らかにVは左K-加群。

---

## 基底

## $K$-右準同型写像

・$K$-右加群 $V_1,V_2$、$f:V_1\to V_2$ とする。
このとき、$K$-右準同型写像 $f$：
$$f(x+y)=f(x)+f(y)\\\ \\
f(x\lambda)=f(x)\lambda$$

- $K$-右加群 $V_1,V_2$、全単射な$K$-右準同型写像 $f:V_1\to V_2$ とする。
このとき、$f^{-1}$ は $K$-右準同型写像。

      ・全単射K-右準同型をK-右同型という。

---

# Banach単位的ノルム環

    ・Banach空間かつノルム環で乗法単位元を持つ。
    ・第一可算だから点列でよい。

##### 正規収束

・$\bm{C,R}$ 上Banach単位的多元環 $A$、集合 $Y$、$u_i:Y\to A$ とする。
このとき、正規収束級数：$\sum u_i(y)$：
$$\|u_p(y)\|\le c_p,\quad\sum c_p(y)\in\bm{C,R}$$

- $\sum u_i(y)$ は各点において絶対収束する。
- $\sum u_i(y)$ は一様収束する。
- $Y$ が位相空間かつ $u_i(y)$ が連続ならば、$\sum u_i(y)$　は連続関数。

---

##### 収束半径

・$\bm{C,R}$ 係数ベキ級数 $F(x)=\sum a_ix^i$ に対して、
収束半径 $\rho$：
$$\rho=\sup\{r\ge0\ |\ \sum|a_i|r^i\in\bm{R}\}$$

    ・ρ>0 ならば収束ベキ級数という。

---

・$\bm{C,R}$ 上Banach単位的多元環 $A$、$\bm{C,R}$ 係数収束ベキ級数 $F(x)=\sum a_ix^i$、収束半径 $\rho>0$ とする。
<br>

- $$\sum a_i\xi_i\quad(\{\xi\ |\ \|\xi\|\le r<\rho,\ 0<r\}$$は正規収束する。
<br>

- $$F(\xi):\{\xi\ |\ \|\xi\|<\rho\}\to\bm{C,R}\\\ \\
F(\xi)=\sum a_i\xi^i$$は連続関数。 

---

・$K$ 係数形式的ベキ級数 $F(x)=\sum a_ip^i$ 、収束半径 $\rho$ とする。

- $$\frac{1}{\rho}=\overline{\lim_{n\to\infty}}|a_n|^{1/n}\\\ \\
\frac{1}{\rho}=\lim_{n\to\infty}|\frac{a_n}{a_{n+1}}|$$

- $F'(x)=\sum_{n\ge1}na_nx^{n-1}$ において、収束半径は $F(x)$ と一致する。
<br>

- $F:\{z\in\bm{C,R}\ |\ |z|<\rho\}\to\bm{C,R},\quad F(z)=\sum a_nz^n$ とする。
このとき、$F$ は微分可能で、
$$\frac{d}{dz}F(z)=F'(z)=\sum_{n\ge1}na_nz^{n-1}$$

      ・実数上でも0を含む開区間で一致すればF(x)=G(x)