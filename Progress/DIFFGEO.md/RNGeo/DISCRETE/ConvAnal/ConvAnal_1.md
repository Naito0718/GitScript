
- [凸関数](#凸関数)
  - [凸性と同値な命題](#凸性と同値な命題)
  - [凸関数の性質](#凸関数の性質)
  - [一変数凸関数](#一変数凸関数)
    - [凸性と同値な命題](#凸性と同値な命題-1)
- [凸集合](#凸集合)
    - [凸包](#凸包)
    - [アフィン包](#アフィン包)
  - [凸集合の位相](#凸集合の位相)
- [ルジャンドル変換](#ルジャンドル変換)
  - [ルジャンドル変換の性質](#ルジャンドル変換の性質)




# 凸関数

<dl><dt>

・$f:\bm{R}^n\to\bm{R}\cup\{\pm\infty\}$ とする。
このとき、実行定義域 $\mathrm{dom}\ f$：
$$\mathrm{dom}\ f=\{x\in\bm{R}^n\ |\ -\infty<f(x)<\infty\}\\\ \\$$

- $f:\bm{R}^n\to\bm{R}\cup\{\infty\}$ とする。
このとき、凸関数 $f$：$$f(\lambda a+(1-\lambda)b)\le\lambda f(a)+(1-\lambda)f(b)\quad(0\le\lambda\le1)$$
ここで、$\mathrm{dom}\ f\neq\phi$ ならば、真凸関数、$>$ で成り立つならば狭義凸関数という。
また、$h:\bm{R}^n\to\bm{R}\cup\{-\infty\}$ に対して、$-h$ が凸関数ならば、凹関数という。
<br>

      ・全部∞でも凸関数。
      ・物理とは逆。
<br>



</dt><dd>




</dd></dl> 

・多変数凸関数 $f:\bm{R}^n\supset X\to\bm{R}\cup\{\infty\},\ f(\lambda a+(1-\lambda)b)\ge\lambda f(a)+(1-\lambda)f(b),\ X$は凸集合

・凸関数の和は凸関数

    ・上に凸でも成り立つ

・凸関数の非負実数倍は凸関数

    ・上に凸でも成り立つ。負なら凹凸入れ替わる

・凸関数$f$に対して、$A\in M(n,\bm{R}),b\in\bm{R}$において$f(Ax+b)$は凸関数

    ・上に凸でも成り立つ
    ・合成はそんなに心配しなくてよい、どうせImは凸っぽくなる
    ・g(x)=f(X-x)も凸


・凸関数の族に対して、$\sup f_j$は凸関数（有限、可算、非可算）

    ・有限または無限個の一次関数の最大値として書かれる関数は凸関数
    ・下に凸ならinfで成り立つ

・多変数について凸ならば、各変数について凸

    ・k変数でも凸
    ・各変数に対してルジャンドル変換を実行できる

・凸関数$f$に対して、$f(y)=f(y\bm{x}_1+(1-y)\bm{x}_2)$は凸関数

    ・各変数のやつはこれの特別な場合



## 凸性と同値な命題

・$f$が二階微分可能ならば、$f$が上に凸$\iff I$ 上 $(\frac{\partial^2f}{\partial x_i\partial x_j})$が半正定値

## 凸関数の性質

・凸関数は連続

・凸関数$f$に対して、$\mathrm{grad}f(x_0)=0$ならば、$f$は$x_0$において最小値を取る

    ・上に凸なら最大値


---

## 一変数凸関数

・$f$が凸$\iff -f$が上に凸

・$f$が狭義単調増加な凸関数ならば、$f^{-1}$は狭義単調増加で上に凸

・$I$の内点で連続で、$I$から高々可算個の点を除いた$I^*$上で$C^1$

・任意の$I$の内点で、$D^{\pm}_xf(x)=f'(x\pm0)$

・任意の$I$の内点で、$f'(x-0)\le f'(x+0)$

    ・上に凸なら反転

・任意の$I$の内点で、$a<b$ならば$f'(a+0)\le f'(b-0)$

    ・上に凸なら反転

・任意の$x_0$に対して、$f'(x_0-0)\le\alpha\le f'(x_0+0)$を満たす$\alpha$を取ると、$f(x)\ge f(x_0)+\alpha(x-x_0)$

    ・fが微分可能な点においてはα=f'(x_0)とできる
    ・上に凸なら反転
    ・α=0と取れれば、fはx_0で最小値を取る

・任意の$I$の内点で、$f'(x-0),f'(x+0)$は単調増加、特に$I^*$上で$f'(x)$は単調増加

    ・上に凸なら反転

・$f'(x_0)=0$ならば、$f$は$x_0$において最小値を取る

    ・上に凸なら最大値



### 凸性と同値な命題

・$f$が$2$回微分可能ならば、$f$が凸$\iff I$ 上 $f''(x)\ge0$

・$f$が凸$\iff f$が連続、$I$から高々可算個の点を除いた集合$I^*$上で$C^1$、$f'(x)$は$I^*$上単調減少

・$f$が凸$\iff f(a_1x_1+...+a_nx_n)\ge a_1f(x_1)+...+a_nf(x_n),\ \sum a_i=1$

・$f$が凸$\iff\forall y_1<y_2<y_3$に対して$(y_3-y_2)f(y_1)-(y_3-y_1)f(y_2)+(y_2-y_1)f(y_3)\ge0$

---

# 凸集合 

・標示関数$\delta_S:\bm{R}^n\to\bm{R}\cup\{\infty\},\ \delta_S(x)=(0\ (x\in S),\infty\ (x\notin S))$

    ・Sが凸集合⇔δ_Sが凸関数

・エピグラフ $\mathrm{epi}f=\{(x,Y)\in\bm{R}^{n+1}\ |\ Y\ge f(x)\}$

    ・fが凸関数⇔epi fは凸集合

<dl><dt>

・部分集合 $S\sub\bm{R}^n$ とする。
このとき、凸集合、錐 $S$：
$$\text{凸集合：}x,y\in S\Rightarrow0\le\forall\lambda\le1\text{ に対して、}\lambda x+(1-\lambda)y\in S\\\ \\
\text{錐：}x\in S\Rightarrow\forall\lambda>0\text{ に対して、}\lambda x\in S$$
ここで、凸集合である錐を凸錐という。
<br>

- $x_1,...,x_m\in\bm{R}^n$ とする。
このとき、凸結合： $$\sum_{i=1}^m\lambda_i=1\text{ なる }\lambda_1,...,\lambda_m\ge0\text{ に対する }\sum_{i=1}^m\lambda_ix_i\\\ \\$$

</dt><dd>

- 部分集合 $S\sub\bm{R}^n$ とする。
このとき、
$$S\text{ は凸錐}\iff x,y\in S\Rightarrow\forall\lambda,\mu>0\text{ に対して、}\lambda x+\mu y\in S\\\ \\$$

- $A\in M(n,\bm{R}),b\in\bm{R}^n$ とする。
このとき、$$S=\{x\in\bm{R}^n\ |\ (Ax)_i\le b_i\}$$
と定めると、これは凸集合で、$b=0$ ならば凸錐。
ここで、$S$ を凸多面体という。

---

・凸集合の族 $S_{\lambda}\sub\bm{R}^n$ とする。
このとき、$\bigcap S_{\lambda},\overline{S}_{\lambda}$ は凸集合。
<br>

- 凸集合 $S\sub\bm{R}^n$ とする。
このとき、$S$ は弧状連結。
<br>

- 凸集合 $S\sub\bm{R}^n$、$x_1,...,x_m\in S$ とする。
このとき、凸結合 $\sum \lambda_i x_i\in S$

</dd></dl> 

---

### 凸包

<dl><dt>

・部分集合 $S\sub\bm{R}^n$ とする。
このとき、$S$ の凸包 $\mathrm{Conv}\ S$：$$\mathrm{Conv}\ S=\bigcap\{C\ |\ S\sub C\text{ であって、}C\text{ は凸集合}\}\\\ \\$$

</dt><dd>

- 部分集合 $S\sub C\sub\bm{R}^n$ とする。
このとき、$$C=\mathrm{Conv}\ S\iff C=\left\{\sum \lambda_i x_i\ |\ x_i\in S,\ \sum\lambda_i=1,\lambda_i\ge0\right\}$$

- $S$ が有限集合ならば、 $\overline{\mathrm{Conv}\ S}=\mathrm{Conv}\ S$
<br>

      ・ケーリークラインの端点定理辺り。
      ・有限って有界性に使うのか。

</dd></dl> 

---

### アフィン包

・凸集合 $S$ とする。
このとき、アフィン包 $\mathrm{aff}\ S$：
$$\mathrm{aff}\ S=\{S\sub W\ |\ W\text{ は }S\text{ を含む最小のアフィン集合}\}$$
と定める。ここで、アフィン集合は線形空間を平行移動したもの。

- 凸集合 $S$、$x\in S$ とする。このとき、相対的内点 $x$：
$$\mathrm{aff}\ S\text{ の部分空間位相を入れた }S\text{ における、}S\text{ の内点 }x$$

---

## 凸集合の位相

・凸集合$S$の位相：$S$を含むアフィン包aff$S$から誘導される位相

    ・S^i=ri S
    ・実変数なら通常の位相

---



# ルジャンドル変換

・関数$f$に対する最小値集合$\arg\min f=\{x\in\bm{R}^n\ |\ f(x)\le f(y),\ \forall y\in S\}$

    ・fが凸ならargmin fは凸集合

・関数$f$、ベクトル$p$に対する$f[-p](x)=f(x)-(p,x)$

    ・fが凸関数ならばf[-p]も凸関数

・劣微分$\partial_{\bm{R}}f(x)=\{p\in\bm{R}^n\ |\ f[-p](y)\ge f[-p](x),\forall y\in S\}$
・$p\in\partial_{\bm{R}}f(x)\iff x\in\arg\min f[-p]$

    ・劣微分は凸集合
    ・xがdom fの内点ならば空でない
    ・fが凸関数かつxで微分可能ならば、p=∇fとして一意的：凸でないとルジャンドル変換は定まらない

・ルジャンドル変換$f^{*}(p)=\sup\{f[-p](x)\}=f[-p](x)\ (x\in\arg\min f[-p])$

    ・supだから一意的
    ・f'(x-0)≦p≦f'(x+0)が成り立つ
    ・凸関数
    ・部分ルジャンドル変換だと変換しなかった部分の凸性は反転する

・逆ルジャンドル変換$f^{**}(q)=\sup\{f^{*}[-q](p)\}=f(x)$ 

・符号が逆のルジャンドル変換$h(p)=-\sup\{f[-p](x)\}$

    ・凸性が逆になる
    ・h'(p)=-x(p)
    ・逆ルジャンドル変換はinf{h(p)+px}にしないといけなくなる（^**でない）
    ・部分ルジャンドル変換では、変換した部分だけ凸性が反転する


## ルジャンドル変換の性質

・$f^*(p)$が$p$で微分可能かつ$f^{-1}(x)$が微分可能で$p=f'(x)$ならば、$f^{*'}(p)=x(p)$

・$f,f^{*}$がともに二階微分可能ならば、$f''(x)f^{*''}(p)=1\quad(p=f'(x))$




---