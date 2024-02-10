
- [$C$-Banach単位的多元環と逆元](#c-banach単位的多元環と逆元)
- [スペクトルとレゾルベント](#スペクトルとレゾルベント)
  - [$σ(x),ρ(x)$ の性質](#σxρx-の性質)
- [集合 $H(K)$](#集合-hk)
  - [正則汎関数計算](#正則汎関数計算)
    - [正則汎関数計算の性質](#正則汎関数計算の性質)
    - [Gelfandの公式](#gelfandの公式)
    - [正則汎関数計算と $exp$](#正則汎関数計算と-exp)


# $C$-Banach単位的多元環と逆元

<dl><dt>

・$\bm{R,C}$-Banach単位的多元環 $A$ とする。
このとき、
$$GL(A)=\{x\in A\ |\ \exist y\in A\text{ であって、}yx=xy=e\}$$
と定めると、これは積演算によって群をなす。
<br>

    ・積で連続ではある。
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

# スペクトルとレゾルベント

・$\bm{C}$-Banach単位的多元環 $A$、$x\in A$ とする。
このとき、
$$\sigma(x)=\{\alpha\in\bm{C}\ |\ \alpha-x\notin GL(A)\}\sub\bm{C}\\\ \\
\rho(x)=\sigma(x)^c\sub\bm{C}\\\ \\
\mathrm{spr}(x)=\sup\{|\alpha|\ |\ \alpha\in\sigma(x)\}\sub[0,\infty]$$
と定めると、$\rho(x)$ は $\bm{C}$ の開集合で、$\mathrm{spr}(x)\le\|x\|$ が成り立つ。
ここで、$\rho(x)$ を $x$ のレゾルベント、$\sigma(x)$ を $x$ のスペクトル、$\mathrm{spr}(x)$ を $x$ のスペクトル半径という。

---

##  $σ(x),ρ(x)$ の性質

<dl><dt>

・$\bm{C}$-Banach単位的多元環 $A$、$x\in A$、$x$ のスペクトル $\sigma(x)$、レゾルベント $\rho(x)$ とする。
<br>

</dt><dd>

- $\alpha,\beta\in\rho(x)$ とする。
このとき、
$$(\alpha-x)^{-1}-(\beta-x)^{-1}=(\beta-\alpha)(\alpha-x)^{-1}(\beta-x)^{-1}\\\ \\$$

- 
$$f:\rho(x)\to A\\\ \\
f(\alpha)=(\alpha-x)^{-1}$$
と定めると、これはBanach空間値正則関数であって、
$$\frac{df}{dz}(\alpha)=-(\alpha-x)^{-2}\\\ \\$$

- $\sigma(x)$ は空でないコンパクト集合。

</dd></dl>

---

# 集合 $H(K)$

<dl><dt>

・空でないコンパクト集合 $K\sub\bm{C}$ とする。
このとき、
$$\mathcal{H}(K)=\{f:\bm{C}\supset D(f)\to\bm{C}\ |\ K\sub D(f)\text{ であって、}f\text{ は開集合 }D(f)\text{ 上で正則}\}$$
とし、$f,g\in\mathcal{H}(K)$、$\alpha\in\bm{C}$ に対して、
$$f+g\coloneqq D(f+g)=D(f)\cap D(g),\quad (f+g)(z)=f(z)+g(z)\quad(\forall z\in D(f+g))\\\ \\
\alpha f\coloneqq D(\alpha f)=D(f),\quad (\alpha f)(z)=\alpha f(z)\quad(\forall z\in D(\alpha f))\\\ \\
fg\coloneqq D(fg)=D(f)\cap D(g),\quad (fg)(z)=f(z)g(z)\quad(\forall z\in D(fg))\\\ \\$$
と定めると、$f+g,\ \alpha f,\ fg\in\mathcal{H}(K)$ が成り立つ。すなわち、$\mathcal{H}(K)$ は $\bm{C}$ 上可換単位的多元環。
<br>

</dt><dd>

- $f,g\in \mathcal{H}(K)$ とする。
このとき、
$$f\sim g\iff\\\ \\
K\sub U\sub D(f)\cap D(g)\text{ なる }\exist\text{ 開集合 }U\sub\bm{C}\text{ であって、}\\\ \\
f(z)=g(z)\quad(\forall z\in U)$$
と定めると、これは $\mathcal{H}(K)$ 上の同値関係であって、
$$[f]+[g]=[f+g],\quad\alpha[f]=[\alpha f],\quad[f][g]=[fg]$$
と定めると、これはwell-defined。
ここで、この同値関係による商集合 $\mathcal{H}/\sim$ を $H(K)$ と書く。明らかに、$H(K)$ は $\bm{C}$ 上可換単位的多元環。
<br>

</dd></dl>

---

## 正則汎関数計算

・$\bm{C}$-Banach単位的多元環 $A$、$x\in A$ とする。
このとき、
$$\Psi_x:H(\sigma(x))\to A\\\ \\
\Psi_x([f])=\frac{1}{2\pi i}\int_Cf(w)(w-x)^{-1}dw\\\ \\
(\sigma(x)\prec C\prec D(f))$$
と定めると、これはwell-defined、すなわち、$C$ によらず、$[f]$ にもよらない。ただし、$f(w)(w-x)^{-1}$ は $D(f)-\sigma(x)$ 上正則。
ここで、$\Psi_x$ を $x$ の関する正則汎関数計算という。

---

### 正則汎関数計算の性質

<dl><dt>

・$\bm{C}$-Banach単位的多元環 $A\neq\{0\}$、$x\in A$、正則汎関数計算 $\Psi_x:H(\sigma(x))\to A$ とする。
<br>

</dt><dd>

- $1:\bm{C}\to\bm{C},\quad 1(z)=1$ とする。
このとき、$1,id\in \mathcal{H}(\sigma(x))$ であって、
$$\Psi_x(1)=1,\quad\Psi_x(id)=x\\\ \\$$

- $[f],[g]\in H(\sigma(x))$、$\alpha\in\bm{C}$ とする。
このとき、
$$\Psi_x(f+g)=\Psi_x(f)+\Psi_x(g),\quad\Psi_x(\alpha f)=\alpha\Psi_x(f)\\\ \\
\Psi_x(fg)=\Psi_x(f)\Psi_x(g)=\Psi_x(g)\Psi_x(f)\\\ \\$$

- $[f]\in H(\sigma(x))$ とする。
このとき、
$$\sigma(\Psi_x(f))=f(\sigma(x))\\\ \\$$

- $[f]\in H(\sigma(x))$、$[g]\in H(f(\sigma(x)))$ とする。
このとき、$[g]\circ[f]$ はwell-definedであって、
$$\Psi_{\Psi_x(f)}(g)=\Psi_x(g\circ f)\\\ \\$$

- $\sigma(x)$ 含む開集合 $U\sub\bm{C}$、$f:\bm{U}\to\bm{C}$ にコンパクト一様収束する正則関数列 $f_n:U\to\bm{C}$ とする。
このとき、
$$\lim_{n\to\infty}\Psi_x(f_n)=\Psi_x(f)$$

</dd></dl>

---

### Gelfandの公式

・$\bm{C}$-Banach単位的多元環 $A\neq\{0\}$、$x\in A$ とする。
このとき、
$$\mathrm{spr}(x)=\lim_{n\to\infty}\sqrt[n]{\|x^n\|}=\inf_{n\in\bm{N}}\sqrt[n]{\|x^n\|}$$

---

### 正則汎関数計算と $exp$

・$\bm{C}$-Banach単位的多元環 $A\neq\{0\}$、$x\in A$ とする。
このとき、
$$\Psi_x(\exp)=\exp(x)=\sum\frac{x^n}{n!}$$


