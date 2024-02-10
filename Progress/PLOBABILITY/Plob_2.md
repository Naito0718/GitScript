
- [漸近解析](#漸近解析)
  - [一変数](#一変数)
  - [スターリング式](#スターリング式)
  - [二変数](#二変数)




# 漸近解析

## 一変数

<dl><dt>

・連続関数 $g,h:[a,b]\to\bm{R}$ とする。
このとき、
$$I:(0,\infty)\to\bm{R}\\\ \\
I(t)=\int_a^be^{th(x)}g(x)dx$$
はwell-defined。   
<br>

</dt><dd>

- 非負値連続関数 $g:[a,b]\to[0,\infty)$ で、$g\neq0$ とする。
このとき、
$$\lim_{t\to\infty}\frac{1}{t}\log I(t)=\sup\{h(x)\ |\ x\in[a,b],\ g(x)>0\}$$



</dd></dl>

---

<dl><dt>

・$c\in[a,b]$ でのみ最大値を取り、$c$ の近傍で $C^2$ で $h''(c)\neq0$ 連続関数 $h:[a,b]\to\bm{R}$、$g(c)>0$ な連続関数 $g:[a,b]\to\bm{R}$ とする。

</dt><dd>

- $a<c<b$ ならば、
$$I(t)\sim\sqrt{\frac{2\pi}{|h''(c)|}}g(c)\frac{e^{th(c)}}{\sqrt{t}}\quad (t\to\infty)\\\ \\$$

      ・～はlimf(x)/g(x)=1 (t→∞)の意味。
      ・なんかかなり面倒だが、納得はできる。ルベーグ積分から確率論p.98
<br>

- $c=a\text{ または }b\text{ であって、}h'(c)=0$ ならば、
$$I(t)\sim\sqrt{\frac{\pi}{2|h''(c)|}}g(c)\frac{e^{th(c)}}{\sqrt{t}}\quad(t\to\infty)\\\ \\$$

- $c=a\text{ または }b\text{ であって、}h'(c)\neq0$ ならば、
$$I(t)\sim{\frac{g(c)}{|h'(c)|}}\frac{e^{th(c)}}{t}\quad(t\to\infty)$$

      ・端なので、ずっと滑り降りてきてるとき。このときh'(aかb)<0

</dd></dl>



## スターリング式

・$$\Gamma(t+1)\sim\sqrt{2\pi}t^{t+1/2}e^{-t}\quad(t\to\infty)$$
特に、$$(n+1)!\sim\sqrt{2\pi n}n^{n}e^{-n}$$

    ・いつものやつ！

## 二変数

---

