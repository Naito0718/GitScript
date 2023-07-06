# 関数解析

##### ノルム空間

・和、スカラー倍（スカラーも点列）、ノルムは連続

    ・u_nが収束列ならCauchy列

##### 総和$\sum_{j\in J}x_j$

・定義

    ・集合Jに対して、その有限部分集合全体Fに集合の包含関係を入れたものは有向集合
    ・ネットx_λ:F→X, x_λ(F)=Σ_F x_λ
    ・有限部分集合$F$に対する和の、FをJに近づけていくときの極限

・性質

    ・総和が収束すれば、{j∊J|x_j≠0}は高々可算
    ・Σ_N x_nが収束すればΣ_n=1 x_nも収束する。（eventually性）逆は一般に成り立たない
    ・ノルム空間（ハウスドルフ）より、収束値を持てば一意的
    
・絶対収束$\sum_{j\in J}\|x_j\|<\infty$（非負実数値のネット）

    ・Banach空間で総和が絶対収束すれば、元の総和も収束する
___



##### 無限次元ベクトル空間の具体例

##### $C[a,b]$

・ノルム$\|u\|=sup|u(x)|$

    ・点列（関数列）の収束は一様収束と同値
    ・このノルムではBanach空間

・ノルム$\|u\|=\int|u(x)|$

    ・このノルムではBanach空間でない

#### $l^1$（絶対収束）

## ノルム環$X$（多元環かつ積の不等式、$X$はノルム空間）（resp.Banach）

・*-環$\ *:X\to X$（$X$は多元環）
    
    ・共役線形、積の反転、自身が逆を与える

・ノルム*-環$\ *:X\to X$（$X$は多元環）（resp.Banach）

    ・ノルム環かつ*-環で、*がノルムを保つ

・$C*$-環

    ・*-環かつBanach環で、|x* x|=|x|^2
    ・C*環ならばBanach*-環

## $L^p$空間

##### Holderの不等式、Minkowskiの不等式

・共役指数$1/p+1/q=1\ (p,q\in(1,\infty))$

    ・(1,∞)の場合も含めてよい
    ・x^{1-t}y^t≦(1-t)x+ty (t∊[0,1],x,y∊(0,∞))
    ・(p-1)q=p

・$(X,\mathfrak{M},\mu)$を測度空間、$p,q$を共役指数、$f,g:X\to[0,\infty]$を可測関数とすると、$\int_X fgd\mu\le(\int_Xf^pd\mu)^{\frac{1}{p}}(\int_Xg^qd\mu)^{\frac{1}{q}}$ （Holder不等式）

    ・可積分関数ではない

・$(X,\mathfrak{M},\mu)$を測度空間、$p\in(1,\infty)$、$f,g:X\to[0,\infty]$を可測関数とすると、$(\int_X(f+g)^pd\mu)^{\frac{1}{p}}\le(\int_Xf^pd\mu)^{\frac{1}{p}}+(\int_Xg^pd\mu)^{\frac{1}{p}}$ (Minkowski不等式)

    ・可積分関数ではない

##### $L^p$空間

・複素数値可測関数$\mathcal{L}(X,\mathfrak{M},\mu)$から構成される同値類$L(X,\mathfrak{M},\mu)$

    ・f~g⇔a.e.f=g
    ・複素数C上ベクトル空間で、積、複素共役がwell-defined

・$L^p(X,\mathfrak{M},\mu)=\{(\int_X|f|^pd\mu)^{\frac{1}{p}}<\infty\}\ (p\in[1,\infty))$

    ・L^pはノルム空間かつベクトル空間

・$L^{\infty}(X,\mathfrak{M},\mu)=\{\inf\{\alpha\ge0\ |\ \mu((\alpha<|f|))=0\}<\infty\}$

    ・本質的上限のこと、任意の実数より大きくなる点が零集合
    ・L^∞はノルム空間かつベクトル空間

---

## $l^p$空間



---