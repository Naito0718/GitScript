



# 可積分条件

・領域 $D\sub\bm{R}^2$、$C^{\infty}$ 写像 $F,G:D\to M(n,\bm{R})$
このとき、
$$H_u=HF,\quad H_v=HG$$
を満たす $C^2$ 解 $H:D\to GL(n,\bm{R})$ が存在するならば、
$$F_v-G_u=FG-GF$$ 
ここで、最後の式を可積分条件という。

- 単連結領域 $D\sub\bm{R}^2$、$(u_0,v_0)\in D$、$x_0\in GL(n,\bm{R})$、可積分条件を満たす $F,G:D\to M(n,\bm{R})$ とする。
このとき、
$$x_0(t)=x_0,\quad x_n(t)=x_0+\int_{t_0}^tf(\tau,x_{n-1}(\tau))d\tau$$
と定めると、$x_n(t)$ はある $C^{\infty}$ 関数かつ逆行列を持つ $x(t)$ に一様収束し、
$$\exist\delta>0\text{ であって、}B((u_0,v_0),\delta){ 上で }\\\ \\
\frac{\partial x}{\partial u}(u,v)=(xF)(u,v),\quad\frac{\partial x}{\partial v}(u,v)=(xG)(u,v)\quad x(u_0,v_0)=x_0$$
さらに、上記の偏微分方程式を満たす解 $x(t)$ は一意的。
<br>

      ・？単連結領域を使うとこがよくわかんない、たぶん一点を拡張するのに使う。




