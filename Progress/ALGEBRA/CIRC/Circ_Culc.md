
- [自然数 $N$](#自然数-n)
  - [普遍環](#普遍環)
- [$K$-右加群から生成される $K$-右加群](#k-右加群から生成される-k-右加群)
  - [部分 $K$-右加群](#部分-k-右加群)
  - [$K$-右加群の同形類](#k-右加群の同形類)
    - [有限次元 $K$-右加群の同形類](#有限次元-k-右加群の同形類)
- [内積 $K$-右加群から生成される群](#内積-k-右加群から生成される群)
- [斜体 $K$ から生成される $K$-右加群](#斜体-k-から生成される-k-右加群)
  - [$K^n$](#kn)
    - [基本的な性質](#基本的な性質)
  - [$K$ 上行列 $M(n,K)$](#k-上行列-mnk)
    - [基本的な性質](#基本的な性質-1)
    - [$K$ との関係](#k-との関係)
- [可換環 $A$ から生成される可換環](#可換環-a-から生成される可換環)
  - [多項式環](#多項式環)
- [可換体 $K$ から生成される可換環](#可換体-k-から生成される可換環)
  - [$K$-多項式環](#k-多項式環)
    - [無限形式的多項式環](#無限形式的多項式環)
      - [位数と単項式](#位数と単項式)
      - [合成](#合成)
      - [逆元](#逆元)
      - [exp](#exp)
      - [$1$ 次元 $K$-加群](#1-次元-k-加群)
- [整数 $Z$ 上多項式環](#整数-z-上多項式環)
- [$R$-加群と $C$-加群](#r-加群と-c-加群)
  - [制限](#制限)
  - [拡大](#拡大)
  - [有限次元](#有限次元)
    - [制限](#制限-1)
    - [拡大](#拡大-1)
  - [多元環の複素化](#多元環の複素化)
  - [$R$](#r)
  - [$M(n,R)$](#mnr)

# 自然数 $N$

・$\bm{N}$ は単位的可換半環。

## 普遍環

・
$$R(\bm{N})=\bm{Z}\\\ \\
\tau(n)=n$$と定めると、これは $\bm{N}$ の普遍環で、
$$\psi(m)=\mathrm{sgn}(m)\phi(|m|)=m\phi(1)$$


# $K$-右加群から生成される $K$-右加群

## 部分 $K$-右加群

・$K$-右加群 $V$、$W\subset V$ に対して、
部分 $K$-右加群 $W$：
$$\forall x,y\in W\text{ に対して }x-y\in W\\\ \\
\forall x\in W,\forall \lambda\in K\text{ に対して }x\lambda\in W$$

---

## $K$-右加群の同形類

・$K$-右加群 $V,W,U$ とする。
このとき、
$$V\oplus W\cong W\oplus V\ \ (K\text{-右同型})\\\ \\
V\oplus (W\oplus U)\cong (V\oplus W)\oplus U\ \ (K\text{-右同型})\\\ \\
V\oplus 0\cong V\ \ (K\text{-右同型})$$したがって、
$$V\sim W\iff V\cong W\ \ (K\text{-右同型})$$と定めると、$\{V\ |\ K\text{-右加群 } V\}/\sim$ は直和に関して半加群。

- 
$$V\otimes W\cong W\otimes V\ \ (K\text{-右同型})\\
\psi(v\otimes w)=w\otimes v\ \ (\text{well-defined})\\\ \\
V\otimes (W\otimes U)\cong (V\otimes W)\otimes U\cong V\otimes W\otimes U\ \ (K\text{-右同型})\\
\psi(v\otimes w\otimes u)=v\otimes(w\otimes u)\\\ \\
(V\oplus W)\otimes U\cong (V\otimes U)\oplus (W\otimes U)\\
\psi((v,w)\otimes u)=(v\otimes u,w\otimes u)\\\ \\
V\otimes K\cong V\ (K\text{-右同型})\\
\psi(u\otimes \alpha)=u\alpha$$したがって、$\{V\ |\ K\text{-右加群 } V\}/\sim$ は直和とテンソル積に関して単位的可換半環。
<br>


- $K$-右加群 $V,W,U$ とする。
このとき、
$$\Psi:V\times (W\otimes U)\to V\otimes W\otimes U\\\ \\
\Psi(t,x)=\Psi\left(t,\sum w_i\otimes u_i\right)=\sum t\otimes w_i\otimes u_i$$はwell-definedな双線形写像。
すなわち、$$\sum v_i\otimes u_i=\sum v_j'\otimes u_j'\\\ \\\Rightarrow \sum t\otimes w_i\otimes u_i=\sum t\otimes w_j'\otimes u_j'$$
<br>

- $K$-右加群 $V,W,U$ とする。
このとき、
$$\Psi:(V\otimes U)\oplus (W\otimes U)\to (V\oplus W)\otimes U\\\ \\
\Psi(x,y)=\Psi\left(\sum v_i\otimes u_i,\ \sum w_i\otimes U_i\right)=\sum (v_i,0)\otimes u_i+(0,w_i)\otimes U_i$$はwell-defined。
すなわち、$$\sum v_i\otimes u_i=\sum v_j'\otimes u_j',\quad \sum w_i\otimes U_i=\sum w_j'\otimes U_j'\\\ \\\Rightarrow \sum (v_i,0)\otimes u_i+(0,w_i)\otimes U_i=\sum (v_j',0)\otimes u_j'+(0,w_j')\otimes U_j'$$。

---

### 有限次元 $K$-右加群の同形類

・$$X=\{V\ |\ V\text{ は有限次元 }K\text{ 加群}\}$$ 
に対して、上記の同値関係を入れたものは、可換半環であって$\bm{N}$ と半環同型。
$$\psi([V])=\dim V\\\ \\
X\cong\bm{N}\ (\text{半環同型})$$


---
---
---

# 内積 $K$-右加群から生成される群

・内積 $K$-右加群 $V$ とする。
このとき、
$$G(V)=\{\alpha:V\to V\ |\ \alpha\text{ は内積 $K$-右同型 }\}$$ は合成で群をなす。

    ・明らかに G(n,K) と群同型。

---

# 斜体 $K$ から生成される $K$-右加群

## $K^n$

### 基本的な性質

・斜体 $K$ に対して、
$K^n$ は$K$-右加群

    ・別にK-左加群にもなる。

- 次元：$n$、基底：$e_i=(0,...,0,1,0,...,0)$

---

## $K$ 上行列 $M(n,K)$

    ・詳細は四元数体のとこに載ってる。

### 基本的な性質

・斜体 $K$ に対して、
$$M(n,K)=\{(a_{ij})\ |\ a_{ij}\in K\}\\\ \\
(a_{ij})+(b_{ij})=\{(a+b)_{ij}\}\\\ \\
(a_{ij})\lambda=\{(\lambda a)_{ij}\}$$と定めると、これは $K$-右加群。

    ・別にK-左加群にもなる。

- 次元：$n^2$、基底：$E_{ij}$

---

### $K$ との関係

・斜体 $K$ に対して、
$$M(n,K)\cong K^{n^2}\ (K-{右同型})\\\ \\
f((a_{ij}))=(a_{11},...,a_{nn})$$

---
---
---

# 可換環 $A$ から生成される可換環

## 多項式環

---

# 可換体 $K$ から生成される可換環

## $K$-多項式環

### 無限形式的多項式環

・可換体 $K$ に対して、
形式的無限多項式環：$$K^{\infty}[x]=\left\{\sum a_nx^n\ |\ a_n\in K\right\}$$

- 演算：
$$\sum a_nx^n+\sum b_nx^n=\sum (a_n+b_n)x^n\\\ \\
c\sum a_nx^n=\sum (ca_n)x^n\\\ \\
\left(\sum a_nx^n\right)\left(\sum b_nx^n\right)=\sum c_nx^n\quad\left(c_n=\sum_{k=1}^na_kb_{n-k}\right)$$と定めると、$K^{\infty}[x]$ は 単位的 $K$-代数。

---

#### 位数と単項式

・$F(x)=\sum a_nx^n\in K^{\infty}[x]$ に対して、
位数：
$$\mathrm{ord}(F)=\min\{n\in\bm{N}\ |\ a_n\neq0\}$$ただし、$F=0$ なら $\infty$

    ・a_nx^n+a_{n+1}x^{n+1}+... のこと

- $\mathrm{ord}(FG)=\mathrm{ord}(F)+\mathrm{ord}(G)$

---

・$F(x)=\sum a_nx^n\in K^{\infty}[x]$ に対して、
単項式 $a_px^p$：
$$\exist p\in\bm{N}\ {であって、}p\neq q\Rightarrow a_q=0$$

- 列 $F_i(x)\in K^{\infty}[x]$ であって、
$$\{i\in\bm{N}\ |\ \mathrm{ord}(F_i)<k,\ k\in\bm{N} \}$$が $\forall k\in\bm{N}$ に対して有限集合であるとする。
このとき、$$F(x)=\sum F_i=\sum a_nx^n\\\ \\
a_n=\sum_i a_{n,i}$$と定めると、$F(x)\in K^{\infty}[x]$
<br>

- $F(x)=\sum a_nx^n\in K^{\infty}[x]$ に対して、
単項式の列 $$F_i=a_ix^i$$を定義すると、
$$F(x)=\sum F_i=a_0+a_1x^1+...$$と書ける。

---

#### 合成

・$F(x)=\sum a_nx^n,\ G(x)=\sum b_nx^n\in K^{\infty}[x]$、$\mathrm{ord}(G)\ge1\quad(b_0=0)$ に対して、
合成：$$F\circ G=\sum a_n(G(x))^n$$と定めると、$F\circ G\in K^{\infty}[x]$

<dl><dt>

- $G(x)\in K^{\infty}[x]$ が $\mathrm{ord}(G)\ge1$ を満たすとする。

</dt><dd>

- $$\mathrm{ord}(G)^n\ge n$$
<br>

- 列 $F_i=a_iG^i(x)$ に対して、
$$\#\{i\in\bm{N}\ |\ \mathrm{ord}(F_i)<k,\ k\in\bm{N} \}\le k$$

</dd></dl> 


---

・$G(x)\in K^{\infty}[x]$ に対する合成：
$$(\cdot)\circ G:K^{\infty}[x]\to K^{\infty}[x]$$とする。
このとき、$(\cdot)\circ G$ は単位的 $K$-準同型。

    ・F◦(・)だと無理。


---

#### 逆元

    ・逆関数ではない

<dl><dt>

・$F(x)=\sum a_nx^n\in K^{\infty}[x]$ とする。
このとき、
$$\exist G(x)\in K^{\infty}[x]\text{ であって、}F(x)G(x)=1\\\ \\
\iff a_0\neq0$$この $G(x)$ を $F(x)$ の逆元といい、
$$G(x)=a_0G_1(x),\quad G_1(x)=\sum_p H(x)^p\\\ \\
H(x)=\sum-\frac{a_n}{a_0}x^n$$と表される。

    ・積は可換
    ・(1-x)(1+x+x^2+...)への代入。
  
</dt><dd>

- $F(x)=\sum a_nx^n\in K^{\infty}[x]$、$G(x)=(F(x))^{-1}$ とする。
このとき、$F(x)$ が収束ベキ級数ならば、$G(x)$ は収束ベキ級数。

      ・逆元の逆元は元に戻ることに注意。

- $$(1-x)^{-1}=1+x+x^2+...$$
  
      ・まあx<1なら成り立つが、証明はよくわからん。

</dd></dl> 

---

#### exp

<dl><dt>

・$$\exp x=\sum\frac{1}{n!}x^n$$と定めると、収束半径 $\infty$
<br>
  
</dt><dd>

- $$G(x)=\sum_{n\ge1}\frac{(-1)^{n-1}}{n}x^n$$と定めると、収束半径 $1$。
さらに、$F(x)=\exp x-1$ とすると、
$$G\circ F=F\circ G=x$$

      ・両方合成可能

</dd></dl> 

---

#### $1$ 次元 $K$-加群

・可換体 $K$、一次元 $K$-加群 $V$ とする。
このとき、
$$T(V)\cong K^{\infty}[x]\ \ (K\text{-加群})\\\ \\
\text{基底 }u\in V\text{　に対して、}\psi(1)=1,\ \ \psi(u\otimes...\otimes u)=x^r$$



---


# 整数 $Z$ 上多項式環

---
---
---

# $R$-加群と $C$-加群

## 制限

・$\bm{C}$-加群 $V$ とする。
このとき、$\alpha\in \bm{R}$ に対して、
$$v\alpha=v(\alpha+i0)$$と定めると、$V_{R}$ は $\bm{R}$-加群。

- $\bm{C}$-加群 $V,W$ とする。
このとき、$$(V\oplus W)_R\cong V_R\oplus W_R\ \ (\bm{R}\text{-同型})$$

---

## 拡大

・$\bm{R}$-加群 $V$、テンソル $\bm{R}$-加群 $V\otimes_{R}\bm{C}$ とする。
このとき、$\alpha\in\bm{C}$ に対して、$$(u\otimes\beta)\alpha=u\otimes\beta\alpha$$ と定めると、これはwell-definedであって、$V\otimes_{R}\bm{C}$ は $\bm{C}$-加群。

- $u\in V\otimes_R\bm{C}$ とする。
このとき、$$\exist\ !\ v_1,v_2\in V\text{ であって、}u=v_1\otimes1+v_2\otimes i$$ここで、$\overline{u}=v_1\otimes1-v_2\otimes i$ を $u$ の共役という。

---

## 有限次元

### 制限

・$n$ 次元 $\bm{C}$ 加群 $V$、基底 $u_i$ とする。
このとき、$V_R$ は $2n$ 次元 $\bm{R}$-加群で、基底 $u_i,u_ii$。

---

### 拡大

・$n$ 次元 $\bm{R}$ 加群 $V$、基底 $u_i$ とする。
このとき、$V\otimes_R\bm{C}$ は $n$ 次元 $\bm{C}$-加群で、基底 $u_i\otimes1$。

- 
$$(V\oplus W)^C\cong V^C\oplus W^C\\\ \\
(V\otimes W)^C\cong V^C\otimes W^C\\\ \\
(V^*)^C\cong (V^C)^*\\\ \\
V^C\cong\overline{V^C}\\\ \\
(\Lambda^r(V))^C\cong\Lambda^r(V^C)\quad(\bm{C}\text{-同型})$$

---

## 多元環の複素化

・$\bm{R}$-多元環 $A$、複素化 $A\otimes\bm{C}$ とする。
このとき、$$(a\otimes\alpha)(b\otimes\beta)=(ab\otimes\alpha\beta)$$と定めると、これはwell-definedで、$A\otimes\bm{C}$ は $\bm{C}$ 上多元環。

---

## $R$

・
$$\bm{R}^n\otimes_R\bm{C}\cong\bm{C}^n\ \ (\bm{C}-\text{同型})\\\ \\
f(a\otimes\alpha)=a\alpha\ \ (\text{well-defined})$$

---

## $M(n,R)$

・
$$M(n,\bm{R})\otimes_R\bm{C}\cong M(n,\bm{C})\ \ (\bm{C}-\text{同型})\\\ \\
M(n,\bm{R})\otimes_R\bm{H}\cong M(n,\bm{H})\ \ (\bm{R}-\text{同型})\\\ \\
f(A\otimes\alpha)=A\alpha\ \ (\text{well-defined})\\\ \\
$$


