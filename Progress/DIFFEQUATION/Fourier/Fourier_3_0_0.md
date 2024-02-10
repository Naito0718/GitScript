
      ・超関数論において開集合Ω上で考えるのはこことソボレフ空間だけ？
      ・新井 仁之　「新・フーリエ解析と関数解析学」参照。

- [超関数空間 $D'(Ω)$](#超関数空間-dω)
  - [Frechet空間 $ε(Ω)$](#frechet空間-εω)
    - [$ε(Ω)$ 上の基本的な写像](#εω-上の基本的な写像)
  - [Frechet空間 $DK(Ω)$](#frechet空間-dkω)
  - [超関数空間 $D'(Ω)$](#超関数空間-dω-1)
    - [超関数空間の性質](#超関数空間の性質)
  - [超関数空間と $ε(Ω)$](#超関数空間と-εω)
- [変分学の基本補題](#変分学の基本補題)
  - [局所可積分空間](#局所可積分空間)
  - [変分学の基本補題](#変分学の基本補題-1)
  - [局所可積分空間と超関数空間](#局所可積分空間と超関数空間)
    - [超関数空間と $L^p$ 空間](#超関数空間と-lp-空間)
- [弱微分](#弱微分)




# 超関数空間 $D'(Ω)$

## Frechet空間 $ε(Ω)$

<dl><dt>

・開集合 $\Omega\sub\bm{R}^N$、
$$p_n:C^{\infty}(\Omega)\to[0,\infty)\\\ \\
p_n(f)=\max_{|\alpha|<n}\sup_{x\in\overline{\Omega}_n}|\partial^{\alpha}f(x)|\\\ \\
\Omega_n=\left\{x\in\bm{R}^n\ |\ |x|<n,\ d(x,\bm{R}^n/\Omega)>\frac{1}{n}\right\}$$
とする。

</dt><dd>

- $\Omega=\bigcup\Omega_n$ で、$\Omega_n\sub\overline{\Omega}_n\sub \Omega_{n+1}\\$
特に、$\overline{\Omega_n}$ はコンパクト。
<br>

- $(p_n)_{n\in\bm{N}}$ はセミノルムの分離族。
ここで、
$$\epsilon(\Omega)=(C^{\infty}(\Omega),\ p_n\text{ から定まるセミノルム位相 }\mathcal{O})$$ とする。
<br>

- $(f_k)\sub\epsilon(\Omega)$、$f\in\epsilon(\Omega)$ とする。
このとき、
$$\lim_{k\to\infty}f_k=f\\\ \\
\iff\forall\alpha\in\bm{N}^N\text{ に対して、}\partial^{\alpha}f_k\text{ が }\partial^{\alpha} f\text{ に広義一様収束}\\\ \\$$

      ・Frechet空間は距離空間なので、点列で考えればよい。
      ・f∊ε(Ω)なので、無限回微分可能。
<br>

- $\epsilon(\Omega)$ はFrechet空間。
<br>

      ・可算分離族は明らか。



</dd></dl> 

---

### $ε(Ω)$ 上の基本的な写像

・開集合 $\Omega\sub\bm{R}^N$、$\alpha\in\bm{N}^N$ とする。
このとき、
$$F:\epsilon(\Omega)\to\epsilon(\Omega)\\\ \\
F(f)=\partial^{\alpha}f$$
は連続線形写像。
<br>

- 開集合 $\Omega\sub\bm{R}^N$、$g\in\epsilon(\Omega)$ とする。
このとき、
$$F:\epsilon(\Omega)\to\epsilon(\Omega)\\\ \\
F(f)=fg$$
は連続線形写像。
<br>

- 開集合 $\Omega_1,\Omega_2\sub\bm{R}^N$、$C^{\infty}$ 同相写像 $\Psi:\Omega_1\to\Omega_2$ とする。
このとき、
$$F:\epsilon(\Omega_1)\to\epsilon(\Omega_2)\\\ \\
F(f)=f\circ \Psi$$
は連続線形写像。

---

## Frechet空間 $DK(Ω)$

・開集合 $\Omega\sub\bm{R}^N$、コンパクト集合 $K\sub\Omega$ とする。
このとき、
$$D_K(\Omega)=\{f\in\epsilon(\Omega)\ |\ \mathrm{supp}\ f\sub K\}$$
は $\epsilon(\Omega)$ の閉部分空間。
よって、自然にFrechet空間。
<br>

- $(f_k)\sub D_K(\Omega)$、$f\in D_K(\Omega)$ とする。
このとき、
$$\lim_{k\to\infty}f_k=f\\\ \\
\iff\forall\alpha\in\bm{N}^N\text{ に対して、}\partial^{\alpha}f_k\text{ が }\partial^{\alpha} f\text{ に一様収束}\\\ \\$$


---

## 超関数空間 $D'(Ω)$

<dl><dt>

・開集合 $\Omega\sub\bm{R}^N$ とする。
このとき、テスト関数空間 $D(\Omega)$：
$$D(\Omega)=C^{\infty}_c(\Omega)=\bigcup_{\text{コンパクト集合 }K\sub\Omega}D_k(\Omega)$$
とすると、これは $\bm{R,C}$ 上ベクトル空間。

    ・台がコンパクトなC^∞関数全体。C_c(Ω)∩C^∞(Ω)のこと。
    ・別に非交和ではないが、接束に近い。
    ・別にテスト関数空間に位相は入ってない。
<br>

- 開集合 $\Omega_1\sub\Omega_2\sub\bm{R}^N$ とする。
このとき、
$$\phi\in D(\Omega_1)\Rightarrow 0\text{ 拡張 }\tilde{\phi}\in D(\Omega_2)$$
したがって、$D(\Omega_1)\sub D(\Omega_2)$ とみなせる。
<br>

      ・超関数の制限も、このように見なして0拡張で値をとる。
<br>

</dt><dd>

- 開集合 $\Omega\sub\bm{R}^N$、テスト関数空間 $D(\Omega)$ とする。
このとき、超関数 $u$：
$$\text{線形汎関数 }u:D(\Omega)\to\bm{R,C}\text{ であって、}\\\ \\
\forall D_K(\Omega)\sub D(\Omega)\text{ に対して}\\\ \\
u_k:D_K(\Omega)\to\bm{R,C}\text{ はFrechet空間上の連続線形汎関数}$$
ここで、超関数全体の集合 $D'(\Omega)$ は $\bm{R,C}$ 上ベクトル空間。
<br>

- $\phi\in D(\Omega)$ とする。
このとき、
$$\iota(\phi):D'(\Omega)\to\bm{C}\\\ \\
\iota(\phi)(u)=u(\phi)$$
とする。このとき、$\iota(\phi)$ は線形汎関数で、$\{\iota(\phi)\}_{\phi\in D(\Omega)}$ は線形汎関数の分離族。
よって、$D'(\Omega)$ に $\{\iota(\phi)\}_{\phi\in D(\Omega)}$ による汎弱位相を入れることができる。この線形位相空間 $D'(\Omega)$ を超関数空間という。
<br>

- $f\in\epsilon(\Omega)$、$\phi\in D(\Omega)$ とする。
このとき、$f\phi\in D(\Omega)$


</dd></dl> 

---

### 超関数空間の性質

・開集合 $\Omega\sub\bm{R}^N$、超関数空間 $D'(\Omega)$、ネット $(u_{\lambda})\sub D'(\Omega)$、$u\in D'(\Omega)$ とする。
このとき、
$$u_{\lambda}\to u\iff\forall\phi\in D(\Omega)\text{ に対して、}u_{\lambda}(\phi)\to u(\phi)\\\ \\$$

    ・u(φ)とかは複素数値。
<br>

- $\forall\phi\in D(\Omega)$ に対して、$u_n(\phi)$ が収束するような点列 $(u_n)\sub D'(\Omega)$ とする。
このとき、
$$u:D(\phi)\to\bm{C}\\\ \\
u(\phi)=\lim_{n\to\infty}u_n(\phi)$$
とすると、$u\in D'(\phi)$、すなわち、超関数の各点収束極限は超関数。
<br>

      ・収束はεとnでよいから簡単！
<br>

---

## 超関数空間と $ε(Ω)$

    ・一応弱微分とか変分学の基本補題の後。
<br>

<dl><dt>

・開集合 $\Omega\sub\bm{R}^N$、$f\in\epsilon(\Omega)$、$u\in D'(\Omega)$ とする。
このとき、
$$\Psi_{f,u}:D(\Omega)\to\bm{C}\\\ \\
\Psi_{f,u}(\phi)=u(f\phi)$$
と定めると、$\Psi\in D'(\Omega)$。ここで、$fu=\Psi_{f,u}$ と書き、$f$ と $u$ の積という。

</dt><dd>

- 多重指数 $I$ とする。
このとき、
$$\partial^I(fu)=\sum_{K\le I}\binom{I}{K}\partial^Kf\partial^{I-K}u$$

- $f\in\epsilon(\Omega)$ とする。
このとき、
$$\times f:D'(\Omega)\to D'(\Omega)\\\ \\
\times f(u)=uf$$
と定めると、これは連続線形写像。
<br>


- $f\in\epsilon(\Omega)$、$[g]\in L^1_{loc}(\Omega)$ とする。
このとき、$[fg]\in L^1_{loc}(\Omega)$ であって、
$$\Psi_{f,V([g])}(\phi)=V([fg])$$
したがって、$f$ と $[g]$ の積 $f[g]$ は $[fg]$
<br>

</dd></dl> 

---

# 変分学の基本補題

## 局所可積分空間

<dl><dt>

・開集合 $\Omega\sub\bm{R}^N$、$p\in[1,\infty]$ とする。
このとき、
$$L^p_{loc}(\Omega)=\{[f]\in L(\Omega)\ |\ \forall\text{ コンパクト集合 }K\sub\Omega\text{ に対して、}[f\chi_K]\in L^p(\Omega)\}$$
と定めると、これは $L(\Omega)$ の部分空間。ここで、$L^p_{loc}(\Omega)$ を $p$ 乗局所可積分空間という。
<br>

    ・L(Ω)は単にa.e.同一視した複素Borel関数。
    ・L^p_{loc}はノルム空間でない。
<br>

</dt><dd>

- 
$$\psi:C(\Omega)\to L(\Omega)\\\ \\
\psi(f)=[f]$$
と定めると、これは単射。よって、$C(\Omega)\sub L(\Omega)$ とみなせる。
<br>

- $p\in[1,\infty]$ とする。
このとき、
$$C(\Omega),L^p_{loc}(\Omega),D(\Omega)\sub L^1_{loc}(\Omega)\\\ \\$$

- 開集合 $\Omega\sub \bm{R}^N$、$f\in L^1(\Omega)$ とする。
このとき、
$$\|f\|_{L^1}=\sup\left\{\left.\int_{\Omega}f(x)\phi(x)dx\ \right|\ \phi\in D(\Omega),\ \sup_{x\in\Omega}|\phi(x)|\le1\right\}$$

</dd></dl> 

---

## 変分学の基本補題

・開集合 $\Omega\sub \bm{R}^N$、$[f]\in L^1_{loc}(\Omega)$ とする。
このとき、
$$\forall\phi\in D(\Omega)\text{ に対して、}\int_{\Omega}f(x)\phi(x)dx=0\\\ \\
\Rightarrow f=0\ \ (a.e.)\\\ \\$$

---

## 局所可積分空間と超関数空間

    ・超関数[f]に注意！
<br>

<dl><dt>

・開集合 $\Omega\sub \bm{R}^N$、$[f]\in L^1_{loc}(\Omega)$ とし、
このとき、
$$u_{[f]}:D(\Omega)\to\bm{C}\\\ \\
u_{[f]}(\phi)=\int_{\Omega}f(x)\phi(x)dx$$
と定めると、これは線形汎関数。
<br>

</dt><dd>

- コンパクト集合 $K\sub\Omega$、$\phi\in D_K(\Omega)$ とする。
このとき、
$$|u_{[f]}(\phi)|\le\|f|_K\|_{L^1}\|\phi\|_{\infty}\quad\ \ (\|\phi\|_{\infty}=\sup_{x\in\Omega}\{|\phi(x)|\})$$
したがって、
$$v:D_K(\Omega)\to\bm{C}\\\ \\
v(\phi)=u_{[f]}(\phi)$$
と定めると、これは連続線形汎関数。
<br>

      ・結局D_K(Ω)の収束は全部の偏微分が収束すること。
<br>

- 
$$V:L^1_{loc}(\Omega)\to D'(\Omega)\\\ \\
V([f])=u_{[f]}$$
と定めると、これは単射線形写像。特に、$L^1_{loc}(\Omega)\sub D'(\Omega)$ とみなせるので、$[f]\in D'(\Omega)$ と言ったときは $[f]=V([f])$ と考えるものとする。

</dd></dl> 

---

### 超関数空間と $L^p$ 空間

・開集合 $\Omega\sub\bm{R}^N$、$p\in[1,\infty]$ とする。
このとき、
$$V_p:L^p(\Omega)\to D'(\Omega)\\\ \\
V_p([f])=[f]$$
と定めると、これは連続関数。

    ・結局D'(Ω)での収束は、任意のD(Ω)の元φに対してu_λ(φ)が収束してればよい。
    ・別にp=∞でもよい。
    ・L^p(Ω)⊂L^p_loc(Ω)。

---
---
---

# 弱微分

<dl><dt>

・開集合 $\Omega\sub\bm{R}^N$、$u\in D'(\Omega)$ とする。
このとき、
$$\Psi_{u,j}:D(\Omega)\to\bm{C}\\\ \\
\Psi_{u,j}(\phi)=-u(\partial_j\phi)$$
と定めると、$\Psi_u\in D'(\Omega)$。ここで、$\partial_ju=\Psi_{u,j}$ と書き、$u$ の第 $j$ 座標に関する弱微分という。
<br>

</dt><dd>

- 多重指数 $I$、$\partial^I=\partial_1^{i_1}...\partial_N^{i_N}$ とする。
このとき、$\partial^Iu\in D'(\Omega)$ であって、
$$\forall \phi\in D(\Omega)\text{ に対して、}\partial^Iu(\phi)=(-1)^{|I|}u(\partial^I\phi)$$
また、
$$\partial^I:D'(\Omega)\to D'(\Omega)\\\ \\
\partial^I(u)=\partial^Iu$$
と定めると、これは連続線形写像。
<br>

- 開集合 $\Omega\sub\bm{R}^N$、第 $j$ 座標で連続な変動関数 $\partial_jf\in C(\Omega)$ を持つ連続関数 $f\in C(\Omega)$ とする。
このとき、$f,\partial_jf\in L^1_{loc}(\Omega)$ であって、
$$\forall\phi\in D(\Omega)\text{ に対して、}\partial_jf(\phi)=-f(\partial_j\phi)\\\ \\$$
特に、$f$ が上記の条件を満たすとき、$\Psi_{V[f],j}=V[\partial_jf]$


</dd></dl> 

---

