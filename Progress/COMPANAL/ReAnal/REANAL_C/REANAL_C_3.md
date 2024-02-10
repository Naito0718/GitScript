

- [積分の簡単な性質](#積分の簡単な性質)
  - [$R$ 上の積分](#r-上の積分)
  - [区間による特性](#区間による特性)
  - [ベクトル値関数の積分](#ベクトル値関数の積分)
- [ディリクレ積分](#ディリクレ積分)
- [$n$ 進数関数](#n-進数関数)


# 積分の簡単な性質

## $R$ 上の積分

・$I=[a,b]\sub\bm{R}$、$I$ 上単調増加または単調減少関数 $f:I\to\bm{R}$ とする。
このとき、$f$ は有界であって、$I$ 上可積分。

- $I=[a,b]$ 上可積分関数 $f:I\to\bm{R}$ とする。
このとき、
$$\int_If(x)dx=\lim_{n\to\infty}\left[\frac{b-a}{n}\sum_{k=1}^nf\left(a+\frac{b-a}{n}k\right)\right]$$

---

## 区間による特性

・$f:I\to\bm{R}$ とする。
このとき、$I$ のある一辺の長さが $0$ ならば、
$$\int_If(x)dx=0$$

---

## ベクトル値関数の積分

・有界可積分関数 $f:[a,b]\to\bm{R}^n$ とする。
このとき、$|f|$ は可積分であって、
$$\left|\int_a^bf(t)dt\right|\le\int_a^b|f(t)|dt\\\ \\$$

  全然示してないが、振幅によるっぽい。
<br>

---

# ディリクレ積分

<dl><dt>

・
$$f:\bm{R}\to\bm{R}\\\ \\
f(x)=\begin{cases}
1 & (x\in\bm{Q}) \\
0 & (x\in\bm{Q}^c) \\    
\end{cases}$$
と定める。

</dt><dd>

- $f$ は $[0,1]$ でリーマン可積分でない。
<br>

      ・ある代表点で収束しても、可積分とは限らない。


</dd></dl> 

---

# $n$ 進数関数

<dl><dt>

・$I=[0,1]$、$2\le n\in\bm{N}$ とし、
$$f:I\to\bm{R}\\\ \\
f(x)=(x\text{ の }n\text{ 進数表示})$$
と定める。
<br>

</dt><dd>

- $f$ は単調増加。特に、$f$ は $I$ 上可積分。
<br>

- $$\int_If(x)dx=\lim_{N\to\infty}\frac{1}{n^N}\sum_{k=0}^{n^N-1} f\left(\frac{k}{n^N}\right)\\\ \\
=\lim_{N\to\infty}\frac{1}{n}0.(n-1)(n-1)...(n-1)\quad(N\text{ 桁})\\\ \\
=\frac{1}{n}\frac{n-1}{10}\frac{1}{1-\frac{n-1}{10}}=\frac{n-1}{n(11-n)}$$


</dd></dl> 