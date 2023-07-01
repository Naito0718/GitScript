# 関数解析

## ノルム空間

・和、スカラー倍（スカラーも点列）、ノルムは連続

    ・u_nが収束列ならCauchy列

### 総和$\sum_{j\in J}x_j$

・定義

    ・集合Jに対して、その有限部分集合全体Fに集合の包含関係を入れたものは有向集合
    ・ネットx_λ:F→X, x_λ(F)=Σ_F x_λ
    ・ノルム空間（ハウスドルフ）より、収束値を持てば一意的

・性質

    ・総和が収束すれば、{j∊J|x_j≠0}は高々可算
    ・Σ_N x_nが収束すればΣ_n=1 x_nも収束する。（eventually性）逆は一般に成り立たない
    
・絶対収束$\sum_{j\in J}\|x_j\|<\infty$（非負実数値のネット）

    ・Banach空間で総和が絶対収束すれば、元の総和も収束する
___

## 無限次元ベクトル空間

### 具体例

#### $C[a,b]$

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