# 微分方程式と物理シミュレーション

## 常微分方程式

#### $s$段ルンゲクッタ法
$$y_{n+1}=y_n+h\sum_{i=1}^sb_ik_i\\\ \\
k_i=f(t_n+hc_i,y_n+h\sum_{j=1}^sa_{ij}k_j)$$
ここで、近似値 $y_{n+1}$ を $y_n$ から計算するときに発生する誤差の大きさが $O(h^{p+1})$ のとき、そのルンゲ゠クッタ公式は $p$ 次精度を持つという。

・付加条件
→陽的ルンゲクッタ法：$(a_{ij})$の上三角と対角部分$=0$
→一貫性？：$\sum_ja_{ij}=c_i$

→ブッチャー配列
$\left(
\begin{array}{c:}
   c_1 & a_{11} & a_{12} & \cdots & a_{1s} \\ 
   c_2 & a_{21} & a_{22} & \cdots & a_{2s} \\ 
   \vdots & \vdots & \vdots & \ddots \\ 
   c_s & a_{s1} & a_{s2} & \cdots &a_{ss} \\ \hline 
    & b_1 & b_2 & \cdots & b_s
\end{array}
\right)$

---

・解くべき方程式：
$$\sum_i^s b_i\frac{dk_i}{d_h}|_{h=0}=\frac{1}{m+1}\frac{d^m}{dx^m}f(x_n,y_n(x_n))\quad(m=0,...,s-1)$$

→$\sum b_i=1$

→$k_1=f(t_n,y_n)$
→$k_2=f(t_n+c_2h,y_n+c_2hk_1)$



---

##### 一段一次：$a_{11}=c_1=0,b_1=1$

→オイラー法：$y_{n+1}=y_n+hf(t_n,y_n)$

---

##### 二段二次：
$$\left(
\begin{array}{c:}
    0 & 0 &   \\ 
   \alpha & \alpha & 0 \\ \hline 
    & 1-\frac{1}{2\alpha} & \frac{1}{2\alpha} & 
\end{array}
\right)$$

・修正オイラー法
$$y_{n+1}=y_n+k_2,\quad k_2=hf(t_n+\frac{h}{2},y_n+\frac{k_1}{2})\\\ \\
k_1=hf(t_n,y)\\\ \\(h:{時間刻み幅})$$

---

##### 四段四次：
$\left(
\begin{array}{c:}
   0 & 0 &  &  &  \\ 
   a_{21} & a_{21} & 0 &  &  \\ 
   c_3 & a_{31} & a_{32} &  \\ 
   c_4 & a_{41} & a_{42} & a_{43} &0 \\ \hline 
    & b_1 & b_2 & b_3 & b_4
\end{array}
\right)$

・ルンゲクッタ法
$$\left(
\begin{array}{c:}
   0 & 0 &  &  &  \\ 
   1/2 & 1/2 & 0 &  &  \\ 
   1/2 & 0 & 1/2 &  \\ 
   1 & 0 & 0 & 1 &0 \\ \hline 
    & 1/6 & 1/3 & 1/3 & 1/6
\end{array}
\right)$$

---

##### 精度評価としてのエネルギー保存則

## ウェーブレット

---

## 離散的非線形系

##### ロジスティック写像

---

## 連続的非線形系

##### 相空間、カオス

---



## 偏微分方程式

#### 二次元Poisson方程式

・解くべき方程式：$U^{next}_{ij}=\frac{1}{4}(U_{i+1,j}+U_{i-1,j}+U_{i,j+1}+U_{i,j-1}-f_{ij}h^2)$

- $\Delta t=\frac{h^2}{4}$ なる熱伝導方程式

##### ヤコビ法

    ・一度ループを終えるまで右辺の値のみU_{ij}を更新しない

##### ガウス-ザイデル法

    ・ループ中に右辺のすでに計算した値U_{i-1,j},U_{i,j-1}を更新する

##### 逐次緩和法（SOR）

・解くべき方程式：$U^{next}_{ij}=(1-\omega)U_{ij}+\frac{\omega}{4}(U_{i+1,j}+U^{next}_{i-1,j}+U_{i,j+1}+U^{next}_{i,j-1}-f_{ij}h^2)$

→ $\Delta t=\frac{\omega h^2}{4},\quad\omega=1~3
$

##### 有限要素法



