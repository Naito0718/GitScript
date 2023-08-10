# 実解析

# 一変数での広義積分

##### 広義積分

・関数$f:[a.b)\to\bm{R}$が $\forall[a,u]$ で可積分かつ $\int_a^{\to b}fdx\in \bm{R}$

    ・両側可積分は積分区間を分割する

→関数$f:[a.b)\to\bm{R}$が $\forall[a,u]$ で可積分ならば、
$\int_a^{\to b}fdx\in \bm{R}\iff\forall\epsilon>0{に対して}\exist c\in I{であって}c<v<u<b{ならば}|\int_v^uf(x)dx|<\epsilon$

---

・絶対収束：$|f|$が広義可積分なこと

→$\int fdx$が絶対収束するならば、$\int fdx$は収束する

→$|f(x)|\le g(x)$かつ広義可積分な$g(x)$が存在すれば、$\int|f(x)|dx\le\int g(x)dx$（絶対収束）

---

##### 収束判定

→関数$f:[a.b)\to\bm{R}$が $\forall[a,u]$ で可積分とする

・$b=\infty$ で $f(x)=O(x^{\alpha})(x\to\infty)$を$\alpha<-1$で満たすならば、$\int_a^{\infty}f(x)dx\in\bm{R}$

---

・$b\in\bm{R}$ で $f(x)=O((b-x)^{\alpha})(x\to -b)$を$\alpha>-1$で満たすならば、$\int_a^{\to b}f(x)dx\in\bm{R}$

---
---
---

# 無限級数

##### 複素級数と同様に成り立つこと

    ・すべて複素変数と同様に証明できる。

・$K$ 係数形式的ベキ級数 $F(x)=\sum a_ip^i$ 、収束半径 $\rho$ とする。

- $$\frac{1}{\rho}=\overline{\lim_{n\to\infty}}|a_n|^{1/n}\\\ \\
\frac{1}{\rho}=\lim_{n\to\infty}|\frac{a_n}{a_{n+1}}|$$

      ・級数の収束

- $F'(x)=\sum_{n\ge1}na_nx^{n-1}$ において、収束半径は $F(x)$ と一致する。

      ・項別微分

- $F:\{z\in\bm{C,R}\ |\ |z|<\rho\}\to\bm{C,R},\quad F(z)=\sum a_nz^n$ とする。
このとき、$F$ は微分可能で、
$$\frac{d}{dz}F(z)=F'(z)=\sum_{n\ge1}na_nz^{n-1}$$

      ・実数上でも0を含む開区間で一致すればF(x)=G(x)
