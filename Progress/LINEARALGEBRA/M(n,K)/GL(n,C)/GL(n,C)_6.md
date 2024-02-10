
- [シンプレクティック群 $Sp(n)$](#シンプレクティック群-spn)
  - [位相的性質](#位相的性質)
  - [性質](#性質)
    - [球面 $S^n$ との関係](#球面-sn-との関係)
    - [射影空間との関係](#射影空間との関係)
    - [交代Hermite行列との関係](#交代hermite行列との関係)
  - [具体的な $n$](#具体的な-n)
    - [$n=1$](#n1)
- [複素シンプレクティック群](#複素シンプレクティック群)



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




# 複素シンプレクティック群

・
$$Sp(n,\bm{C})=\{A\in M(n,\bm{C})\ |\ A^TJ_nA=J_n\}\\\ \\
J_n=\begin{pmatrix}
0 & I_n \\
-I_n & 0 \\
\end{pmatrix}$$
と定めると、$Sp(n,\bm{C})$ は $GL(n,\bm{C})$ の部分群で、$A^{-1}=-J_nA^TJ_n$