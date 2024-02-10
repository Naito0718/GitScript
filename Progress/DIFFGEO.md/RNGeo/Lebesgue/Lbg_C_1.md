



# $exp$ とLebesgue積分

|**$Lbg- 1$**|
|:-|

$c_1<c_2$ なる $c_1,c_2\in\bm{R}$、可測関数 $f:\bm{R}\to\bm{C}$、Borel測度 $\mu:\mathfrak{B}_{\bm{R}}\to[0,\infty]$ とする。
このとき、
$$e^{c_1x}f(x),e^{c_2x}f(x)\in L^1(\bm{R},\mathfrak{B}_{\bm{R}},\mu)\text{ が成り立つ}\\\ \\
\Rightarrow c_1<\mathrm{Re}(z)<c_2\text{ なる }z\in\bm{C},\ n\in\bm{N}\text{ に対して、}x^ne^{zx}f(x)\in L^1(\bm{R},\mathfrak{B}_{\bm{R}},\mu)\text{ であって、}\\\ \\
g:\{z\in\bm{C}\ |\ c_1<\mathrm{Re}(z)<c_2\}\to\bm{C}\\\ \\
g(z)=\int_{\bm{R}}e^{zx}f(x)d\mu(x)\\\ \\
\text{は正則関数であって、}g^{(n)}(z)=\int_{\bm{R}}x^ne^{zx}f(x)d\mu(x)\\\ \\$$

>qed,確率論p.36（岩田）

