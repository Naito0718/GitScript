
- [$1/(z-a)$](#1z-a)
  - [回転数](#回転数)
    - [連結成分と回転数](#連結成分と回転数)
    - [ホモローグ $0$](#ホモローグ-0)
    - [簡単な図形](#簡単な図形)
- [$1/(|z|^p+1)$](#1zp1)
  - [実 $1/(|x|^p+1)$](#実-1xp1)
- [$z^n/(1-z^n)$](#zn1-zn)
  - [$Σz^n/(1-z^n)$](#σzn1-zn)



# $1/(z-a)$

<dl><dt>

・$a\in\bm{C}$ とする。
$$f:\bm{C}-\{a\}\to\bm{C}\\\ \\
f(z)=\frac{1}{z-a}$$
と定めると、$f$ は $\bm{C}-\{a\}$ 上正則。
<br>

    ・正則関数の逆。
<br>

</dt><dd>

- $r>0$ とする。
このとき、
$$\int_{\partial B(a,r)}\frac{1}{z-a}dz=2\pi i\\\ \\$$

- $D=\bm{C}-\{a-t\ |\ t\ge0\}$ とする。
このとき、$D$ は $\bm{C}$ 内の領域であって、
$$\forall z\in D\text{ に対して、}\frac{d}{dz}\mathrm{Log}(z-a)=\frac{1}{z-a}$$
特に、$D$ 内の区分的 $C^1$ 曲線に対する複素線積分値は $\mathrm{Log}(z_1-a)-\mathrm{Log}(z_0-a)$
<br>

- $r>0$、$f:\partial(B(a,r))\to\bm{C},\ f(z)=1$ とする。このとき、[f/(ξ-z)^n](CA_C_2_1_1.md) より、
$$F:\bm{C}-\partial(B(a,r))\to\bm{C}\\\ \\
F(z)=\int_{\partial(B(a,r))}\frac{d\xi}{\xi-z}=\begin{cases}
2\pi i & |z-a|<r  \\
0  & |z-a|>r \\
\end{cases}$$
が成り立つ。


</dd></dl>

---

## 回転数

    ・変な図形のときは、どこかで切断して分けて考えるとよい。
<br>

<dl><dt>

・$a\in\bm{C}$、$a$ を通らない区分的 $C^1$ 閉曲線 $C\sub\bm{C}-\{a\}$ とする。
このとき、
$$\frac{1}{2\pi i}\int_C\frac{dz}{z-a}\in\bm{Z}$$
ここで、
$$n(C,a)=\frac{1}{2\pi i}\int_C\frac{dz}{z-a}$$
と書き、$n(C,a)$ を $a$ に関する $C$ の回転数という。
<br>

</dt><dd>

- $$n(-C,a)=-n(C,a)\\\ \\$$

- 区分的 $C^1$ 閉曲線が、ある星形領域 $D$ に含まれるとする。
このとき、
$$\forall a\in D^c\text{ に対して、}n(C,a)=0\\\ \\$$

- $a\in\bm{C}-\{0\}$、$b\in\bm{C}$ とし、
$$\phi:\bm{C}\to\bm{C}\\\ \\
\phi(z)=az+b$$
とする。このとき、
$$n(\phi(C),\phi(a))=n(C,a)$$
すなわち、回転数は正則一次変換で不変。

</dd></dl>

---

### 連結成分と回転数

・区分的 $C^1$ 閉曲線 $C\sub\bm{C}$、$D=\bm{C}-C$ とする。
このとき、$D$ は開集合であって、
$$D\text{ の各連結成分 }D_i\text{ 上で }n(C,z)\text{ は定数であって、有界でない連結成分上では }n(C,z)=0$$
また、
$$\forall n\in\bm{N}\text{ に対して、}\{z\in\bm{C}\ |\ n(C,z)=n\}\text{ は }\bm{C}\text{ の開かつ閉集合}$$

---

### ホモローグ $0$

・領域 $D\sub\bm{C}$、$D$ 内の区分的 $C^1$ 曲線 $C\sub D$ とする。
このとき、$C$ がホモローグ $0$：
$$\forall a\in D^c\text{ に対して、}n(C,a)=0\\\ \\$$

    ・0にホモロジー同値？
<br>

- 一次元チェイン $C_1+...+C_k\sub\bm{C}$ とする。
このとき、サイクル $C_1+...+C_k$：
$$\text{すべての }C_i\text{ が閉曲線}$$
サイクルに対しても回転数 $n(C_1+...+C_k,a)$、ホモローグ $0$ の概念を考えることができる。
<br>

      ・m周円はm個のサイクルとして考えるとよい。

---

### 簡単な図形

・$a\in\bm{C}$ を中心とする半径 $r>0$ の円 $C:z(t)=a+re^{it}\quad(0\le t\le2\pi)$ とする。
このとき、
$$n(C,a)=1$$
特に、$m$ 周円 $mC:z(t)=a+re^{it}\quad(0\le t\le2m\pi)$ に対しては、
$$n(mC,a)=m$$
である。
<br>

- $a\in\bm{C}$ を対角線中心とする長方形 $C$ とする。
$$n(C,a)=1$$
特に、長方形領域中の $z$ に対して $n(C,z)=1$、外側の $z'$ に対して $n(C,z')=0$

---

# $1/(|z|^p+1)$

・$p>1$ とする。

---

## 実 $1/(|x|^p+1)$

    ・p>1。
<br>

・$$f:\bm{R}\to(0,1)\\\ \\
f(x)=\frac{1}{|x|^p+1}$$
と定めると、$f$ は値域がwell-definedな $0$ に関する偶関数。
<br>

- 
$$\int_{\bm{R}}\frac{1}{|x|^p+1}dm=\int_{0}^{\infty}\frac{2}{x^p+1}dm\le\frac{2p}{p-1}$$
特に、$f\in\mathcal{L}^1(\bm{R})$


---

# $z^n/(1-z^n)$

## $Σz^n/(1-z^n)$

    ・杉浦p.260