
- [常螺旋](#常螺旋)
- [無限円筒 $S^1×R$](#無限円筒-s1r)
- [カテノイド](#カテノイド)
  - [ヘリコイド](#ヘリコイド)
- [円錐面](#円錐面)
- [接線曲面](#接線曲面)
- [トリチェリの回転体](#トリチェリの回転体)





# 常螺旋
$$p(t)=(a\cos t,a\sin t,ht)$$
・弧長：$s(t)=(a^2+h^2)^{\frac{1}{2}}t$
・曲率：$\kappa=\frac{a}{a^2+h^2}$
・捩率：$\tau=\frac{h}{a^2+h^2}$

---

# 無限円筒 $S^1×R$

<dl><dt>

・
$$p:\bm{R}^2\to\bm{R}^3\\\ \\
p(u,v)=\begin{pmatrix}
\cos u \\ \sin u \\ v \\
\end{pmatrix}$$
とする。

    ・実際は正則レベル集合とした後、座標変換するべきだと思われる。
<br>

</dt><dd>

- $$p_u=\begin{pmatrix}
-\sin u  \\ \cos u \\ 0  
\end{pmatrix},\quad p_v=\begin{pmatrix}
0  \\ 0 \\ 1  
\end{pmatrix}\\\ \\
p_{uu}=\begin{pmatrix}
-\cos u  \\ -\sin u \\ 0  
\end{pmatrix},\quad p_{uv}=0,\quad p_{vv}=0\\\ \\$$

- 
$$E=1,\ F=0,\ G=1\\\ \\
\nu=\begin{pmatrix}
\cos u  \\ \sin u \\ 0  
\end{pmatrix}=-p_{uu}\\\ \\
L=-1,\ M=0,\ N=0\\\ \\$$

- $$K=0,\ H=-\frac{1}{2}$$

<br>

- 

</dd></dl>

・$2$ 次元 $C^{\infty}$ 積多様体。

---

# カテノイド

<dl><dt>

・$D=(-\pi,\pi)\times\bm{R}$ とする。
このとき、$$p:\bm{R}^2\to\bm{R}^3\\\ \\
p(u,v)=\begin{pmatrix}
\cos u\cosh v \\ \sin u\cosh v \\ v \\
\end{pmatrix}$$
と定める。
<br>

</dt><dd>

- $$p_u=\cosh v\begin{pmatrix}
-\sin u  \\ \cos u \\ 0  
\end{pmatrix},\quad p_v=\begin{pmatrix}
\cos u\sinh v  \\ \sin u\sinh v \\ 1  
\end{pmatrix}\\\ \\
p_{uu}=\cosh v\begin{pmatrix}
-\cos u  \\ -\sin u \\ 0  
\end{pmatrix},\quad p_{uv}=\sinh v\begin{pmatrix} -\sin u \\ \cos u \\ 0 \end{pmatrix},\quad p_{vv}=\cosh v\begin{pmatrix} \cos u \\ \sin u \\ 0 \end{pmatrix}\\\ \\$$

- 
$$E=\cosh^2 v,\ F=0,\ G=\cosh^2 v\\\ \\
\nu=\frac{1}{\cosh v}\begin{pmatrix}
\cos u  \\ \sin u \\ -\sinh v  
\end{pmatrix}\\\ \\
L=-1,\ M=0,\ N=1\\\ \\$$

- $$K=-\frac{1}{\cosh^4v},\ H=0$$

</dd></dl>

---

## ヘリコイド

<dl><dt>

・$D=(-\pi,\pi)\times\bm{R}$ とする。
このとき、$$p:D\to\bm{R}^3\\\ \\
p(u,v)=\begin{pmatrix}
\cos u\sinh v \\ \sin u\sinh v \\ u \\
\end{pmatrix}$$
と定める。
<br>

</dt><dd>

- $$p_u=\begin{pmatrix}
-\sin u\sinh v  \\ \cos u\sinh v \\ 1
\end{pmatrix},\quad p_v=\cosh v\begin{pmatrix}
\cos u  \\ \sin u \\ 0  
\end{pmatrix}\\\ \\
p_{uu}=\sinh v\begin{pmatrix}
-\cos u  \\ -\sin u \\ 0  
\end{pmatrix},\quad p_{uv}=\cosh v\begin{pmatrix}
 -\sin u \\ \cos u \\ 0 \\
\end{pmatrix},\quad p_{vv}=\sinh v\begin{pmatrix}
\cos u  \\ \sin u \\ 0 \\
\end{pmatrix}\\\ \\$$

- 
$$E=\cosh^2 v,\ F=0,\ G=\cosh^2 v\\\ \\
\nu=\frac{1}{\cosh v}\begin{pmatrix}
-\sin u  \\ \cos u \\ -\sinh v  
\end{pmatrix}\\\ \\
L=0,\ M=1,\ N=0\\\ \\$$

- $$K=-\frac{1}{\cosh^4v},\ H=0$$

<br>

- 

</dd></dl>

---


# 円錐面

<dl><dt>

・$D=\{(u,v)\in\bm{R}^2\ |\ v>0\}\sub\bm{R}^2$ とする。
このとき、
$$p:\bm{R}^2\to\bm{R}^3\\\ \\
p(u,v)=v\begin{pmatrix}
\cos u \\ \sin u \\ 1 \\
\end{pmatrix}$$
と定める。

<br>

</dt><dd>

- $$p_u=v\begin{pmatrix}
-\sin u  \\ \cos u \\ 0  
\end{pmatrix},\quad p_v=\begin{pmatrix}
\cos u  \\ \sin u \\ 1  
\end{pmatrix}\\\ \\
p_{uu}=v\begin{pmatrix}
-\cos u  \\ -\sin u \\ 0  
\end{pmatrix},\quad p_{uv}=\begin{pmatrix}
-\sin u    \\ \cos u \\ 0
\end{pmatrix},\quad p_{vv}=0\\\ \\$$

- 
$$E=v^2,\ F=0,\ G=2\\\ \\
\nu=\frac{1}{\sqrt{2}}\begin{pmatrix}
\cos u  \\ \sin u \\ -1  
\end{pmatrix}\\\ \\
L=-\frac{v}{\sqrt{2}},\ M=0,\ N=0\\\ \\$$

- $$K=0,\ H=-\frac{1}{2\sqrt{2}v}$$

<br>


</dd></dl>

---

# 接線曲面

<dl><dt>

・$D=\{(u,v)\in\bm{R}^2\ |\ v>0\}\sub\bm{R}^2$ とする。
このとき、
$$p:\bm{R}^2\to\bm{R}^3\\\ \\
p(u,v)=\begin{pmatrix}
\cos u \\ \sin u \\ u \\
\end{pmatrix}+v\begin{pmatrix}
-\sin u \\ \cos u \\ 1 \\
\end{pmatrix}$$
と定める。

<br>

</dt><dd>

- $$p_u=\begin{pmatrix}
-\sin u  \\ \cos u \\ 1  
\end{pmatrix}+v\begin{pmatrix}
-\cos u  \\ -\sin u \\ 0  
\end{pmatrix},\quad p_v=\begin{pmatrix}
-\sin u  \\ \cos u \\ 1  
\end{pmatrix}\\\ \\
p_{uu}=\begin{pmatrix}
-\cos u  \\ -\sin u \\ 0  
\end{pmatrix}+v\begin{pmatrix}
\sin u  \\ -\cos u \\ 0  
\end{pmatrix},\quad p_{uv}=\begin{pmatrix}
-\cos u    \\ -\sin u \\ 0
\end{pmatrix},\quad p_{vv}=0\\\ \\$$

- 
$$E=2+v^2,\ F=2,\ G=2\\\ \\
\nu=\frac{1}{\sqrt{2}}\begin{pmatrix}
-\sin u  \\ \cos u \\ -1  
\end{pmatrix}\\\ \\
L=-\frac{v}{\sqrt{2}},\ M=0,\ N=0\\\ \\$$

- $$K=0,\ H=-\frac{1}{2\sqrt{2}v}$$

<br>


</dd></dl>

---


# トリチェリの回転体

$$p(t)=(x,y,\frac{1}{\sqrt{x^2+y^2}})\quad(x^2+y^2\le1)$$

→$z\ge1$にのみ存在する、$z$軸回転対称な形

---

・体積：$V=\int_1^{\infty}\pi x^2dy=\pi$

→一方、断面積$S_{slash}=\int_{\to0}^1\frac{1}{x}=\infty$