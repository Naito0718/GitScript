
- [$R^3$ における回転](#r3-における回転)
  - [外積](#外積)
  - [基底変換](#基底変換)
  - [軸周りの回転](#軸周りの回転)
    - [座標軸回りの回転](#座標軸回りの回転)
- [$R^3$ における微小回転](#r3-における微小回転)
  - [微小回転行列](#微小回転行列)
  - [三次元極座標における微小回転行列](#三次元極座標における微小回転行列)
  - [ある軸周りの微小回転](#ある軸周りの微小回転)
  - [二次までの微小回転行列](#二次までの微小回転行列)
- [曲線の直線対称移動](#曲線の直線対称移動)



# $R^3$ における回転

## 外積

・$\bm{a},\bm{b}\in\bm{R}^3$ とする。
このとき、
$$\bm{a}\times\bm{b}=\begin{pmatrix}
0 & -a_3 & a_2 \\
a_3 & 0 & -a_1 \\
-a_2 & a_1 & 0\\
\end{pmatrix}\bm{b}$$
ここで、$\tilde{a}=\begin{pmatrix}
0 & -a_3 & a_2 \\
a_3 & 0 & -a_1 \\
-a_2 & a_1 & 0\\
\end{pmatrix}$ は反対称行列。
<br>

- 
$$\bm{d}\bm{d}^T-\tilde{d}^2=\begin{pmatrix}
|\bm{d}|^2 & 0 & 0 \\
0 & |\bm{d}|^2 & 0 \\
0 & 0 & |\bm{d}|^2 \\  
\end{pmatrix}\\\ \\$$

- $$\tilde{d}\bm{d}\bm{d}^T=\bm{d}\bm{d}^T\tilde{d}=0$$


---

## 基底変換

・$\bm{a}\in\bm{R}^3,\ \bm{a}=\sum a_i\bm{e}^{i}=\sum a'_{i}\bm{n}^i$ とする。
このとき、$\begin{pmatrix}\bm{n}^1 & \bm{n}^2 & \bm{n}^3\end{pmatrix}\in SO(3)$ であって、
$$\begin{pmatrix} a_1 \\ a_2 \\ a_3\end{pmatrix}=\begin{pmatrix}\bm{n}^1 & \bm{n}^2 & \bm{n}^3\end{pmatrix}\begin{pmatrix} a'_1 \\ a'_2 \\ a'_3\end{pmatrix}$$

---

## 軸周りの回転

    ・回転軸は常に存在する。GL(n,C)_4_1参照。
<br>

・$\bm{a},\bm{b}\in\bm{R}^3,\ |a|=|b|$ とする。
このとき、回転軸 $\bm{d}$、回転角 $\theta$ で $a$ が $b$ に回転したと考えると、
$$\bm{b}=(\cos\theta I+(1-\cos\theta)dd^T+\sin\theta\tilde{d})\bm{a}$$
さらに、
$$\cos\theta I+(1-\cos\theta)dd^T+\sin\theta\tilde{d}\in SO(3)\\\ \\$$

- $R\in SO(3)$ とする。
このとき、
$$\bm{d}=\frac{1}{\sqrt{4-(\mathrm{tr}R-1)^2}}\begin{pmatrix} R_{32}-R_{23} \\ R_{13}-R_{31} \\ R_{21}-R_{12} \end{pmatrix},\quad d_i=-\frac{\epsilon_{ijk}}{\sqrt{4-(\mathrm{tr}R-1)^2}}R_{jk}$$
と定めると、$\bm{d}$ は $R$ の軸

<br>

- $\bm{a},\bm{b}\in\bm{R}^3,\ |a|=|b|$ とする。
このとき、$$R=2\frac{(\bm{a}+\bm{b})(\bm{a}+\bm{b})^T}{(\bm{a}+\bm{b})^T(\bm{a}+\bm{b})}-I$$
と定めると、これは

    ・直交行列かつb=Ra？

---

### 座標軸回りの回転

・$R\in SO(3)$ とする。
このとき、
$$R\text{ が }z\text{ 軸周りの回転}\iff\exist\theta\in[0,2\pi)\text{ であって、}R=\begin{pmatrix}
\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0 \\
0 & 0 & 1 \\
\end{pmatrix}\\\ \\
R\text{ が }x\text{ 軸周りの回転}\iff\exist\theta\in[0,2\pi)\text{ であって、}R=\begin{pmatrix}
1 & 0 & 0 \\
0 & \cos\theta & -\sin\theta \\
0 & \sin\theta & \cos\theta \\
\end{pmatrix}\\\ \\
R\text{ が }y\text{ 軸周りの回転}\iff\exist\theta\in[0,2\pi)\text{ であって、}R=\begin{pmatrix}
\cos\theta & 0 & -\sin\theta \\
0 & 1 & 0 \\
\sin\theta & 0 & \cos\theta \\
\end{pmatrix}\\\ \\$$

    ・基底ベクトルを並べればよい。y方向は計算してみれば分かる。

---

# $R^3$ における微小回転

## 微小回転行列


<dl><dt>

・微小回転行列 $E+\epsilon$ とする。ただし、$E+\epsilon\in SO(3)$ を要請する。
<br>

</dt><dd>

- 微小回転行列の逆も再び微小回転行列であることを要請する。
このとき、
$$(E+\epsilon)^{-1}=E-\epsilon\\\ \\
\epsilon^T=-\epsilon$$
したがって、$$\exist\bm{\epsilon}\in\bm{R}^3\text{ であって、}\epsilon=\tilde{\bm{\epsilon}}$$

- 
$$(E+\epsilon)\bm{\epsilon}=\bm{\epsilon}\\\ \\
\forall \bm{r}\in \bm{R}^3\text{ に対して、}\begin{pmatrix} 0 \\ 0 \\ \epsilon_3\end{pmatrix}\times \bm{r}=\begin{pmatrix} -\epsilon y \\ \epsilon_3 x \\ 0 \end{pmatrix}$$
したがって、$\bm{\epsilon}$ は回転軸であって、各 $\epsilon_i$ は 座標軸 $x^i$ に対して、反時計回りに $\tan^{-1}\epsilon_i=\epsilon_i$ 回転させる。
また、外積の線形性より、任意の微小回転は各座標軸に分解して考えることができ、$|\epsilon|$ を微小回転の大きさとしても一般性を失わない。
<br>

- 微小回転行列 $E+\epsilon^1,\ E+\epsilon^2$ とする。
このとき、
$$(E+\epsilon_2)(E+\epsilon_1)=E+\epsilon_1+\epsilon_2\\\ \\$$
したがって、続けて微小回転させるときは、微小回転の和で表せる。
<br>


</dd></dl>

---

## 三次元極座標における微小回転行列

<dl><dt>

・
$$\bm{r}=(x,y,z)=(r\sin\theta\cos\phi,r\sin\theta\sin\phi,r\cos\theta)$$
とする。
このとき、極座標微小変換 $\mathcal{D}$：
$$\mathcal{D}:[0,\infty)\times[0,\pi]\times[0,2\pi)\to\bm{R}^3\\\ \\
\mathcal{D}(r,\theta,\phi)=(r+a\epsilon,\theta+b\epsilon,\phi+c\epsilon)$$
とし、変換後の位置 $\bm{r}'$ とすると、
$$x'=x+\epsilon\left(\frac{a}{r}x-cy+b\cos\phi z\right)\\\ \\
y'=y+\epsilon\left(cx+\frac{a}{r}y+b\sin\phi z\right)\\\ \\
z'=z+\epsilon(-br\sin\theta+a\cos\theta)\\\ \\$$

</dt><dd>

- 
$$\mathcal{D}\text{ が }z\text{ 軸に関しての微小回転}\iff a=0,b=0$$
であって、
$$\bm{r}'=(x-y\epsilon',y+x\epsilon',z)\\\ \\$$
ここで、$c$ は任意の実数でよいので、$\epsilon'=c\epsilon$ として一般性を失わない。
<br>

- $$\mathcal{D}\text{ が }x\text{ 軸に関しての微小回転}\iff a=0,\ \frac{c}{b}=\frac{\cos\theta\cos\phi}{\sin\theta\sin\phi}\\\ \\
\mathcal{D}\text{ が }y\text{ 軸に関しての微小回転}\iff a=0,\ \frac{c}{b}=-\frac{\cos\theta\sin\phi}{\sin\theta\cos\phi}\\\ \\$$
であって、
$$\bm{r}'_x=\left(x,y+\epsilon\frac{b}{\sin\phi}z,z-\epsilon\frac{b}{\sin\phi}y\right)\\\ \\
\bm{r}'_y=\left(x+\epsilon\frac{b}{\cos\phi}z,y,z-\epsilon\frac{b}{\cos\phi}x\right)$$
特に、陽に $\phi$ が現われないことと、$z$ 軸微小回転の時との対応を考えると、
$$b_x=-\sin\phi,\ b_y=\cos\phi\\\ \\
\bm{r}'_x=\left(x,y-\epsilon z,z+\epsilon y\right)\\\ \\
\bm{r}'_y=\left(x+\epsilon z,y,z-\epsilon x\right)$$


</dd></dl>

---

## ある軸周りの微小回転

<dl><dt>

・回転角 $\omega$、回転軸方向の単位ベクトル $\bm{n}$ とする。
このとき、回転ベクトル $\bm{\omega}$：
$$\bm{\omega}=\omega\bm{n}\\\ \\$$

</dt><dd>

- 


- $$\mathcal{D}\text{ が }x\text{ 軸に関しての微小回転}\iff a=0,\ \frac{c}{b}=\frac{\cos\theta\cos\phi}{\sin\theta\sin\phi}\\\ \\
\mathcal{D}\text{ が }y\text{ 軸に関しての微小回転}\iff a=0,\ \frac{c}{b}=-\frac{\cos\theta\sin\phi}{\sin\theta\cos\phi}\\\ \\$$
であって、
$$\bm{r}'_x=\left(x,y+\epsilon\frac{b}{\sin\phi}z,z-\epsilon\frac{b}{\sin\phi}y\right)\\\ \\
\bm{r}'_y=\left(x+\epsilon\frac{b}{\cos\phi}z,y,z-\epsilon\frac{b}{\cos\phi}x\right)$$
特に、陽に $\phi$ が現われないことと、$z$ 軸微小回転の時との対応を考えると、
$$b_x=-\sin\phi,\ b_y=\cos\phi\\\ \\
\bm{r}'_x=\left(x,y-\epsilon z,z+\epsilon y\right)\\\ \\
\bm{r}'_y=\left(x+\epsilon z,y,z-\epsilon x\right)$$


</dd></dl>


## 二次までの微小回転行列

$$\bm{R(\epsilon_0),R(\epsilon)}$$

→ 任意の軸周りの一次の微小回転行列$R(\epsilon_0)$は交換する
→ 任意の軸周りの回転行列$R(\theta)$に対して、$R(0)=I$
→ $$R_z(\epsilon)= \
\begin{pmatrix} \
1-\frac{\epsilon^2}{2} & -\epsilon & 0 \\   \
\epsilon &  1-\frac{\epsilon^2}{2} & 0 \\   \
 0 & 0 & 1   \
\end{pmatrix},\quad R_x(\epsilon)\
\begin{pmatrix} \
1 & 0 & 0 \\   \
0 &  1-\frac{\epsilon^2}{2} & -\epsilon \\   \
 0 & \epsilon & 1-\frac{\epsilon^2}{2}   \
\end{pmatrix},\quad R_y(\epsilon)\\
\begin{pmatrix} \
1-\frac{\epsilon^2}{2} & 0 & \epsilon \\   \
0 &  1 & 0 \\   \
 -\epsilon & 0 &  1-\frac{\epsilon^2}{2}  \
\end{pmatrix},\quad \\$$
→ $[R_x(\epsilon),R_y(\epsilon)]=R_z(\epsilon^2)-R(0)$

---

# 曲線の直線対称移動

・$f(x)$ を $y=\tan\theta x+b$ で対称移動させる：
$$f(x)-b\text{ を、}\frac{\pi}{2}-\theta\text{ 回転}\Rightarrow y\text{ 軸対称変換 }\Rightarrow\theta-\frac{\pi}{2}\text{ 回転}$$
