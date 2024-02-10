
- [積分と極限](#積分と極限)



# 積分と極限

・開集合 $U$、連続関数 $f:U\to\bm{R}$、十分小さい実数 $\epsilon>0$、$x\in U$ とする。
このとき、
$$g_x:[-\epsilon,\epsilon]\times[0,1]\to\bm{R}\\\ \\
g_x(h,\theta)=f(x+h\theta e_j)$$
と定めると、$g$ の定義域はwell-defined。
<br>

- $g$ は連続関数であって、
$$\forall x\in U\text{ に対して、}\lim_{h\to 0}\Big(\sup_{\theta\in[0,1]}|f(x+h\theta e_j)-f(x)|\Big)=0\\\ \\
\forall x\in U\text{ に対して、}\lim_{h\to 0}\int_0^1f(x+\theta he_j)d\theta=f(x)$$