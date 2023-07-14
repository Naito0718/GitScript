# $\bm{R}^n$の幾何学



## $\bm{R}^2$

#### 平面曲線

・曲率 $\kappa(s)=|\gamma''(s)|$

曲率$\kappa(s)$が与えられたとき、$\theta(s)=\int_{s_0}^s\kappa(s') ds'$、$\gamma(s)=\int_{s_0}^sds'(\cos\theta(s'),\sin\theta(s'))$とすれば、これは与えられた曲率を持つ曲線


・回転数

## $\bm{R}^3$

#### 空間曲線

・曲率$\kappa=|(\dot p\times\ddot p)|/|\dot p|^3$、捩率$\tau$

    ・Frenet-Serretの公式
    ・曲率κと捩率τ等しい⇔回転と平行移動で重なる
    ・曲率κ非負ならば、捩率τ=0⇔曲線は平面に含まれる
    ・任意の関数τ(s)、非負関数κ(s)が与えられたとき、e_1,e_2,e_3の初期値が与えられればκ、τを曲率、捩率とする曲線が一意的に存在する

・回転数

・パラメータ表示$p(s)$

    ・κ=(p'')^{1/2}, τ=det(p',p'',p''')/κ^2

##### 常螺旋$p(t)=(a\cos t,a\sin t,ht)$
・弧長$s(t)=(a^2+h^2)^{\frac{1}{2}}t$
・曲率$\kappa=\frac{a}{a^2+h^2}$
・捩率$\tau=\frac{h}{a^2+h^2}$

#### 空間曲面