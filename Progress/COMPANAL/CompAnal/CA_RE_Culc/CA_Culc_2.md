
- [指数関数 $\\exp z$](#指数関数-exp-z)
  - [簡単な関係式](#簡単な関係式)
- [三角関数 $\\sin z,\\ \\cos z$](#三角関数-sin-z-cos-z)
  - [展開](#展開)
    - [テイラー展開（多項式展開）](#テイラー展開多項式展開)
  - [定積分](#定積分)
  - [不定積分](#不定積分)



# 指数関数 $\exp z$

## 簡単な関係式

・$i^l=e^{i\frac{l\pi}{2}}\quad(l=0,1,...)$

---

# 三角関数 $\sin z,\ \cos z$

・$\sin(x-\frac{l\pi}{2})=\frac{1}{2i}(e^{ix}-(-1)^le^{-ix})\quad (l=0,1,...,\ x\in\bm{R})$

・$\frac{1}{2}\int_{0}^{\pi}\sin^n\theta=\frac{1}{2}\int_0^n\cos^n\theta=\int_0^{\pi/2}\sin\theta^n\\ \
=\begin{cases} \
\frac{n-1}{n}...\frac{2}{3} & (n{奇数})  \\  \
\frac{n-1}{n}...\frac{1}{2}\frac{\pi}{2} & (n{偶数})    \
\end{cases}$

## 展開

### テイラー展開（多項式展開）

・$x=a$ での展開：
常に可能で、$f(x)=f(a)+f'(a)(x-a)+...$

    ・いつもの形に代入するわけにはいかない。展開してからまとめるとよい。

---

## 定積分

・$\int_0^{\pi}\frac{\sin\theta'}{\sqrt{r^2+r'^2-2rr'\cos\theta'}}d\theta'=\frac{1}{rr'}(r+r'-|r-r'|)\quad(r,r'>0)$

---

## 不定積分

・$$\int \frac{e^x}{x}$$

    なぞな関数出てきた、Ei(x)?