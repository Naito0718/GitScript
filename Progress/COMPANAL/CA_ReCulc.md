# 実関数、初等関数の具体例、計算例

## 級数$\sum c_nx^n$

・実級数$f(x)=\sum c_nx^n$に対して、定義域を複素数に拡張することができる

    ・絶対収束する級数について、拡大前と拡大後の収束範囲は整合する。したがって実級数でも収束半径を考えることができる

## 指数関数 $\exp z$

・$i^l=e^{i\frac{l\pi}{2}}\quad(l=0,1,...)$

## 三角関数 $\sin z,\ \cos z$

・$\sin(x-\frac{l\pi}{2})=\frac{1}{2i}(e^{ix}-(-1)^le^{-ix})\quad (l=0,1,...,\ x\in\bm{R})$

・$\frac{1}{2}\int_{0}^{\pi}\sin^n\theta=\frac{1}{2}\int_0^n\cos^n\theta=\int_0^{\pi/2}\sin\theta^n\\ \
=\begin{cases} \
\frac{n-1}{n}...\frac{2}{3} & (n{奇数})  \\  \
\frac{n-1}{n}...\frac{1}{2}\frac{\pi}{2} & (n{偶数})    \
\end{cases}$

## 定積分

・$\int_0^{\pi}\frac{\sin\theta'}{\sqrt{r^2+r'^2-2rr'\cos\theta'}}d\theta'=\frac{1}{rr'}(r+r'-|r-r'|)\quad(r,r'>0)$