
- [Radon-Nikodim微分と複素数値測度での積分](#radon-nikodim微分と複素数値測度での積分)
  - [複素数値測度と密度関数](#複素数値測度と密度関数)
    - [実数値測度とHahn分解](#実数値測度とhahn分解)
    - [実数値測度とJordan分解](#実数値測度とjordan分解)
  - [絶対連続とRadon-Nikodymの定理、Radon-Nikodym微分](#絶対連続とradon-nikodymの定理radon-nikodym微分)
  - [複素数値測度に対する全変動](#複素数値測度に対する全変動)
    - [複素数値測度の積分](#複素数値測度の積分)
- [Radon測度](#radon測度)
  - [局所コンパクトHausdorff空間 $X$ 上のRadon測度](#局所コンパクトhausdorff空間-x-上のradon測度)
    - [Radon測度](#radon測度-1)
    - [有限測度とRadon測度](#有限測度とradon測度)
    - [Radon汎関数とRiesz-Markov-角谷の表現定理](#radon汎関数とriesz-markov-角谷の表現定理)
  - [第二可算性とRadon測度](#第二可算性とradon測度)
    - [複素数値Radon測度](#複素数値radon測度)
  - [複素数値Radon測度のなすBanach空間 $M(X)$](#複素数値radon測度のなすbanach空間-mx)






# Radon-Nikodim微分と複素数値測度での積分

## 複素数値測度と密度関数

<dl><dt>

・可測空間 $X$、$\nu:\mathfrak{M}\to\bm{C}$ に対して、
複素数値測度 $\nu$：
$$\forall\text{ 非交叉列 }E_n\subset\mathfrak{M}\text{ に対して、}\\\ \\
\nu\left(\bigcup_{n\in\bm{N}} E_n\right)=\sum_{n\in\bm{N}}\nu(E_n)$$

    ・実数値測度も同様。

</dt><dd>

- $$\nu(\phi)=0\\\ \\
\text{ 非交叉な可測集合 }E_1,...,E_N\subset \mathfrak{M}\text{ に対して、}\nu\left(\bigcup_{n=1}^NE_n\right)=\sum_{n=1}^n\nu(E_n)\\\ \\
\text{単調増加列 }E_n\subset\mathfrak{M}\text{ に対して、}\nu(\bigcup E_n)=\lim_{n\to\infty}\nu(E_n)\\\ \\
\text{単調減少列 }E_n\subset\mathfrak{M}\text{ に対して、}\nu(\bigcap E_n)=\lim_{n\to\infty}\nu(E_n)$$

      ・実数値測度でも同様。

- 複素数値測度 $\mu_1,\mu_2$ に対して、
$$\mu_1+\mu_2,\quad \lambda\mu_1$$ も複素数値測度。

      ・実数値測度も同様。

</dd></dl>

---

<dl><dt>

・測度空間 $(X,\mathfrak{M},\mu)$ とする。

</dt><dd>

- 非負値可測関数 $f:X\to[0,\infty]$ に対して、
$$\mu_f:\mathfrak{M}\to[0,\infty]\\\ \\
\mu_f(E)=\int_Efd\mu$$は $(X,\mathfrak{M})$ 上の測度。
さらに、$\mu$ に関して絶対連続。
<br>

- - $f\in\mathcal{L}^1_{\bm{R}}(X)$ に対して、
$$\mu_f:\mathfrak{M}\to\bm{R}\\\ \\
\mu_f(E)=\int_Efd\mu$$は $(X,\mathfrak{M})$ 上の実数値測度。
さらに、$\mu$ に関して絶対連続で、
  - Hahn分解：$$(f\ge0),\ (f<0)\in\mathfrak{M}$$
  - Jordan分解：$$\mu_{f_{\pm}}(E)=\int_Ef_{\pm}d\mu\in[0,\infty)$$
<br>

- $f\in\mathcal{L}^1(X)$ に対して、
$$\mu_f:\mathfrak{M}\to\bm{C}\\\ \\
\mu_f(E)=\int_Efd\mu$$は $(X,\mathfrak{M})$ 上の複素数値測度。
さらに、$\mu$ に関して絶対連続。

</dd></dl>

---

### 実数値測度とHahn分解

・可測空間 $(X,\mathfrak{M})$、実数値測度 $\nu:\mathfrak{M}\to\bm{R}$、$P\in\mathfrak{M}$ とする。
このとき、$P$ が $\nu$ に対して非負、非正：
$$\forall E\in\mathfrak{M}\text{ に対して }\nu(E\cap P)\ge0\\\ \\
\forall E\in\mathfrak{M}\text{ に対して }\nu(E\cap P)\le0$$

    ・非負な集合列E_nの合併∪E_nも非負

<dl><dt>

・可測空間 $(X,\mathfrak{M})$、実数値測度 $\nu:\mathfrak{M}\to\bm{R}$ とする。

</dt><dd>

- $$\forall A\in \mathfrak{M},\ \forall \epsilon>0\text{ に対して、}\exist B\in\mathfrak{M}\text{ であって、}\\\ \\
B\subset A,\quad\nu(B)\ge\nu(A)\\\ \\
\nu(E)\ge-\epsilon\quad(B\supset\forall E\in\mathfrak{M})\\\ \\$$

- $$\forall A\in\mathfrak{M}\text{ に対して、}\exist\nu\text{ に対して非負} P\in\mathfrak{M}\text{ であって、}\\\ \\
\nu(P)\ge\nu(A)\\\ \\$$ 

- $$\sup\{\nu(E)\ |\ e\in\mathfrak{M}\}<\infty\\\ \\$$

- $X$ の可測分割 $A_+,A_-$ であって、それぞれ非負、非正であるものが存在する。

      ・Hahn分解
      ・N=P^c

</dd></dl>

---

### 実数値測度とJordan分解

・可測空間 $(X,\mathfrak{M})$、測度 $\mu_1,\mu_2:\mathfrak{M}\to[0,\infty]$ とする。
このとき、互いに特異 $\mu_1\perp\mu_2$：
$$\exist\text{ 可測分割 }X=A_1\cup A_2\text{ であって、}\\\ \\
\mu_1(E)=\mu_1(E\cap A_1),\ \mu_2(E)=\mu_2(E\cap A_2)\quad(\forall E\in\mathfrak{M})\\\ \\$$

      ・実数値測度、複素数値測度でも同様。

- 可測空間 $(X,\mathfrak{M})$、実数値測度 $\nu:\mathfrak{M}\to\bm{R}$ とする。
このとき、$$\exist\text{ 有限測度 }\nu_+,\nu_-:\mathfrak{M}\to[0,\infty)\text{ であって、}\\\ \\
\nu_+\perp\nu_-,\quad\nu=\nu_+-\nu_-$$を満たすものがただ一つ存在する。
さらに、Hahn分解 $A_+,A_-$ に対して、
$$\nu_{\pm}(E)=\pm\nu(E\cap A_{\pm})\quad(\forall E\in\mathfrak{M})$$が成り立つ。

      ・Jordan分解
      ・正負はこれでよい。

---

## 絶対連続とRadon-Nikodymの定理、Radon-Nikodym微分

<dl><dt>

・測度空間 $(X,\mathfrak{M},\mu)$、測度 $\nu$ とする。
このとき、$\nu$ が $\mu$ に対して絶対連続 $\nu<<\mu$：
$$\mu(E)=0\Rightarrow\nu(E)=0$$

    ・実数値測度、複素数値測度 ν に対しても同様。

</dt><dd>

- 有限測度空間 $(X,\mathfrak{M},\mu)$、有限測度 $\nu:\mathfrak{M}\to[0,\infty)$ とする。
このとき、
$$\mathcal{L}^1(X,\mu)\ni \exist f:X\to[0,\infty),\ \exist\text{ 有限測度 }\lambda:\mathfrak{M}\to[0,\infty)\text{ であって、}\\\ \\
\nu=\mu_f+\lambda,\quad\lambda\perp\mu\\\ \\$$

      ・Radon-Nikodymの定理

- $\sigma-$有限測度空間 $(X,\mathfrak{M},\mu)$、$\sigma-$有限測度 $\nu:\mathfrak{M}\to[0,\infty]$ とする。
このとき、
$$\exist\text{ 非負値可測関数 }f:X\to[0,\infty),\ \exist\text{ $\sigma-$有限測度 }\lambda:\mathfrak{M}\to[0,\infty)\text{ であって、}\\\ \\
\nu=\mu_f+\lambda,\quad\lambda\perp\mu\\\ \\$$

      ・Radon-Nikodymの定理


- $\sigma-$有限測度空間 $(X,\mathfrak{M},\mu)$、実数値測度 $\nu:\mathfrak{M}\to\bm{R}$ とする。
このとき、
$$\exist f\in\mathcal{L}_{\bm{R}}^1(X,\mu),\ \exist\text{ 実数値測度 }\lambda:\mathfrak{M}\to\bm{R}\text{ であって、}\\\ \\
\nu=\mu_f+\lambda,\quad\lambda\perp\mu\\\ \\$$

      ・Radon-Nikodymの定理

- $\sigma-$有限測度空間 $(X,\mathfrak{M},\mu)$、複素数値測度 $\nu:\mathfrak{M}\to\bm{C}$ とする。
このとき、
$$\exist f\in\mathcal{L}^1(X,\mu),\ \exist\text{ 複素数値測度 }\lambda:\mathfrak{M}\to\bm{C}\text{ であって、}\\\ \\
\nu=\mu_f+\lambda,\quad\lambda\perp\mu\\\ \\$$

      ・Radon-Nikodymの定理

</dd></dl>



---

<dl><dt>

・$\sigma-$有限測度空間 $(X,\mathfrak{M},\mu)$ とする。

</dt><dd>

- $\mu$ に対して絶対連続な $\sigma-$有限測度 $\nu:\mathfrak{M}\to[0,\infty)$ に対して、
$$\exist\text{ 非負値可測関数} f:X\to[0,\infty)\text{ であって、}\\\ \\
\nu=\mu_f$$

      ・f:Radon-Nikodym微分

- $\mu$ に対して絶対連続な実数値測度 $\nu:\mathfrak{M}\to\bm{R}$ に対して、
$$\exist f\in\mathcal{L}^1_{\bm{R}}(X,\mu)\text{ であって、}\\\ \\
\nu=\mu_f$$

      ・f:Radon-Nikodym微分

- $\mu$ に対して絶対連続な複素数値測度 $\nu:\mathfrak{M}\to\bm{C}$ に対して、
$$\exist f\in\mathcal{L}^1(X,\mu)\text{ であって、}\\\ \\
\nu=\mu_f$$

      ・f:Radon-Nikodym微分

- $f_1,f_2$ が共に $\nu$ の $\mu$ に対するRadon-Nikodym微分ならば、
$$f_1=f_2\ \ (\mu-a.e.)$$

</dd></dl>

---

## 複素数値測度に対する全変動

<dl><dt>

・可測空間 $X$、複素数値測度 $\nu:\mathfrak{M}\to \bm{C}$ とする。
このとき、全変動 $|\nu|:\mathfrak{M}\to[0,\infty]$：
$$|\nu|(E)=\sup\left\{\sum_{i=1}^n|\nu(E_i)|\ |\ E_1,...,E_n\subset E\text{ は } E\text{ の有限可測分割} \right\}$$

</dt><dd>

- 実数値測度 $\nu:\mathfrak{M}\to \bm{R}$ とする。
このとき、
$$|\nu|=\nu_++\nu_-\quad(\nu_{\pm}\text{ はJordan分解})\\\ \\$$

- 測度空間 $(X,\mathfrak{M},\mu)$、$f\in \mathcal{L}^1(X)$ とする。
このとき、全変動 $|\mu_f|$ は有限測度で、
$$|\mu_f|=\mu_{|f|}\\\ \\$$

- 複素数値測度 $\nu:\mathfrak{M}\to\bm{C}$ の全変動 $|\nu|:\mathfrak{M}\to[0,\infty)$ は有限測度で、$\nu$ は $|\nu|$ に対して絶対連続。

</dd></dl>

### 複素数値測度の積分

<dl><dt>

・可測空間 $X$、複素数値測度 $\nu:\mathfrak{M}\to \bm{C}$、$\nu$ の全変動 $|\nu|$ に対するRadon-Nikodim微分 $h\in\mathcal{L}^1(X,|\nu|)$、$f\in\mathcal{L}^1(X,|\nu|)$ とする。
このとき、$f$ の $\nu$ による積分：
$$\int_X fd\nu=\int_Xfhd|\nu|$$

</dt><dd>

- $|h(x)|=1\ \ (|\nu|-a.e.)$
<br>

- 測度空間 $(X,\mathfrak{M},\mu)$、非負値可測関数 $f,g:X\to[0,\infty]$とする。
このとき、
$$\int_Xgd\mu_f=\int_Xfgd\mu\\\ \\$$

- 測度空間 $(X,\mathfrak{M},\mu)$、$f\in\mathcal{L}^1(X)$、複素数値可測関数 $g:X\to\bm{C}$ とする。
このとき、
$$g\in\mathcal{L}^1(X,|\mu_f|)\iff fg\in\mathcal{L}^1(X,\mu)\\\ \\
\int_Xg(x)d\mu_f=\int_Xfgd\mu\\\ \\$$

      ・最後のgを含む集合は、どうせ|h|=1だからこれでよい。

- 測度空間 $(X,\mathfrak{M},\mu)$、複素数値測度 $\nu:\mathfrak{M}\to\bm{C}$、$f\in\mathcal{L}^1(X)$、複素数値 $|\nu|-$可測関数 $g:X\to\bm{C}$ とする。
このとき、
$$\nu_f:\mathfrak{M}\to\bm{C}\\\ \\
\nu_f(E)=\int_Efd\nu$$は複素数値測度で、
$$\nu_f(E)=|\nu|_{fh}(E)\quad(h:\nu\text{ の }|\nu|\text{ に関するRadon-Nikodim微分})\\\ \\
g\in\mathcal{L}^1(X,|\nu_f|)\iff fg\in\mathcal{L}^1(X,|\nu|)\\\ \\
\forall g\in\mathcal{L}^1(X,|\nu_f|)\text{ に対して、}\int_Xgd\nu_f=\int_Xfgd\nu$$

      ・これはμ関係ない。
      ・最後のgを含む集合は、どうせ|h|=1だからこれでよい。

</dd></dl>

---

# Radon測度

## 局所コンパクトHausdorff空間 $X$ 上のRadon測度

・コンパクト集合$K$に対して、
$$K\prec f\iff f\in C_c(X),\ f:X\to[0,1],\ f(x)=1\ (\forall x\in K)$$

- 開集合 $U$に対して、
$$f\prec U\iff f\in C_c(X),\ f:X\to[0,1],\ suppf\subset U$$

- $K\subset U$なるコンパクト集合$K$と開集合$U$に対して、
$$K\prec f\prec U\iff f\in C_c(X),\ f:X\to[0,1],\ f(x)=1\ (\forall x\in K),\ suppf\subset U$$

- 任意の$K\subset U$なるコンパクト集合$K$と開集合$U$に対して、$K\prec f\prec U$なる$f$が存在する

        ・Urysohn

・開集合 $U_1\subset U_2$ に対して、
$f\prec U_1\Rightarrow f\prec U_2$

・コンパクト集合　$K_1\subset K_2$ に対して、
$K_2\prec f\Rightarrow K_1\prec f$

---

### Radon測度
$$\bm{\mu:\mathfrak{B}_X\to[0\to\infty]}$$

・定義：局所コンパクトHausdorff空間 $X$ としたとき、

- 任意のコンパクト集合$K$に対して、$\mu(K)<\infty$

- $$\mu(E)=\inf\{\mu(V)\ |\ E\subset V{なる開集合}\}$$

        ・外部正則性

- $\mu(E)<\infty$または $E$ が開集合の時、
$$\mu(E)=\sup\{\mu(K)\ |\ K\subset E{なるコンパクト集合}\}$$

      ・内部正則性

---

・局所コンパクトHausdorff空間$X$、Radon測度 $\mu$ とする。

- $f\in C_c(X)\Rightarrow f$ は $\mu$-可積分
- 開集合 $V$ に対して、$$\mu(V)=\sup\left\{\int fd\mu\ |\ f\prec V\right\}$$
- コンパクト集合 $K$ に対して、$$\mu(K)=\inf\left\{\int fd\mu\ |\ K\prec f\right\}$$

---

question

### 有限測度とRadon測度

・局所コンパクトHausdorff空間 $X$、有限Borel測度 $\mu:\mathfrak{M}\to[0,\infty)$ とする。
このとき、
$$\mu\text{ がRadon測度}\\\ \\
\iff\forall B\in\mathfrak{B}\text{ に対して、}\mu(B)=\sup\{\mu(K)\ |\ \text{コンパクト集合 }K\subset B\}$$

    ・内部正則性が成り立つこと。

---

### Radon汎関数とRiesz-Markov-角谷の表現定理

・Radon汎関数：線形汎関数 $\Lambda: C_{c,\bm{R}}\to\bm{R}$ であって、$$\Lambda(f)\ge0\quad(f:0\to[0,\infty))$$

- $f(x)\le g(x)\ (\forall x\in X)$ なる $f,g\in C_{c,\bm{R}}$ に対して、 $\Lambda(f)\le\Lambda(g)$

        ・単調性

---

・局所コンパクトHausdorff空間 $X$、Radon汎関数 $\Lambda$ とする。このとき、

- $$\mu_0:\mathcal{O}_X\to[0,\infty],\quad\mu_0(V)=\sup\{\Lambda(f)\ |\ f\prec V\}$$


- $$\mu^*:2^X\to[0,\infty],\quad \mu^*(E)=\inf\{\mu_0(V)\ |\ E\subset V\in\mathcal{O}_X\}$$
 
- $$\mathfrak{M}_f=\{E\in2^X\ |\ \mu^*(E)<\infty,\ \mu^*(E)=\sup\{\mu^*(K),\ \forall{コンパクト集合} K\subset E\}\}$$　

- $\mathfrak{M}=\{E\in 2^X\ |\ E\cap K\in\mathfrak{M}_f\ (\forall {コンパクト集合}K )\}$

と定める。

---

・$\mu^*(\phi)=\mu_0(\phi)=0$ で、 $\mu^*,\mu_0$は単調：$E\subset F\Rightarrow \mu_0(E)\subset \mu_0(F),\ \mu^*(E)\subset \mu^*(F)$
- $\mu^*$ は $\mu_0$ の拡張
- $\mu_0$ は劣 $\sigma$-加法的：任意の開集合列 $U_n$ に対して、 $\mu_0(\bigcup U_n)\le\sum \mu_0(U_n)$
- $\mu^*$は劣 $\sigma$-加法的：任意の集合列 $E_n$ に対して、 $\mu^*(\bigcup E_n)\le\sum \mu^*(E_n)\\\ \\$


・コンパクト集合 $K$ に対して、 $K\in\mathfrak{M}_f$ かつ
$\mu^*(K)=\inf\{\Lambda f\ |\ K\prec f\}=\inf\{\Lambda f\ |\ f\in C_{c,+}(X),\ f|_{K}=1\}$

    ・C_{c,+}は台がコンパクトな連続で、実数値かつ非負ってこと

- 開集合 $V$ に対して、
$$\mu^*(V)=\sup\{\mu^*(K)\ |\ \forall{コンパクト集合}K\subset V\}$$したがって、$\mu^*(V)<\infty\Rightarrow V\in\mathfrak{M}_f\\\ \\$


・非交叉列 $E_n\in\mathfrak{M}_f$ に対して、
$\mu^*(\bigcup E_n)=\sum\mu^*(E_n)$
さらに、$\mu^*(\bigcup E_n)<\infty$ ならば、$\bigcup E_n\in\mathfrak{M}_f\\\ \\$

・$\forall E\in\mathfrak{M}_f,\forall\epsilon>0$ に対して、
$K\subset E\subset V$ かつ $\mu^*(K-V)<\epsilon$ を満たすコンパクト集合 $K$、開集合 $V$ が存在する
- $\mathfrak{M}$は$\sigma$-加法族であって、$\mathfrak{B}_X\subset\mathfrak{M}_f$
- $\mathfrak{M}_f=\{E\in\mathfrak{M}\ |\ \mu^*(E)<\infty\}\\\ \\$

・$\mu:\mathfrak{B}_X\ni B\to\mu^*(B)\in[0,\infty]$
はRadon測度
- $\Lambda(f)=\int fd\mu$

    ・右辺はC_c,+以外の関数にも拡張できる！

---

・局所コンパクトHausdorff空間 $X$、Radon汎関数 $\Lambda$ とする。
このとき、
$$\Lambda(f)=\int fd\mu$$を満たすRadon測度 $\mu$ がただ一つ存在する

    ・Riesz-Markov-角谷の表現定理

---

## 第二可算性とRadon測度

・$\sigma$-コンパクト：位相空間 $X$ に対して、
$$X=\bigcup K_n$$ を満たすコンパクト集合列 $K_n$ が存在する

- 第二可算空間は $\sigma$-コンパクト

---

・$\sigma$-コンパクトな局所コンパクトHausdorff空間 $X$、Radon測度 $\mu:\mathfrak{B}_X\to[0,\infty]$ とする。

- $\forall B\in\mathfrak{B}_X,\epsilon>0$ に対して、$$F\subset B\subset U,\quad \mu(U-F)<\epsilon$$ なる閉集合 $F$、開集合 $U$ が存在する  
<br>       


- $\forall B\in\mathfrak{B}_X$ に対して、
$\mu(B)=\sup\{\mu(K)\ |\ \forall{コンパクト集合}K\subset B\}$

---

・第二可算局所コンパクトHausdorff空間 $X$、Borel測度 $\mu:\mathfrak{B}_X\to[0,\infty]$ とする。
このとき、
$$\mu(K)<\infty\ (\forall{コンパクト集合}K)$$ ならば、$\mu$ はRadon測度

---

### 複素数値Radon測度

・第二可算局所コンパクトHausdorff空間 $X$ とする。
このとき、複素数値Borel測度ならば、複素数値Radon測度。

---

## 複素数値Radon測度のなすBanach空間 $M(X)$

<dl><dt>

・局所コンパクトHausdorff空間 $X$、複素数値Borel測度 $\nu:\mathfrak{B}\to\bm{C}$ とする。
このとき、複素数値Radon測度 $\nu$：
$$\text{全変動 }|\nu|\text{ がRadon測度}$$

</dt><dd>

- $M(X)$ は各Borel集合ごとの演算で $\bm{C}$ 上ベクトル空間。
<br>

- $$\|\nu\|=|\nu|(X)$$は $M(X)$ 上のノルム。
<br>

- Radon測度 $\mu:\mathfrak{B}\to[0,\infty]$、$f\in\mathcal{L}^1(X,\mu)$ とする。
このとき、
$$\mu_f:\mathfrak{B}\to\bm{C},\quad\mu_f(B)=\int_Bfd\mu$$ は $M(X)$ の元で、
$$\|\mu_f\|=\|f\|_1\\\ \\$$

- 複素数値Radon測度 $\nu\in M(X)$、$f\in\mathcal{L}^1(X,|\nu|)$ とする。
このとき、
$$\nu_f:\mathfrak{B}\to\bm{C},\quad\mu_f(B)=\int_Bfd\nu$$ は $M(X)$ の元で、
$$\|\nu_f\|=\|f\|_{|\nu|,1}\\\ \\$$

- $\nu\in M(X)$ とし、
$$\phi_{\nu}:C_0(X)\to\bm{C}\\\ \\
\phi_{\nu}(f)=\int_Xfd\nu$$と定める。このとき、
$\phi_{\nu}\in C_0(X)^*$であって、
$$\psi:M(X)\to C_0(X)^*\\\ \\
\psi(\nu)=\phi_{\nu}$$ は等長写像。


</dd></dl>
