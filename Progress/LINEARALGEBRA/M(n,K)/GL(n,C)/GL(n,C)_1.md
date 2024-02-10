
- [位相群としての $GL(n,C)$](#位相群としての-glnc)
  - [位相的性質](#位相的性質)
    - [行列式写像](#行列式写像)
    - [埋め込み](#埋め込み)
    - [$SL(n,C)$ との関係](#slnc-との関係)
    - [多様体構造](#多様体構造)
  - [$GL(n,R)$](#glnr)
- [具体的な $n$](#具体的な-n)
  - [$n=1$](#n1)
- [特殊線形群 $SL(n,C)$](#特殊線形群-slnc)
  - [位相的性質](#位相的性質-1)
    - [多様体構造](#多様体構造-1)
  - [実一般線形群 $GL(n,R)$](#実一般線形群-glnr)

# 位相群としての $GL(n,C)$

## 位相的性質

・$GL(n,\bm{C})$ はHausdorff局所コンパクト空間。

- 相対距離：$d(\alpha,\beta)=\|\alpha-\beta\|$

      ・別にα-β∊GL(n,C)でなくてもよい。
<br>

- 逆元：$\alpha\mapsto\alpha^{-1}$ は連続。
したがって、$GL(n,\bm{C})$ は位相群。

      ・Rでも同様。Hは四元数体参照。
---

### 行列式写像

・行列式写像：
$$\det:GL(n,\bm{C})\to \bm{C}^{\times}$$は連続全射な準同型写像。

- $$GL(n,\bm{C})=\mathrm{det}^{-1}\{z\in\bm{C}\ |\ z\neq0\}$$

### 埋め込み

・$$i:GL(n-1,\bm{C})\to i(GL(n-1,\bm{H}))\sub GL(n,\bm{C})\\\ \\
i(A)=\begin{pmatrix}
A &  \\
& 1 \\
\end{pmatrix}$$は群同相写像。よって、
$GL(n-1,\bm{C})$ は $GL(n,\bm{C})$ の部分群とみなせる。

    ・G(n,R,C,H) でも成り立つ。また、H上でも成立つ。
<br>

- $A\in G(n,\bm{C})$ に対して、
$$A\in G(n-1,\bm{C})\iff Ae_n=e_n$$

      ・四元数体上でも成り立つ。


---

・$$i:GL(n-1,\bm{C})\times GL(1,\bm{C})\to i(GL(n-1,\bm{C})\times GL(1,\bm{C}))\sub GL(n,\bm{C})\\\ \\
i(A,a)=\begin{pmatrix}
A &  \\
& a \\
\end{pmatrix}$$は群同相写像。よって、
$$GL(n-1,\bm{H})\times GL(1,\bm{H})\sub GL(n,\bm{H})$$は部分群とみなせる。

    ・G(n,R,C,H)×G(1,R,C,H) でも成り立つ。また、H上でも成り立つ。
<br>

- $A\in GL(n,\bm{C})$ に対して、
$$A\in GL(n-1,\bm{C})\times GL(1,\bm{C})\iff AE_n=E_nA$$

      ・G(n,R,C,H)×G(1,R,C,H) でも成り立つ。また、H上でも成り立つ。



---

### $SL(n,C)$ との関係


$$GL(n,\bm{C})/SL(n,\bm{C})\cong\bm{C}^{*}\quad(\text{群同相})$$

      ・実数上でも成り立つ。

### 多様体構造

・$GL(n,\bm{C})$ は $\bm{R}^{2n^2}$ の開集合としての多様体構造を持つ。さらに、$Q(g,h)=g^{-1}h$ は実解析写像。
したがって、$GL(n,\bm{C})$ は $2n^2$ 次元リー群。

    ・GL(n,R) でも同様。
    ・n次元C上ベクトル空間でも同様。このとき、基底の違いは無視できる。

---

## $GL(n,R)$

・$GL(n,\bm{R})$ は $GL(n,\bm{C})$ の閉部分群。



---

# 具体的な $n$

## $n=1$

・$\bm{C}^{\times}=GL(1,\bm{C})$

    ・要素も位相も（乗法）群演算も同じ。

---

# 特殊線形群 $SL(n,C)$

## 位相的性質


・$SL(n,\bm{C})$ は $M(n,\bm{C})$ の閉集合で、$GL(n,\bm{C})$ の閉部分群かつ正規部分群であって、
$$SL(n,\bm{C})=\ker\det(1)$$  
<br>

- $SL(n,\bm{C})$ は第二可算な局所コンパクトHausdorff空間。
<br>

</dd></dl> 

---

### 多様体構造

---

## 実一般線形群 $GL(n,R)$

 ・$GL(n,\bm{R})\subset GL(n,\bm{C})$ は閉部分群。

---
---
---



