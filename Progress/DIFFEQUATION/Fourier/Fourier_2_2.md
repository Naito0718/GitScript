
- [Dirichlet核](#dirichlet核)
  - [連続周期関数とフーリエ解析](#連続周期関数とフーリエ解析)
  - [自乗可積分関数？](#自乗可積分関数)
- [$PC$ 上のフーリエ解析](#pc-上のフーリエ解析)



# Dirichlet核

<dl><dt>

・$l>0,\ \omega=\frac{\pi}{l}$ とする。
このとき、
$$D_N:\bm{R}\to\bm{C}\\\ \\
D_N(\theta)=\sum_{k=-N}^Ne^{ik\omega x}$$
と定めると、これは $2l$ 周期の偶関数。ここで、$D_N$ をDirichlet核という。
<br>

</dt><dd>

- $a\in\bm{R}$ とする。
このとき、
$$\frac{1}{2l}\int_{-l}^lD_N(a-\theta)d\theta=\frac{1}{2l}\int_{-l}^lD_N(\theta)d\theta=1$$
<br>

      ・k=0以外の項別積分0
<br>

- $P_r$ のフーリエ係数：
$a_n=\frac{1}{\sqrt{2\pi}}r^{|n|}$

---

- 
$$\forall \theta\in\bm{R}-2l\bm{Z}\text{ に対して、}\\\ \\
D_N(\theta)=\frac{\sin(N+\frac{1}{2})\omega \theta}{\sin\frac{\omega \theta}{2}}\\\ \\$$

</dd></dl>

---

## 連続周期関数とフーリエ解析

・$f:\bm{R}\to\bm{R}$ を周期 $2l$ の連続関数、$x_0\in[-l,l)$とする。
このとき、$\int_{-\delta}^{\delta}\left|\frac{f(x_0+h)-f(x_0)}{h}\right|^2dh<\infty$

## 自乗可積分関数？


# $PC$ 上のフーリエ解析

