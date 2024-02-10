
- [離散空間](#離散空間)
  - [離散距離空間](#離散距離空間)
- [距離空間](#距離空間)
  - [開球 $B(x,r)$](#開球-bxr)
    - [有限個の開球の分割](#有限個の開球の分割)
    - [閉球を含む自然な開球](#閉球を含む自然な開球)
  - [集合距離 $d(A,B)$](#集合距離-dab)
  - [収束する点列](#収束する点列)
  - [直積距離空間](#直積距離空間)
    - [修正距離](#修正距離)
    - [直積距離](#直積距離)



# 離散空間

## 離散距離空間

・集合 $X$ とする。
このとき、
$$d:X\times X\to[0,\infty)\\\ \\
d(x,y)=\begin{cases}
1 & (x=y)  \\
0 & (x\neq y) \\
\end{cases}$$
と定めると、$d$ は $X$ 上の距離で、定まる位相は離散空間と同じ。

<br>

・距離空間 $X$、離散閉部分空間 $\Gamma\sub X$ とする。
このとき、
$$\Gamma\text{ が点列コンパクト}\iff \Gamma\text{ は有限集合}$$

    ・部分空間位相が離散位相。

---

# 距離空間

## 開球 $B(x,r)$

・開球 $B(x,r)=\{y\in X\ |\ d(x,y)<r\}$ は開集合

- 閉球 $\overline{B(x,r)}$ は閉集合

---

### 有限個の開球の分割

・有限個の開球 $B(x_i,r_i)\ \ (i=1,...,n)$ に対して、
$$\exist S\subset \{1,...,n\}\text{ であって、}\\\ \\
B(x_i,r_i)\cap B(x_j,r_j)=\phi\quad(i,j\in S,\ i\neq j)\\\ \\
\bigcup_{i=1}^n B(x_i,r_i)\sub \bigcup_{j\in S}B(x_j,3r_j)$$

      ・ルベーグ測度のとこで出てきた。

---

### 閉球を含む自然な開球

・距離空間 $X$、開集合 $D\sub X$、コンパクト集合 $K\sub D$ とする。
このとき、
$$\exist\delta>0\text{ であって、}K\sub\{x\in X\ |\ d(x,K)<\delta\}\sub D\\\ \\$$

    ・真ん中の集合は開集合。あと、点列コンパクト性よりあるy∊Kでd(x,K)=d(x,y)
<br>

- 距離空間 $X$、$a\in X$、$r,\delta>0$ とする。
このとき、
$$\left\{x\in X\ |\ d\left(x,\overline{B(a,r)}\right)<\delta\right\}\sub B(a,r+\delta)\\\ \\$$

      ・Xがノルム空間なら等号成り立つ?R^Nなら成り立つ。

---

## 集合距離 $d(A,B)$

    ・infのやつ

<dl><dt>

・距離空間 $(X,d)$、部分集合 $E,F\sub X$ とする。

</dt><dd>


- 
$$d(x,E)=0\iff x\in\overline{E}\\\ \\$$

- $r>0$ とする。
このとき、
$$\{x\in X\ |\ d(x,E)>r\},\ \ \{x\in X\ |\ d(x,E)<r\}$$
はともに $X$ の開集合。
<br>

- $$d(E,F)=d(\overline{E},F)\\\ \\$$

- コンパクト集合 $\phi\neq K\sub X$、開集合 $V\supset K$ とする。
このとき、$$d(K,X-V)>0$$


</dd></dl> 


---

## 収束する点列

<dl><dt>

・距離空間 $X$、収束点列 $(x_n)\sub X,\ \lim_{n\to\infty}x_n=x\in X$ とする。

</dt><dd>

- 任意の部分列 $x_{n(k)}$ も収束列であって、$\lim_{n\to\infty}x_{k(n)}=x$

- $$\{x_n\ |\ n\in\bm{N}\}$$ は有界集合

</dd></dl> 

## 直積距離空間

### 修正距離

<dl><dt>

・距離空間 $(X,d)$ とする。
このとき、
$$d_r:X\to[0,\infty)\\\ \\
d_r(x,y)=\min\{1,d(x,y)\}$$
と定めると、これは距離。
<br>

</dt><dd>

- $x,y\in X$、$0<\epsilon\le1$ とする。
このとき、
$$d(x,y)<\epsilon\iff d_r(x,y)<\epsilon$$
よって、$\mathcal{O}_d=\mathcal{O}_{d_r}$ が成り立つ。
<br>

- 完備距離空間 $(X,d)$ とする。
このとき、$(X,d_r)$ は完備距離空間。

</dd></dl> 

---

### 直積距離

・距離空間の列 $(X_n,d_n)$ とする。
このとき、
$$d:\Pi_{n\in\bm{N}}X_n\to[0,\infty)\\\ \\
d(x,y)=\sum_{n=1}^{\infty} \frac{1}{2^n}\Big[\min\{1,d_n(p_n(x),p_n(y))\}\Big]$$
と定めると、これはwell-defined。



