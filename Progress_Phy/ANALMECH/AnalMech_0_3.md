



# 時間変化する座標系

$$\bm{r}=xe_1+ye_2+ze_3=Xe_x(t)+Ye_y(t)+Ze_z$$
とする。
このとき、
- $\bm{v}=\dot{x}e_1+\dot{y}e_2+\dot{z}e_3,\ \bm{v}_{C}=\dot{X}e_x(t)+\dot{Y}e_y(t)+\dot{z}e_3$ とする。
このとき、
$$\dot{\bm{r}}=\bm{v}=\bm{v}_C+\omega e_3\times\bm{r}\\\ \\$$

- $\bm{a}=\ddot{x}e_1+\ddot{y}e_2+\ddot{z}e_3,\ \bm{v}_{C}=\ddot{X}e_x(t)+\ddot{Y}e_y(t)+\ddot{z}e_3$ とする。
このとき、
$$\ddot{\bm{r}}=\bm{a}=\bm{a}_C+2\omega(e_z\times\bm{v}_C)+\omega^2 e_3\times(e_3\times\bm{r})$$

---

## $z$ 軸周りで回転する座標系

・角速度 $\omega>0$ とする。
このとき、
$$e_x(t)=\begin{pmatrix}\cos\omega t \\ \sin\omega t \\ 0\end{pmatrix},\quad e_y(t)=\begin{pmatrix}-\sin\omega t \\ \cos\omega t \\ 0\end{pmatrix},\quad e_z=\begin{pmatrix}0 \\ 0 \\ 1\end{pmatrix}$$
と定めると、$\forall t\text{ に対して、}(e_x(t),e_y(t),e_z)$ は正規直交基底。
<br>

- $$\dot{e_x}(t)=\omega e_y(t),\quad\dot{e_y}(t)=-\omega e_x(t),\quad\dot{e_z}=0$$

---

## 標準座標との関係

・$$\bm{r}=xe_1+ye_2+ze_3=Xe_x(t)+Ye_y(t)+Ze_z$$
とする。
このとき、明らかに $z=Z,\ e_3=e_z$

- $\bm{v}=\dot{x}e_1+\dot{y}e_2+\dot{z}e_3,\ \bm{v}_{C}=\dot{X}e_x(t)+\dot{Y}e_y(t)+\dot{z}e_3$ とする。
このとき、
$$\dot{\bm{r}}=\bm{v}=\bm{v}_C+\omega e_3\times\bm{r}\\\ \\$$

- $\bm{a}=\ddot{x}e_1+\ddot{y}e_2+\ddot{z}e_3,\ \bm{v}_{C}=\ddot{X}e_x(t)+\ddot{Y}e_y(t)+\ddot{z}e_3$ とする。
このとき、
$$\ddot{\bm{r}}=\bm{a}=\bm{a}_C+2\omega(e_z\times\bm{v}_C)+\omega^2 e_3\times(e_3\times\bm{r})$$


# 時間変化する座標系への変換

