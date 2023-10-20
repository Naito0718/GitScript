
- [正準変換](#正準変換)
- [座標系](#座標系)
  - [三次元極座標](#三次元極座標)
- [単一ばね](#単一ばね)
  - [一次元](#一次元)
    - [抵抗があるとき](#抵抗があるとき)
      - [$γ$ が小さいとき](#γ-が小さいとき)
      - [$γ$ が大きいとき](#γ-が大きいとき)
      - [$γ=ω$](#γω)
  - [二次元](#二次元)
  - [自然長距離 $l\_0$ に束縛されているとき](#自然長距離-l_0-に束縛されているとき)
- [複数ばね](#複数ばね)
  - [一次元](#一次元-1)
- [振り子](#振り子)
  - [単振り子](#単振り子)
    - [微小振動](#微小振動)
  - [空気抵抗](#空気抵抗)
  - [強制振動](#強制振動)
- [円錐振り子](#円錐振り子)
  - [Borda振り子](#borda振り子)
  - [剛体振り子](#剛体振り子)




# 正準変換

・正準変換$$\begin{pmatrix}Q \\ P\end{pmatrix}=   \
\begin{pmatrix}a & b \\ c & d\end{pmatrix}\begin{pmatrix}q \\ p\end{pmatrix}    \\
$$
$\det A=1,b\neq0$
母関数$F(q,Q)=\frac{1}{b}\frac{q}{Q}-\frac{1}{2b}(aq^2+dQ^2)$$

---

# 座標系

## 三次元極座標

・$x=re_r,\ \dot{x}=\dot{r}e_r+r\dot{\theta}e_\theta+r\dot{\phi}\sin\theta e_{\phi},\\\ \\ 
\ddot{x}=e_r(\ddot{r}-r\dot{r}^2+r\dot{\phi}^2\sin^2\theta)+e_{\theta}(r\ddot{\theta}+2\dot{r}\dot{\theta}-r\dot{\phi}^2\sin\theta\cos\theta)+e_{\phi}(2\dot{r}\dot{\phi}\sin\theta+2r\dot{\theta}\dot{\phi}\cos\theta+r\ddot{\phi}\sin\theta)$

→$\dot{e}_r=\dot{\theta}e_{\theta}+\dot{\phi}\sin\theta e_{\phi},\ \dot{e}_{\theta}=-\dot{\theta}e_{r}+\dot{\phi}\cos\theta e_{\phi},\ \dot{e}_{\phi}=-
\dot{\phi}(\sin\theta e_r+\cos\theta e_{\theta})$

---



・

# 単一ばね

## 一次元

・自然長$l_0$に対して、$x(t)=l_0+c_1\cos(\omega t+\phi),\quad\omega=\sqrt{\frac{k}{m}}$

---

### 抵抗があるとき

・質量 $m$、角振動数 $\omega>0$、抵抗係数 $\gamma>0$ とする。
このとき、運動方程式：
$$m\ddot{x}=-m\omega^2x-2m\gamma\dot{x}$$

    ・なんかうまくラグランジアン書けない...
    ・ばね定数について、ω=√(k/m)
<br>  

- 一般解：
$$x(t)=C_1e^{\lambda t}+C_2e^{-\lambda t}\\\ \\
\lambda=-\gamma+\sqrt{\gamma^2-\omega^2}$$

#### $γ$ が小さいとき

・一般解：
$$x(t)=e^{-\gamma t}(C_1\cos\alpha t+C_2\sin\alpha t)\\\ \\
\alpha=\sqrt{\omega^2-\gamma^2}>0$$

#### $γ$ が大きいとき

・一般解：
$$x(t)=e^{-\gamma t}(C_1e^{\alpha t}+C_2e^{-\alpha t})\\\ \\
\alpha=\sqrt{\gamma^2-\omega^2}>0$$

#### $γ=ω$

・一般解：
$$x(t)=e^{-\gamma t}(C_1t+C_2)\\\ \\$$

---

## 二次元

## 自然長距離 $l_0$ に束縛されているとき

・解くべき方程式：$\frac{d^2x}{dt^2}=-\frac{kx}{m}(1-\frac{l_0}{\sqrt{x^2+l_0^2}})$

---

・振動解：$|x|<<l_0$

→解くべき方程式：$\frac{d^2x}{dt^2}=-\omega x^3,\quad\omega=\frac{k}{2ml_0^2}$

    ・ワイエルシュトラスの楕円関数？

---

# 複数ばね

## 一次元



---

# 振り子

## 単振り子

・質量 $m$、振り子の長さ $l$ とする。
このとき、ラグランジアン $L$：
$$L(\theta,\dot{\theta})=\frac{l^2\dot{\theta}^2}{2}+mgl\cos\theta$$
したがって、EL方程式：
$$\ddot{\theta}=-\frac{g}{l}\sin\theta$$

---

### 微小振動

・質量 $m$、振り子の長さ $l$ とする。
このとき、ラグランジアン $L$：
$$L(\theta,\dot{\theta})=\frac{ml^2\dot{\theta}^2}{2}-\frac{mgl}{2}\theta^2$$
したがって、EL方程式：
$$\ddot{\theta}=-\frac{g}{l}\theta\\\ \\
$$
特に、これは一般の場合のラグランジアン、EL方程式両方に整合する。

    ・整合については、定数項無視できる。
<br>

- 一般解：
$$\theta(t)=C_1\cos\omega t+C_2\sin\omega t\\\ \\
\omega=\sqrt{\frac{g}{l}}$$

---

## 空気抵抗

・

---

## 強制振動



---

# 円錐振り子

・質量 $m$、振り子の長さ $l$ とする。
このとき、ラグランジアン $L$：
$$L(\theta,\dot{\theta},\dot{\phi})=\frac{l^2\dot{\theta}^2}{2}+mgl\cos\theta$$
したがって、EL方程式：
$$\ddot{\theta}=-\frac{g}{l}\sin\theta$$


## Borda振り子

・

## 剛体振り子




