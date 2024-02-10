
- [簡単なフーリエ級数展開](#簡単なフーリエ級数展開)
  - [$f(x)=x$](#fxx)
  - [$f(x)=x^2$](#fxx2)
  - [$f(x)=|x|$](#fxx-1)
  - [$f(x)=e^x$](#fxex)
  - [不連続な関数](#不連続な関数)
- [簡単なフーリエ変換](#簡単なフーリエ変換)
  - [$f(x)=b$](#fxb)



# 簡単なフーリエ級数展開

    ・a_0/2に注意。部分積分計算はまとめて！
    ・余弦級数：何も考えずに[0,π]でa_nだけ計算すればよい。偶関数と同じ。

## $f(x)=x$

・$$f:[-\pi,\pi]\to\bm{R},\quad f(x)=x$$
とする。
このとき、
$$\frac{1}{\pi}\int x\sin nxdx=\frac{2}{n}(-1)^{n+1}\\\ \\
f(x)=(-2)\sum_n\frac{(-1)^n}{n}\sin nx$$

- $\frac{\pi}{4}=1-\frac{1}{3}+\frac{1}{5}-...$

      ・ライプニッツ級数。

---

・$$f:[-\pi,\pi]\to\bm{R},\quad f(x)=x$$
とする。
このとき、
$$\frac{1}{2\pi}\int xdx=0\\\ \\
\frac{1}{2\pi}\int xe^{-inx}dx=\frac{i(-1)^n}{n}\quad(n\neq0)\\\ \\
f(x)=i\left(\sum_{n\ge1}\frac{(-1)^n}{n}e^{inx}+\frac{(-1)^n}{-n}e^{-inx}\right)$$

    ・計算すればsin系と同じになる。

---

## $f(x)=x^2$

・$$f:[-\pi,\pi]\to\bm{R},\quad f(x)=x^2$$
とする。このとき、
$$\frac{1}{\pi}\int x^2\cos nxdx=\frac{4}{n^2}(-1)^{n}\\\ \\
f(x)=\frac{\pi^2}{3}+\sum_{n\ge1}4\frac{(-1)^n}{n^2}\cos nx$$

---

・正弦級数：$$\frac{2}{\pi}\int x^2\sin nxdx=2\pi\frac{(-1)^{n+1}}{n}+\frac{4}{\pi}\frac{(-1)^n-1}{n^3}\\\ \\
\sum\left(2\pi\frac{(-1)^{n+1}}{n}+2\frac{(-1)^n-1}{n^3}\right)\sin nx$$

---

---

・$$f:[-\pi,\pi]\to\bm{R},\quad f(x)=x^2$$
とする。
このとき、
$$\frac{1}{2\pi}\int x^2dx=\frac{\pi^2}{3}\\\ \\
\frac{1}{2\pi}\int x^2e^{-inx}dx=\frac{2(-1)^n}{n^2}\quad(n\neq0)\\\ \\
f(x)=\frac{\pi^2}{3}+2\left(\sum_{n\ge1}\frac{(-1)^n}{n^2}(e^{inx}+e^{-inx})\right)$$

    ・計算すればcos系と同じになる。

---

## $f(x)=|x|$

$$f:[-\pi,\pi]\to\bm{R},\quad f(x)=|x|$$
とする。このとき、
$$\frac{1}{\pi}\int x\cos nxdx=\frac{2}{\pi n^2}((-1)^{n}+1)\\\ \\
f(x)=\frac{\pi}{2}-\frac{4}{\pi}\sum_{n\ge1}\frac{1}{(2n-1)^2}\cos (2n-1)x$$


---

## $f(x)=e^x$

・$$f:[-\pi,\pi]\to\bm{R},\quad f(x)=e^x$$
とする。
このとき、
$$\frac{1}{2\pi}\int e^xe^{-inx}dx=\frac{e^{\pi}-e^{-\pi}}{2\pi}\frac{(-1)^n}{1-in}\\\ \\
f(x)=\frac{e^{\pi}-e^{-\pi}}{2\pi}\left(\sum_{-\infty}^{\infty}\frac{(-1)^n}{1-in}e^{inx}\right)$$

    ・計算すればsin系と同じになる。

---

## 不連続な関数

・$$f:[-\pi,\pi]\to\bm{R},\quad f(x)=\begin{cases}
-1 & (-\pi\le x\le 0) \\
1 & (0\le x\le\pi)    \\
\end{cases}$$
とする。このとき、
$$\frac{1}{\pi}\int f(x)\sin nxdx=\frac{2}{\pi n}((-1)^{n+1}+1)\\\ \\
f(x)=\frac{2}{\pi}\sum_{n\ge1}4\frac{(-1)^{n+1}+1}{n^2}\sin nx\\\ \\
=\frac{4}{\pi}\sum\frac{1}{2n-1}\sin(2n-1)x$$

    ・不連続点の扱いは左に合わせる。左右からのlim。

---

# 簡単なフーリエ変換

## $f(x)=b$

    ・定数のフーリエ変換

