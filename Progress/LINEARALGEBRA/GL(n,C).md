- [一般線形群 $GL(n,C)$](#一般線形群-glnc)
        - [位相線形空間としての $M(n,C)$](#位相線形空間としての-mnc)
        - [位相群としての $GL(n,C)$](#位相群としての-glnc)
- [特殊直交群$SO(n,R)$](#特殊直交群sonr)
        - [$n=2$](#n2)
        - [$n=3$](#n3)
        - [$n=4$](#n4)
  - [一般Lorentz群$O(n-1,1)$](#一般lorentz群on-11)
        - [$R$上ベクトル空間$V$における正則対称双一次形式$B$](#r上ベクトル空間vにおける正則対称双一次形式b)
        - [$n=4$（Lorentz群）](#n4lorentz群)
  - [ユニタリ群 $U(n)$](#ユニタリ群-un)
        - [$n=1$](#n1)
        - [$n=2$](#n2-1)
  - [特殊ユニタリ群 $SU(n)$](#特殊ユニタリ群-sun)
        - [$n=1$](#n1-1)
        - [$n=2$](#n2-2)


# 一般線形群 $GL(n,C)$

##### 位相線形空間としての $M(n,C)$

・ノルム：$$\|\alpha\|=\sqrt{\sum|a_{ij}|^2}$$

- 明らかに $\bm{R}^{2n}\cong M(n,\bm{C})$ で線形同型

- $M(n,\bm{C})$ はBanach $*$-環

        ・ノルムが異なるので、有界線形作用素 B(H) で考えているわけではない
        ・C*まで言える？

---
・行列式写像：$\det:M(n,\bm{C})\to\bm{C}$ は連続

- 小行列式写像：$M(n,\bm{C})\to M(n,\bm{C}),\quad\alpha\mapsto\tilde{\alpha}$ は連続


---

##### 位相群としての $GL(n,C)$

・相対距離：$d(\alpha,\beta)=\|\alpha-\beta\|$

    ・別にα-β∊GL(n,C)でなくてもよい

- 逆元：$\alpha\mapsto\alpha^{-1}$ は連続

---

・行列式写像：
$$\det:GL(n,\bm{C})\to C^{\times}$$は準同型写像

##### 特殊線形群 $SL(n,C)

・特殊線形群：$SL(n,\bm{C})=\ker\det\quad(\det:GL(n,\bm{C}\to C^{\times}))$

- $SL(n,\bm{C})$ は $GL(n,\bm{C})$ の正規部分群



# 特殊直交群$SO(n,R)$

---

##### $n=2$

---

##### $n=3$

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

##### $n=4$

---

## 一般Lorentz群$O(n-1,1)$

##### $R$上ベクトル空間$V$における正則対称双一次形式$B$



---

##### $n=4$（Lorentz群）



---

## ユニタリ群 $U(n)$

・行列式：$|\det U|=1$

→$$U=e^{i\frac{\alpha}{n}}U',\quad(\det U=e^{i\alpha})$$とおくと、$U'\in SU(n)$

---

##### $n=1$

---

##### $n=2$

・$A=\begin{pmatrix}
a & -\bar{c}    \\
c & \bar{a}    \\
\end{pmatrix}\quad(|a|^2+|b|^2=1)$

---

## 特殊ユニタリ群 $SU(n)$

##### $n=1$

---

##### $n=2$

・$A=\begin{pmatrix}
a & -\bar{c}    \\
c & \bar{a}    \\
\end{pmatrix}\quad(|a|^2+|b|^2=1)$
と書ける

