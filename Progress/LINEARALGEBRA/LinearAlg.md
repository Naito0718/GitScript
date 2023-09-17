- [$R$ 上の斜体 $K$](#r-上の斜体-k)
  - [自己同型群](#自己同型群)
- [$K$-右加群](#k-右加群)
  - [基本的な性質](#基本的な性質)
    - [定義](#定義)
    - [$K$-右準同型写像](#k-右準同型写像)
    - [テンソル積](#テンソル積)
      - [$K$-多元環に対するテンソル積](#k-多元環に対するテンソル積)
    - [テンソル $K$-多元環](#テンソル-k-多元環)
      - [次数付き $K$-多元環](#次数付き-k-多元環)
        - [次数付き $K$-多元環から生成される次数付き $K$-多元環](#次数付き-k-多元環から生成される次数付き-k-多元環)
    - [外積 $K$-多元環](#外積-k-多元環)
      - [直和と外積](#直和と外積)
    - [双対 $K$-加群](#双対-k-加群)
    - [共役 $C$-加群](#共役-c-加群)
    - [有限次元](#有限次元)
      - [基底](#基底)
      - [準同型変換と行列](#準同型変換と行列)
      - [$K$-右準同型写像の全単射性](#k-右準同型写像の全単射性)
      - [テンソル積](#テンソル積-1)
      - [外積](#外積)
      - [双対](#双対)
        - [双対と外積](#双対と外積)
        - [共役と外積](#共役と外積)
- [Clifford多元環](#clifford多元環)
  - [対称内積を持つ $K$-加群](#対称内積を持つ-k-加群)
  - [Clifford多元環](#clifford多元環-1)
    - [直和とClifford](#直和とclifford)
    - [$\\bm{Z}\_2$ 次数付き $K$-多元環](#bmz_2-次数付き-k-多元環)
      - [生成される $\\bm{Z}\_2$ 次数付き多元環](#生成される-bmz_2-次数付き多元環)
  - [有限次元](#有限次元-1)
    - [$R$ などに対する性質](#r-などに対する性質)
- [内積 $K$- 右加群](#内積-k--右加群)
  - [定義](#定義-1)
    - [長さ $||x||$](#長さ-x)
  - [内積 $K$-右準同型](#内積-k-右準同型)
  - [有限次元](#有限次元-2)
    - [正規直交基底](#正規直交基底)
    - [基底の変換](#基底の変換)
    - [共役と双対](#共役と双対)
- [$K$-多元環](#k-多元環)
- [Banach単位的ノルム環](#banach単位的ノルム環)
  - [収束ベキ級数](#収束ベキ級数)
    - [正規収束](#正規収束)
    - [収束半径](#収束半径)
    - [演算と収束](#演算と収束)
      - [和と積](#和と積)
      - [合成](#合成)
      - [線形写像とベキ級数](#線形写像とベキ級数)
    - [収束する指数写像](#収束する指数写像)


# $R$ 上の斜体 $K$

## 自己同型群

・$\bm{R}$ 上の斜体 $K$ とする。
このとき、$$\mathrm{Aut}(K)=\{f:K\to K\ |\ f\text{ は全単射で積を保つ }\bm{R}\text{-群準同型}\}$$は合成によって群をなす。これを $\bm{R}$ 上の斜体 $K$ の自己同型群という。

---

# $K$-右加群

## 基本的な性質

### 定義

・加群 $V$、斜体 $K$ に対して、
$K$-右加群 $V$：
$$x\lambda\in V\\\ \\
x(\lambda\mu)=(x\lambda)\mu\\\ \\
x(\lambda+\mu)=x\lambda+x\mu\\\ \\
(x+y)\lambda=x\lambda+y\lambda\\\ \\
x1=x$$

    ・スカラー倍が逆なら左K-加群。

- 可換体 $K$ 上ベクトル空間 $V$：
$$x\lambda=\lambda x\in V\text{ であって、}V\text{ は右 }K\text{-加群}$$

      ・このとき、明らかにVは左K-加群。

---

### $K$-右準同型写像

・$K$-右加群 $V_1,V_2$、$f:V_1\to V_2$ とする。
このとき、$K$-右準同型写像 $f$：
$$f(x+y)=f(x)+f(y)\\\ \\
f(x\lambda)=f(x)\lambda$$

- $K$-右加群 $V_1,V_2$、全単射な$K$-右準同型写像 $f:V_1\to V_2$ とする。
このとき、$f^{-1}$ は $K$-右準同型写像。

      ・全単射K-右準同型をK-右同型という。

---

### テンソル積

<dl><dt>

・$K$-右加群 $V,W$ とする。
このとき、
$$\exist\ K\text{-右加群 }V\otimes W,\exist\ K\text{-双線形写像 }\tau:V\times W\to V\otimes W\text{ であって、}\\\ \\
\forall\ K\text{-右加群 }U,\forall\ K\text{-双線形写像 }\phi:V\times W\to U\text{ に対して、}\exist\ !\ K\text{-右準同型 }\psi:V\otimes W\to U\text{ であって、}\\\ \\
\phi=\psi\circ\tau$$ここで、$(V\otimes W,\tau)$ をテンソル積という。

</dt><dd>

- テンソル積 $(V\otimes_1W,\tau_1),(V\otimes_2W,\tau_2)$ とする。
このとき、$\tau_2=f\circ \tau_1$ を満たす $K$-右同型
$$f:V\otimes_1W\to V\otimes_2W$$がただ一つ存在する。 

- $$\tau((a,b))=a\otimes b\\\ \\
\forall x\in V\otimes W\text{ に対して、}\exist v_i,w_i\text{ であって、}\\
x=\sum_i (v_i\otimes w_i)\\\ \\$$

- $K$-右同型な $K$-右加群 $V_1,V_2,W_1,W_2,\ V_1\cong V_2,\ W_1\cong W_2\ (K\text{-右同型})$、テンソル積 $V_1\otimes W_1,V_2\otimes W_2$ とする。
このとき、$$V_1\otimes W_1\cong V_2\otimes W_2\ (K\text{-右同型})$$ であり、$V_2\otimes W_2$ は $V_1,W_1$ のテンソル積。
<br>

- - $$V\otimes W=F(V\times W)/I(V\times W)\\\ \\
I(V\times W)=\lang\{(u+u',w)-(u,w)-(u',w),\ (u,w+w')-(u,w)-(u,w'),\\\ \\ (u\alpha,w)-(u,w)\alpha,\ (u,w\alpha)-(u,w)\alpha\}\rang\\\ \\
\tau((u,w))=[(u,w)]=u\otimes w\\\ \\
\psi'(\sum(u,w)\alpha_{u,w})=\sum\phi((u,w))\alpha_{u,w},\quad\psi'(I(V\times W))=0\ \ (\psi\text{ は誘導されるやつ})$$と定めると、$(V\otimes W,\tau)$ は普遍環。

        ・F(V×W)は形式的有限和全体の集合。
        ・I(V×W)のとこの演算は形式和。  
        ・前の半加群のときと同じ。
        ・3個以上でテンソル積を作るときは、I(V×W)の要素を増すだけでよい。
        ・このΨ'はwell-defined

</dd></dl>

---

#### $K$-多元環に対するテンソル積

・$K$-多元環 $A,B$、テンソル積 $A\otimes B$ とする。
このとき、
$$(a\otimes b)(a'\otimes b)=(aa'\otimes bb')$$と定めると、この積はwell-definedで、$A\otimes B$ は$K$-多元環。

    ・同型類の演算も同様に成り立つ。

- 単位的 $K$-多元環 $A,B$、テンソル積 $A\otimes B$、$x\in A\otimes B$ とする。
このとき、$A\otimes B$ は単位的で、
$$\exist u\in A,v\in B\text{ であって、}x=u\otimes 1+1\otimes v$$

---

### テンソル $K$-多元環

・可換体 $K$-加群 $V$ とする。
このとき、
$$\exist\ K\text{-単位的多元環 }T(V),\exist\ K\text{-準同型写像 }\tau:V\to T(V)\text{ であって、}\\\ \\
\forall\ K\text{-多元環 }A,\forall\ K\text{-準同型写像 }\phi:V\to A\text{ に対して、}\exist\ !\ K\text{-多元環準同型 }\psi:T(V)\to A\text{ であって、}\\\ \\
\phi=\psi\circ\tau$$ここで、$(T(V),\tau)$ をテンソル $K$-多元環という。

</dt><dd>

- テンソル $K$-多元環 $(T(V)_1,\tau_1),(T_2(V),\tau_2)$ とする。
このとき、$\tau_2=f\circ \tau_1$ を満たす $K$-多元環同型
$$f:T_1(V)\to T_2(V)$$がただ一つ存在する。
<br> 

- $K$-多元環同型な $K$-加群 $V,W,\ V\cong W\ (K\text{-多元環同型})$、テンソル $K$-多元環 $T(V),T(W)$ とする。
このとき、$$T(V)\cong T(W)\ \ (K\text{-多元環同型})$$ であり、$T(W)$ は $V$ のテンソル $K$-多元環。

      ・同様に、テンソル K-多元環と多元環同型な空間は、Vのテンソル K-多元環。
<br>

- $$T(V)=\lang\{K,\tau(V)\}\rang$$

      ・生成は積も考える。

- $\tau$ は単射。
<br>

- - $$T(V)=\bigoplus_{r\ge0}T^r(V),\quad T^r(V)=V\otimes...\otimes V,\ T^0(V)=K\\\ \\
(u_1\otimes...\otimes u_r)\times(v_1\otimes...\otimes v_s)=u_1\otimes...\otimes v_s\quad(\text{well-defined})\\\ \\
(u_1\otimes...\otimes u_r)\times\alpha=(u_1\alpha)\otimes...\otimes u_r\\\ \\
X=\alpha+u_1x+\left(\sum u_{i_2}\otimes v_{i_2}\right)x^2+...\\\ \\
\tau(u)=ux\\\ \\
\psi(1_{T(V)})=1_A,\quad\psi(u_1\otimes...\otimes u_r)=\phi(u_1)...\phi(u_r)$$と定めると、$(T(V),\tau)$ はテンソル $K$-多元環。

        ・分配法則は仮定する。
        ・多項式環みたいになってる。  

  - 上記のテンソル $K$-多元環において、
  $$0_{T(V)}=0,\ \ 1_{T(V)}=1\in K$$

</dd></dl>

---

#### 次数付き $K$-多元環

    ・テンソル積 K-多元環は連結な次数付き K-多元環（に同型）

・$K$-多元環 $A$ とする。
このとき、次数付き $K$-多元環 $A$：
$$\exist\text{部分 }K\text{ 加群列 }A^r\sub A\text{ であって、}A=\bigoplus_{r\ge0}A^r\\\ \\
A^rA^s\sub A^{r+s}$$

- 次数付き $K$-多元環 $A$ とする。
このとき、連結：$$A^0=K$$

- 次数付き $K$-多元環 $A,B$、$f:A\to B$ とする。
このとき、次数付き $K$-多元環準同型：
$$f(A^r)\sub B^r$$

---

##### 次数付き $K$-多元環から生成される次数付き $K$-多元環

・次数付き $K$-多元環 $A=\bigoplus_{r\ge0}A^r,\ B=\bigoplus_{r\ge0}B^r$ とする。
このとき、
$$A\hat{\otimes}B=\bigoplus_{r\ge0}(A\hat{\otimes}B)^r,\quad(A\hat{\otimes}B)^n=\bigoplus_{r+s=n}(A^r\otimes B^s)\\\ \\
a\in A^r,b\in B^s,a'\in A^{r'},b'\in B^{s'}\text{ に対して、}\\
(a\otimes b)(a'\otimes b')=(-1)^{sr'}(aa'\otimes bb')\in A^{r+r'}\otimes B^{s+s'}\quad(\text{well-defined})$$ と定めると、これは次数付き $K$-多元環。
また、$X\in A\hat{\otimes}B$ に対して、
$$X=(a_0\otimes b_0)+(a_1'\otimes b_0'y+a_0'\otimes b_1' z)x\\\ \\
+(a_2''\otimes b_0''y^2+a_1''\otimes b_1'' yz+a_0''\otimes b_2''z^2)x^2+...$$と書ける。

    ・多項式環のように見るとよい。
    ・両方単位的ならば、生成されるやつも単位的。

- 次数付き $K$-多元環 $A=\bigoplus_{r\ge0}A^r,\ B=\bigoplus_{r\ge0}B^r,\ C=\bigoplus_{r\ge0}C^r$、次数付き $K$-多元環準同型 $f:A\to B,\ g:B\to C$ とする。
このとき、$$f(a)g(b)=(-1)^{rs}g(b)f(a)\ \ (a\in A^r,b\in B^s)$$ を満たすならば、
$$h:A\hat{\otimes}B\to C\\\ \\
h(a\otimes b)=f(a)g(b)\ \ (a\in A^r,b\in B^s)$$は次数付き $K$-多元環準同型。
<br>

- 次数付き $K$-多元環 $A$、次数付き $K$-多元環同型な次数付き $K$-多元環 $B,C$ とする。
このとき、
$$A\hat{\otimes}B\cong A\hat{\otimes} C\ \ (\text{次数付き $K$-多元環同型})$$


---

### 外積 $K$-多元環

    ・積：ab=a∧b、τ(u)=uと書く。

・可換体 $K$-加群 $V$ とする。
このとき、
$$\exist\ K\text{-単位的多元環 }\Lambda(V),\exist\ K\text{-準同型写像 }\tau:V\to T(V),\ \tau(u)^2=0 \text{ であって、}\\\ \\
\forall\ K\text{-単位的多元環 }A,\forall\ K\text{-準同型写像 }\phi:V\to A,\ \phi(u)^2=0\text{ に対して、}\exist\ !\ K\text{-多元環準同型 }\psi:V\to A\text{ であって、}\\\ \\
\phi=\psi\circ\tau$$ここで、$(\Lambda
(V),\tau)$ を外積 $K$-多元環という。

</dt><dd>

- 外積 $K$-多元環 $(\Lambda(V)_1,\tau_1),(\Lambda_2(V),\tau_2)$ とする。
このとき、$\tau_2=f\circ \tau_1,\ f(u)^2=0$ を満たす $K$-多元環同型
$$f:\Lambda_1(V)\to \Lambda_2(V)$$がただ一つ存在する。

      ・次数付き

<br> 

- $K$-同型な $K$-加群 $V,W,\ V\cong W\ (K\text{-同型})$、外積 $K$-多元環 $\Lambda(V),\Lambda(W)$ とする。
このとき、$$\Lambda(V)\cong \Lambda(W)\ \ (K\text{-多元環同型})$$ であり、$\Lambda(W)$ は $V$ の外積 $K$-多元環。

      ・f◦τでよい、2乗で0
      ・同様に、外積K-多元環と多元環同型なやつは、Vの外積K-多元環。

- $\tau$ は単射で、$$\tau(u)\tau(v)+\tau(v)\tau(u)=0\\\ \\
\Lambda(V)=\lang K,\tau(V)\rang$$
<br>

- - $$\Lambda(V)=T(V)/\mathfrak{a}(V),\quad \mathfrak{a}(V)=\left\{\sum a_ix_ib_i\ |\ x_i=\tau(u_i)^2,\ a_i,b_i\in T(V)\right\}\\\ \\
\tau(u)=[\tau_{T(V)}(u)]\\\ \\
\psi_{T(V)}(\mathfrak{a}(V))=0\text{ より、誘導される写像}\psi$$と定めると、$(\Lambda(V),\tau)$ は外積 $K$-多元環。

        ・分配法則は仮定する。
        ・多項式環みたいになってる。  

  - 上記の外積 $K$-多元環において、
  $$0_{T(V)}=0,\ \ 1_{T(V)}=1\in K$$

  - 上記の外積 $K$-多元環において、射影 $\pi:T(V)\to T(V)/\mathfrak{a}(V)$ とする。
  このとき、$\pi$ は $K$-多元環準同型で、$$\Lambda^r(V)=\pi(T^r(V))$$
  とすると、$$\Lambda(V)=\bigoplus_{r\ge0}\Lambda^r(V),\quad\Lambda^0(V)=K,\Lambda^1(V)=V$$であって、$\Lambda(V)$ は連結な次数付き $K$-多元環。

        ・任意の外積K-多元環もこの性質を保つ。
        ・後半の連結性とかは全単射から

</dd></dl>


---

#### 直和と外積

・$K$-多元環 $V=V_1\oplus V_2$、外積 $K$-多元環 $(\Lambda(V_1),\tau_1),(\Lambda(V_2)\tau_2)$ とする。
このとき、
$$\tau:V\to\Lambda(V_1)\hat{\otimes}\Lambda(V_2)\\\ \\
\tau(u_1+u_2)=\tau_1(u_1)\otimes1+1\otimes\tau(u_2)$$と定めると、$(\Lambda(V_1)\hat{\otimes}\Lambda(V_2),\tau)$ は $V$ の外積 $K$-多元環。

    ・次数付き同型でもある。

- $$\Lambda(V_1)\hat{\otimes}\Lambda(V_2)=\lang K,\tau_1(V_1)\otimes1,1\otimes\tau_2(V_2)\rang$$


---

### 双対 $K$-加群

    ・Hom(V,K)=V*
    ・Hom(V,W)の特別な場合

・$K$-右加群 $V,W$ とする。このとき、
$$(V\oplus W)^*\cong V^*\oplus W^*\ \ (K\text{-右同型})\\
\psi(\xi,\eta)(v,w)=\xi(u)+\eta(w),\quad\psi^{-1}(\phi)=(\phi(\cdot,0),\phi(0,\cdot))$$

---

### 共役 $C$-加群

・$\bm{C}$-加群 $V$ とする。
このとき、
$$\overline{V}=V\\\ \\
v\cdot\alpha=v\overline{\alpha}$$と定めると、これは $\bm{C}$ 加群。

- $\bm{C}$-加群 $V$ とする。
このとき、
$$\overline{(V\oplus W)}\cong \overline{V}\oplus \overline{W}\ \ (K\text{-右同型})\\
\overline{V\otimes W}=\overline{V}\otimes\overline{W}\ \ (K\text{-右同型})\\
\overline{\overline{V}}=V\ \ (K\text{-右同型})\\\ \\
\overline{V^*}\cong\overline{V}^*\ \ (K\text{-右同型})\\
\psi(\xi)=\overline{\xi}(u),\quad\overline{\xi}(u)=\overline{\xi(u)}$$


---

### 有限次元

#### 基底

    ・右一次独立、基底の定義はベクトル空間と同じ。

<dl><dt>

・$n$ 次元右 $K$-加群 $V$ とする。


</dt><dd>

- $n+1$ 個以上の元は右一次従属

- 右一次独立な $n+1$ 個の元は基底となる。

</dd></dl>

---

・有限次元右 $K$-加群 $V,W$ とする。
このとき、
$\dim V=\dim W\iff V\cong W\ (K\text{-右同型})$

---

#### 準同型変換と行列

・$K$-右準同型 $\alpha:V\to V$ と基底 $u_1,...,u_n$ に対して、
$$y=\alpha(x)\iff y=Ax$$を満たす行列 $A\in M(n,K)$ がただ一つ存在し、$$A_{ij}=\alpha(u_i)\text{ の第 $j$ 成分}$$

- $K$-右準同型 $\alpha,\beta:V\to V$、基底 $u_1,...,u_n$、対応する行列 $A,B$ に対して、
$$y=\alpha\circ\beta(x)\iff y=AB x\\\ \\$$

- $K$-右準同型 $\alpha:V\to V$、$2$ つの基底 $u_i,v_i\ \ (i=1,...,n)$、対応する行列 $A,B$ に対して、
$$B=T^{-1}BT$$を満たす $T\in M(n,K)$ が存在して、
$$T_{ij}=v_j\text{ の第 $i$ 成分}$$


---

#### $K$-右準同型写像の全単射性

・有限次元 $K$-右加群 $V$、$K$-右準同型 $\alpha:V\to V$ とする。
このとき、
$$\alpha\text{ は単射}\iff\alpha\text{ は全射}\iff\alpha\text{ は全単射}$$特に、$A,B\in M(n,K)$ に対して、$AB=E\Rightarrow BA=E$

---

#### テンソル積

・有限次元 $K$-右加群 $V$、基底 $v_i,w_j$ とする。
このとき、$v_i\otimes w_j$ は $V\otimes W$ の基底。

- $K$-右加群 $V$、有限次元 $K$-右加群 $W$、基底 $w_i$ とする。
このとき、$$\sum_{i}^n v_i\otimes w_i=0\Rightarrow v_i=0$$

---

#### 外積

・$n$ 次元 $K$-加群 $V$、基底 $v_i$ とする。
このとき、
$$\#\{1,u_i\wedge u_j\ \ (i<j),\ ...,\ u_1\wedge...\wedge u_n\}=2^n$$ は基底。

- $$\#\{u_{i_1}\wedge...\wedge u_{i_r}\}={}_n C_k$$は $\Lambda^r(V)$ の基底。特に、$r>n$ ならば、$\Lambda^r(V)=0$

- $$u_i\wedge u_i=0,\quad u_i\wedge u_j+u_j\wedge u_i=0$$


---

#### 双対

・有限次元 $K$-右加群 $V$、基底 $v_i$ とする。
このとき、
$$f_i:V\to K\\\ \\
f_i(v_j)=\delta_{ij}$$ は $V^*$ の基底。

- 
$$(V\otimes W)^*\cong V^*\otimes W^*\\
\psi(\xi\otimes\eta)(v\otimes w)=\xi(v)\eta(w)\\\ \\
(V^*)^*\cong V\\
\psi(u)(\xi)=\xi(u)$$

    ・テンソルと双対の全射では、ηは基底を1に移すやつで、ξはgη^{-1}

##### 双対と外積

・$$\Lambda^r(V^*)\cong(\Lambda^r(V))^*\ \ (K\text{-同型})\\\ \\
f(\xi_1\wedge...\wedge\xi_r)(u_1\wedge...\wedge u_r)=\det(\xi_j(u_i))$$

    ・写像は基底を基底に移す。
    ・多元環同型ではない。
    ・多様体とかで大事！

---

##### 共役と外積

・有限次元 $\bm{C}$-加群 $V$ において、
$$\Lambda^r(\overline{V})\cong\overline{\Lambda(V)}\ \ (\bm{C}-\text{同型})$$

---
---
---

# Clifford多元環

## 対称内積を持つ $K$-加群

・$K$-加群 $V$ とする。
このとき、対称内積 $\lang u,v\rang\in K$：
$$\lang u,v\rang=\lang v,u\rang\\\ \\
\lang u+u',v\rang=\lang u,v\rang+\lang u',v\rang\\\ \\
\lang u,v\alpha\rang=\lang u,v\rang\alpha$$

- $\bm{K}^n$、$c_i\in K$ とする。
このとき、$$\lang u,v\rang=\sum u_iv_ic_i$$は対称内積。

      ・c_i=1,-1のときが重要。

---

## Clifford多元環

・可換体 $K$-加群 $V$ とする。
このとき、
$$\exist\ K\text{-単位的多元環 }C(V),\exist\ K\text{-準同型写像 }\tau:V\to C(V),\ \tau(u)^2=\lang u,u\rang \text{ であって、}\\\ \\
\forall\ K\text{-単位的多元環 }A,\forall\ K\text{-準同型写像 }\phi:V\to A,\ \phi(u)^2=\lang u,u\rang\text{ に対して、}\exist\ !\ K\text{-多元環準同型 }\psi:C(V)\to A\text{ であって、}\\\ \\
\phi=\psi\circ\tau$$ここで、$(C(V),\tau)$ をClifford多元環という。

</dt><dd>

- Clifford多元環 $(C_1(V),\tau_1),(C_2(V),\tau_2)$ とする。
このとき、$\tau_2=f\circ \tau_1,\ f(u)^2=\lang u,u\rang$ を満たす $K$-多元環同型
$$f:\Lambda_1(V)\to \Lambda_2(V)$$がただ一つ存在する。

      ・次数付き

<br> 

- 内積を保つ $K$-同型な $K$-加群 $V,W,\ V\cong W\ (K\text{-内積同型})$、Clifford多元環 $C(V),C(W)$ とする。
このとき、$$C(V)\cong C(W)\ \ (K\text{-多元環同型})$$ であり、$C(W)$ は $V$ の外積 $K$-多元環。

      ・τ◦fでよい、2乗で0
      ・同様にClifford多元環と多元環同型なやつは、VのClifford多元環。これは内積関係ない。

- $\tau$ は単射で、$$\lang u,v\rang=0\Rightarrow\tau(u)\tau(v)+\tau(v)\tau(u)=0\\\ \\
C(V)=\lang K,\tau(V)\rang$$
<br>

- - $$C(V)=T(V)/\mathfrak{a}(V),\quad \mathfrak{a}(V)=\left\{\sum a_ix_ib_i\ |\ x_i=\tau(u_i)^2-\lang u_i,u_i\rang,\ a_i,b_i\in T(V)\right\}\\\ \\
\tau(u)=[\tau_{T(V)}(u)]\\\ \\
\psi_{T(V)}(\mathfrak{a}(V))=0\text{ より、誘導される写像 }\tilde{\psi}$$と定めると、$(C(V),\tau)$ はClifford多元環。

        ・分配法則は仮定する。
        ・多項式環みたいになってる。  

  - 上記のClifford多元環において、
  $$0_{T(V)}=0,\ \ 1_{T(V)}=1\in K$$

  - 上記の外積 $K$-多元環において、射影 $\pi:T(V)\to T(V)/\mathfrak{a}(V)$ とする。
  このとき、$\pi$ は $K$-多元環準同型で、$$\Lambda^r(V)=\pi(T^r(V))$$
  とすると、$$C(V)=C^0(V)\oplus C^1(V),\quad C^0(V)=\pi(\bigoplus_{r\ge0}T^{2r}(V)),\ C^1(V)=\pi(\bigoplus_{r\ge0}T^{2r+1}(V))$$であって、$C(V)$ は $\bm{Z}_2$ 次数付き $K$-多元環。

        ・任意のClifford多元環もこの性質を保つ。

</dd></dl>

---

### 直和とClifford

・対称内積 $K$-多元環 $V=V_1\oplus V_2$、Clifford多元環 $(C(V_1),\tau_1),(C(V_2)\tau_2)$ とする。
このとき、
$$\tau:V\to C(V_1)\hat{\otimes}C(V_2)\\\ \\
\tau(u_1+u_2)=\tau_1(u_1)\otimes1+1\otimes\tau(u_2)$$と定めると、$(C(V_1)\hat{\otimes}C(V_2),\tau)$ は $V$ のClifford多元環。

    ・次数付き同型でもある。

- $$C(V_1)\hat{\otimes}C(V_2)=\lang K,\tau_1(V_1)\otimes1,1\otimes\tau_2(V_2)\rang$$

---


### $\bm{Z}_2$ 次数付き $K$-多元環

・$\bm{K}$-多元環 $A=A^0\oplus A^1$ とする。
このとき、$\bm{Z}_2$ 次数付き $K$-多元環：
$$A^0A^0,A^1A^1\sub A^0,\quad A^0A^1,A^1A^0\sub A^1\\\ \\$$

- $\bm{Z}_2$ 次数付き $K$-多元環 $A,B$、$K$-多元環準同型 $f:A\to B$ とする。
このとき、$\bm{Z}_2$ 次数付き $K$-多元環 $f$：$$f(A^r)\sub B^r$$

---

#### 生成される $\bm{Z}_2$ 次数付き多元環

・次数付き $K$-多元環 $A=A^0\oplus A^1,\ B=B^0\oplus B^1,\ C=C^0\oplus C^1$ とする。

$$A\hat{\otimes}B=(A\hat{\otimes}B)^0\oplus (A\hat{\otimes}B)^1,\quad(A\hat{\otimes}B)^0=(A^0\otimes B^0)\oplus(A^1\otimes B^1),\ \ (A\hat{\otimes}B)^1=(A^0\otimes B^1)\oplus(A^1\otimes B^1)\\\ \\
a\in A^r,b\in B^s,a'\in A^{r'},b'\in B^{s'}\text{ に対して、}\\
(a\otimes b)(a'\otimes b')=(-1)^{sr'}(aa'\otimes bb')\quad(\text{well-defined})$$ と定めると、これは $\bm{Z}_2$ 次数付き $K$-多元環。

    ・多項式環のように見るとよい。
    ・両方単位的ならば、生成されるやつも単位的。

<br>

- 次数付き $K$-多元環 $A$、次数付き $K$-多元環同型な次数付き $K$-多元環 $B,C$ とする。
このとき、
$$A\hat{\otimes}B\cong A\hat{\otimes} C\ \ (\text{次数付き $K$-多元環同型})$$

- 次数付き $K$-多元環- 次数付き $K$-多元環 $A=A^0\oplus A^1,\ B=B^0\oplus B^1,\ C=C^0\oplus C^1$、$\bm{Z}_2$ 次数付き $K$-多元環準同型 $f:A\to B,\ g:B\to C$ とする。
このとき、$$f(a)g(b)=(-1)^{rs}g(b)f(a)\ \ (a\in A^r,b\in B^s)$$ を満たすならば、
$$h:A\hat{\otimes}B\to C\\\ \\
h(a\otimes b)=f(a)g(b)\ \ (a\in A^r,b\in B^s)$$は次数付き $K$-多元環準同型。
<br>

- 次数付き $K$-多元環 $A$、次数付き $K$-多元環同型な次数付き $K$-多元環 $B,C$ とする。
このとき、
$$A\hat{\otimes}B\cong A\hat{\otimes} C\ \ (\text{次数付き $K$-多元環同型})$$

---

## 有限次元

・対称内積 $n$ 次元 $K$-加群 $V$、直交基底 $e_1,...,e_n$ とする。
このとき、
$$\#\{1,u_iu_j\ \ (i<j),\ ...,\ u_1...u_n\}=2^n$$ は基底。

    ・直交基底が存在するかは不明。


- $$\#\{1,u_{i_1}... u_{i_{2r}}\}=2^{n-1}$$は $C^1(V)$ の基底。
<br>

- $$u_i^2=\lang u_i,u_i\rang,\quad u_iu_j+u_ju_i=0\ \ (i\neq j)$$

---

### $R$ などに対する性質



---
---
---

# 内積 $K$- 右加群

    ・K=R,C,H とする。

## 定義

・$K$-右加群 $V$ に対して、
内積：
$$(x,y)=\overline{(y,x)}\\\ \\
(x,y_1\alpha+y_2\beta)=(x,y_1)\alpha+(x,y_2)\beta\\\ \\
(x,x)\ge0,\quad(x,x)=0\iff x=0$$

    ・内積を持つものを内積K-右加群という。
    ・長さ：||x||=√(x,x)

- 内積 $K$-右加群 $V$ に対して、
$$(x_1+x_2,y)=(x_1,y)+(x_2,y)\\\ \\
(x\lambda,y)=\overline{\lambda}(x,y)\\\ \\
\forall y\in V\text{ に対して }(x,y)=0\iff x=0\quad(\text{正則性})$$

- 正規直交する元の組は右一次独立。

---

### 長さ $||x||$

・
$$\|x\|\ge0,\quad\|x\|=0\iff x=0,\quad\|x\lambda\|=\|x\||\lambda|\\\ \\
|(x,y)|\le\|x\|\|y\|\\\ \\
\|x+y\|\le\|x\|+\|y\|$$

- 距離：$\|x-y\|$ によって、$V$ は距離空間。

---

## 内積 $K$-右準同型

・内積 $K$-右加群 $V,W$、$K$-右準同型 $\alpha:V\to V$ とする。
このとき、内積 $K$-右準同型：
$$(\alpha(x),\alpha(y))_W=(x,y)_V$$

---

## 有限次元

### 正規直交基底

<dl><dt>

・有限次元内積 $K$-右加群 $V$ とする。


</dt><dd>

- $V$ は正規直交基底を持つ。

- 右一次独立な元の組に対して、それらを含む正規直交基底が存在する。

</dd></dl>

---

・有限次元内積 $K$-右加群 $V,W$ とする。
このとき、
$$\dim V=\dim W\iff V\cong W\ \ (\text{内積 $K$-右同型 })$$


---

### 基底の変換

・$n$ 次元内積 $K$-右加群 $V$、正規直交基底 $e_i,f_i$ とする。
ここで、
$$T=(t_{ij})\in M(n,K)\\\ \\
f_j=\sum_i e_it_{ij}$$と定めると、
$$T\in G(n,K)$$

---

### 共役と双対

・内積有限次元 $\bm{C}$ 加群 $V$ とする。
このとき、
$$\overline{V}\cong V^*\\
\psi(u)=\xi_u,\quad\xi_u(v)=(u,v)\\\ \\$$

- 内積有限次元 $\bm{C}$ 加群 $V$、基底 $u_i$ とする。
このとき、$u_i$ は $\overline{V}$ の基底。
<br>

- 内積有限次元 $\bm{C}$ 加群 $V$、正規直交基底 $u_i$ とする。
このとき、上記の同型において、$\psi(u_i)$ は $V^*$ の双対基底：$$\psi(u_i)(u_j)=\delta_{ij}$$

---
---
---

# $K$-多元環

    ・斜体では定義されない。
    ・環かつベクトル空間で、整合する。
    ・K-イデアルは部分空間なるイデアル。




---

# Banach単位的ノルム環

    ・Banach空間かつノルム環で乗法単位元を持つ。
    ・第一可算だから点列でよい。

## 収束ベキ級数

### 正規収束

・Banach単位的 $\bm{C,R}$-代数 $A$、集合 $Y$、$u_i:Y\to A$ とする。
このとき、正規収束級数：$\sum u_i(y)$：
$$\|u_p(y)\|\le c_p,\quad\sum c_p(y)\in\bm{C,R}$$

- $\sum u_i(y)$ は各点において絶対収束する。
- $\sum u_i(y)$ は一様収束する。
- $Y$ が位相空間かつ $u_i(y)$ が連続ならば、$\sum u_i(y)$　は連続関数。

---

### 収束半径

・$\bm{C,R}$ 係数ベキ級数 $F(x)=\sum a_ix^i$ に対して、
収束半径 $\rho$：
$$\rho=\sup\{r\ge0\ |\ \sum|a_i|r^i\in\bm{R}\}$$

    ・ρ>0 ならば収束ベキ級数という。

---

・Banach単位的 $\bm{C,R}$-代数 $A$、$\bm{C,R}$ 係数収束ベキ級数 $F(x)=\sum a_ix^i$、収束半径 $\rho>0$ とする。
<br>

- $$\sum a_i\xi_i\quad(\{\xi\ |\ \|\xi\|\le r<\rho,\ 0<r\}$$は正規収束する。
<br>

- $$F(\xi):\{\xi\ |\ \|\xi\|<\rho\}\to\bm{C,R}\\\ \\
F(\xi)=\sum a_i\xi^i$$は連続関数。 

---

・$K$ 係数形式的ベキ級数 $F(x)=\sum a_ip^i$ 、収束半径 $\rho$ とする。

- $$\frac{1}{\rho}=\overline{\lim_{n\to\infty}}|a_n|^{1/n}\\\ \\
\frac{1}{\rho}=\lim_{n\to\infty}|\frac{a_n}{a_{n+1}}|$$

- $F'(x)=\sum_{n\ge1}na_nx^{n-1}$ において、収束半径は $F(x)$ と一致する。
<br>

- $F:\{z\in\bm{C,R}\ |\ |z|<\rho\}\to\bm{C,R},\quad F(z)=\sum a_nz^n$ とする。
このとき、$F$ は微分可能で、
$$\frac{d}{dz}F(z)=F'(z)=\sum_{n\ge1}na_nz^{n-1}$$

      ・実数上でも0を含む開区間で一致すればF(x)=G(x)

---

### 演算と収束

#### 和と積

<dl><dt>

・ともに収束半径 $\ge\rho>0$ である $\bm{C,R}$ 係数収束ベキ級数 $F(x),G(x)$ とする。
<br>

</dt><dd>

- $$A(x)=F(x)+G(x),\quad B(x)=F(x)G(x)$$とおくと、$A(x),B(x)$ の収束半径 $\ge\rho$ である。
さらに、Banach単位的 $\bm{C,R}$-代数 $A$、$\|\xi\|<\rho$ なる $\xi\in A$ とすると、
$$A(\xi)=F(\xi)+G(\xi),\quad B(\xi)=F(\xi)G(\xi)\\\ \\$$

- Banach単位的 $\bm{C,R}$-代数 $A$、絶対収束級数 $\sum\xi_p,\ \sum\eta_p\sub A$ とする。
このとき、$$\zeta_p=\sum_{k=0}^p \xi_k\eta_{p-k}$$と定めると、
$\sum \zeta_p$ は絶対収束し、
$$\sum\zeta_p=\left(\sum\xi_q\right)\left(\sum\eta_p\right)$$

</dd></dl>

---

#### 合成

<dl><dt>

・$\bm{C,R}$ 係数収束ベキ級数 $F(x)=\sum a_px^p\ ,G(x)=\sum b_px^p,\ \mathrm{ord}(G)\ge1$、$H=F\circ G$、収束半径 $\rho(F),\ \rho(G),\ \rho(H)$ とする。
<br>

</dt><dd>

- $\exist\delta>0$ であって、$0<r<\delta$ ならば、
$$\sum |b_p|r^p<\rho(F),\quad r<\rho(G),\quad r<\rho(H)$$したがって、$H(x)$ は収束ベキ級数。
<br>

- $0<r$ を上記の仮定を満たす実数、Banach単位的 $\bm{C,R}$-代数 $A$、$\|\xi\|<r$ なる $\xi\in A$ とすると、
$$\|G(\xi)\|<\rho(F),\quad H(\xi)=F(G(\xi))$$


</dd></dl>


---

#### 線形写像とベキ級数

・Banach単位的 $\bm{C,R}$-代数 $A$、$\bm{C,R}$ 係数収束ベキ級数 $F(x)=\sum a_ix^i$、収束半径 $\rho>0$ とする。
また、$K$-単位的連続線形写像 $\psi:A\to A$ とする。

このとき、$\alpha\in B$ に対して $F(\alpha)$ が収束するならば、
$\psi(\alpha)$ も収束して、
$$F(\psi(\alpha))=\psi(F(\alpha))$$

---

### 収束する指数写像

<dl><dt>

・Banach単位的 $\bm{C,R}$-代数 $A$ とする。
このとき、
$$\exp:A\to A\\\ \\
\exp(\alpha)=\sum\frac{1}{n!}\alpha^n$$ は連続関数。
<br>

</dt><dd>

- $$\log:\{\alpha\in A\ |\ \|\alpha-1_A\|\le 1\}\to A\\\ \\
\log(\alpha)=\sum_{n\ge1}\frac{(-1)^{n-1}}{n}(\alpha-1_A)^n$$は連続関数。
<br>

- $$U=\{\alpha\in A\ |\ \|\alpha-1_A\|<1/2\},\quad N=\log U,\\\ \\
N_0=\{\alpha\in A\ |\ \|\alpha\|<\log 2\}$$ とする。
このとき、$\exp$ は $N_0$ 上単射で　
$$\log(\exp\alpha)=\alpha\ \ (\forall\alpha\in N_0)$$ であって、$N$ は$$N\sub N_0,\quad\exp N=U$$を満たす $0_A$ の開近傍。
さらに、$U$ は $1_A$ の開近傍で、開集合 $U,N$ は $\exp,\log$ によって同相。

</dd></dl>



---