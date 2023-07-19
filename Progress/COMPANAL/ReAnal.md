# 実解析

## 一変数での広義積分

##### 広義積分

・関数$f:[a.b)\to\bm{R}$が $\forall[a,u]$ で可積分かつ $\int_a^{\to b}fdx\in \bm{R}$

    ・両側可積分は積分区間を分割する

→関数$f:[a.b)\to\bm{R}$が $\forall[a,u]$ で可積分ならば、
$\int_a^{\to b}fdx\in \bm{R}\iff\forall\epsilon>0{に対して}\exist c\in I{であって}c<v<u<b{ならば}|\int_v^uf(x)dx|<\epsilon$

---

・絶対収束：$|f|$が広義可積分なこと

→$\int fdx$が絶対収束するならば、$\int fdx$は収束する

→$|f(x)|\le g(x)$かつ広義可積分な$g(x)$が存在すれば、$\int|f(x)|dx\le\int g(x)dx$（絶対収束）

---

##### 収束判定

→関数$f:[a.b)\to\bm{R}$が $\forall[a,u]$ で可積分とする

・$b=\infty$ で $f(x)=O(x^{\alpha})(x\to\infty)$を$\alpha<-1$で満たすならば、$\int_a^{\infty}f(x)dx\in\bm{R}$

---

・$b\in\bm{R}$ で $f(x)=O((b-x)^{\alpha})(x\to -b)$を$\alpha>-1$で満たすならば、$\int_a^{\to b}f(x)dx\in\bm{R}$