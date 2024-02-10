
- [表現](#表現)
  - [表現写像](#表現写像)
    - [表現写像との関係](#表現写像との関係)
- [無限次元表現](#無限次元表現)
- [種々の生成される表現](#種々の生成される表現)
  - [直和表現](#直和表現)
    - [直和表現の簡単な性質](#直和表現の簡単な性質)
  - [テンソル積表現](#テンソル積表現)
    - [直和表現との関係](#直和表現との関係)
  - [双対表現](#双対表現)
    - [直和,テンソル積表現との関係](#直和テンソル積表現との関係)
    - [$Hom(V,W)$](#homvw)
    - [一次元](#一次元)
  - [共役表現](#共役表現)
    - [直和,テンソル積,双対表現との関係](#直和テンソル積双対表現との関係)
  - [外積表現](#外積表現)



# 表現

<dl><dt>

・位相群 $G$ が有限次元 $\bm{H}$-加群 $V$ に群として作用するとする。
このとき、位相群 $G$ による作用：
$$\exist\text{ 基底 }u_i\text{ に対して、}xu_i=\sum u_ja_{ji}(x)\text{ と表すとき、}\\\ \\
a_{ji}:G\to K\text{ が連続}$$
これが成り立つとき、$V$ を $G-\bm{H}$ 加群という。

    ・Vに位相入ってないのか！

<br>

- 位相群 $G$、$G-\bm{H}$ 加群 $V$、部分空間 $W\sub V$ とする。
このとき、部分 $G-\bm{H}$ 加群：
$$\forall g\in G,w\in W\text{ に対して、}gw\in W$$

      ・商空間も同様に成り立つ。（係数関数の連続性もよい）
<br>

</dt><dd>

- 位相群 $G$、有限次元 $\bm{H}$ 右加群 $V$ 、ベクトル空間への作用 $\Psi:G\times V\to V$ とする。また、$V$ には $\bm{R}^N$ と同様の位相を入れる。
このとき、
$$\Psi\text{ が連続}\iff V\text{ は }G-\bm{H}\text{ 加群}\\\ \\$$

      ・どうせノルムは全部同値。
      ・Vが位相線形空間なら、⇐は成り立つ。
<br>

- 位相群 $G$、$G-\bm{H}$ 加群 $V,W$、$\bm{H}$-準同型 $f:V\to W$ とする。
このとき、$G-\bm{H}$ 準同型：
$$f(gv)=gf(v)$$

      ・逆もG-H準同型。

</dd></dl>

---

## 表現写像

・位相群 $G$ とする。
このとき、$n$ 次元 $\bm{H}$ 表現 $A$：
$$\text{連続群準同型 }A:G→GL(n,\bm{H})\\\ \\$$

- 位相群 $G$、表現 $A:G→GL(n,\bm{H})$、$P\in GL(n,\bm{H})$ とする。
このとき、
$$PAP^{-1}:G\to GL(n,\bm{H})\\\ \\
PAP^{-1}(g)=PA(g)P^{-1}$$は $G$ の表現。
<br>

- 位相群 $G$、$n$ 次元 $\bm{H}$ 表現全体の集合 $R(G,n,\bm{H})$、$A,B\in R(G,n,\bm{H})$ とする。
このとき、
$$A\sim B\iff \exist P\in GL(n,\bm{H})\text{ であって、}A=PBP^{-1}$$
は $R(G,n,\bm{H})$ 上の同値関係。

---

### 表現写像との関係

<dl><dt>

・位相群 $G$ とする。
このとき、有限 $(\ge1)$ 次元 $G-\bm{H}$ 加群の $G-\bm{H}$ 同型類と、$G$ の 有限 $(\ge1)$ 次元 $\bm{H}$-表現同値類全体の集合との間には全単射が存在し、
$$gu_i=\sum u_ja_{ji}(g)\text{ に対して、}A(g)=(a_{ij}(g))\\\ \\
A(g)=(a_{ij}(g))\text{ に対して、}gu_i=\sum u_ja_{ji}(g)$$

    ・0のときはただの一致。
    ・表現の同値類は上のR(G,n,H)のやつ。

</dt><dd>

- 上記の対応において、$A:G\to GL(n,\bm{H})$ は表現で、$gu$ は位相群 $G$ による有限次元 $\bm{H}$ 加群への作用。
<br>

- $V$ の別の基底に対して定まる表現 $A'$ に対して、$A\sim A'$
また、$V\cong W$ ならば、その表現 $B$ に対して、$A\sim B$
<br>

- $V$ の別の基底に対して定まる $G-\bm{H}$ 加群 $V'$ に対して、$V\cong V'$
また、$A\sim B$ ならば、$V$ のそれぞれの基底に対して定まる $G-\bm{H}$ 加群 $V,V'$ に対して、$V\cong V'$

</dd></dl>

---

# 無限次元表現

・位相群 $G$、可換体 $K$ 上ベクトル空間 $V$、$\pi:G\to GL_K(V)$ とする。
このとき、連続表現 $(\pi,V)$：
$$\pi\text{ は連続でなくてもよい群準同型で、}\\\ \\
\psi:G\times V\to V,\quad \pi(g,h)=\pi(g)v\text{ は連続}$$

    ・この連続でなくてもよい群準同型πって作用のことか。

---
---
---


# 種々の生成される表現

## 直和表現

<dl><dt>

・位相群 $G$、$G-\bm{H}$ 加群 $V,W$ とする。
このとき、
$$(v,w)\in V\oplus W\text{ に対して、}\\\ \\
g(v,w)=(gv,gw)$$ は $G-\bm{H}$ 加群。

    ・別に無限でもよい。
    ・VとWの次元は異なっててよい。

・位相群 $G$、表現 $A:G\to GL(n,\bm{H}),\ B:G\to GL(m,\bm{H})$ とする。
このとき、
$$A\oplus B:G\to GL(n+m,\bm{H})\\\ \\
A\oplus B(g)=\begin{pmatrix}
A(g) & 0    \\
0 & B(g)    \\
\end{pmatrix}$$は $G$ の表現。
<br>

</dt><dd>

- 位相群 $G$、（有限次元） $G-\bm{H}$ 加群 $V,V',W,W'$ とし、$V\cong V',\ W\cong W'\quad(G-\bm{H}\text{ 同型})$ とする。
このとき、
$$V\oplus W\cong V'\oplus W'\quad(G-\bm{H}\text{ 同型})\\\ \\$$

- 位相群 $G$、有限次元 $G-\bm{H}$ 加群 $V,W$、基底 $v_i,w_i$ とし、その基底に対する表現を $A,B$ とする。
このとき、$G-\bm{H}$ 加群 $V\oplus W$ の基底 $(v_i,0),(0,w_j)$ に関する $G$ の表現は $A\oplus B$。

</dd></dl>

---

### 直和表現の簡単な性質

・位相群 $G$、有限次元 $G-\bm{H}$ 加群 $V,W,U$ とする。
このとき、
$$V\oplus W\cong W\oplus V\ \ (G-\bm{H}\text{同型})\\\ \\
V\oplus (W\oplus U)\cong (V\oplus W)\oplus U\ \ (G-\bm{H}\text{同型})\\\ \\
V\oplus 0\cong V\ \ (G-\bm{H}\text{同型})$$



---

## テンソル積表現 

<dl><dt>

・位相群 $G$、有限次元 $G-\bm{H}$ 加群 $V,W$ とする。
このとき、
$$v\otimes w\in V\otimes W\text{ に対して、}\\\ \\
g(v\otimes w)=(gv)\otimes(gw)$$ は $G-\bm{H}$ 加群。

- 位相群 $G$、表現 $A:G\to GL(n,\bm{H}),\ B:G\to GL(m,\bm{H})$ とする。
このとき、
$$A\otimes B:G\to GL(nm,\bm{H})\\\ \\
A\otimes B(g)=\begin{pmatrix}
A(g)b_{11}(g) & \cdots & A(x)b_{1m}(g)    \\
\cdots & \cdots & \cdots    \\
A(g)b_{m1}(g) & \cdots & A(x)b_{mm}(g) 
\end{pmatrix}$$は $G$ の表現。ここで、$(A\otimes B(g))^{-1}=A(g)^{-1}\otimes B(g)^{-1}$
<br>

</dt><dd>

- 位相群 $G$、有限次元 $G-\bm{H}$ 加群 $V,V',W,W'$ とし、$V\cong V',\ W\cong W'\quad(G-\bm{H}\text{ 同型})$ とする。
このとき、
$$V\otimes W\cong V'\otimes W'\quad(G-\bm{H}\text{ 同型})\\\ \\$$

- 位相群 $G$、有限次元 $G-\bm{H}$ 加群 $V,W$、基底 $v_i,w_i$ とし、その基底に対する表現を $A,B$ とする。
このとき、$G-\bm{H}$ 加群 $V\otimes W$ の基底 $v_1\otimes w_1,...,v_n\otimes w_1,...$ に関する $G$ の表現は $A\otimes B$。


</dd></dl>

---

### 直和表現との関係

・位相群 $G$、有限次元 $G-\bm{H}$ 加群 $V,W,U$ とする。
このとき、
$$V\otimes W\cong W\otimes V\ \ (G-\bm{H}\text{同型})\\
\psi(v\otimes w)=w\otimes v\ \ \\\ \\
V\otimes (W\otimes U)\cong (V\otimes W)\otimes U\cong V\otimes W\otimes U\ \ (G-\bm{H}\text{同型})\\
\psi(v\otimes w\otimes u)=v\otimes(w\otimes u)\\\ \\
(V\oplus W)\otimes U\cong (V\otimes U)\oplus (W\otimes U)\\
\psi((v,w)\otimes u)=(v\otimes u,w\otimes u)\\\ \\
V\otimes \bm{H}\cong V\ (G-\bm{H}\text{同型})\\
\psi(u\otimes \alpha)=u\alpha$$

    ・Hへの作用は単位的作用とする。

---


## 双対表現

・位相群 $G$、有限次元 $G-\bm{H}$ 加群 $V$、双対 $\bm{H}$ 加群 $V^{\vee}$、$\xi\in V^{\vee}$ とする。
このとき、
$$g\xi(v)=\xi(g^{-1}v)$$
とすると、これは表現。
<br>

- 位相群 $G$、表現 $A:G\to GL(n,\bm{H})$ とする。
このとき、
$$A^{\vee}:G\to GL(n,\bm{H})\\\ \\
A^{\vee}(g)=A(g^{-1})^T$$は $G$ の表現。
<br>

</dt><dd>

- 位相群 $G$、有限次元 $G-\bm{H}$ 加群 $V$、基底 $v_i$ とし、その基底に対する表現を $A$ とする。
このとき、$G-\bm{H}$ 加群 $V^{\vee}$ の双対基底 $f_i$ に関する $G$ の表現は $A^{\vee}$。


</dd></dl>

---

### 直和,テンソル積表現との関係

・位相群 $G$、有限次元 $G-\bm{H}$ 加群 $V,W$ とする。
このとき、
$$V^{\vee}\oplus W^{\vee}\cong (V\oplus W)^{\vee}\ \ (G-\bm{H}\text{同型})\\\ \\
\phi(\xi,\eta)(v,w)=\xi(v)+\eta(w)\\\ \\ \\\ \\
V^{\vee}\otimes W^{\vee}\cong(V\otimes W)^{\vee} \ \ (G-\bm{H}\text{同型})\\\ \\
\phi(\xi\otimes\eta)(v\otimes w)=\xi(v)\eta(w)\\\ \\ \\\ \\
V\cong (V^{\vee})^{\vee}\ \ (G-\bm{H}\text{同型})\\\ \\
\phi(v)(\xi)=\xi(v)\\\ \\$$

---

### $Hom(V,W)$

・位相群 $G$、有限次元 $G-\bm{H}$ 加群 $V,W$、$A\in\mathrm{Hom}(V,W)$ とする。
このとき、
$$(gA)(v)=g[A(g^{-1}v)]$$
とすると、これは表現。
<br>

- 位相群 $G$、有限次元 $G-\bm{H}$ 加群 $V,W$ とする。
このとき、
$$V^{\vee}\otimes W\cong \mathrm{Hom}(V,W)\ \ (G-\bm{H}\text{同型})\\\ \\
\phi(\xi\otimes W)(v)=w(\xi(v))\\\ \\$$

---

### 一次元 

・位相群 $G$、$1$ 次元 $G-\bm{H}$ 加群 $V$ とする。
このとき、
$$V\otimes V^{\vee}\cong K\\\ \\
\phi(\xi\otimes v)=\xi(v)$$

    ・テンソル積の次元的に、一次元でしか成り立たない。


---


## 共役表現

    ・複素数上だけ。

・位相群 $G$、有限次元 $G-\bm{C}$ 加群 $V$、共役 $\bm{C}$ 加群 $\overline{V}$ とする。
このとき、$\overline{V}$ は $V$ と同じ作用で $G-\bm{C}$ 加群。
<br>

- 位相群 $G$、表現 $A:G\to GL(n,\bm{C})$ とする。
このとき、
$$\overline{A}:G\to GL(n,\bm{H})\\\ \\
\overline{A}(g)=\overline{A(g)}$$は $G$ の表現。
<br>

</dt><dd>

- 位相群 $G$、有限次元 $G-\bm{C}$ 加群 $V$、基底 $v_i$ とし、その基底に対する表現を $A$ とする。
このとき、$G-\bm{C}$ 加群 $\overline{V}$ の基底 $v_i$ に関する $G$ の表現は $\overline{A}$


</dd></dl>

---

### 直和,テンソル積,双対表現との関係

・位相群 $G$、有限次元 $G-\bm{C}$ 加群 $V,W$ とする。
このとき、
$$\overline{V}\oplus \overline{W}\cong \overline{V\oplus W}\ \ (G-\bm{C}\text{同型})\\\ \\
\overline{V}\otimes \overline{W}\cong\overline{V\otimes W}\ \ (G-\bm{C}\text{同型})\\\ \\
V\cong \overline{\overline{V}}\ \ (G-\bm{C}\text{同型})\\\ \\
overline{V^{\vee}}\cong(\overline{V})^{\vee}\\\ \\
\phi(\xi)=\overline{\xi}$$

    ・最後のは全部の値で共役を取るようにしたやつ。

---

## 外積表現

    ・R,C（可換体）だけ。（M(n,H)、GL(n,H)とかが無いから）

・有限次元 $G-\bm{C}$ 加群 $V$、$r$ 次外積 $\bm{C}$-加群 $\Lambda^r(V)$ とする。
このとき、
$$u_1\wedge...\wedge u_r\in V\otimes W\in V\otimes W\text{ に対して、}\\\ \\
g(u_1\wedge...\wedge u_r)=(gu_1)\wedge...\wedge(gu_r)$$ は $G-\bm{C}$ 加群。

    ・無限次元でもwell-definedではある。+--


---
---
---

