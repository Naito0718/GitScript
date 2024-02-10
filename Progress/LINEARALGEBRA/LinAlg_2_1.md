
    ・結局Kは体か斜体かどっちや！？

- [有限次元右 $K$-加群](#有限次元右-k-加群)
  - [基底](#基底)
  - [準同型変換と行列](#準同型変換と行列)
    - [$K$-右準同型写像の全単射性](#k-右準同型写像の全単射性)
  - [テンソル積](#テンソル積)
  - [外積](#外積)
  - [双対](#双対)
    - [双対と外積](#双対と外積)
    - [共役と外積](#共役と外積)
    - [内部積](#内部積)
    - [ホッジ双対](#ホッジ双対)
- [有限次元Clliford多元環](#有限次元clliford多元環)



# 有限次元右 $K$-加群

## 基底

    ・右一次独立と、基底の定義はベクトル空間と同じ。
<br>

<dl><dt>

・$n$ 次元右 $K$-加群 $V$ とする。
<br>

</dt><dd>

- $n+1$ 個以上の元は右一次従属。

- 右一次独立な $n$ 個の元は基底となる。
<br>

- 有限集合 $S$、$\lang S\rang=V$ とする。
このとき、
$$\exist v_1,...,v_n\in S\text{ であって、}(v_1,...,v_n)\text{ は} V\text{ の基底}$$

</dd></dl>

---

・有限次元右 $K$-加群 $V,W$ とする。
このとき、
$\dim V=\dim W\iff V\cong W\ (K\text{-右同型})$

---

## 準同型変換と行列

・$K$-右準同型 $\alpha:V\to V$ と基底 $u_1,...,u_n$ に対して、
$$y=\alpha(x)\iff y=Ax$$を満たす行列 $A\in M(n,K)$ がただ一つ存在し、$$A_{ij}=\alpha(u_i)\text{ の第 $j$ 成分}$$

- $K$-右準同型 $\alpha,\beta:V\to V$、基底 $u_1,...,u_n$、対応する行列 $A,B$ に対して、
$$y=\alpha\circ\beta(x)\iff y=AB x\\\ \\$$

- $K$-右準同型 $\alpha:V\to V$、$2$ つの基底 $u_i,v_i\ \ (i=1,...,n)$、対応する行列 $A,B$ に対して、
$$B=T^{-1}BT$$を満たす $T\in M(n,K)$ が存在して、
$$T_{ij}=v_j\text{ の第 $i$ 成分}$$


---

### $K$-右準同型写像の全単射性

・有限次元 $K$-右加群 $V$、$K$-右準同型 $\alpha:V\to V$ とする。
このとき、
$$\alpha\text{ は単射}\iff\alpha\text{ は全射}\iff\alpha\text{ は全単射}$$特に、$A,B\in M(n,K)$ に対して、$AB=E\Rightarrow BA=E$

---

## テンソル積

・有限次元 $K$-右加群 $V$、基底 $v_i,w_j$ とする。
このとき、$v_i\otimes w_j$ は $V\otimes W$ の基底。

- $K$-右加群 $V$、有限次元 $K$-右加群 $W$、基底 $w_i$ とする。
このとき、$$\sum_{i}^n v_i\otimes w_i=0\Rightarrow v_i=0$$

---

## 外積

・$n$ 次元 $K$-加群 $V$、基底 $v_i$ とする。
このとき、
$$\#\{1,u_i\wedge u_j\ \ (i<j),\ ...,\ u_1\wedge...\wedge u_n\}=2^n$$ は $\Lambda(V)$ の基底。
<br>

- $$\#\{u_{i_1}\wedge...\wedge u_{i_r}\}={}_n C_r$$は $\Lambda^r(V)$ の基底。特に、$r>n$ ならば、$\Lambda^r(V)=0$
<br>

- $$u_i\wedge u_i=0,\quad u_i\wedge u_j+u_j\wedge u_i=0$$

---

## 双対

・有限次元 $K$-右加群 $V$、基底 $v_i$ とする。
このとき、
$$f_i:V\to K\\\ \\
f_i(v_j)=\delta_{ij}$$ は $V^*$ の基底。
<br>

- 
$$(V\otimes W)^*\cong V^*\otimes W^*\\
\psi(\xi\otimes\eta)(v\otimes w)=\xi(v)\eta(w)\\\ \\
(V^*)^*\cong V\\
\psi(u)(\xi)=\xi(u)\\\ \\$$

    ・テンソルと双対の全射では、ηは基底を1に移すやつで、ξはgη^{-1}

---

### 双対と外積

・$$\Lambda^r(V^*)\cong(\Lambda^r(V))^*\ \ (K\text{-同型})\\\ \\
f(\xi_1\wedge...\wedge\xi_r)(u_1\wedge...\wedge u_r)=\det(\xi_j(u_i))\\\ \\$$

    ・写像は基底を基底に移す。
    ・多元環同型ではない。
    ・多様体とかで大事！
<br>

- 上記の写像 $f$ について、$\xi\in\Lambda^r(V^{\vee}),\ \eta\in\Lambda^{l}(V^{\vee})$ とすると、
$$f(\xi\wedge\eta)(v_1\wedge...\wedge v_{r+l})\\\ \\
=\sum_{\substack{1\le\sigma(1)<...<\sigma(k)\le k+l\\\ \\ 1\le\sigma(k+1)<...<\sigma(k+l)\le k+l}} (\mathrm{sgn}(\sigma))f(v_{\sigma(1)},...,v_{\sigma(k)})g(v_{\sigma(k+1)},...,v_{\sigma(k+l)})\\\ \\$$

      ・基底だけ代入してみればよい。

---

### 共役と外積

・有限次元 $\bm{C}$-加群 $V$ において、
$$\Lambda^r(\overline{V})\cong\overline{\Lambda(V)^r}\quad(\bm{C}-\text{同型})$$

---

### 内部積

    ・無限次元でも定義できるみたいだけど、ホッジ双対は有限次元じゃないとダメっぽい。
<br>

<dl><dt>

・$n$ 次元 $K$-加群 $V$、$v\in V$ とする。
このとき、
$$\iota_v:(\Lambda^r(V))^*\to(\Lambda^{r-1}(V))^*\\\ \\
\iota_v(\beta)(v_1\wedge...\wedge v_{r-1})=\beta(v\wedge v_1\wedge...\wedge v_{r-1})$$
と定めると、これはwell-definedな線形写像。ただし、$r=0$ ならば $\iota_v=0$ とする。
<br>

    ・r=0でもよいが、r>nだと無意味。
<br>

</dt><dd>

- $$\iota_v\circ\iota_v=0,\quad\iota_v\circ\iota_w=-\iota_w\circ\iota_v\\\ \\$$

- $\alpha\in(\Lambda^l(V))^*,\beta\in(\Lambda^s(V)^*)$ とする。
このとき、$$\iota_v(\alpha\wedge\beta)=\iota_v(\alpha)\wedge\beta+(-1)^l\alpha\wedge\iota_v(\beta)$$
すなわち、$\iota$ は次数 $-1$ の反導分。
<br>

</dd></dl>

---

### ホッジ双対

---

# 有限次元Clliford多元環

・対称内積 $n$ 次元 $K$-加群 $V$、直交基底 $e_1,...,e_n$ とする。
このとき、
$$\#\{1,u_iu_j\ \ (i<j),\ ...,\ u_1...u_n\}=2^n$$ は基底。

    ・直交基底が存在するかは不明。


- $$\#\{1,u_{i_1}... u_{i_{2r}}\}=2^{n-1}$$は $C^1(V)$ の基底。
<br>

- $$u_i^2=\lang u_i,u_i\rang,\quad u_iu_j+u_ju_i=0\ \ (i\neq j)$$

---

