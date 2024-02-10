
- [$R,C$ 上ベクトル空間の基底の存在](#rc-上ベクトル空間の基底の存在)
- [$C$ 上ベクトル空間と $R$ 上ベクトル空間](#c-上ベクトル空間と-r-上ベクトル空間)
  - [線形写像](#線形写像)
  - [反双線形写像](#反双線形写像)
- [Minkowski汎関数](#minkowski汎関数)
  - [$R$ 上におけるHahn-Banachの拡張定理](#r-上におけるhahn-banachの拡張定理)



# $R,C$ 上ベクトル空間の基底の存在

・$\bm{R,C}$ 上ベクトル空間 $V$、部分集合 $D\subset V$ が $D\backslash\{0\}\neq\phi$ を満たすとする。
このとき、$$\mathrm{span}(D_0)=\mathrm{span}(D)$$を満たす線形独立な $D_0\subset D$ が存在する。

<details><summary>proof</summary><div>

a

>https://old.math.jp/wiki/%E9%80%9F%E7%BF%92%E3%80%8C%E7%B7%9A%E5%BD%A2%E7%A9%BA%E9%96%93%E8%AB%96%E3%80%8D#4._.E7.B7.9A.E5.BD.A2.E7.8B.AC.E7.AB.8B.E6.80.A7.E3.80.81.E7.B7.9A.E5.BD.A2.E7.A9.BA.E9.96.93.E3.81.AE.E6.AC.A1.E5.85.83

</div></details><br>



- $\bm{C,R}$ 上ベクトル空間 $V$、線形独立な部分集合 $B,C$ とする。
このとき、$\mathrm{span}(B)=\mathrm{span}(C)$ ならば、
$B,C$ の濃度は等しい。
<br>

- $\bm{C,R}$ 上ベクトル空間 $V$、線形独立な部分集合 $B\subset V$ とする。
このとき、$B\subset C$ を満たす $V$ の基底 $C$ が存在する。

---

# $C$ 上ベクトル空間と $R$ 上ベクトル空間

## 線形写像

・実数上の線形写像 $\phi:V_{\bm{R}}\to\bm{R}$ に対して、
$$\psi(x)=\phi(x)-i\phi(ix)$$は $\bm{C}$ 上の線形写像。

---

## 反双線形写像

<dl><dt>

・$\bm{C}$ 上ベクトル空間 $V,W$、$T:V\to W$ とする。
このとき、反線形写像 $T$：
$$T(u+v)=Tu+Tv,\quad T(\alpha u)=\bar{\alpha}Tu\\\ \\
(\forall u,v\in V,\ \forall \alpha\in \bm{C})\\\ \\$$

- $\bm{C}$ 上ベクトル空間 $V,W,U$、$S:V\times W\to U$ とする。
このとき、準双線形写像 $S$：$S$ は第一引数で反線形、第二引数で線形。
<br>

</dt><dd>

- $\bm{C}$ 上ベクトル空間 $V,W$、準双線形写像 $\Psi:V\times V\to W$ とする。
このとき、
$$\Psi(u,v)=\frac{1}{4}\sum_{k=0}^3i^k\Psi(i^ku+v,i^ku+v)$$  

      ・偏極恒等式

</dd></dl>

---

# Minkowski汎関数

・$\bm{R,C}$ 上ベクトル空間 $V$、$m:V\to\bm{R}$ とする。 
このとき、Minkowski汎関数 $m$：
$$\forall x,y\in V\text{ に対して、}m(x+y)\le m(x)+m(y)\\\ \\
\forall\alpha\in[0,\infty),\ \forall x\in V\text{ に対して、}\text{ に対して }m(\alpha x)=\alpha m(x)$$

---

## $R$ 上におけるHahn-Banachの拡張定理

・$\bm{R}$ 上ベクトル空間 $V$、Minkowski汎関数 $m:V\to\bm{R}$、部分空間 $M\subset V$、線形汎関数 $\phi:M\to\bm{R}$ とする。
このとき、$\phi(x)\le m(x)\ (\forall x\in M)$ ならば、
$$\exist\tilde{\phi}\in V^*\text{ であって、}\\\ \\
\tilde{\phi}|_M=\phi,\quad\tilde{\phi}(x)\le m(x)\quad (\forall x\in X)\\\ \\$$

    ・R上！また、一意性は成り立たない。

