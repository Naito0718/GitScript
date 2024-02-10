
- [Frechet空間から定まるFrechet空間](#frechet空間から定まるfrechet空間)
  - [閉部分空間](#閉部分空間)
  - [直積空間](#直積空間)



# Frechet空間から定まるFrechet空間

## 閉部分空間

・$\bm{R,C}$ 上Frechet空間 $V$、閉部分空間 $M\subset V$ とする。
このとき、
$$\mathcal{P}=\{p_n|_M\ |\ n\in\bm{N}\}$$
と定めると、これは高々可算なセミノルムの分離族。
よって、$M$ は自然にFrechet空間であって、この位相は相対位相と一致する。
<br>

    ・コーシー性は明らか。一致することは、結局距離考えればよい。
<br>

---

## 直積空間

・$\bm{R,C}$ 上Frechet空間 $V,W$、$p_{V,n}\in\mathcal{P}_V,\ p_{W,n}\in\mathcal{P}_{W,n}$ とする。
このとき、
$$p_{n,V,W}:V\times W\to[0,\infty)\\\ \\
p_n(x,y)=p_{V,n}(x)+p_{W,n}(y)\\\ \\
\mathcal{P}_{V,W}=\{p_{n,V,W}\ |\ n\in\bm{N}\}$$
と定めると、$p_{n,V,W}$ はセミノルムで、$\mathcal{P}$ は高々可算なセミノルムの分離族。
よって、$V\times W$ は自然にFrechet空間。
<br>

    ・コーシー性は明らか。
    ・セミノルムの番号は適当に同じにしないと、p_nが定義できない。
<br>

- $$\frac{1}{4}\left(\frac{p_{V,n}(x_1-x_2)+p_{W,n}(y_1-y_2)}{1+p_{V,n}(x_1-x_2)+p_{W,n}(y_1-y_2)}\right)\le \frac{1}{2}\left(\frac{p_{V,n}(x_1-x_2)}{1+p_{V,n}(x_1-x_2)}\right)+\frac{1}{4}\left(\frac{p_{W,n}(y_1-y_2)}{1++p_{W,n}(y_1-y_2)}\right)\\\ \\
\le \frac{p_{V,n}(x_1-x_2)+p_{W,n}(y_1-y_2)}{1+p_{V,n}(x_1-x_2)+p_{W,n}(y_1-y_2)}$$
したがって、平行移動不変距離 $d$ と直積位相距離 $d_{V\times W}$ は同値。
よって、この位相は直積位相と一致する。




