
- [運動量](#運動量)
- [角運動量](#角運動量)
  - [変換に対する性質](#変換に対する性質)
    - [原点の移動](#原点の移動)
    - [初速度を与えた座標系](#初速度を与えた座標系)
    - [空間回転](#空間回転)
  - [$z$ 軸についてのみ対称な系](#z-軸についてのみ対称な系)
- [ネーターの定理](#ネーターの定理)




# 運動量

# 角運動量

・$\forall\text{ 微小回転行列 }E+\epsilon=E+\tilde{\bm{\epsilon}}$ に対して不変な孤立系のラグランジアン $L$ とする。
このとき、微小回転後のラグランジアンを $L'$ とすると、$$L'-L=\delta L=\sum\frac{\partial L_i}{\partial \bm{r}_i}\cdot\delta\bm{r}_i+\frac{\partial L}{\partial \bm{v}_i}\cdot\delta\bm{v}_i=0\\\ \\
\delta\bm{r}_i=\bm{\epsilon}\times\bm{r}_i,\quad\delta\bm{v}_i=\epsilon\times\bm{v}_i$$
より、$$\bm{\epsilon}\cdot\frac{d}{dt}\sum(\bm{r}_i\times\bm{p}_i)=0\\\ \\
\Rightarrow\frac{d}{dt}\sum(\bm{r}_i\times\bm{p}_i)=0$$
ここで、保存量 $\bm{M}=\sum(\bm{r}_i\times\bm{p}_i)$ を全角運動量という。

---

## 変換に対する性質

### 原点の移動

・$\bm{a}\in\bm{R}^3$、原点を $\bm{a}$ 動かす変換 $\bm{r}'=\bm{r}-\bm{a}$ とする。
このとき、変換後の全角運動量を $\bm{M}'$ とすると、
$$\bm{M}'=\bm{M}-\bm{a}\times\bm{P}$$
したがって、
$$\frac{d\bm{M}'}{dt}=0$$
であって、系全体が静止しているとき、全角運動量は原点を動かす変換で不変。

---

### 初速度を与えた座標系

・$\bm{V}\in\bm{R}^3$、$t=t_0$ で座標系に初速度を与える変換 $\bm{v}'=\bm{v}-\bm{V},\quad\bm{r}'=\bm{r}$ とする。
このとき、変換後の全角運動量を $\bm{M}'$ とすると、
$$\bm{M}'=\bm{M}-\left(\sum m_i\right)\bm{R}\times
\bm{V}$$
特に、$$V=\frac{d\bm{R}}{dt}(t_0)$$
の時は、$\bm{M}'=\bm{M}-\bm{R}\times\bm{P}$

---

### 空間回転

---

## $z$ 軸についてのみ対称な系

・$\forall z\text{ 軸周りの微小回転行列 }E+\epsilon=E+\tilde{\bm{\epsilon}},\quad\bm{\epsilon}_x=\bm{\epsilon}_y=0$ に対して不変な孤立系のラグランジアン $L$ とする。
このとき、微小回転後のラグランジアンを $L'$ とすると、$$L'-L=\delta L=\sum\frac{\partial L_i}{\partial \bm{r}_i}\cdot\delta\bm{r}_i+\frac{\partial L}{\partial \bm{v}_i}\cdot\delta\bm{v}_i=0\\\ \\
\delta\bm{r}_i=\bm{\epsilon}\times\bm{r}_i,\quad\delta\bm{v}_i=\epsilon\times\bm{v}_i$$
より、$$\bm{\epsilon}\cdot\frac{d}{dt}\sum(\bm{r}_i\times\bm{p}_i)=0\\\ \\
\Rightarrow\frac{d}{dt}\left\{\sum(\bm{r}_i\times\bm{p}_i)\right\}_z=0\\\ \\$$

- 円柱座標 $(r,\theta,z)$、$z$ 軸周りの任意の微小回転で不変なラグランジアン $L$ とする。
このとき、
$$\bm{M}_z=\sum\frac{\partial L}{\partial\dot{\theta}_i}=\sum m_ir_i^2\dot{\theta}_i$$

---

# ネーターの定理




