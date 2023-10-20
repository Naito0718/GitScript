
- [距離空間](#距離空間)
  - [開球 $B(x,r)$](#開球-bxr)
    - [有限個の開球の分割](#有限個の開球の分割)
  - [集合距離 $d(A,B)$](#集合距離-dab)
  - [収束する点列](#収束する点列)
- [$R$](#r)
  - [連結性](#連結性)
  - [写像 $f$](#写像-f)
        - [$C,R$ への写像](#cr-への写像)
        - [区間の同値類別と円周 $S^1$](#区間の同値類別と円周-s1)
  - [Lebesgue測度](#lebesgue測度)
    - [定義](#定義)
  - [整数 $Z$](#整数-z)
  - [単位円と区間](#単位円と区間)



# 距離空間

## 開球 $B(x,r)$

・開球 $B(x,r)=\{y\in X\ |\ d(x,y)<r\}$ は開集合

- 閉球 $\overline{B(x,r)}$ は閉集合

### 有限個の開球の分割

・有限個の開球 $B(x_i,r_i)\ \ (i=1,...,n)$ に対して、
$$\exist S\subset \{1,...,n\}\text{ であって、}\\\ \\
B(x_i,r_i)\cap B(x_j,r_j)=\phi\quad(i,j\in S,\ i\neq j)\\\ \\
\bigcup_{i=1}^n B(x_i,r_i)\sub \bigcup_{j\in S}B(x_j,3r_j)$$

      ・ルベーグ測度のとこで出てきた。

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

- $$d(E,F)=d(\overline{E},F)$$

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



---
---
---
# $R$

    ・R^nは微分幾何

## 連結性

・空でない凸集合は弧状連結

→開球体、閉球体も弧状連結

---

## 写像 $f$

##### $C,R$ への写像

・絶対値とか和の連続性

---

##### 区間の同値類別と円周 $S^1$

・区間 $[0,1]$ に対する同値関係：
$$x\sim y\iff x=y\ or\ (x,y)=(1,0),(0,1)$$

- 同値類全体の集合：$I/\sim\ \cong[0,1)$。
さらに、$I/\sim\ \cong S^1,\quad f(t)=(\sin2\pi t,\cos2\pi t)$

        ・集合として、位相でない、近くとみなしたいならS^1
        ・できるだけ似ているように同値類別の代表元を選びたい！→胞体分割

---

## Lebesgue測度

### 定義

・$f\in C_{c,\bm{R}}(\bm{R})$ に対して、
$$\Lambda:C_{c,\bm{R}}(\bm{R})\to\bm{R} \\\ \\
\Lambda(f)=\int_Ifdx\quad(\mathrm{supp}f\subset \text{有界閉区間 }I,\ \text{リーマン積分})$$はRadon汎関数。
したがって、
$$m:\mathfrak{B}_{\bm{R}}\to [0,\infty]\\\ \\
\Lambda f=\int_{\bm{R}}fdm\quad(\forall f\in C_{c,\bm{R}}(\bm{R}))$$を満たすRadon測度 $m$ がただ一つ存在する。
よって、この測度をLebesgue測度とする。

- $\bm{R}$ 上のLebesgue測度 $m$ に対して、$m([b-a])=b-a$

      ・普通の意味での長さを与える。

---

## 整数 $Z$

・$\bm{Z}$ は $\bm{R}$ の離散部分群。

---

## 単位円と区間

・$I=[0,1]$、$A={0,1}$ とする。
このとき、$A$ を点とみなした集合 $I/A$、単位円 $S^1$ に対して、
$$I/A\cong S^1\ (\text{同相})$$

- $A=(-\infty,0]\cup[1,\infty)\sub\bm{R}$ とする。
このとき、$A$ を点とみなした集合 $\bm{R}/A$、単位円 $S^1$ に対して、
$$\bm{R}/A\cong S^1\ (\text{同相})$$