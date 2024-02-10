
- [三次元ラプラス方程式](#三次元ラプラス方程式)
  - [極座標](#極座標)
  - [円柱座標](#円柱座標)



# 三次元ラプラス方程式

三次元ラプラス方程式：$\Delta\phi(x,y,z)=0$

## 極座標

    ・これリーマン幾何の範疇か？
<br>

<dl><dt>

・ラプラス方程式 $\Delta\phi=0$ とする。
このとき、極座標変換すると、極座標におけるラプラス方程式：
$$\Delta\phi=\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial\phi}{\partial r}\right)+\frac{1}{r^2\sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta\frac{\partial\phi}{\partial \theta}\right)+\frac{1}{r^2\sin^2\theta}\frac{\partial^2\phi}{\partial\phi^2}=0$$
となる。

    ・テンソル解析参照。
<br>

</dt><dd>

・極座標におけるラプラス方程式の解：$\phi(r)=R(r)\Theta(\theta)\Phi(\phi)$ とする。
このとき、解くべき方程式：
$$\frac{d^2\Phi}{d\phi^2}+m^2\Phi=0\quad(m{は複素数かも})\\\ \\
\frac{d}{dr}\left(r^2\frac{dR}{dr}\right)-n(n+1)R=0\\\ \\
\frac{1}{\sin\theta}\frac{d}{d\theta}\left(\sin\theta\frac{d\Theta}{d\theta}\right)+\left\{n(n+1)-\frac{m^2}{\sin^2\theta}\right\}\Theta=0$$

    ・変数分離した？特殊関数が完全系であることによってる？
<br>

- $\Phi(\phi)=e^{\pm im\phi}$、したがって、$m=0,\pm1,\pm2,...$でなければならない

- $R(r)=Ar^n+Br^{-n-1}$
- $\Theta(\theta)=P_n^m(\cos\theta)\quad({ルジャンドル陪関数})$

    ・？？？
<br>

- 一般解：
$$V(r,\theta,\phi)=\sum_{n,m} \left(A_nr^n+\frac{B_n}{r^{n+1}}\right)(C_m\cos m\phi+D_m\sin m\phi)P_n^m(\cos\theta)\\\ \\
(n=0,1,...,\quad m=-l,-l+1,...,l-1,l)$$

      ・？？？

</dd></dl>


---

## 円柱座標

・ラプラス方程式 $\Delta\phi=0$ とする。
このとき、円柱座標変換すると、円柱座標におけるラプラス方程式：
$$\Delta\phi=\frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial\phi}{\partial r}\right)+\frac{1}{r^2}\frac{\partial^2\phi}{\partial \theta^2}+\frac{\partial^2\phi}{\partial z^2}=0\\\ \\$$

    ・テンソル解析参照。

・円柱座標におけるラプラス方程式の解：$\phi(r)=R(r)\Theta(\theta)\Phi(\phi)$ とする。
このとき、解くべき方程式：
$$\frac{d^2\Phi}{d\phi^2}+m^2\Phi=0\quad(m{は複素数かも})\\\ \\
\frac{d}{dr}\left(r^2\frac{dR}{dr}\right)-n(n+1)R=0\\\ \\
\frac{1}{\sin\theta}\frac{d}{d\theta}\left(\sin\theta\frac{d\Theta}{d\theta}\right)+\left\{n(n+1)-\frac{m^2}{\sin^2\theta}\right\}\Theta=0$$

    ・変数分離した。完全系であることによってる？
