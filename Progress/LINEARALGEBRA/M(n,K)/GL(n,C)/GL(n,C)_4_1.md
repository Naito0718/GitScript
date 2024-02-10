
- [特殊直交群$SO(n)$](#特殊直交群son)
  - [位相的性質](#位相的性質)
    - [位相幾何的性質](#位相幾何的性質)
  - [簡単な性質](#簡単な性質)
  - [球面 $S^n$ との関係](#球面-sn-との関係)
    - [作用](#作用)
    - [ファイバー空間](#ファイバー空間)
  - [交代行列との関係](#交代行列との関係)
  - [具体的な $n$](#具体的な-n)
    - [$n=1$](#n1)
    - [$n=2$](#n2)
      - [簡単な指数行列](#簡単な指数行列)
      - [単位円周との関係](#単位円周との関係)
    - [$n=3$](#n3)
    - [$n=4$](#n4)
    - [$n=8$](#n8)




# 特殊直交群$SO(n)$

## 位相的性質

・$GL(n,\bm{C})$ の閉部分群であって、$O(n)=trat^{-1}(I)\cap \det^{-1}(1)$

・コンパクト集合、すなわち $U(n)$ の閉集合。

---

### 位相幾何的性質

・$SO(n)$ は弧状連結。

---

## 簡単な性質

<dl><dt>

・$$\forall A\in SO(n)\text{ に対して、}\exist X\in O(n)\text{ であって、}\\\ \\
X^{-1}AX=\begin{pmatrix}
A_1 &  \\
& \ddots \\
& & A_m \\
& & & (1)\\
\end{pmatrix}\quad A_i=\begin{pmatrix}
\cos\theta_i & -\sin\theta_i  \\
\sin\theta_i & \cos\theta_i \\
\end{pmatrix}\\\ \\(\theta_i\in\bm{R},\ \ (1):\text{ $n$ が偶数のときは消えて、奇数なら $1$})$$
特に、$n$ が奇数ならば、$\lambda=1$ は $A$ の固有値であって、その固有ベクトルは実ベクトルに取れる。
<br>

    ・XはSO(n) の元に取れるらしい？、群と位相

</dt><dd>

- 上記に加えて、
$$\alpha=\begin{pmatrix}
\alpha_1 &  \\
& \ddots \\
& & \alpha_m \\
& & & (0)\\
\end{pmatrix}\quad \alpha_i=\begin{pmatrix}
0 & \theta_i  \\
\theta_i & 0 \\
\end{pmatrix}\\\ \\((0):\text{ $n$ が偶数のときは消えて、奇数なら $0$})$$と定めると、
$$\exp\alpha=X^{-1}AX$$したがって、
$$u:[0,1]\to SO(n)\\\ \\
u(t)=\exp (tX\alpha X^{-1})$$ は単位元 $E$ と $A$ を結ぶ道。


</dd></dl> 

---

## 球面 $S^n$ との関係

・
$$p:SO(n)\to S^{n-1}\\\ \\
p(A)=Ae_{n}$$と定める。
このとき、次の同相が誘導される。
$$SO(n)/SO(n-1)\cong S^{n-1}\\\ \\$$

    ・こいつら全部作用によるのか。

---

### 作用

・
$$\mu:SO(n)\times S^{n-1}\to S^{n-1}\\\ \\
\mu(A,x)=Ax$$
と定めると、これは連続な作用で、効果的かつ推移的に働く。

---

### ファイバー空間

  ・群と位相p.180

## 交代行列との関係

・交代行列 $A\in M(n,\bm{R})$ とする。
このとき、$$\exp A\in SO(n)$$

    ・Hermiteだと対角は実数なだけだからSUではない。

---

## 具体的な $n$

### $n=1$

・$SO(1)=\{1\}$

---

### $n=2$

・
$$SO(2)=\left\{\begin{pmatrix}
\cos\theta & -\sin\theta \\
\sin\theta & \cos\theta \\
\end{pmatrix}\ |\ \theta\in\bm{R}\right\}\\\ \\$$

- $\theta_1,\theta_2\in\bm{R}$、$$\begin{pmatrix}
\cos\theta_1 & -\sin\theta_1 \\
\sin\theta_1 & \cos\theta_1 \\
\end{pmatrix},\ \begin{pmatrix}
\cos\theta_2 & -\sin\theta_2 \\
\sin\theta_2 & \cos\theta_2 \\
\end{pmatrix}\in SO(2)$$ とする。
このとき、
$$\begin{pmatrix}
\cos\theta_1 & -\sin\theta_1 \\
\sin\theta_1 & \cos\theta_1 \\
\end{pmatrix}\begin{pmatrix}
\cos\theta_2 & -\sin\theta_2 \\
\sin\theta_2 & \cos\theta_2 \\
\end{pmatrix}=\begin{pmatrix}
\cos(\theta_1+\theta_2) & -\sin(\theta_1+\theta_2) \\
\sin(\theta_1+\theta_2) & \cos(\theta_1+\theta_2) \\
\end{pmatrix}$$

---

#### 簡単な指数行列

・
$$A=\begin{pmatrix}
0 & -\theta \\  
\theta & 0 \\
\end{pmatrix}\quad(\theta\in\bm{R})$$とする。
このとき、
$$\exp A=\begin{pmatrix}
\cos\theta & -\sin\theta \\  
\sin\theta & \cos\theta \\
\end{pmatrix}\in SO(2)$$

---

#### 単位円周との関係

<dl><dt>

・トーラス：$\bm{T}=\bm{R}/2\pi\bm{Z}$ とする。
このとき、$2\pi\bm{Z}$ は離散部分群、すなわち閉部分群である。
したがって、$\bm{T}$ は、$\bm{R}$ と同様の演算で位相群。
<br>

- 単位円周：$S^1\sub\bm{C}^{\times}$、$x,y\in S^1$ とする。
このとき、$\bm{S}^1$ は $\bm{C}^{\times}$ の閉部分群。

      ・R^2で見ようがCで見ようが位相は同じ。
<br>

</dt><dd>

- 
$$f:\bm{T}\to S^1\\\ \\
f([\theta])=e^{i\theta}$$
と定めると、これは群同相写像。

    ・局所コンパクト群どうしの開写像定理。
<br>

- 
$$f:S^1\to SO(2)\\\ \\
f(x+iy)=\begin{pmatrix}
x & -y  \\
y & x \\
\end{pmatrix}$$
と定めると、これは群同型写像で、同相。

  ・同相？
<br>

- 
$$f:SO(2)\to \bm{T}\\\ \\
f\left(\begin{pmatrix}
\cos\theta & -\sin\theta \\  
\sin\theta & \cos\theta \\
\end{pmatrix}\right)=[\theta]$$
と定めると、これは群同型写像で、同相。

  ・同相？
</dd></dl> 

  

---

### $n=3$

・直交座標系の間の変換$\bar{x}=Ax$に対して、
$$A=\begin{pmatrix}
\cos\alpha_1 & \cos\beta_1 & \cos\gamma_1    \\
\cos\alpha_2 & \cos\beta_2 & \cos\gamma_2 \\
\cos\alpha_3 & \cos\beta_3 & \cos\gamma_3  \\
\end{pmatrix},\quad(\alpha_i,\beta_i,\gamma_i{はそれぞれ軸の方位角})$$
と書ける

→$A\in SO(3)$
→高次元でも同じ式が成り立つ

    ・高次元でも角度は定義できる

---

・$A\in SO(3)$を指定する$3$つの実数

→回転軸が$z$軸となす角 $\theta$ と方位角 $\phi$、回転角 $\phi'$

---

・

---

### $n=4$

・$SO(4)=SO(\bm{H})$

    ・？群と位相、p.108

・$$SO(4)\cong S^3\times SO(3)\ (\text{同相})$$

      ・？

### $n=8$

・$$SO(8)\cong S^7\times SO(7)\ (\text{同相})$$

---
---
---