- [直交群 $O(n)$](#直交群-on)
  - [位相的性質](#位相的性質)
    - [位相幾何的性質](#位相幾何的性質)
  - [球面 $S^n$ との関係](#球面-sn-との関係)
  - [射影空間 $RP$ との関係](#射影空間-rp-との関係)
  - [$SO(n)$ との関係](#son-との関係)
    - [$n=1$](#n1)
    - [$n=2$](#n2)
    - [$n=4$](#n4)
    - [$n=8$](#n8)
- [複素直交群 $O(n,C)$](#複素直交群-onc)
        - [位相的性質](#位相的性質-1)
- [ユニタリ群 $U(n)$](#ユニタリ群-un)
  - [位相的性質](#位相的性質-2)
    - [位相幾何的性質](#位相幾何的性質-1)
  - [性質](#性質)
    - [球面 $S^n$ との関係](#球面-sn-との関係-1)
    - [射影空間との関係](#射影空間との関係)
    - [$SU(n)$ との関係](#sun-との関係)
    - [交代Hermite行列との関係](#交代hermite行列との関係)
  - [具体的な $n$](#具体的な-n)
    - [$n=1$](#n1-1)
    - [$n=2$](#n2-1)
- [特殊直交群$SO(n)$](#特殊直交群son)
  - [位相的性質](#位相的性質-3)
    - [位相幾何的性質](#位相幾何的性質-2)
  - [性質](#性質-1)
  - [球面 $S^n$ との関係](#球面-sn-との関係-2)
  - [交代行列との関係](#交代行列との関係)
  - [具体的な $n$](#具体的な-n-1)
    - [$n=1$](#n1-2)
    - [$n=2$](#n2-2)
      - [簡単な指数行列](#簡単な指数行列)
    - [$n=3$](#n3)
    - [$n=4$](#n4-1)
    - [$n=8$](#n8-1)
- [特殊ユニタリ群 $SU(n)$](#特殊ユニタリ群-sun)
  - [位相的性質](#位相的性質-4)
    - [位相幾何的性質](#位相幾何的性質-3)
  - [球面 $S^n$ との関係](#球面-sn-との関係-3)
  - [具体的な $n$](#具体的な-n-2)
    - [$n=1$](#n1-3)
    - [$n=2$](#n2-3)
- [一般Lorentz群$O(n-1,1)$](#一般lorentz群on-11)
        - [$R$上ベクトル空間$V$における正則対称双一次形式$B$](#r上ベクトル空間vにおける正則対称双一次形式b)
        - [$n=4$（Lorentz群）](#n4lorentz群)
- [シンプレクティック群 $Sp(n)$](#シンプレクティック群-spn)
  - [位相的性質](#位相的性質-5)
  - [性質](#性質-2)
    - [球面 $S^n$ との関係](#球面-sn-との関係-4)
    - [射影空間との関係](#射影空間との関係-1)
    - [交代Hermite行列との関係](#交代hermite行列との関係-1)
  - [具体的な $n$](#具体的な-n-3)
    - [$n=1$](#n1-4)



# 直交群 $O(n)$

## 位相的性質

・$GL(n,\bm{C})$ の閉部分群であって、$O(n)=trat^{-1}(I)\cap GL(n,\bm{R})$

・コンパクト集合

---

### 位相幾何的性質

・$O(n)$ は $2$ つの弧状連結成分を持ち、単位元 $E$ を含む方が $SO(n)$ である。

---

## 球面 $S^n$ との関係

・
$$p:O(n)\to S^{n-1}\\\ \\
p(A)=Ae_{n}$$と定める。
このとき、次の同相が誘導される。
$$O(n)/O(n-1)\cong S^{n-1}\ (\text{同相})$$

---

## 射影空間 $RP$ との関係

・
$$f:O(n)\to RP_{n-1}\\\ \\
f(A)=AEA^{T}$$と定める。
このとき、次の同相が誘導される。
$$O(n)/(O(n-1)\times S^0)\cong RP(n-1)$$

---

## $SO(n)$ との関係

・$$O(n)/SO(n)\cong S^0=\{-1,1\}\ (\text{群同相})$$

- $$O(n)\cong S^{0}\times SO(n)\ (\text{同相})$$

---

### $n=1$

・明らかに$$O(1)\cong S^0=\{-1,1\}$$

    ・別にO(1)も{-1,1}。

### $n=2$

 ・$O(2)=\left\{\begin{pmatrix}
      \\
      \\
 \end{pmatrix}\ |\ \theta\in[)\right\}$

---

### $n=4$

・$$O(4)\cong S^3\times O(3)\ (\text{同相})$$

    ・？群と位相、p.108

### $n=8$

・$$O(8)\cong S^7\times O(7)\ (\text{同相})$$


# 複素直交群 $O(n,C)$

##### 位相的性質

・$GL(n,\bm{C})$ の閉部分群であって、$O(n,\bm{C})=trat^{-1}(I)$

---
---
---

# ユニタリ群 $U(n)$

## 位相的性質

・$GL(n,\bm{C})$ の閉部分群であって、$U(n)=dagt^{-1}(I)$

・コンパクト集合、すなわち $GL(n,\bm{C})$ の有界閉集合

---

### 位相幾何的性質

・$U(n)$ は弧状連結。

---

## 性質

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

### 球面 $S^n$ との関係

・
$$p:U(n)\to S_{\bm{C}}^{n-1}\\\ \\
p(A)=Ae_{n}$$と定める。
このとき、次の同相が誘導される。
$$U(n)/U(n-1)\cong S^{2n-1}$$4

---

### 射影空間との関係

・
$$f:U(n)\to CP{n-1}\\\ \\
f(A)=AEA^{\dag}$$と定める。
このとき、次の同相が誘導される。
$$U(n)/(U(n-1)\times S^2)\cong HP(n-1)\ (\text{同相})$$

---

### $SU(n)$ との関係

・$$U(n)/SU(n)\cong S^1\ (\text{ 群同相})$$


---

### 交代Hermite行列との関係

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


# 特殊直交群$SO(n)$

## 位相的性質

・$GL(n,\bm{C})$ の閉部分群であって、$O(n)=trat^{-1}(I)\cap \det^{-1}(1)$

・コンパクト集合、すなわち $U(n)$ の閉集合。

---

### 位相幾何的性質

・$SO(n)$ は弧状連結。

---

## 性質

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
$$u:I\to SO(n)\\\ \\
u(A)=\exp (tX\alpha X^{-1})$$ は単位元 $E$ と $A$ を結ぶ道。


</dd></dl> 

---

## 球面 $S^n$ との関係

・
$$p:SO(n)\to S^{n-1}\\\ \\
p(A)=Ae_{n}$$と定める。
このとき、次の同相が誘導される。
$$SO(n)/SO(n-1)\cong S^{n-1}$$

---

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

・$$SO(2)\cong S^1\text{同相}$$

    ・群同相？

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

# 特殊ユニタリ群 $SU(n)$

## 位相的性質

・$GL(n,\bm{C})$ の閉部分群であって、$O(n)=dagt^{-1}(I)\cap \det^{-1}(1)$

・コンパクト集合

---

### 位相幾何的性質

・$SU(n)$ は弧状連結。

---

## 球面 $S^n$ との関係

・
$$p:SU(n)\to S_{\bm{C}}^{n-1}\\\ \\
p(A)=Ae_{n}$$と定める。
このとき、次の同相が誘導される。
$$SU(n)/SU(n-1)\cong S^{2n-1}$$

---

## 具体的な $n$

### $n=1$

・$SU(1)=\{1\}$

---

### $n=2$

・$A=\begin{pmatrix}
a & -\bar{c}    \\
c & \bar{a}    \\
\end{pmatrix}\quad(|a|^2+|b|^2=1)$
と書ける

- $SU(2)\cong S^3\text{同相}$

    ・群同相？

---
---
---

# 一般Lorentz群$O(n-1,1)$

##### $R$上ベクトル空間$V$における正則対称双一次形式$B$



---

##### $n=4$（Lorentz群）



---
---
---

# シンプレクティック群 $Sp(n)$

・$Sp(n)=\{A\in M(n,\bm{H})\ |\ AA^{\dag}=E\}$

## 位相的性質

・$GL(n,\bm{H})$ の閉部分群であって、$Sp(n)=dagt^{-1}(I)$

- コンパクト集合。

---

## 性質

<dl><dt>

・$$\forall A\in Sp(n)\text{ に対して、}\exist X\in Sp(n)\text{ であって、}\\\ \\
X^{-1}AX=\begin{pmatrix}
\ddots\\
& e^{i\theta_i}  \\
& & \ddots
\end{pmatrix}\quad(\theta_i\in\bm{R})$$

    ・固有値のこと。エルミート行列の話ではない。
    ・？、群と位相、付録

</dt><dd>

- 上記に加えて、
$$\alpha=\begin{pmatrix}
i\theta_1 &  \\
& \ddots \\
& & i\theta_m \\
\end{pmatrix}$$と定めると、
$$\exp\alpha=X^{-1}AX$$したがって、
$$u:I\to Sp(n)\\\ \\
u(A)=\exp (tX\alpha X^{-1})$$ は単位元 $E$ と $A$ を結ぶ道。


</dd></dl> 

---

### 球面 $S^n$ との関係

・
$$p:Sp(n)\to S_{\bm{H}}^{n-1}\\\ \\
p(A)=Ae_{n}$$と定める。
このとき、次の同相が誘導される。
$$Sp(n)/Sp(n-1)\cong S^{4n-1}$$

### 射影空間との関係

・
$$f:Sp(n)\to HP{n-1}\\\ \\
f(A)=AEA^{\dag}$$と定める。
このとき、次の同相が誘導される。
$$Sp(n)/(Sp(n-1)\times S^3)\cong HP(n-1)\ (\text{同相})$$

---

### 交代Hermite行列との関係

・交代Hermite行列 $A\in M(n,\bm{H})$ とする。
このとき、$\exp A\in Sp(n)$


## 具体的な $n$

### $n=1$

・明らかに$$Sp(1)\cong S_H^1\cong S^3$$