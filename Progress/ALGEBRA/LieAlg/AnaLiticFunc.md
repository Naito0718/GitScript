
- [Banach単位的ノルム環](#banach単位的ノルム環)
  - [収束ベキ級数](#収束ベキ級数)
    - [正規収束](#正規収束)
    - [収束半径](#収束半径)
    - [演算と収束](#演算と収束)
      - [和と積](#和と積)
      - [合成](#合成)
      - [線形写像とベキ級数](#線形写像とベキ級数)
    - [収束する指数写像](#収束する指数写像)
- [多変数実解析的写像](#多変数実解析的写像)
  - [正規収束](#正規収束-1)
  - [収束域](#収束域)
  - [多変数実解析的写像](#多変数実解析的写像-1)
    - [演算と収束](#演算と収束-1)
      - [和と積](#和と積-1)
      - [合成](#合成-1)
      - [線形写像とベキ級数](#線形写像とベキ級数-1)
    - [収束する指数写像](#収束する指数写像-1)


# Banach単位的ノルム環

    ・Banach空間かつノルム環で乗法単位元を持つ。
    ・第一可算だから点列でよい。

## 収束ベキ級数

### 正規収束

・Banach単位的 $\bm{C,R}$-代数 $A$、集合 $Y$、$u_i:Y\to A$ とする。
このとき、正規収束級数：$\sum u_i(y)$：
$$\|u_i(y)\|\le c_i,\quad\sum c_i(y)\in\bm{C,R}$$

- $\sum u_i(y)$ は各点において絶対収束する。
- $\sum u_i(y)$ は一様収束する。
- $Y$ が位相空間かつ $u_i(y)$ が連続ならば、$\sum u_i(y)$　は連続関数。

---

### 収束半径

・$\bm{C,R}$ 係数ベキ級数 $F(x)=\sum a_ix^i$ に対して、
収束半径 $\rho$：
$$\rho=\sup\{r\ge0\ |\ \sum|a_i|r^i\in\bm{R}\}$$

    ・ρ>0 ならば収束ベキ級数という。

---

・Banach単位的 $\bm{C,R}$-代数 $A$、$\bm{C,R}$ 係数収束ベキ級数 $F(x)=\sum a_ix^i$、収束半径 $\rho>0$ とする。
<br>

- $$\sum a_i\xi^i\quad(\{\xi\ |\ \|\xi\|\le r<\rho,\ 0<r\})$$は正規収束する。
<br>

- $$F(\xi):\{\xi\ |\ \|\xi\|<\rho\}\to A\\\ \\
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

---

### 演算と収束

#### 和と積

<dl><dt>

・ともに収束半径 $\ge\rho>0$ である $\bm{C,R}$ 係数収束ベキ級数 $F(x),G(x)$ とする。
<br>

</dt><dd>

- $$A(x)=F(x)+G(x),\quad B(x)=F(x)G(x)$$とおくと、$A(x),B(x)$ の収束半径 $\ge\rho$ である。
さらに、Banach単位的 $\bm{C,R}$-代数 $A$、$\|\xi\|<\rho$ なる $\xi\in A$ とすると、
$$A(\xi)=F(\xi)+G(\xi),\quad B(\xi)=F(\xi)G(\xi)\\\ \\$$

- Banach単位的 $\bm{C,R}$-代数 $A$、絶対収束級数 $\sum\xi_p,\ \sum\eta_p\sub A$ とする。
このとき、$$\zeta_p=\sum_{k=0}^p \xi_k\eta_{p-k}$$と定めると、
$\sum \zeta_p$ は絶対収束し、
$$\sum\zeta_p=\left(\sum\xi_q\right)\left(\sum\eta_p\right)$$

</dd></dl>

---

#### 合成

<dl><dt>

・$\bm{C,R}$ 係数収束ベキ級数 $F(x)=\sum a_px^p\ ,G(x)=\sum b_px^p,\ \mathrm{ord}(G)\ge1$、$H=F\circ G$、収束半径 $\rho(F),\ \rho(G),\ \rho(H)$ とする。
<br>

</dt><dd>

- $\exist\delta>0$ であって、$0<r<\delta$ ならば、
$$\sum |b_p|r^p<\rho(F),\quad r<\rho(G),\quad r<\rho(H)$$したがって、$H(x)$ は収束ベキ級数。
<br>

- $0<r$ を上記の仮定を満たす実数、Banach単位的 $\bm{C,R}$-代数 $A$、$\|\xi\|<r$ なる $\xi\in A$ とすると、
$$\|G(\xi)\|<\rho(F),\quad H(\xi)=F(G(\xi))$$


</dd></dl>


---

#### 線形写像とベキ級数

・Banach単位的 $\bm{C,R}$-代数 $A$、$\bm{C,R}$ 係数収束ベキ級数 $F(x)=\sum a_ix^i$、収束半径 $\rho>0$ とする。
また、$K$-単位的連続線形写像 $\psi:A\to A$ とする。

このとき、$\alpha\in B$ に対して $F(\alpha)$ が収束するならば、
$\psi(\alpha)$ も収束して、
$$F(\psi(\alpha))=\psi(F(\alpha))$$

---

### 収束する指数写像

<dl><dt>

・Banach単位的 $\bm{C,R}$-代数 $A$ とする。
このとき、
$$\exp:A\to A\\\ \\
\exp(\alpha)=\sum\frac{1}{n!}\alpha^n$$ は連続関数。
<br>

</dt><dd>

- $$\log:\{\alpha\in A\ |\ \|\alpha-1_A\|\le 1\}\to A\\\ \\
\log(\alpha)=\sum_{n\ge1}\frac{(-1)^{n-1}}{n}(\alpha-1_A)^n$$は連続関数。
<br>

- $$U=\{\alpha\in A\ |\ \|\alpha-1_A\|<1/2\},\quad N=\log U,\\\ \\
N_0=\{\alpha\in A\ |\ \|\alpha\|<\log 2\}$$ とする。
このとき、$\exp$ は $N_0$ 上単射で　
$$\log(\exp\alpha)=\alpha\ \ (\forall\alpha\in N_0)$$ であって、$N$ は$$N\sub N_0,\quad\exp N=U$$を満たす $0_A$ の開近傍。
さらに、$U$ は $1_A$ の開近傍で、開集合 $U,N$ は $\exp,\log$ によって同相。

</dd></dl>



---

# 多変数実解析的写像

    ・正規収束のとこは、Y=N×...×Nとすればよい。

## 正規収束

<dl><dt>

・Banach単位的 $\bm{C,R}$-代数 $A$、集合 $Y$、$u_{i_1,...,i_n}:Y\to A$ とする。
このとき、正規収束級数：$\sum u_{i_1,...,i_n}(y)$：
$$\|u_{i_1,...,i_n}(y)\|\le c_{i_1,...,i_n},\quad\sum_I c_I(y)\in\bm{C,R}$$

    ・N×...×NでF近似列を取る。

</dt><dd>

- $\sum u_{I}(y)$ は各点において絶対収束する。

      ・絶対収束すればもとのやつも収束する。

- $\sum u_i(I)$ は一様収束する。

      ・結局収束するので、一列化してよい。

- $Y$ が位相空間かつ $u_I(y)$ が連続ならば、$\sum u_I(y)$　は連続関数。

</dd></dl>

---

## 収束域

・$\bm{C,R}$ 係数ベキ $n$ 級数 $F(x)=\sum_{i_1,...,i_n=0} a_{i_1,..,i_n}x_1^{i_1}...x_n^{i_n}\in\bm{R,C}[x]$ に対して、
収束域 $\Gamma$：
$$\Gamma=(\{(r_1,...,r_n)\ |\ r_i\ge0,\ \sum_{i_1,...,i_n=0} |a_{i_1,..,i_n}|r_1^{i_1}...r_n^{i_n}\in\bm{R,C}\})^{\circ}$$

    ・Γ≠φ ならば収束ベキ級数という。
    ・内部取った。

- $$\bm{r}\in\Gamma\iff\exist \bm{r}'\in\Gamma\text{ であって、}r_i\le r_i'$$
    

---

<dl><dt>

・Banach単位的 $\bm{C,R}$-代数 $A$、$\bm{C,R}$ 係数収束ベキ $n$ 級数 $F(x)=\sum a_Ix^I$、収束域 $R\in\Delta\neq\phi$ とする。
<br>

</dt><dd>

- $$\sum a_I\xi^I\quad(\{\xi\in A^n\ |\ \|\xi_i\|\le r_i<R_i,\ 0<r_i\})$$は正規収束する。
<br>

- 
$$F(\xi):\{\xi\in A^r\ |\ \|\xi_i\|<R_i\}\to A\\\ \\
F(\xi)=\sum a_I\xi^I$$
は連続関数。 

</dd></dl>

---

<dl><dt>

・$\bm{C,R}$ 係数収束ベキ $n$ 級数 $F(x)=\sum a_Ix^I$、収束域 $R\in\Delta\neq\phi$ とする。
<br>

</dt><dd>

- 
$$\partial F(x)/\partial x^k=\sum_{i_1,...,i_n=0,i_k=1}i_ka_{i_1,...,i_n}x_1^{i_1}...x^{i_k-1}...x^{i_n}$$
において、収束域は $F(x)$ と一致する。

      ・i_kは1から
<br>

- $F:\{z\in\bm{C^n,R^n}\ |\ |z_i|<R_i\}\to\bm{C,R},\quad F(z)=\sum a_Iz^I$ とする。
このとき、$F$ は微分可能で、
$$\frac{\partial }{\partial z^k}F(z)=\sum_{i_1,...,i_n=0,i_k=1}i_ka_{i_1,...,i_n}z_1^{i_1}...z^{i_k-1}...z^{i_n}$$

      ・R^n,C^n内で、0近傍上で一致すればF(x)=G(x)
      ・FはC^∞。
      ・複素数の偏微分？

</dd></dl>

---

## 多変数実解析的写像

・$u\in\bm{R}^n$、開近傍 $u\in U\sub\bm{R}^n$、$f:U\to\bm{R}$ とする。
このとき、$f$ が実解析的：
$$\exist\text{ 収束 }n\text{ ベキ級数 }F(x)\text{ であって、}\\\ \\
f(\xi)=F(\xi-u)=\sum a_I(\xi-u)^I$$
ここで、開集合 $D\sub\bm{R}^n$ 上の各点で実解析的であるとき、$f$ を $D$ 上実解析的という。

    ・ベキ級数展開とも言う。

- 開集合 $D\sub\bm{R}^n$ 上実解析的な $f:D\to\bm{R}$ とする。
このとき、$f$ は $D$ 上 $C^{\infty}$ で、各点のベキ級数展開は一意的に定まる。







### 演算と収束

#### 和と積

<dl><dt>

・ともに収束半径 $\ge\rho>0$ である $\bm{C,R}$ 係数収束ベキ級数 $F(x),G(x)$ とする。
<br>

</dt><dd>

- $$A(x)=F(x)+G(x),\quad B(x)=F(x)G(x)$$とおくと、$A(x),B(x)$ の収束半径 $\ge\rho$ である。
さらに、Banach単位的 $\bm{C,R}$-代数 $A$、$\|\xi\|<\rho$ なる $\xi\in A$ とすると、
$$A(\xi)=F(\xi)+G(\xi),\quad B(\xi)=F(\xi)G(\xi)\\\ \\$$

- Banach単位的 $\bm{C,R}$-代数 $A$、絶対収束級数 $\sum\xi_p,\ \sum\eta_p\sub A$ とする。
このとき、$$\zeta_p=\sum_{k=0}^p \xi_k\eta_{p-k}$$と定めると、
$\sum \zeta_p$ は絶対収束し、
$$\sum\zeta_p=\left(\sum\xi_q\right)\left(\sum\eta_p\right)$$

</dd></dl>

---

#### 合成

<dl><dt>

・$\bm{C,R}$ 係数収束ベキ級数 $F(x)=\sum a_px^p\ ,G(x)=\sum b_px^p,\ \mathrm{ord}(G)\ge1$、$H=F\circ G$、収束半径 $\rho(F),\ \rho(G),\ \rho(H)$ とする。
<br>

</dt><dd>

- $\exist\delta>0$ であって、$0<r<\delta$ ならば、
$$\sum |b_p|r^p<\rho(F),\quad r<\rho(G),\quad r<\rho(H)$$したがって、$H(x)$ は収束ベキ級数。
<br>

- $0<r$ を上記の仮定を満たす実数、Banach単位的 $\bm{C,R}$-代数 $A$、$\|\xi\|<r$ なる $\xi\in A$ とすると、
$$\|G(\xi)\|<\rho(F),\quad H(\xi)=F(G(\xi))$$


</dd></dl>


---

#### 線形写像とベキ級数

・Banach単位的 $\bm{C,R}$-代数 $A$、$\bm{C,R}$ 係数収束ベキ級数 $F(x)=\sum a_ix^i$、収束半径 $\rho>0$ とする。
また、$K$-単位的連続線形写像 $\psi:A\to A$ とする。

このとき、$\alpha\in B$ に対して $F(\alpha)$ が収束するならば、
$\psi(\alpha)$ も収束して、
$$F(\psi(\alpha))=\psi(F(\alpha))$$

---

### 収束する指数写像

<dl><dt>

・Banach単位的 $\bm{C,R}$-代数 $A$ とする。
このとき、
$$\exp:A\to A\\\ \\
\exp(\alpha)=\sum\frac{1}{n!}\alpha^n$$ は連続関数。
<br>

</dt><dd>

- $$\log:\{\alpha\in A\ |\ \|\alpha-1_A\|\le 1\}\to A\\\ \\
\log(\alpha)=\sum_{n\ge1}\frac{(-1)^{n-1}}{n}(\alpha-1_A)^n$$は連続関数。
<br>

- $$U=\{\alpha\in A\ |\ \|\alpha-1_A\|<1/2\},\quad N=\log U,\\\ \\
N_0=\{\alpha\in A\ |\ \|\alpha\|<\log 2\}$$ とする。
このとき、$\exp$ は $N_0$ 上単射で　
$$\log(\exp\alpha)=\alpha\ \ (\forall\alpha\in N_0)$$ であって、$N$ は$$N\sub N_0,\quad\exp N=U$$を満たす $0_A$ の開近傍。
さらに、$U$ は $1_A$ の開近傍で、開集合 $U,N$ は $\exp,\log$ によって同相。

</dd></dl>



---