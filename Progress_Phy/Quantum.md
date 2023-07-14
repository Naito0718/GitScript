# 量子力学

## 状態や演算子の性質

・交換関係
・不確定性関係

    ・時間に依存しないことに注意

・演算子の次元が合わないやつはテンソルで表現する？固有値がうまくいきそう

---

## ハミルトニアン $H$

##### 時間発展演算子 $\mathcal{U}(t,t_0)$

・シュレディンガー方程式



・シュレディンガー表示とハイゼンベルグ表示

    ・状態が時間発展するか、演算子が時間発展するか
    ・不確定性関係はハイゼンベルグ表示のとき分かりやすい！

##### シュレディンガー方程式

・

---

## 角運動量 $J$

##### 微小回転$R(\epsilon_0),R(\epsilon)$

・任意の軸周りの一次の微小回転行列$R(\epsilon_0)$は交換する
・任意の軸周りの回転行列$R(\theta)$に対して、$R(0)=I$
・$$R_z(\epsilon)= \
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
・$[R_x(\epsilon),R_y(\epsilon)]=R_z(\epsilon^2)-R(0)$

##### 微小回転演算子 $\mathcal{D}(n,d\phi)=1-i(\frac{J\cdot n}{\hbar})d\phi$

    ・x×pと定義するわけではない！後で特別な場合に一致するのを見る

・$D_n(\phi)=\exp(\frac{-iJ\cdot n\phi}{\hbar})$
$D_{n_1}(\phi_1)D_{n_2}(\phi_2)=D_{n_3}(\phi_3)$
$(D_{n_1}(\phi_1)D_{n_2}(\phi_2))D_{n_3}(\phi_3)=D_{n_1}(\phi_1)(D_{n_2}(\phi_2)D_{n_3}(\phi_3))$
$D_{x_i}(d\phi_1)D_{x_j}(d\phi_2)=\epsilon_{ijk}(D_{x_k}(d^2\phi_3)-1)$

・


---

## 自由粒子

・ポテンシャルなし（ハイゼンベルグ表示）

    ・古典粒子と同じ
    ・初期値とt秒後の位置に関する不確定性関係

・ポテンシャルあり（解析的関数）（ハイゼンベルグ表示）

    ・古典粒子と同じ、運動方程式、速度と運動量の関係
    ・期待値取ればシュレディンガー表示でも成り立つ（エーレンフェストの定理）

## 一次元

・縮退はない

## 一次元井戸ポテンシャル

・

## 一次元調和振動子

・演算子法

    ・ハミルトニアンH
    ・消滅演算子、生成演算子、個数演算子、H=hω(N+1/2)


## 外部磁場中にある電子（$1/2$スピン）

・
