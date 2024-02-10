
- [ユニタリ群 $U(n)$](#ユニタリ群-un)
  - [位相的性質](#位相的性質)
    - [位相幾何的性質](#位相幾何的性質)
  - [簡単な性質](#簡単な性質)
  - [球面 $S^n$ との関係](#球面-sn-との関係)
    - [作用](#作用)
  - [射影空間との関係](#射影空間との関係)
  - [$SU(n)$ との関係](#sun-との関係)
  - [交代Hermite行列との関係](#交代hermite行列との関係)
  - [具体的な $n$](#具体的な-n)
    - [$n=1$](#n1)
    - [$n=2$](#n2)



# ユニタリ群 $U(n)$

## 位相的性質

・$GL(n,\bm{C})$ の閉部分群であって、
$$U(n)=dagt^{-1}(I)$$

・$U(n)$ はコンパクト集合。

---

### 位相幾何的性質

・$U(n)$ は弧状連結。

---

## 簡単な性質

<dl><dt>

・$$\forall A\in U(n)\text{ に対して、}\exist X\in U(n)\text{ であって、}\\\ \\
X^{-1}AX=\begin{pmatrix}
\ddots\\
& e^{i\theta_i}  \\
& & \ddots
\end{pmatrix}\quad(\theta_i\in\bm{R})$$

    ・固有値のこと。エルミート行列の話ではない。

</dt><dd>

- 上記に加えて、
$$\alpha=\begin{pmatrix}
i\theta_1 &  \\
& \ddots \\
& & i\theta_m \\
\end{pmatrix}$$と定めると、
$$\exp\alpha=X^{-1}AX$$したがって、
$$u:I\to U(n)\\\ \\
u(A)=\exp (tX\alpha X^{-1})$$ は単位元 $E$ と $A$ を結ぶ道。


</dd></dl> 

---

## 球面 $S^n$ との関係

・
$$p:U(n)\to S_{\bm{C}}^{n-1}\\\ \\
p(A)=Ae_{n}$$と定める。
このとき、次の同相が誘導される。
$$U(n)/U(n-1)\cong S^{2n-1}$$

---

### 作用

・
$$\mu:U(n)\times S_{\bm{C}}^{n-1}\to S_{\bm{C}}^{n-1}\\\ \\
\mu(A,x)=Ax$$
と定めると、これは連続な作用で、効果的に働く。

---

## 射影空間との関係

・
$$f:U(n)\to CP{n-1}\\\ \\
f(A)=AEA^{\dag}$$と定める。
このとき、次の同相が誘導される。
$$U(n)/(U(n-1)\times S^2)\cong HP(n-1)\ (\text{同相})$$

---

## $SU(n)$ との関係

・$$U(n)/SU(n)\cong S^1\ (\text{ 群同相})$$


---

## 交代Hermite行列との関係

・交代Hermite行列 $A\in M(n,\bm{C})$ とする。
このとき、$\exp A\in U(n)$


---


<dl><dt>

・$$U(n)\cong S^1\times SU(n)\ (\text{同相})$$

    ・群同相ではない。

</dt><dd>

- 行列式：$|\det U|=1$
<br>

- $U\in U(n)$ とする。
このとき、$$U=e^{i\frac{\alpha}{n}}U',\quad(\det U=e^{i\alpha})$$とおくと、$U'\in SU(n)$


</dd></dl> 

---

## 具体的な $n$

### $n=1$

・明らかに$$U(1)\cong S_C^1\cong S^2$$

---

### $n=2$

・$A=\begin{pmatrix}
a & -\bar{c}    \\
c & \bar{a}    \\
\end{pmatrix}\quad(|a|^2+|b|^2=1)$

---
---
---