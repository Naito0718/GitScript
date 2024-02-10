
    ・内積は第二が共役

- [区分的に連続,$C^1$ な関数 $PC$](#区分的に連続c1-な関数-pc)
  - [フーリエ級数展開](#フーリエ級数展開)
- [$C^m(Ω)$](#cmω)
  - [ワイエルシュトラスの近似定理](#ワイエルシュトラスの近似定理)
- [$B^m(Ω)$](#bmω)
- [$L^p(R^n)$](#lprn)
  - [コンパクト台による近似](#コンパクト台による近似)





# 区分的に連続,$C^1$ な関数 $PC$

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
<br>

      ・f'も一様収束する。

---

## フーリエ級数展開

・$f\in PC^1([-\pi,\pi])$ で、$f(-\pi)=f(\pi)$ とする。
このとき、
$$\forall\theta\in[-\pi,\pi]\text{ に対して、}\\\ \\
f(\theta)=\frac{1}{\sqrt{2\pi}}e^{in\theta}\int_{-\pi}^{\pi}f(\phi)e^{-in\phi}d\phi\\\ \\$$

    ・f'が自乗可積分ならよい。⇐？？？

---

# $C^m(Ω)$

・開集合 $\Omega\sub\bm{R}^n$ とする。
このとき、$$C^m(\Omega)=\{f:\Omega\to\bm{R,C}\ |\ f\text{ は }C^{m}\}\\\ \\
C^{\infty}(M)=\bigcap C^m(\Omega)$$
とすると、これらは $\bm{R,C}$ 上ベクトル空間。

---

## ワイエルシュトラスの近似定理

・$f\in C^0[a,b]$ とする。
このとき、
$$\forall\epsilon\text{ に対して、}\exist\text{ 多項式 }P(x)\text{ であって、}\\\ \\
\|f(x)-P(x)\|<\epsilon\quad(\text{一様収束ノルム})$$

---

# $B^m(Ω)$

・開集合 $\Omega\sub\bm{R}^n$ とする。
このとき、$$B^m(\Omega)=\{f\in C^m(\Omega)\ |\ \text{すべての偏関数が }\Omega\text{ 上有界 }\}\\\ \\
\|f\|=\sum_{|\alpha|<m}\sup_{x\in\Omega}|D^{\alpha}f(x)|$$
とすると、これは $\bm{R,C}$ 上Banach空間。

---

# $L^p(R^n)$

## コンパクト台による近似

<dl><dt>

・$f\in L^p(\bm{R}^n)$ とする。
このとき、
$$\forall\epsilon>0\text{ に対して、}\exist g\in C_c(\bm{R}^n)\text{ であって、}\|f-g\|_{L^p}<\epsilon$$

    ・局所コンパクト空間のRadon測度のとこ。
<br>

</dt><dd>

- $C_c(\bm{R}^n)\sub L^p(\bm{R}^n)$ であって、
$$\overline{C_c(\bm{R}^n)}= L^p(\bm{R}^n)\\\ \\$$

      ・上の定理から従う。
<br>

- $f\in L^p(\bm{R}^n)$、$p\in[1,\infty)$ とする。
このとき、
$$\lim_{|h|\to0}\int_{\bm{R}^n}|f(x+h)-f(x)|^pdx=0$$ 

      ・平行移動のL^p連続性。
      ・これは収束定理で扱えないらしい？？？関数解析p.44

</dd></dl>

---
---
---


