# テンソル解析

## 基礎

・性質
$(a_{ij}+a_{ji})x_ix_j=2a_{ij}x_ix_j$


・注意
$a_{ij}(x_i+y_j)\neq a_{ij}x_i+a_{ij}y_j$
$(a_{ij}+a_{ji})x_iy_j\neq 2a_{ij}x_iy_j$

    ・両辺で添え字の動く範囲が変わる

・行列表記$[a^i_j]_{mn},[a^{ij}]_{mn}$

    上付き添え字が行

#### 二階のテンソル $a_{ij}$

・$y^i=a^{ij}x_j$に対して、$b_{ir}a^{rj}=\delta_{ij}$なる二階テンソル$b_{ir}$が存在すれば、$x_i=b_{ir}y^{r}$

##### 二次形式 $Q=a_{ij}x_ix_j$

・$x_i=b_{ij}y_j$を代入すると、$Q=(g_{ij}b_{ir}b_{jl})y_ry_l$

・$\frac{\partial}{\partial x_k}Q=(a_{ij}+a_{ji})x_i$
$\frac{\partial^2}{\partial x_k\partial x_l}Q=a_{lk}+a_{kl}$

##### 交代テンソル $a_{ij}=-a_{ij}$

・$a_{ij}x_ix_j=0$

##### 対称テンソル $a_{ij}=a_{ij}$

---

## 
