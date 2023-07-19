# 力学系の計算、具体例

##### 正準変換

・正準変換$$\begin{pmatrix}Q \\ P\end{pmatrix}=   \
\begin{pmatrix}a & b \\ c & d\end{pmatrix}\begin{pmatrix}q \\ p\end{pmatrix}    \\
$$
$\det A=1,b\neq0$
母関数$F(q,Q)=\frac{1}{b}\frac{q}{Q}-\frac{1}{2b}(aq^2+dQ^2)$

---

## 座標系

##### 三次元極座標

・$x=re_r,\ \dot{x}=\dot{r}e_r+r\dot{\theta}e_\theta+r\dot{\phi}\sin\theta e_{\phi},\\\ \\ 
\ddot{x}=e_r(\ddot{r}-r\dot{r}^2+r\dot{\phi}^2\sin^2\theta)+e_{\theta}(r\ddot{\theta}+2\dot{r}\dot{\theta}-r\dot{\phi}^2\sin\theta\cos\theta)+e_{\phi}(2\dot{r}\dot{\phi}\sin\theta+2r\dot{\theta}\dot{\phi}\cos\theta+r\ddot{\phi}\sin\theta)$

→$\dot{e}_r=\dot{\theta}e_{\theta}+\dot{\phi}\sin\theta e_{\phi},\ \dot{e}_{\theta}=-\dot{\theta}e_{r}+\dot{\phi}\cos\theta e_{\phi},\ \dot{e}_{\phi}=-
\dot{\phi}(\sin\theta e_r+\cos\theta e_{\theta})$

---

## 振り子

### 単振り子

・

### 空気抵抗

・

##### Borda振り子

・

##### 剛体振り子

・

## ばね

##### 単純ばね

・

## 万有引力

##### 質点$M$の周りを質点$m$が外力なしで回っているとき

・系のラグランジアン：$L(r,\dot{r},\theta)=\frac{m}{2}(r^2+(r\dot{\theta})^2)+\frac{mMG}{r}$

→解くべき方程式：
$$\frac{d}{dt}(r^2\dot{\theta})=0\\\ \\
\frac{d}{dt}\dot{r}=-\frac{mMG}{r^3}+mr\dot{\theta}$$

→系の角運動量の保存：$\frac{dL}{dt}=0$
よって、運動は面内

    ・運動方程式から導出

##### 球対称な密度分布


