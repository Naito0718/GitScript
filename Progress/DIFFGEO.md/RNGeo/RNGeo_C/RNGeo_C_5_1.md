
- [$R^n$ の単体](#rn-の単体)
  - [単体の位相](#単体の位相)
  - [単体複体](#単体複体)
    - [$q$-骨格](#q-骨格)
      - [単体写像](#単体写像)
      - [局所一次写像](#局所一次写像)
- [複体](#複体)
  - [凸胞体](#凸胞体)
  - [多面体](#多面体)
  - [レトラクション](#レトラクション)



# $R^n$ の単体

- 一次元単体 $\sigma$ とする。
このとき、
$$\exist v\in\bm{R}^N\text{ であって、}\sigma=\{v\}\\\ \\$$

- 二次元単体 $\sigma$ とする。
このとき、
$$\exist a,b\in\bm{R}^N,\ a\neq b\text{ であって、}\\\ \\
\sigma=\{b+t(a-b)\ |\ 0\le t\le1\}\\\ \\$$

- 三次元単体 $\sigma$ とする。
このとき、
$$\exist v_0,v_1,v_2\in\bm{R}^N,\ v_0\neq v_1\neq v_2,\ [v_0-v_2,v_1-v_2]\text{ は一次独立であって、}\\\ \\
\sigma=\{tv_0+sv_1+(1-t-s)v_2\ |\ 0\le t+s\le1,\ 0\le t,s\}\\\ \\$$
よって、これは三角形の内部と境界。
<br>

- 四次元単体 $\sigma$ とする。
このとき、
$$\exist v_0,v_1,v_2,v_3\in\bm{R}^N,\ v_0\neq v_1\neq v_2\neq v_3,\ [v_0-v_3,v_1-v_3,v_2-v_3]\text{ は一次独立であって、}\\\ \\
\sigma=\{tv_0+sv_1+rv_2+(1-t-s-r)v_3\ |\ 0\le t+s+r\le1,\ 0\le t,s,r\}\\\ \\$$よって、これは四面体の内部と境界。
<br>

      ・証明っぽいのはできる！

---

## 単体の位相

<dl><dt>

・$p$-単体 $\sigma\sub\bm{R}^n$ とする。
このとき、
$$d_{\sigma}:\sigma\times\sigma\to[0,\infty)\\\ \\
d(x,y)=\sum_{i=0}^p|\lambda_i-\mu_j|$$
と定めると、これは距離。

</dt><dd>

- $\bm{R}^n$ のマンハッタン距離 $d_{\infty}$ とする。
このとき、
$$\forall x,y\in\sigma\text{ に対して、}\\\ \\
\min\{|v_0|,...,|v_p|\}d(x,y)\le d_{\infty}\le \left(\sum_{i=1}^p|v_i|\right)d(x,y)$$
ただし、最小値を取る時 $0$ を取るものは除いて考える。
したがって、単体の位相は $\bm{R}^n$ の部分空間位相と一致する。
<br>

- $\sigma$ は閉集合であって、$\forall x\in \sigma\text{ に対して、}|x|<\sum|v_i|$
したがって、$\sigma$ はコンパクト集合。

</dd></dl>

---

## 単体複体

<dl><dt>

・$\bm{R}^n$ の単体を要素に持つ集合 $K$ とする。
このとき、単体複体 $K$：
$$\sigma\in K\Rightarrow\text{ 任意の }\sigma\text{ の面 }\tau\in K\\\ \\
\sigma_1,\sigma_2\in K,\ \sigma\cap\tau\neq\phi\Rightarrow\sigma\cap\tau\text{ は }\sigma,\tau\text{ の面}\\\ \\$$
ここで、$\dim K=\max\{\dim\sigma\ |\ \sigma\in K\}$ とし、部分集合 $L\sub K$ が単体複体であるとき、部分複体という。
<br>

    ・一般には共通部分取っても単体ではない。
<br>

- 単体複体 $K$ とする。
このとき、多面体 $|K|$：
$$|K|=\bigcup_{\sigma\in K}\sigma\\\ \\$$

</dt><dd>

- $p$-単体 $\sigma=[v_0,...,v_p]$ とする。
このとき、
$$K(\sigma)=\{\tau\ |\ \tau\text{ は }\sigma\text{ の面}\}\\\ \\
K(\partial\sigma)=K(\sigma)-\{\sigma\}$$
と定めると、これらは単体複体で 
$$|K(\sigma)|=\sigma,\quad|K(\partial\sigma)|=\bigcup\{\sigma\text{ の }p-1\text{ 面}\}$$

</dd></dl>

---

### $q$-骨格

<dl><dt>

・単体複体 $K$、$q\in\bm{N}\cup\{0\}$ とする。
このとき、$q$-骨格 $K^q$：
$$K^q=\{\sigma\in K\ |\ \dim\sigma\le q\}$$
ここで、$K^0$ を頂点集合という。
<br>

    ・φ含んだり含まなかったりする。

<br>

</dt><dd>

- $$K^0\sub K^1\sub...\sub K^{\dim K}=K$$

</dd></dl>

---

#### 単体写像

<dl><dt>

・単体的複体 $K,M$、頂点集合 $K^0,M^0$、$f:K^0\to M^0$ とする。
このとき、単体写像 $f$：
$$\forall\text{ ある }K\text{ 単体の頂点 }\{v_0,...,v_p\}\text{ に対して、}\\\ \\
\{f(v_0),...,f(v_p)\}\text{ はある }M\text{ の単体の頂点}\\\ \\$$

- 単体的複体 $K$、$v\in K^0$ とする。
このとき、
$$v:K\to\Pi_{x\in K^0}\bm{R}\\\ \\
\forall x\in[v_0,...,v_p]\text{ に対して、}v(x)=\begin{cases}
\lambda_i & (v=v_i) \\
0 & (v\notin\{v_0,...,v_p\})  
\end{cases}\\\ \\$$
と定めると、これはwell-defined、すなわち、$x$ が属する単体 $\sigma$ によらない。また、明らかに $K$ が単体であったときの一次写像の拡張であって、$\sum_{v\in K^0} v(x)=1$ が成り立つ。
<br>

</dt><dd>

- 単体写像 $f:K^0\to M^0$ とする。
このとき、
$$\tilde{f}:|K|\to |M|,\quad f':K\to M\\\ \\
\forall w\in M^0\text{ に対して、}w(\tilde{f}(x))=\sum_{f(v)=w}v(x)\\\ \\
f'([v_1,...,v_p])=[f(v_1),...,f(v_p)]$$
と定めると、$\tilde{f}$ は各 $\sigma$ 上で一次写像。
特に、$f$ が全単射ならば、$\tilde{f}$ は全単射であり、このとき $K,W$ は同型であるという。

<br>

      ・チルダfは座標を座標に飛ばしてる。
      ・別に同型は同値関係ではない。


</dd></dl>

---

#### 局所一次写像




---

# 複体

## 凸胞体

・
有限部分集合 $\Gamma\sub\bm{R}^k$ とする。
このとき、凸胞体 $\mathrm{conv}(A)$



## 多面体

<dl><dt>

・部分集合 $P\sub\bm{R}^n$ とする。
このとき、有限多面体 $P$：
$$\exist\text{ 単体 }\sigma_1,...,\sigma_n\sub\bm{R}^N\text{ であって、}P=\bigcup_{i=1}^n\sigma_i\\\ \\
P\text{ の単体分割に属する }\sigma_0\sub P\text{ に対して、その辺 }\tau^q\text{ も }P\text{ の単体分割に属する。}\\\ \\
P\text{ の単体分割に属する }\sigma_0,\sigma_1\sub P\text{ に対して、}\sigma_1\cap\sigma_2\neq\phi\text{ ならば、}\sigma_1\cap\sigma_2\text{ は }\sigma_1,\sigma_2\text{ の辺}\\\ \\$$

    ・単体分割の次元はバラバラでよい。

- 有限多面体 $P=\bigcup_{i=1}^n\sigma_i\sub\bm{R}^N$、部分集合 $Q\sub P$ とする。
このとき、部分多面体 $Q$：
$$Q=\bigcup_{i_k}\sigma_{i_k}\sub\bm{R}^N\text{ であって、}Q{ は部分多面体}\\\ \\$$

</dt><dd>

- 単体 $\sigma$ は有限多面体であって、$\partial \sigma$ は $\sigma$ は部分多面体。
<br>

- $I=[0,1],\quad I^n=\Pi_{i=1}^n I$ とする。
このとき、$I^n$ は有限多面体であって、

</dd></dl>

---

## レトラクション

・有限多面体 $P$、部分多面体 $Q\sub P$ とする。
このとき、$P\times0\cup Q\times [0,1]$ は $P\times I$ の強変位レトラクト。