
    ・内積は第二が共役

- [簡単な実関数空間](#簡単な実関数空間)
  - [区分的に連続,$C^1$ な関数 $PC$](#区分的に連続c1-な関数-pc)
    - [フーリエ級数展開](#フーリエ級数展開)
  - [$C^m(Ω)$](#cmω)
    - [ワイエルシュトラスの近似定理](#ワイエルシュトラスの近似定理)
  - [$B^m(Ω)$](#bmω)
- [$L^p(R^n)$](#lprn)
  - [コンパクト台による近似](#コンパクト台による近似)
- [$(-π,π)$ 上のフーリエ解析](#-ππ-上のフーリエ解析)
  - [Poisson核](#poisson核)
    - [Poisson積分](#poisson積分)
      - [Poisson積分の正則性](#poisson積分の正則性)
    - [稠密な部分集合](#稠密な部分集合)
  - [CONS](#cons)
    - [フーリエ係数](#フーリエ係数)
    - [アーベル総和](#アーベル総和)
    - [三角関数系](#三角関数系)
  - [畳み込み](#畳み込み)
    - [可換Banach環 $L^1(-π,π)$](#可換banach環-l1-ππ)
  - [多重フーリエ級数](#多重フーリエ級数)



# 簡単な実関数空間

## 区分的に連続,$C^1$ な関数 $PC$

・
$$PC([a,b],\bm{R}^d)=\\\ \\
\{f:[a,b]\to\bm{R}^d\ |\ \exist\text{ 分割 }\Delta\text{ であって各}I_k\text{ 上連続で、}\\
\text{ 両端での極限 }f(a_k-0),f(a_k+0)\in\bm{R}\}\\\ \\
\|f\|_{\infty}=\sup_{[a,b]}\{|f|\}$$
とする。
このとき、$PC([a,b],\bm{R}^d)$ は $\bm{R}$ 上ベクトル空間で、$\|f\|_{\infty}$ はノルム。

    ・端点での値はf(a_k)∊R^dだが、別に両端からの値の両方とも等しくないかも。
    ・一様収束ノルム。
    ・区分的に連続。

---

・$$PC^1([a,b],\bm{R}^d)=\\
\{\text{連続関数 }f:[a,b]\to\bm{R}^d\ |\ \exist\text{ 分割 }\Delta\text{ であって各}I_k\text{ 上 }C^1{ で、}\\
\text{ 両端での極限 }f'(a_k-0),f'(a_k+0)\in\bm{R}\}$$
は $\bm{R}$ 上ベクトル空間。
同様に定義される $PC^1([a,b],\bm{R}^d)$ も $\bm{R}$ 上ベクトル空間。 

      ・f'(a_k) が定義されてないとき、f'(a_k)=f'(a_k+0)
      ・区分的にC^1級。

- $f\in PC^1([a,b],\bm{R}^d)$ とする。
このとき、
$$\|f\|_{0}=\sup_{[a,b]}\{|f|\}\\\ \\
\|f\|_{1}=\sup_{[a,b]}\{|f|\}+\sup_{[a,b]}\{|f'|\}$$
はともに $PC^1([a,b],\bm{R}^d)$ のノルム。


      ・f'も一様収束する。

---

### フーリエ級数展開

・$f\in PC^1([-\pi,\pi])$ で、$f(-\pi)=f(\pi)$ とする。
このとき、
$$f(\theta)=\frac{1}{\sqrt{2\pi}}e^{in\theta}\int_{-\pi}^{\pi}f(\phi)e^{-in\phi}d\phi\\\ \\$$

    ・f'が自乗可積分ならよい。

---

## $C^m(Ω)$

・開集合 $\Omega\sub\bm{R}^n$ とする。
このとき、$$C^m(\Omega)=\{f:\Omega\to\bm{R,C}\ |\ f\text{ は }C^{m}\}\\\ \\
C^{\infty}(M)=\bigcap C^m(\Omega)$$
とすると、これらは $\bm{R,C}$ 上ベクトル空間。

---

### ワイエルシュトラスの近似定理

・$f\in C^0[a,b]$ とする。
このとき、
$$\forall\epsilon\text{ に対して、}\exist\text{ 多項式 }P(x)\text{ であって、}\\\ \\
\|f(x)-P(x)\|<\epsilon\quad(\text{一様収束ノルム})$$

---

## $B^m(Ω)$

・開集合 $\Omega\sub\bm{R}^n$ とする。
このとき、$$B^m(\Omega)=\{f\in C^m(\Omega)\ |\ \text{すべての変偏関数が }\Omega\text{ 上有界 }\}\\\ \\
\|f\|=\sum_{|\alpha|<m}\sup_{x\in\Omega}|D^{\alpha}f(x)|$$
とすると、これは $\bm{R,C}$ 上Banach空間。

    ・D^α=D^{α_1}_1...D^{α_n}_n、 D^0f=f

---

# $L^p(R^n)$

## コンパクト台による近似

<dl><dt>

・$f\in L^1(\bm{R}^n)$ とする。
このとき、
$$\forall\epsilon>0\text{ に対して、}\exist g\in C_0(\bm{R}^n)\text{ であって、}\|f-g\|_{L^p}<\epsilon$$

    ・？？？ルベーグ積分の本にありそう。
    ・これはp=1。
<br>

</dt><dd>

- $C_0(\bm{R}^n)\sub L^p(\bm{R}^n)$ であって、
$$\overline{C_0(\bm{R}^n)}= L^p(\bm{R}^n)\\\ \\$$

      ・上の定理から従う。
<br>

- $f\in L^p(\bm{R}^n)$、$p\in[1,\infty)$ とする。
このとき、
$$\lim_{|h|\to0}\int_{\bm{R}^n}|u(x+h)-u(x)|^pdx=0$$ 

      ・平行移動のL^p連続性。
      ・これは収束定理で扱えないらしい？？？関数解析p.44

</dd></dl>

---
---
---


# $(-π,π)$ 上のフーリエ解析

    ・フーリエ級数。
    ・R上で連続ならば、T上でも連続。（逆も成り立つ。）
    ・結局実数上に拡張できる。
    ・同値関係的な位相が入ってるわけではないので、やっぱりRの部分集合でよい。
    ・！もうキモイから(-π,π)上で！

## Poisson核

    ・デルタ関数みたいに振る舞う


<dl><dt>

・$$P_r(\theta)=\frac{1}{2\pi}\sum_{-\infty}^{\infty}r^{|n|}e^{in\theta}\quad(0\le r<1,\ \infty<\theta<-\infty)$$
とする。これをPoisson核という。
<br>

</dt><dd>

- $P_{r,n}(\theta)$ は $P_r(\theta)$ に一様収束する。
<br>

- $P_r$ は $2\pi$ 周期関数。
<br>

- $$\int_{-\pi}^{\pi}P_r(\theta)=1$$

      ・n=0以外の項別積分0
<br>

- $P_r$ のフーリエ係数：
$a_n=\frac{1}{\sqrt{2\pi}}r^{|n|}$

---

- $$P_r(\theta)=\frac{1}{2\pi}\frac{1-r^2}{1+r^2-2r\cos\theta}=\frac{1}{2\pi}\frac{1-r^2}{|1-re^{i\theta}|^2}\\\ \\$$

- $P_r(\theta)>0\\\ \\$

- 
$$\forall\ 0<\epsilon,\ \ 0<\delta<\pi\text{ に対して、}\exist 1>r_0>0\text{ であって、}\\\ \\
1>r>r_0\Rightarrow|\sup_{\delta\le|\theta|\le\pi}P_r(\theta)\ |<\epsilon$$


</dd></dl>

---

### Poisson積分

<dl><dt>

・$f\in L^1(-\pi,\pi)$、Poisson核 $P_r$ とする。
このとき、Poisson積分：
$$P_r*f(\theta)=\frac{1}{2\pi}\int\frac{1-r^2}{1+r^2-2r\cos(\theta-\phi)} f(\phi)d\phi\\\ \\$$

</dt><dd>

- $f\in L^1(-\pi,\pi)$ とする。
このとき、Poisson積分 $P_r*f(\theta)$ は $\bm{R}$ 上連続関数。
特に、$P_r*f\in L^{p}(-\pi,\pi)\quad(p\in[1,\infty])$
<br>

- $p\in[1,\infty]$、$f\in L^p(-\pi,\pi)$ とする。
このとき、$P_r*f\in L^p(-\pi,\pi)$ で、
$$\|P_r*f\|_{L^p}\le\|f\|_{L^p}\\\ \\$$

- $p\in[1,\infty)$、$f\in L^p(-\pi,\pi)$ とする。
このとき、
$$\forall\epsilon\text{ に対して、}\exist 1>r_0>0\text{ であって、}\\\ \\
1>r>r_0\Rightarrow\|P_r*f-f\|_{L^p}<\epsilon\\\ \\$$

- $f\in C_{\#}(-\pi,\pi)$ とする。
このとき、
$$\lim_{r\to1}\|P_r*f-f\|_{L^{\infty}}=0$$

      ・[-π,π]上連続でf(-π)=f(π)。
      ・最後のはPoisson核のとこで示した。

---

- $f\in L^1(-\pi,\pi)$、$f$ のフーリエ係数 $a_n=(f,\phi_n)$ とする。
このとき、
$$P_r*f(\theta)=\frac{1}{\sqrt{2\pi}}\sum_{-\infty}^{\infty}a_nr^{|n|}e^{in\theta}\quad(\theta\in(-\pi,\pi))$$

      ・これはa.e.でなく全体で成り立つ。


</dd></dl>


---

#### Poisson積分の正則性

### 稠密な部分集合

<dl><dt>

・$$C_{\#}=\{f:[-\pi,\pi]\to\bm{C}\ |\ f\text{ は連続関数で、}f(-\pi)=f(\pi)\}$$
と定める。
このとき、$p\in[1,\infty)$ とすると、
$$\overline{C_{\#}}=L^{p}(-\pi,\pi)$$

    ・L^p(R^n)の稠密性のとこによる。
<br>

- $f\in C_{\#}$、$a_n=(f,e^{in\theta})$ とする。
このとき、$$f_r(\theta)=\frac{1}{\sqrt{2\pi}}\sum_{-\infty}^{\infty} a_nr^{|n|}e^{in\theta}\quad(0\le r<1)$$
と定める。
<br>

</dt><dd>

- $f_{r,N}$ は $f_r$ に一様収束し、$f_r\in\mathrm{span}\{\phi_n\}$
<br>

- ポアソン核 $P_r(\theta)$ とする。
このとき、
$$f_r(\theta)=\int_{-\pi}^{\pi}P_r(\theta-\phi)f(\phi)d\phi=\int_{-\pi}^{\pi}P_r(\phi)\tilde{f}(\theta-\phi)d\phi\\\ \\
(\ \tilde{f}\text{ は }f\text{ を周期的に拡張したもの}\ )\\\ \\$$

- $$\lim_{r\to1}\sup|f_r-f|=0$$


</dd></dl>

---

## CONS

・$L^2(-\pi,\pi)$ とする。
このとき、
$$\phi_k(x)=\frac{1}{\sqrt{2\pi}}e^{ikx}\quad(k=0,\pm1,...)$$
は $L^2(-\pi,\pi)$ の正規直交系で、CONSである。

    ・Poisson核による。

- $f\in L^2(-\pi,\pi)$ とする。
このとき、
$$f(\theta)=\frac{1}{\sqrt{2\pi}}e^{in\theta}\int_{-\pi}^{\pi}f(\phi)e^{-in\phi}d\phi$$

---

### フーリエ係数

・$f,g\in L^{p}(-\pi,\pi)$、$f,g$ のフーリエ係数 $a_n,b_n$ とする。
このとき、
$$\forall n\text{ に対して }a_n=b_n\\\ \\
\Rightarrow f=g\ \ (a.e.)$$

---

### アーベル総和

・$f\in L^p(-\pi,\pi)$、$f$ のフーリエ係数 $a_n$ とする。
このとき、
$$f(\theta)=\lim_{r\to1}\frac{1}{\sqrt{2\pi}}\sum_{-\infty}^{\infty}a_nr^{|n|}e^{in\theta}\quad(L^p\text{ 収束})$$
このように、フーリエ級数が収束しなくても、上式右辺の級数が収束するとき、アーベル総和可能という。

- $f\in L^1(-\pi,\pi)$、フーリエ係数 $a_n$ とする。
このとき、
$$\lim_{n\to\pm\infty}a_n=0$$

---

### 三角関数系

- $$\left\{\frac{1}{\sqrt{2\pi}},\ \frac{1}{\sqrt{\pi}}\cos n\theta,\ \frac{1}{\sqrt{\pi}}\sin n\theta\right\}\quad(n=1,2,...)$$
は $L^2(-\pi,\pi)$ の正規直交系で、
$$\frac{1}{\sqrt{2\pi}}=\phi_0,\\\ \\
\frac{1}{\sqrt{\pi}}\cos n\theta=\frac{1}{\sqrt{2}}(\phi_n+\phi_{-n}),\quad\frac{1}{\sqrt{\pi}}\sin n\theta=\frac{1}{\sqrt{2}i}(\phi_n-\phi_{-n})$$
よって、これはCONS

      ・係数が√入ってるが、結局いつものフーリエ級数展開と同じ形になる。

- $e^{in\theta}$ におけるフーリエ係数 $c_n$、$\cos n\theta,\sin n\theta$ におけるフーリエ係数 $a_n,b_n$ とする。
このとき、
$$c_{n}=\frac{a_n-ib_n}{2}\\\ \\
c_{-n}=\frac{a_n+ib_n}{2}\quad(n\ge0)$$

    ・L^2(-π,π)上。
    ・これはa_0もうまく表せてる。

---

## 畳み込み

<dl><dt>

・$p\in[1,\infty]$、$f\in L^p(-\pi,\pi)$、$g\in L^1(-\pi,\pi)$ とし、それぞれ $2\pi$ 関数として延長する。
このとき、
$$h(\theta)=\int_{-\pi}^{\pi}f(\theta-\phi)g(\phi)d\phi\quad(-\pi<\theta<\pi)$$
と定める。これはwell-defined、すなわち $[f]=[f'],\ [g]=[g']\Rightarrow [f*g]=[f'*g']$
また、$f*g$ を畳み込みという。

    ・πとかの値は適当。
    ・畳み込み自体はhがL^1であれば定義される。


</dt><dd>

- $h\in L^p(-\infty,\infty)$ であって、
$$\|h\|_{L^p}\le\|f\|_{L^p}\|g\|_{L^1}\\\ \\$$

- 畳み込み $h=f*g$ とする。このとき、$g*f$ も定義できて、
$$f*g=g*f\quad (a.e.)\\\ \\$$



- $f,g\in L^1(-\pi,\pi)$、畳み込み $h=f*g$ とし、それぞれのフーリエ係数 $a_n,b_n,c_n$ とする。
このとき、
$$c_n=\sqrt{2\pi}a_nb_n\\\ \\$$

      ・フーリエ係数はちゃんと定義される。
      ・別にフーリエ級数展開可能でなくてもよい。

---

- $p,q\in[1,\infty]$ で $1/p+1/q\ge1$ とし、$f\in L^p(-\pi,\pi)$、$g\in L^{q}(-\pi,\pi)$ とする。
このとき、$f*g$ が定義されて、
$$f*g\in L^r(-\pi,\pi),\ \ \frac{1}{r}=\frac{1}{p}+\frac{1}{q}-1\le1\\\ \\
(1/p+...=0\text{ ならば }r=\infty)\\\ \\
\|f*g\|_{L^r}\le\|f\|_{L^p}\|g\|_{L^q}$$

      ・ヤング不等式

</dd></dl>

---

### 可換Banach環 $L^1(-π,π)$

・$L^1(-\pi,\pi)$ は、畳み込み $*$ を積とする $\bm{C}$ 上可換Banach*-環。
また、単位元は存在しない。

    ・C*環ではない。

---

## 多重フーリエ級数

・零でない可測集合 $\Omega_2,...,\Omega_N\sub\bm{R}$、可算なCONS $(\phi^n_k)\sub\Omega_n$ とする。
このとき、
$$\phi_{k_1,...,k_N}(x_1,...,x_N)=\phi^1_{k_1}(x_1)...\phi^N_{k_N}(x_N)$$
とすると、これは $L^2(\Omega_1\times...\times\Omega_N)$ の可算なCONS。
特に、$$(\frac{1}{\sqrt{2\pi}})^Ne^{i\sum n_kx_k}\quad(n_k\in\bm{Z})$$ は $L^2([-\pi,\pi]\times...\times[-\pi,\pi])$ の可算なCONS。

---





