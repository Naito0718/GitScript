
    ・第二可算局所コンパクト群専用ページ！？

- [局所コンパクト位相群とHaar測度](#局所コンパクト位相群とhaar測度)
  - [準備](#準備)
    - [局所コンパクトHausdorff空間 $X$ 上の連続関数環](#局所コンパクトhausdorff空間-x-上の連続関数環)
    - [非負値なコンパクトサポート関数とHarr測度の準備](#非負値なコンパクトサポート関数とharr測度の準備)
  - [局所コンパクト群上のHarr測度](#局所コンパクト群上のharr測度)
    - [Harr測度の性質](#harr測度の性質)
    - [モジュラー関数](#モジュラー関数)
    - [ユニモジュラー](#ユニモジュラー)
  - [$L^p$ 空間](#lp-空間)
    - [合成積](#合成積)
      - [Youngの不等式](#youngの不等式)
    - [$L^1$ 群環](#l1-群環)
    - [測度群環 $M(G)$ とディラック測度](#測度群環-mg-とディラック測度)
- [局所コンパクト群のユニタリ表現](#局所コンパクト群のユニタリ表現)



# 局所コンパクト位相群とHaar測度

    ・Hausdorffでもある。
    ・離散群は局所コンパクト群。



## 準備

### 局所コンパクトHausdorff空間 $X$ 上の連続関数環

    ・FuncAnal_1参照。

<dl><dt>

・局所コンパクト位相群 $G$、$f\in C_0(G)$ とする。

</dt><dd>

- 
$$\forall\epsilon>0\text{ に対して、}\exist\text{ 対称開近傍 }V\in\mathcal{N}(e),\ V^{-1}=V\text{ であって、}\\\ \\
yx^{-1}\in V\ \ \mathrm{or}\ \ x^{-1}y\in V\Rightarrow|f(x)-f(y)|<\epsilon\\\ \\$$ 

- 
$$\psi_L,\psi_R:G\to C_0(G)\\\ \\
\psi_L(g)=L_gf,\quad\psi_R(g)=R_gf$$
はともにノルム*-環 $C_0(G)$ 上連続。

    ・C_0(G)はsupノルムが入ってる。
    ・f∊C_c(G)なら、L_gf∊C_c(G)。

</dd></dl>

---

### 非負値なコンパクトサポート関数とHarr測度の準備

<dl><dt>

・局所コンパクト群 $G$ とする。
また、
$$C_{c,+}=\{f\in C_c(G)\ |\ f(g)\ge0\ \ \forall g\in G\},\quad C_{c,++}=C_{c,+}(G)-\{0\}$$ とする。
このとき、
$$C_{c,++}\neq\phi\\\ \\
\forall f\in C_{c,++}\text{ に対して、}\|f\|>0$$

    ・上のはUrysohnによる。
    ・C_{c,++}のHarr測度での積分は、(0,∞)。
<br>

- 局所コンパクト群 $G$、$f,g\in C_{c,++}$ とする。
このとき、
$$(f,g)=\\\ \\
\inf\left\{\sum_{j=1}^nc_j\ |\ c_j\ge0\text{ かつ、}\forall x\in G\text{ に対して、}\exist x_j\in G\text{ であって、}\right.\\\ \\
\left.f(x)\le\sum c_jL_{x_j}g(x)\right\}$$
と定めると、これはwell-defined、すなわち右辺の集合は空でない。
<br>

</dt><dd>

- 局所コンパクト群 $G$、$f,g,h\in C_{c,++}$、$\alpha>0$ とする。
このとき、
$$0<\frac{\|f\|}{\|g\|}<(f,g)<\infty\\\ \\
(f+g,h)\le(f,h)+(g,h)\\\ \\
(\alpha f,g)=\alpha(f,g)\\\ \\
(L_yf,g)=(f,g)\\\ \\
(f,h)\le(f,g)(g,h)$$


</dd></dl>

---

・局所コンパクト群 $G$、$\phi,f_0,\in C_{c,++}$ とする。
このとき、
$$\Lambda_{\phi}:C_{c,++}\to(0,\infty)\\\ \\
\Lambda_{\phi,f_0}(f)=\frac{(f,\phi)}{(f_0,\phi)}$$
と定めると、これはwell-defined。

- 局所コンパクト群 $G$、$\phi,f_0,f,g\in C_{c,++}$ とする。
このとき、
$$\Lambda_{\phi,f_0}(f+g)\le\Lambda_{\phi,f_0}(f)+\Lambda_{\phi,f_0}(g)\\\ \\
\Lambda_{\phi,f_0}(\alpha f)=\alpha\Lambda_{\phi,f_0}(f)\\\ \\
\Lambda_{\phi,f_0}(L_gf)=\Lambda_{\phi,f_0}(f)\\\ \\
\frac{1}{(f,f_0)}\le\Lambda_{\phi,f_0}\le(f,f_0)\\\ \\$$

-  局所コンパクト群 $G$、$f_0,f,g\in C_{c,++}$ とする。
このとき、
$$\forall\epsilon>0\text{ に対して、}\exist\ G\text{ の開近傍 }U\in\mathcal{N}(e)\text{ であって、}\\
\mathrm{supp}\ \phi\sub U\text{ なる }\forall\phi\in C_{c,++}\text{ に対して、}\\\ \\
\Lambda_{\phi,f_0}(f)+\Lambda_{\phi,f_0}(g)\le \Lambda_{\phi,f_0}(f+g)+\epsilon$$

---
---
---


## 局所コンパクト群上のHarr測度

・局所コンパクト群 $G$、Radon測度：$\mu:\mathfrak{B}_G\to[0,\infty]$ とする。
このとき、左、右Harr測度 $\mu$：
$$\text{左：}\mu(G)>0,\quad\mu(gB)=\mu(B)\ \ (\forall g\in G,\ \forall B\in\mathfrak{B}_G)\\\ \\
\text{右：}\mu(G)>0,\quad\mu(Bg)=\mu(B)\ \ (\forall g\in G,\ \forall B\in\mathfrak{B}_G)$$


<br>
<dl><dt>

・局所コンパクト位相群 $G$、$f\in C_0(G)$ とする。



</dt><dd>

- 単位元の開近傍 $e\in U\sub G$ とする。
$$X=\Pi_{f\in C_{c,++}}[(f_0,f)^{-1},(f,f_0)]\\\ \\
K(U)=\{\{\Lambda_{\varphi,f_0}(f)\}_{f\in C_{c,++}(G)}\ |\ \varphi\in C_{c,++}(G),\ \mathrm{supp}\ \varphi\sub U\}$$
と定めると、$X$ はコンパクト集合で、$K(U)\neq\phi$ 
さらに、$U_1\sub U_2$ ならば $K(U_1)\sub K(U_2)$ であって、$$\bigcap_{U\text{ は単位元の開近傍}}\overline{K(U)}\neq\phi$$
<br>

- $$\Lambda_0\in \bigcap_{U\text{ は単位元の開近傍}}\overline{K(U)}$$ とする。このとき、
$$\forall \text{ 開近傍 }U\in\mathcal{N}(e),\ \forall\epsilon>0,\forall\text{ 有限個の }f_1,...,f_n\in C_{c,++}\text{ に対して、}\\
\exist\varphi\in C_{c,++}(G),\ \mathrm{supp}\ \varphi\sub U\text{ であって、}\\\ \\
|\Lambda_0(f_i)-\Lambda_{\varphi,f_0}(f_i)|<\epsilon$$
したがって、$f,g\in C_{c,++}(G)$、$\alpha>0$ とすると、
$$\Lambda_0(f)>0\\\ \\
\Lambda_0(f+g)=\Lambda_0(f)+\Lambda_0(g)\\\ \\
\Lambda_0(\alpha f)=\alpha\Lambda_0(f)\\\ \\
\Lambda_0(L_gf)=\Lambda_0(f)\\\ \\$$

- $\Lambda_0(0)=0$ とし、
$$\Lambda:C_{c,\bm{R}}(G)\to\bm{R}\\\ \\
\Lambda(f)=\Lambda_0(f_+)-\Lambda_0(f_-)$$
と定めると、$\Lambda$ はRadon汎関数。

      ・mathpediaのルベーグ積分参照。
<br>

- 上記のRadon汎関数によって定まるRadon測度 $\mu$ は、左Harr測度。
したがって、任意の局所コンパクト位相群 $G$ に対して、左Harr測度が存在する。
<br>

</dd></dl>

- 局所コンパクト群 $G$、左Harr測度 $\mu_1,\mu_2:\mathfrak{B}_G\to[0,\infty]$ とする。
このとき、
$$\exist c>0\text{ であって、}\mu_1(B)=c\mu_2(B)\ \ (\forall B\in\mathfrak{B}_G)$$

      ・右も同様。
      ・もし左Harr測度で関数を積分するなら、それはあるHarr測度での積分のc倍になる。
      ・ちょっとしたHaar測度とC_{c,+}関数の積分の関係。

---


### Harr測度の性質

・局所コンパクト群 $G$、左Harr測度 $\mu:\mathfrak{B}_G\to[0,\infty]$、非負値Borel関数 $f:G\to[0,\infty]$ とする。
このとき、
$$\int_GL_yfd\mu=\int_Gfd\mu$$

    ・右Harrでも同様。

- 第二可算局所コンパクト群 $G$、左Harr測度 $\mu:\mathfrak{B}_G\to[0,\infty]$、空でない開集合 $U\sub G$ とする。
このとき、
$$\mu(U)>0$$

---

### モジュラー関数

<dl><dt>

・局所コンパクト群 $G$、左Harr測度 $\mu:\mathfrak{B}_G\to[0,\infty]$、$g\in G$ とする。
このとき、
$$\mu_g:\mathfrak{B}_G\to[0,\infty]\\\ \\
\mu_g(B)=\mu(Bg)$$は左Harr測度。
よって、
$$\Delta:G\to(0,\infty)\\\ \\
\mu(Bg)=\Delta(g)\mu(B)\quad(\forall B\in\mathfrak{B}_G)$$
はwell-defined。これをモジュラー関数という。

    ・gBにすると、Harr測度なので変わらない。
    ・選んだ測度に依存する。
<br>

</dt><dd>

- 局所コンパクト群 $G$、左Harr測度 $\mu:\mathfrak{B}_G\to[0,\infty]$、非負値Borel関数 $f:G\to[0,\infty]$ とする。
このとき、
$$\Delta(y)\int_Gf(x)d\mu=\int_Gf(xy^{-1})d\mu\\\ \\
\Delta:G\to(0,\infty)\text{ は乗法群 }(0,\infty)\text{ への連続準同型}\\\ \\$$

</dd></dl>

---

・局所コンパクト位相群 $G$、左Harr測度 $\mu$ とする。
このとき、
$$\Lambda_{\Delta}:C_{c,\bm{R}}(G)\to\bm{R}\\\ \\
\Lambda_{\Delta}(f)=\int_G f(x^{-1})\Delta(x)^{-1}d\mu$$とすると、これはRadon汎関数。
さらに、$$\int_G f(yx^{-1})\Delta(x)^{-1}d\mu=\int_G f(x^{-1})\Delta(x)^{-1}d\mu$$より、上記のRadon汎関数より定まるRadon測度 $\mu_{\Delta}$ は左Haar測度。

    ・リー群と表現論、p.80
<br>

- $$\int_Gf(x^{-1})\Delta(x^{-1})d\mu=\int_Gf(x)d\mu$$

      ・f◦Jは非負値Borelだから、これでfの変数をひっくり返せる。


---

### ユニモジュラー

・局所コンパクト群 $G$、左Harr測度 $\mu:\mathfrak{B}_G\to[0,\infty]$ とする。
このとき、$\mu$ がユニモジュラー：
$$\Delta(g)=1\ \ (\forall g\in G)$$
これは、$\mu$ が右Harr測度であることと同値。
特に、任意の左Harr測度 $\mu$ がユニモジュラーなとき、$G$ がユニモジュラーであるという。
<br>

- 局所コンパクト可換群、離散群、コンパクト群はユニモジュラー。

## $L^p$ 空間

・局所コンパクト位相群 $G$、左Harr測度 $\mu$、$p\in[1,\infty)$、$f\in L^p(G,\mu)$ とする。
このとき、
$$L:G:\to L^p(G,\mu)\\\ \\
L(g)=[L_gf]$$は well-definedであって、$L^p$ ノルムで連続。
したがって、$L$ はBanach空間 $L^p(G,\mu)$ 値有界連続関数。

    ？？？

### 合成積

    ・畳み込み
    ・G：コンパクトなら像は可分か？

・局所コンパクト群 $G$、Harr測度 $\mu$、$p\in[1,\infty)$、$f\in L^p(G,\mu)$ とする。

#### Youngの不等式

・

### $L^1$ 群環

### 測度群環 $M(G)$ とディラック測度

    ・ディラック測度はR^Nでも通用する。

---
---
--- 

# 局所コンパクト群のユニタリ表現

    ・無限次元表現も考える。







