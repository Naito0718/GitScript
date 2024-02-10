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
- [Clifford多元環](#clifford多元環)
  - [対称内積を持つ $K$-加群](#対称内積を持つ-k-加群)
  - [Clifford多元環](#clifford多元環-1)
    - [直和とClifford](#直和とclifford)
    - [$Z2$ 次数付き $K$-多元環](#z2-次数付き-k-多元環)
      - [生成される $Z2$ 次数付き多元環](#生成される-z2-次数付き多元環)
    - [$R$ などに対する性質](#r-などに対する性質)


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

- $K$-右加群 $V,W$、テンソル積とそれに同型な $K$-右加群 $V\otimes W\cong X\ \ (f\text{ で }K\text{-右同型})$ とする。
このとき、$(X,f\circ\tau)$ は $V,W$ のテンソル積。

      ・一意性も確認！
<br>

---

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

<dl><dt>

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
<br>

    ・多項式環のように見るとよい。
    ・両方単位的ならば、生成されるやつも単位的。
<br>

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

<dl><dt>

    ・積：ab=a∧b、τ(u)=uと書く。

・可換体 $K$-加群 $V$ とする。
このとき、
$$\exist\ K\text{-単位的多元環 }\Lambda(V),\exist\ K\text{-準同型写像 }\tau:V\to T(V),\ \tau(u)^2=0 \text{ であって、}\\\ \\
\forall\ K\text{-単位的多元環 }A,\forall\ K\text{-準同型写像 }\phi:V\to A,\ \phi(u)^2=0\text{ に対して、}\exist\ !\ K\text{-多元環準同型 }\psi:V\to A\text{ であって、}\\\ \\
\phi=\psi\circ\tau$$ここで、$(\Lambda
(V),\tau)$ を外積 $K$-多元環という。
<br>

</dt><dd>

- 外積 $K$-多元環 $(\Lambda(V)_1,\tau_1),(\Lambda_2(V),\tau_2)$ とする。
このとき、$\tau_2=f\circ \tau_1,\ f(u)^2=0$ を満たす $K$-多元環同型
$$f:\Lambda_1(V)\to \Lambda_2(V)$$がただ一つ存在する。
<br>

      ・次数付き
<br> 

- $K$-同型な $K$-加群 $V,W,\ V\cong W\ (K\text{-同型})$、外積 $K$-多元環 $\Lambda(V),\Lambda(W)$ とする。
このとき、$$\Lambda(V)\cong \Lambda(W)\ \ (K\text{-多元環同型})$$ であり、$\Lambda(W)$ は $V$ の外積 $K$-多元環。
<br>

      ・f◦τでよい、2乗で0
      ・同様に、外積K-多元環と多元環同型なやつは、Vの外積K-多元環。
<br>

- $\tau$ は単射で、$$\tau(u)\tau(v)+\tau(v)\tau(u)=0\\\ \\
\Lambda(V)=\lang K,\tau(V)\rang\\\ \\$$

- - $$\Lambda(V)=T(V)/\mathfrak{a}(V),\quad \mathfrak{a}(V)=\left\{\sum a_ix_ib_i\ |\ x_i=\tau(u_i)^2,\ a_i,b_i\in T(V)\right\}\\\ \\
\tau(u)=[\tau_{T(V)}(u)]\\\ \\
\psi_{T(V)}(\mathfrak{a}(V))=0\text{ より、誘導される写像}\psi$$と定めると、$(\Lambda(V),\tau)$ は外積 $K$-多元環。
<br>

        ・分配法則は仮定する。
        ・多項式環みたいになってる。  
<br>

  - 上記の外積 $K$-多元環において、
  $$0_{T(V)}=0,\ \ 1_{T(V)}=1\in K\\\ \\$$

  - 上記の外積 $K$-多元環において、射影 $\pi:T(V)\to T(V)/\mathfrak{a}(V)$ とする。
  このとき、$\pi$ は $K$-多元環準同型で、$$\Lambda^r(V)=\pi(T^r(V))$$
  とすると、$$\Lambda(V)=\bigoplus_{r\ge0}\Lambda^r(V),\quad\Lambda^0(V)=K,\Lambda^1(V)=V$$であって、$\Lambda(V)$ は連結な次数付き $K$-多元環。
<br>

        ・任意の外積K-多元環もこの性質を保つ。
        ・後半の連結性とかは全単射から

</dd></dl>


---

#### 直和と外積

・$K$-多元環 $V=V_1\oplus V_2$、外積 $K$-多元環 $(\Lambda(V_1),\tau_1),(\Lambda(V_2)\tau_2)$ とする。
このとき、
$$\tau:V\to\Lambda(V_1)\hat{\otimes}\Lambda(V_2)\\\ \\
\tau(u_1+u_2)=\tau_1(u_1)\otimes1+1\otimes\tau(u_2)$$と定めると、$(\Lambda(V_1)\hat{\otimes}\Lambda(V_2),\tau)$ は $V$ の外積 $K$-多元環。
<br>

    ・次数付き同型でもある。
<br>

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

<dl><dt>

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


### $Z2$ 次数付き $K$-多元環

・$\bm{K}$-多元環 $A=A^0\oplus A^1$ とする。
このとき、$\bm{Z}_2$ 次数付き $K$-多元環：
$$A^0A^0,A^1A^1\sub A^0,\quad A^0A^1,A^1A^0\sub A^1\\\ \\$$

- $\bm{Z}_2$ 次数付き $K$-多元環 $A,B$、$K$-多元環準同型 $f:A\to B$ とする。
このとき、$\bm{Z}_2$ 次数付き $K$-多元環 $f$：$$f(A^r)\sub B^r$$

---

#### 生成される $Z2$ 次数付き多元環

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

### $R$ などに対する性質



---
---
---



