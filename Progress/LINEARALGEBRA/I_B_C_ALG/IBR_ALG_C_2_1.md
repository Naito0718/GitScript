
- [$R$-Banach単位的多元環](#r-banach単位的多元環)
- [スペクトル $σ(x)$,レゾルベント $ρ(x)$](#スペクトル-σxレゾルベント-ρx)
  - [$σ(x),ρ(x)$ の性質](#σxρx-の性質)


# $R$-Banach単位的多元環

<dl><dt>

・$\bm{R}$-Banach単位的多元環 $A$ とする。
このとき、
$$GL(A)=\{x\in A\ |\ \exist y\in A\text{ であって、}yx=xy=e\}$$
と定めると、これは積演算によって群をなす。
<br>

    ・積の連続性を含む。
<br>

</dt><dd>

- $x\in A,\ \|A\|<1$ とする。
このとき、$1-x\in GL(A)$ であって、
$$(1-x)^{-1}=\sum_{n\in\bm{N}}x^n$$
ただし、右辺は絶対収束する。
<br>

      ・まあ収束ベキ級数への代入とみるのがよさそう。
<br>

- $GL(A)$ は $A$ の開集合。
<br>

- 
$$J:GL(A)\to GL(A)\\\ \\
J(x)=x^{-1}$$
と定めると、これは同相写像。したがって、$GL(A)$ は積に関して位相群。

</dd></dl>

---

# スペクトル $σ(x)$,レゾルベント $ρ(x)$

・$\bm{R}$-Banach単位的多元環 $A$、$x\in A$ とする。
このとき、
$$\sigma(x)=\{\alpha\in\bm{R}\ |\ \alpha-x\notin GL(A)\}\sub\bm{R}\\\ \\
\rho(x)=\sigma(x)^c\sub\bm{R}\\\ \\
\mathrm{spr}(x)=\sup\{|\alpha|\ |\ \alpha\in\sigma(x)\}\sub[0,\infty]$$
と定めると、$\rho(x)$ は $\bm{C}$ の開集合で、$\mathrm{spr}(x)\le\|x\|$ が成り立つ。
ここで、$\rho(x)$ を $x$ のレゾルベント、$\sigma(x)$ を $x$ のスペクトル、$\mathrm{spr}(x)$ を $x$ のスペクトル半径という。
<br>

---

##  $σ(x),ρ(x)$ の性質

<dl><dt>

・$\bm{R}$-Banach単位的多元環 $A$、$x\in A$、$x$ のスペクトル $\sigma(x)$、レゾルベント $\rho(x)$ とする。
<br>

</dt><dd>

- $\alpha,\beta\in\rho(x)$ とする。
このとき、
$$(\alpha-x)^{-1}-(\beta-x)^{-1}=(\beta-\alpha)(\alpha-x)^{-1}(\beta-x)^{-1}\\\ \\$$

- $$f:\rho(x)\to A\\\ \\
f(\alpha)=(\alpha-x)^{-1}$$
と定めると、これは連続関数であって、
$$\forall\alpha\in\rho(x)\text{ に対して、}\lim_{h\to 0}\frac{f(\alpha+h)-f(\alpha)}{h}=-(\alpha-x)^{-2}\\\ \\$$

- $\sigma(x)$ はコンパクト集合。

</dd></dl>


