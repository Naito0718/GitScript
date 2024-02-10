
- [球面曲線](#球面曲線)
  - [錐面](#錐面)
- [平坦曲面](#平坦曲面)
  - [平面内の（曲）面](#平面内の曲面)
- [柱面](#柱面)
- [接線曲面](#接線曲面)
- [等温座標系](#等温座標系)



# 球面曲線

・正則曲線 $\gamma:I\to S^2$ とする。
このとき、測地的曲率関数 $\mu$：
$$\mu:I\to\bm{R}\\\ \\
\mu(s)=e(s)\cdot u(s)$$
ここで、$u(s)=\gamma(s)\times e(s)$ は単位法ベクトル。

---

## 錐面

---

# 平坦曲面

・正則曲面 $p:\bm{R}^2\to\bm{R}^3$ とする。
このとき、平坦曲面 $p$：ガウス曲率 $K=0$ 

## 平面内の（曲）面

・$r=r(\theta)$で与えられる平面

→面積：$S=\frac{1}{2}\int_0^{2\pi}r(\theta)^2d\theta$
また、$Se_z=\frac{1}{2}\oint_Cx'\times dx'$

---

# 柱面

・正則曲線 $\gamma:I\to\bm{R}^2$ とする。
このとき、柱面 $p$：
$$p:I\times\bm{R}\to\bm{R}^3\\\ \\
p(u,v)=(\gamma(u),v)$$

---

# 接線曲面

・正則曲線 $\gamma:I\to\bm{R}^3$ とする。
このとき、接線曲面 $p$：
$$p:I\times\bm{R}_+\to\bm{R}^3\\\ \\
p(u,v)=\gamma(u)+v\gamma'(u)$$
ここで、接線曲面は正則曲面。

    ・？？？

---

# 等温座標系

<dl><dt>

・$\bm{R}^3$ 内の超曲面 $M$ とする。
このとき、等温座標系 $M$：
$$\forall M\text{ のチャート }(U,\phi;x^1,x^2),\ \forall p\in U\text{ に対して、}\\\ \\
g_{(U,\phi)}(p)=\begin{pmatrix}
E(p) & 0  \\
0 & E(p) \\  
\end{pmatrix},\quad E=\left(\frac{\partial}{\partial x^1}p,\ \frac{\partial}{\partial x^1}p\right)\\\ \\$$
明らかに、$G_{(U,\phi)}(p)=E(p)^2,\quad\sqrt{G_{(U,\phi)}(p)}=E(p)$

    ・が、存在するかどうか？デイビッドテンソルには書いてなさげ？
<br>

</dt><dd>

- $$\bm{n}(p)=\frac{1}{\sqrt{G_{(U,\phi)}(p)}}\left(\frac{\partial}{\partial x^1}p\times\frac{\partial}{\partial x^2}p\right)=E(p)\left(\frac{\partial}{\partial x^1}p\times\frac{\partial}{\partial x^2}p\right)\\\ \\$$

- ガウス曲率 $K$、平均曲率 $H$ とする。
このとき、
$$K=\frac{LN-M^2}{E^2},\quad H=\frac{L+N}{2E}\\\ \\$$

- クリストッフェル記号 $\Gamma$ とする。
このとき、
$$\Gamma^1_{11}(p)=\frac{\partial E}{\partial x^1}(p)\frac{1}{2E(p)}=\Gamma^2_{12}(p)=-\Gamma^1_{22},\quad\Gamma^2_{11}=(p)=-\frac{\partial E}{\partial x^2}(p)\frac{1}{2E(p)}=-\Gamma^1_{12}(p)=-\Gamma^2_{22}(p)\\\ \\
$$

- $$[\mathcal{U}_1,\mathcal{U}_2]=\begin{pmatrix}
0 & -P & \frac{E_{x^2}(L-N)-2E_{x^1}M}{2E^2} \\\\
P & 0 & \frac{E_{x^1}(L-N)-2E_{x^2}M}{2E^2} \\\\
Q & R & 0 \\
\end{pmatrix}\\\ \\
P=\frac{LN-M^2}{E},\quad Q=\frac{L+N}{2E}E_{x^2},\quad R=-\frac{L+N}{2E}E_{x^1}\\\ \\$$

- $$[\mathcal{U}_1,\mathcal{U}_2]=\mathcal{U}_{1,x^1}-\mathcal{U}_{2.x^2}\\\ \\
\iff\begin{cases}
\Delta(\log E)=-EK  \\
L_{x^2}-M_{x^1}=HE_{x^2}  \\
M_{x^2}-N_{x^1}=-HE_{x^1}  \\
\end{cases}$$





</dd></dl>
