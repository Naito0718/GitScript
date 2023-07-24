# テンソル解析

## 基礎

・性質
$(a_{ij}+a_{ji})x_ix_j=2a_{ij}x_ix_j$

---

・注意
$a_{ij}(x_i+y_j)\neq a_{ij}x_i+a_{ij}y_j$
$(a_{ij}+a_{ji})x_iy_j\neq 2a_{ij}x_iy_j$

    ・両辺で添え字の動く範囲が変わる

---

・行列表記$[a^i_j]_{mn},[a^{ij}]_{mn}$

    上付き添え字が行

---

## テンソル

##### 一階

・反変テンソル： $\bar{T}^i=T^r\frac{\partial\bar{x}^i}{\partial x^r}$

    ・変換はC^2とする

→加重反変テンソル：$\bar{T}^i=wT^r\frac{\partial\bar{x}^i}{\partial x^r}$

→共変テンソル：$\bar{T}_i=T_r\frac{\partial x^r}{\partial \bar{x}^i}$

##### 二階

・二階反変テンソル：
$$\bar{T}^{ij}=T^{rs}\frac{\partial\bar{x}^i}{\partial x^r}\frac{\partial\bar{x}^j}{\partial x^s}$$

→二階共変テンソル：
$$\bar{T}_{ij}=T_{rs}\frac{\partial x^r}{\partial \bar{x}^i}\frac{\partial x^s}{\partial \bar{x}^j}$$

→二階混合テンソル
$$\bar{T}^i_{j}=T^r_{s}\frac{\partial \bar{x}^i}{\partial x^r}\frac{\partial x^s}{\partial \bar{x}^j}$$

---

・ヤコビアン：
$$J=\left(\frac{\partial\bar{x}_i}{\partial x_j}\right)$$

→$\bar{J}J=I$

→二階の反変テンソル $T$ に対して、$\bar{T}=JTJ^T$

→二階の共変テンソル $U$ に対して、$\bar{U}=(\bar{J})^TU\bar{J}$

---

・二階反変テンソル $T^{ij}$に対して、$T^{ir}T_{rj}=\delta_{ij}$ なる $T_{ij}$が存在するとき、 $\bar{T}^{ir}U_{rj}$ なる二階テンソル $U_{ij}$が存在し、$U_{ij}=\bar{T}_{ij}$


→二階反変テンソル $T^{ij}$に対して、$T^{ir}T_{rj}=\delta_{ij}$ なる $T_{ij}$が存在するとき、 $T_{ij}$は共変テンソル

    ・二階共変テンソル $U_{ij}$ の場合も同様
    ・U^{-1}=JU^{-1}J^Tのこと
---

##### 高階

・$p$ 階反変 $q$ 階共変テンソル：
$$\bar{T}^{i_1...i_p}_{j_1...j_q}=T^{r_1...r_p}_{s_1...s_q}\frac{\partial \bar{x}^{i_1}}{\partial x^{r_1}}\frac{\partial \bar{x}^{i_2}}{\partial x^{r_2}}...\frac{\partial \bar{x}^{i_p}}{\partial x^{r_p}}\frac{\partial x^{s_1}}{\partial \bar{x}^{j_1}}\frac{\partial x^{s_q}}{\partial \bar{x}^{j_q}}$$

---

・不変量：座標変換で不変な量

→任意の $n$ 階反変テンソル $T$ と $n$ 階共変テンソル $U$ に対して、$T^{i_1...i_n}U_{i_1...i_n}=E$は不変量

    ・一階なら内積、二階ならTr

