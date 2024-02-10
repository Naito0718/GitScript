
- [適当なポテンシャル](#適当なポテンシャル)
  - [$1/cosh^2$](#1cosh2)
- [正準変換](#正準変換)
- [三次元極座標](#三次元極座標)
- [三次元円柱座標](#三次元円柱座標)



# 適当なポテンシャル

## $1/cosh^2$

・質点 $m$、エネルギー $E<0$、$\alpha\in\bm{R}$、$-U_0<E$、ポテンシャル $$U(x)=-\frac{U_0}{\cosh^2\alpha x}$$ とする。
このとき、
$$U(x_0)=E\iff x_0=\pm\frac{1}{a}\cosh^{-1}\left(\sqrt{\frac{U_0}{-E}}\right)\\\ \\
T(E)=\frac{2}{a}\sqrt{-\frac{2m}{E}}\sin^{-1}\left(\sqrt{\frac{-E}{E+U_0}}\sinh ax_0\right)$$



# 正準変換

・正準変換$$\begin{pmatrix}Q \\ P\end{pmatrix}=\begin{pmatrix}a & b \\ c & d\end{pmatrix}\begin{pmatrix}q \\ p\end{pmatrix}$$
$\det A=1,b\neq0$
母関数$F(q,Q)=\frac{1}{b}\frac{q}{Q}-\frac{1}{2b}(aq^2+dQ^2)$

---

# 三次元極座標

<dl><dt>

・$$r=\sqrt{x^2+y^2+z^2},\quad\theta=\tan^{-1}\left(\frac{\sqrt{x^2+y^2}}{z}\right),\quad\phi=\tan^{-1}\left(\frac{y}{x}\right)\\\ \\
(\sqrt{x^2+y^2}\text{ は }\sin\theta>0)$$
とし、
$$\bm{e}_r=\begin{pmatrix} \sin\theta\cos\phi \\ \sin\theta\sin\phi \\ \cos\theta  \end{pmatrix},\quad\bm{e}_{\theta}=\begin{pmatrix} \cos\theta\cos\phi \\ \cos\theta\sin\phi \\ -\sin\theta  \end{pmatrix},\quad \bm{e}_{\phi}=\begin{pmatrix} -\sin\phi \\ \cos\phi \\ 0  \end{pmatrix}\\\ \\$$
と定める。
<br>

</dt><dd>

- $$\dot{\bm{e}_r}=\dot{\theta}\bm{e}_{\theta}+\dot{\phi}\sin\theta \bm{e}_{\phi}\\\ \\
\dot{\bm{e}_{\theta}}=-\dot{\theta}\bm{e}_{r}+\dot{\phi}\cos\theta \bm{e}_{\phi}\\\ \\
\dot{\bm{e}_{\phi}}=-
\dot{\phi}(\sin\theta \bm{e}_r+\cos\theta \bm{e}_{\theta})\\\ \\$$

- $\frac{\partial\theta}{\partial x}$

- $$\bm{r}=r\bm{e}_r,\\\ \\
\dot{\bm{r}}=\dot{r}\bm{e}_r+r\dot{\theta}\bm{e}_{\theta}+r\dot{\phi}\sin\theta \bm{e}_{\phi},\\\ \\ 
\ddot{\bm{r}}=\bm{e}_r(\ddot{r}-r\dot{r}^2+r\dot{\phi}^2\sin^2\theta)+\bm{e}_{\theta}(r\ddot{\theta}+2\dot{r}\dot{\theta}-r\dot{\phi}^2\sin\theta\cos\theta)+\bm{e}_{\phi}(2\dot{r}\dot{\phi}\sin\theta+2r\dot{\theta}\dot{\phi}\cos\theta+r\ddot{\phi}\sin\theta)$$

</dd></dl>

---

# 三次元円柱座標

<dl><dt>

・$$\rho=\sqrt{x^2+y^2},\quad\theta=\tan^{-1}\left(\frac{y}{x}\right)\\\ \\$$
とし、
$$\bm{e}_{\rho}=\begin{pmatrix} \cos\theta \\ \sin\theta\sin\phi \\ 0  \end{pmatrix},\quad\bm{e}_{\theta}=\begin{pmatrix} \cos\theta\cos\phi \\ \cos\theta\sin\phi \\ 0  \end{pmatrix}$$
と定める。
<br>

</dt><dd>

- $$\dot{\bm{e}_r}=\dot{\theta}\bm{e}_{\theta}+\dot{\phi}\sin\theta \bm{e}_{\phi}\\\ \\
\dot{\bm{e}_{\theta}}=-\dot{\theta}\bm{e}_{r}+\dot{\phi}\cos\theta \bm{e}_{\phi}\\\ \\
\dot{\bm{e}_{\phi}}=-
\dot{\phi}(\sin\theta \bm{e}_r+\cos\theta \bm{e}_{\theta})\\\ \\$$

- $\frac{\partial\theta}{\partial x}$

- $$\bm{r}=r\bm{e}_r,\\\ \\
\dot{\bm{r}}=\dot{r}\bm{e}_r+r\dot{\theta}\bm{e}_{\theta}+r\dot{\phi}\sin\theta \bm{e}_{\phi},\\\ \\ 
\ddot{\bm{r}}=\bm{e}_r(\ddot{r}-r\dot{r}^2+r\dot{\phi}^2\sin^2\theta)+\bm{e}_{\theta}(r\ddot{\theta}+2\dot{r}\dot{\theta}-r\dot{\phi}^2\sin\theta\cos\theta)+\bm{e}_{\phi}(2\dot{r}\dot{\phi}\sin\theta+2r\dot{\theta}\dot{\phi}\cos\theta+r\ddot{\phi}\sin\theta)$$

</dd></dl>


