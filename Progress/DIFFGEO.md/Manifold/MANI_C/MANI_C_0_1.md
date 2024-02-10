
- [実解析多様体の $C^{∞}$ との対応](#実解析多様体の-c-との対応)
  - [多様体](#多様体)
    - [実解析多様体の開集合](#実解析多様体の開集合)
    - [積多様体](#積多様体)
  - [接空間 $T\_pM$](#接空間-t_pm)
  - [ベクトル場](#ベクトル場)
    - [微分 $F$\*](#微分-f)
    - [曲線と速度ベクトル](#曲線と速度ベクトル)
    - [はめ込みと沈め込み](#はめ込みと沈め込み)





# 実解析多様体の $C^{∞}$ との対応

## 多様体

### 実解析多様体の開集合

・$m$ 次元実解析多様体 $M$、開集合 $V\sub M$、$M$ のアトラス $(U_{\lambda},\phi)$ とする。
このとき、$V$ は　$m$ 次元実解析多様体で、$(U_{\lambda}\cap V,\phi_V)$ はアトラス。

---

### 積多様体

・$m,n$ 次元実解析多様体 $M,N$、アトラス $(U_{\lambda},\phi_{\lambda})\sub M,\ (V_{\eta},\psi_{\eta})$ とする。
このとき、$M\times N$ は $m+n$ 次元実解析多様体で、$(U_{\lambda,\eta},\phi_{\lambda}\times\psi_{\eta})$ はアトラス。

---

## 接空間 $T_pM$

    ・C^ω(M)上の、線形汎関数かつ導分であるもの全体。

・$m$ 次元実解析多様体 $M$、$p\in M$、チャート $(U,\phi)\sub M$ とする。
このとき、$\frac{\partial}{\partial x^i}|_p$ は $T_pM$ の基底。よって、$\mathrm{dim}\ T_pM=N$
<br>

    ・これの証明は結局C^∞と同じ。

---

## ベクトル場

    ・実解析ベクトル場：とりあえず係数関数が全部実解析。
    ・括弧積もwell-defined。

・$m$ 次元実解析多様体 $M$、開集合 $U\sub M$、$U$ 上で定められたベクトル場 $X$、$f\in C^{\omega}(U)$ とする。
このとき、
$$Xf:U\to\bm{R}\\\ \\
Xf(p)=X_p(f)$$
と定めると、これはwell-definedで、$X$ が実解析ベクトル場ならば $Xf\in C^{\omega}(U)$

---

### 微分 $F$*

<dl><dt>

・$m,n$ 次元実解析多様体 $M,N$、実解析写像 $F:M\to N$ とする。
<br>

</dt><dd>

- $f\in C_{F(p)}^{\omega}(N)$ に対して、
$$f\circ F\in C_p^{\omega}(M)$$

      ・任意の f に対して同じ値（同値類）を返す。

- 
$$F_*:T_pM\to T_{F(p)}N\\\ \\
F_*(X_p)(f)=X_p(f\circ F)$$と定めると、これはwell-definedで線形写像。
<br>

- $C^{\omega}$ 写像の合成について、
$$(G\circ F)_{*,p}=G_{*,F(p)}\circ F_{*,p}$$特に、$1_{M}:M\to M$ に対して、
$$(1_{M})_{*,p}=1_{T_p(M)}$$

- $F$ が微分同相ならば、
微分 $F_*:T_p(M)\to T_{F(p)}N$ は同型写像。
<br>

- $$F_*\left(\left.\frac{\partial}{\partial x^i}\right|_p\right)=\sum_j\frac{\partial F^j}{\partial x^i}(p)\left.\frac{\partial}{\partial y^j}\right|_{F(p)}$$

      ・逆関数定理⇔微分F_*が線形同型。

- 定数関数 $F:M\to N,\ F(p)=q$ に対して、
$$F_*=0$$

</dd></dl>

---

### 曲線と速度ベクトル

・$m$ 次元 $C^{\omega}$ 多様体 $M$、$p\in M$ とする。
このとき、$p$ を始点とする滑らかな曲線 $c$：
$$c:(a,b)\to M,\quad c(0)=p\\\ \\
\text{を満たす }C^{\omega}\text{ 写像}$$

- 速度ベクトル：
$$c'(t)=c_{*}\left(\left.\frac{d}{dt}\right|_p\right)\in T_{c(t)}M$$

      ・R^nへの曲線ならば、c'(t)=dc^i/dt(t) ∂/∂x^i|_(c(t))

- $\forall p\in M,\ \forall X_p\in T_pM$ に対して、$\exist\epsilon >0$ と滑らかな曲線 $c:(-\epsilon,\epsilon)\to M$ であって、
$$c(0)=p,\ c'(0)=X_p$$さらに、この滑らかな曲線は
$$X_p(f)=\left.\frac{d}{dt}\right|_0(f\circ c)\quad (\forall f\in C_p^{\infty}(M))\\\ \\
F_{*,p}(X_p)=\left.\frac{d}{dt}\right|_0(F\circ c)(t)\quad(\forall C^{\infty}\text{ 写像 }F:M\to N)$$を満たす。

      ・X_p は与えられてる。

---

### はめ込みと沈め込み



<dl><dt>

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$p\in M$、$C^{\infty}$ 写像 $F:M\to N$ に対して、
点 $p$ におけるはめ込み、沈め込み：
$$F_{*,p}:T_pM\to T_{F(p)}N\text{ がそれぞれ単射、全射。}$$

    ・pで沈め込みになるとき、pを正則点という。正則点でなければ臨界点。
    ・臨界点の像：臨界値、それ以外：正則値

</dt><dd>

- $$F\text{ がはめ込み}\Rightarrow m\le n\\\ \\
F\text{ が沈め込み}\Rightarrow m\ge n\\\ \\$$

- $$q\text{ が臨界値}\iff \exist p\in F^{-1}(q)\text{ であって、}p\text{ は臨界点}\\\ \\
q\text{ が正則値}\iff \forall p\in F^{-1}(q)\text{ が正則点}\\\ \\$$

      ・実数値関数なら、pが臨界点⇔∂f/∂x^i(p)=0 (i=1,...,m)

</dd></dl>


---

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$p\in M$、$C^{\infty}$ 写像 $F:M\to N$ に対して、
$p$ における $F$ の階数：
$$\dim F_{*,p}(T_pM)=\mathrm{rank}\frac{\partial F^i}{\partial x^j}(p)\\\ \\
$$


---