# テンソル解析的な具体例と計算例

## 二階のテンソル $a_{ij}$

→ $y^i=a^{ij}x_j$に対して、$b_{ir}a^{rj}=\delta_{ij}$なる二階テンソル$b_{ir}$が存在すれば、$x_i=b_{ir}y^{r}$

→ $\det (A_{ij})_{n}=e_{i_1,...,i_n}a_{1i_1}...a_{ni_n}$

→ $(u\times v)_i=e_{ijk}x_jy_k$

---

##### 二次形式 $Q=a_{ij}x_ix_j$

・$\bar{x}=Ax$に対して、$Q=(g_{ij}b_{ir}b_{jl})\bar{x}_r\bar{x}_l\quad(B=A^{-1})$

---

・微分：$\frac{\partial}{\partial x_k}Q=(a_{ij}+a_{ji})x_i$

→ $\frac{\partial^2}{\partial x_k\partial x_l}Q=a_{lk}+a_{kl}$

---

##### 交代テンソル $a_{ij}=-a_{ij}$

・$a_{ij}x_ix_j=0$

---

##### 対称テンソル $a_{ij}=a_{ij}$

---

##### 距離

・$\bar{x}=Ax$のとき、$d(x,y)=\sqrt{g_{ij}\bar{\Delta \bar{x}_i}\Delta\bar{x}_j}\quad(G=(AA^T)^{-1},\Delta\\bar{x_i}=x_i-y_i)$

---

## $(p,q)$テンソル

##### 接ベクトル：$T^i=\frac{dx^i}{dt}\quad(x^i=x^i(t))$

・接ベクトル場は一階反変テンソル

##### 勾配：$\nabla F\quad(F{はスカラー場})$

・$\bar{F}(\bar{x})=F\circ x(\bar{x})$

→勾配は一階共変テンソル

---

・$$E=\frac{dx^r}{dt}(\nabla F)_r=\frac{dF}{dt}$$
は不変量

