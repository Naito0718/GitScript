# 量子力学

・ブラケット記法の意味

    ・並進、回転、時間発展は物理的空間全体を変換する→どんな系でも有効！
    ・基本位置空間で考えたいが、運動量空間、スピン空間で考えたり、基底をちょっと変えてみたりしたいことがある→ヒルベルト空間は抽象的で、系の自由度を決めて初めて空間の次元が定まる！
    ・内積で波動関数になるのは、|x>が連続固有値だから！

・波動関数 $\psi(x)$ は位置固有ケット $\ket{x}$ のフーリエ係数

→平行移動演算子は

## 状態$\ket{\alpha}$、演算子$A$

・交換関係
・不確定性関係

    ・時間に依存しないことに注意

・演算子の次元が合わないやつはテンソルで表現する？固有値がうまくいきそう

---

## 位置演算子、運動量演算子

##### 位置演算子 $x$

・$[x_i,x_j]=0$

---

##### 平行移動演算子 $\mathcal{J}(x')$ と運動量演算子 $p$

・微小平行移動：$\mathcal{J}(dx')=1-i\frac{p_i}{\hbar}dx'_i$

→$\mathcal{J}(dx')\ket{x}=\ket{x+dx'}$

→$\bra{x'}\mathcal{J}(dx')\ket{\alpha}=\braket{x'-dx'|\alpha}$

→$\mathcal{J}(dx')^{\dag}\mathcal{J}(dx')=\mathcal{J}(dx')\mathcal{J}(dx')^{\dag}=1$

→$\mathcal{J}(-dx')=\mathcal{J}(dx')^{-1}$

→$\mathcal{J}(dx')\mathcal{J}(dx'')=\mathcal{J}(dx'')\mathcal{J}(dx')=\mathcal{J}(dx'+dx'')$

---

・交換関係：$[x_i,\mathcal{J}(dx'_j)]=dx_j\delta_{ij}$

→$[x_i,p_j]=i\hbar\delta_{ij}$

→$\braket{(\Delta x_i)^2}\braket{(\Delta p_i)^2}\ge\hbar^2/2$

→$[p_i,p_j]=0$

→$[p_i,\mathcal{J}(dx'_j)]=0$
特に、$\mathcal{J}(dx)\ket{p}=(1-\frac{ip_i}{\hbar}dx'_i)\ket{p}$

---

・有限平行移動：$\mathcal{J}(\Delta x_i)=\exp(-\frac{ip_i}{\hbar}\Delta x_i)$


---

##### 波動関数 $\psi(x)$ による表現



---

## 時間依存しないハミルトニアン $H$

##### 時間発展演算子 $\mathcal{U}(t,t_0)$

・シュレディンガー方程式



・シュレディンガー表示とハイゼンベルグ表示

    ・状態が時間発展するか、演算子が時間発展するか
    ・不確定性関係はハイゼンベルグ表示のとき分かりやすい！

### 波動関数表示

    ・すべてL^2(X)の元、すなわち有限値しかとらないし、積分も有限

・解くべき方程式
$$\left(-\frac{\hbar^2}{2m}\Delta+V(x)\right)\phi(x)=E\phi(x)\\\ \\
\psi(x,t)=\phi(x)e^{-i\frac{E}{\hbar}t}$$

→フラックス

→確率密度が時間変化しないこと

    ・定常状態

##### 束縛状態

→$\lim_{|x|\to\infty}|\phi(x)|=0$

---

・$V(r)\le V_0$ならば、$E>V_0$

→$\nabla\phi(r)\neq0$

    ・発散しない

→$\braket{E}=E,\ \braket{T}>0,\ \braket{V}\ge V_0$

---

・このとき、取りうる$E$の値は離散的

    ・偏微分方程式論による

### 曲線座標での波動関数表示

---

## 角運動量 $J$

##### 微小回転$R(\epsilon_0),R(\epsilon)$

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

##### 微小回転演算子と角運動量
$$\mathcal{D}(n,d\phi)=1-i\left(\frac{J\cdot n}{\hbar}\right)d\phi$$

    ・x×pと定義するわけではない！後で特別な場合に一致するのを見る

・$D_n(\phi)=\exp(\frac{-iJ\cdot n\phi}{\hbar})$
→ $D_{n_1}(\phi_1)D_{n_2}(\phi_2)=D_{n_3}(\phi_3)$
→ $(D_{n_1}(\phi_1)D_{n_2}(\phi_2))D_{n_3}(\phi_3)=D_{n_1}(\phi_1)(D_{n_2}(\phi_2)D_{n_3}(\phi_3))$
→ $D_{x_i}(d\phi_1)D_{x_j}(d\phi_2)=\epsilon_{ijk}(D_{x_k}(d^2\phi_3)-1)$

---

・正準交換関係：$[J_i,J_j]=\epsilon_{ijk}i\hbar J_kS$


---


