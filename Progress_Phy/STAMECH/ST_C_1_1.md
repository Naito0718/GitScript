
- [気体分子運動論の分布関数を無視した導出](#気体分子運動論の分布関数を無視した導出)
- [基本原理の導出的な](#基本原理の導出的な)
  - [分配関数](#分配関数)
  - [逆温度 $β$](#逆温度-β)
- [考え方](#考え方)
  - [熱平衡状態](#熱平衡状態)
  - [状態数](#状態数)
  - [速度分布関数](#速度分布関数)



# 気体分子運動論の分布関数を無視した導出


# 基本原理の導出的な

## 分配関数

・大きな熱浴 $H$、それに接している系 $S$、全系 $T$ とし、平衡状態にあるとする。また、全系のエネルギー $T_0\pm\Delta$、エネルギー $H_r$ の単位エネルギー幅近傍の状態数 $\eta(H_r)$ とする。
このとき、$P(E_r)\sim\eta(T_0-E_r)2\Delta$
したがって
$$\frac{P(E_r)}{P(E_r')}=\frac{\eta(T_0-E_r)}{\eta(T_0-E_r')}=e^{\log\eta(T_0-E_r)-\log\eta(T_0-E_r')}$$

    ・熱浴のエネルギー準位 H_i、系のエネルギー準位 E_j とすると、常に H_i>>E_j
<br>

- $\frac{d}{dE}(\log\circ\eta)(E)$ が $E_0$ 周りで一定 $(=\beta)$ ならば、
$$\frac{P(E_r)}{P(E_r')}\sim e^{-\beta(E_r-E_{r'})}$$
すなわち $P(E_r)\sim e^{-\beta E_r}$ で、規格化すると基本原理に近づく。

---

## 逆温度 $β$

<dl><dt>

・独立した系 $S_A,S_B$、取りうるエネルギー準位 $A_i,A_j$ とし、$S_A$ と $S_B$ を接触させる。ここで、全系 $S_T$ のエネルギー $T_{ij}=A_i+B_j$ とする。
このとき、
$$P_T(T_k)=\frac{e^{\beta_T}A_i}{\sum e^{-\beta_TA_i}}\frac{e^{\beta_T}B_j}{\sum e^{-\beta_TB_j}}\\\ \\$$


</dt><dd>

- $S_A$ が $A_i$ にある確率 $P(A_i)$、$S_B$ が $B_j$ にある確率 $P(B_j)$：
$$P_T(A_i)=\frac{e^{\beta_T}A_i}{\sum e^{-\beta_TA_i}}\\\ \\
P_T(B_i)=\frac{e^{\beta_T}B_j}{\sum e^{-\beta_TB_j}}$$
したがって、平衡状態にあるとき、系 $S_A,S_B$ は同じ $\beta_T$ を持つ。
ここで、$\beta$ を逆温度といい、温度：$\beta=\frac{1}{kT}$ という。

    ・k：ボルツマン定数。
    ・別に圧力とかの可能性もあったが、こう定義したらうまくいく。

</dd></dl>

# 考え方

## 熱平衡状態

・すべての早い現象が過ぎて、遅い現象がまだ起こっていないとき。

・熱平衡状態にある二つの系を一つとしてみた系も、また平衡状態にある。

---

## 状態数

・系が同じエネルギーを持つ状態の数。はちゃめちゃ多いが、現実なので有限！

---

## 速度分布関数



<dl><dt>

・速度分布関数 $f(v_x,v_y,v_z)$ ：
速度が $\bm{v}~\bm{v}+d\bm{v}$ の間にあるような粒子の数が
$$f(v_x,v_y,v_z)dv_xdv_ydv_z$$
で与えられるような $f$
<br>

    ・ある時間幅Δtとしたとき、変動する分子数の任意の時刻でのΔtでの平均が一定値fdvであると考える。
    ・幅を持たせることで、fがパルス的なふるまいをしないことを要請する。
<br>

</dt><dd>

- 系の全粒子数 $N$ とする。
このとき、
$$\int_{\bm{R}^3}f(\bm{v})d\bm{v}=N\\\ \\$$

    ・系の大きさは有限だが、速度はその限りではない。
<br>

- $f$ は各変数について偶関数、すなわち
$$f(v_x,v_y,v_z)=f(-v_x,v_y,v_z)$$
などが成り立つ。
<br>

    ・空間の等方性による。


</dd></dl>