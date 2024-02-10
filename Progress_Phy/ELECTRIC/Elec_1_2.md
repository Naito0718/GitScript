
    ・そのうち古典的な電磁場と光子の関係を説明するかも、ジャクソンp.5

- [一般の電磁場の性質](#一般の電磁場の性質)
  - [エネルギー保存](#エネルギー保存)
  - [積分形](#積分形)
- [電荷粒子の古典力学](#電荷粒子の古典力学)
  - [エネルギー保存](#エネルギー保存-1)
  - [運動量保存](#運動量保存)
  - [古典粒子近似](#古典粒子近似)
    - [電流密度](#電流密度)
    - [オームの法則](#オームの法則)
    - [物体が速度 $v$ で動くとき](#物体が速度-v-で動くとき)



# 一般の電磁場の性質

<dl><dt>

・真空中の電磁場を記述する方程式は、以下で与えられる。
$$\nabla\cdot\bm{D}=\rho\\\ \\
\nabla\times\bm{H}-\frac{\partial\bm{D}}{\partial t}=\bm{j}\\\ \\
\nabla\times\bm{E}+\frac{\partial\bm{B}}{\partial t}=0\\\ \\
\nabla\cdot \bm{B}=0\\\ \\
$$
ただし、$\bm{D}=\epsilon_0\bm{E},\quad\bm{B}=\mu_0\bm{H},\quad \frac{1}{c^2}=\epsilon_0\mu_0$ が成り立つ。
<br>

</dt><dd>

- $$\frac{\partial\rho}{\partial t}+\nabla\cdot\bm{j}=0$$

</dd></dl>

---

## エネルギー保存

<dl><dt>

・$$\frac{1}{\mu_0}\mathrm{div}(E\times B)+E\cdot j=-\frac{\partial}{\partial t}\left(\frac{1}{2}\epsilon_0E^2+\frac{1}{2\mu_0}B^2\right)$$
ここで、エネルギー密度 $w(x,t)=\frac{1}{2}\epsilon_0E^2+\frac{1}{2\mu_0}B^2$、ポインティングベクトル $S=\frac{1}{\mu_0}(E\times B)$ と定める。
<br>

</dt><dd>

- $E\cdot j=0$ とする。
このとき、$$\frac{\partial w}{\partial t}+\mathrm{div}\ S=0$$
特に、これは連続の式であり、$S$ はエネルギー流れとみなせる。
<br>

</dd></dl>

---

## 積分形

・有限領域 $V\sub\bm{R}^3$、閉曲線 $C\sub\bm{R}^3$ とする。
このとき、
$$\oint_{\partial V}\bm{D}\cdot \bm{n}dS=\int_V\rho dV\\\ \\
\oint_{\partial V}\bm{B}\cdot\bm{n}dS=0\\\ \\
\oint_C\bm{H}\cdot d\bm{r}=\int_{S_C}\left(\bm{j}+\frac{\partial\bm{D}}{\partial t}\right)\cdot\bm{n}dS\\\ \\
\oint_C\bm{E}\cdot d\bm{r}=-\int_{S_C}\frac{\partial\bm{B}}{\partial t}\cdot\bm{n}dS\\\ \\$$
ここで、$S_C$ は $C$ を張る任意の閉曲面。

---

# 電荷粒子の古典力学

・電磁場内の位置 $x_i(t)$ にある電荷 $e_i$ の系を考える。
このとき、電荷密度 $\rho_i$、電流密度 $j_i$： 
$$\rho_i(x,t)=e_i\delta^3(x-x_i(t))\\\ \\
j_i(x,t)=e_i\dot{x}_i(t)\delta^3(x-x_i(t))\\\ \\$$
このとき、
$$\frac{\partial\rho}{\partial t}+\mathrm{div}\ j=0\\\ \\$$
である。ここで、質量 $m_i$ の電荷 $e_i$ に働く力 $F$ と運動方程式は、
$$F_i=\int dx^3(\rho_i E+j_i\times B)=e_iE(x_i(t),t)+e_i\dot{x}_i(t)\times B(x_i(t),t)\\\ \\
(eom):m_i\frac{d^2x_i}{dt^2}=F_i$$
で与えられる。

---

## エネルギー保存

・$$-\frac{d}{dt}\sum\frac{1}{2}m_i\dot{x}_i^2+W=\int$$

## 運動量保存

## 古典粒子近似

### 電流密度

平均速度：$v_D=\frac{1}{N}\sum v_i$
電流密度：$i_e=Nev_D=e\sum v_i$

    ・Nは単位体積当たりの電子数、単位に注意

### オームの法則


    ・電子群の運動に対する抵抗力はその平均速度に比例する（衝突回数）
    ・自己場、磁場は無視する

・外部から電場 $E$ が作用した時の記述方程式：$m(\frac{dv_D}{dt}+\frac{1}{\tau}v_D)=eE,\quad(\tau:{緩和時間})$

    ・電子群だけどeEで与えられるっぽい

- 定常状態：$v_D=\frac{e\tau}{m}E$
- $\sigma=\frac{Ne^2\tau}{m}$

---

### 物体が速度 $v$ で動くとき

→ $v_D=v$

・一様な面電荷密度 $\sigma$ の板が速度 $v$ で動くとき

- $i_e=\sigma v$

        ・Ne=σ



