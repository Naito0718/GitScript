
- [Hilbert空間から定まるベクトル空間](#hilbert空間から定まるベクトル空間)
  - [閉部分空間](#閉部分空間)
  - [双対空間 $X$\*](#双対空間-x)
  - [直和Hilbert空間](#直和hilbert空間)
- [最適近似](#最適近似)
  - [閉部分空間と最適近似](#閉部分空間と最適近似)



# Hilbert空間から定まるベクトル空間

## 閉部分空間

・$\bm{R,C}$ 上Hilbert空間 $V$、部分空間 $M\subset V$ とする。
このとき、
$$M\text{ が }V\text{ の内積でHilbert空間}\iff\overline{M}=M$$

---

## 双対空間 $X$*

・$\bm{C}$ 上ヒルベルト空間 $\mathcal{H}$、双対空間 $\mathcal{H}^*$ とする。
このとき、
$$\phi:\mathcal{H}\to\mathcal{H}^*\\\ \\
\phi(v)=(v,\cdot)$$
と定めると、これは全単射反線形写像で、$$\|v\|=\|\phi(v)\|\\\ \\$$

    ・別にv=0でも成り立つ
    ・R上でも同様。

---

## 直和Hilbert空間

    ・どこで出てくんの？

・空でない集合 $J$、$\bm{C}$ 上Hilbert空間 $\mathcal{H}_j$、$l^2$ 直和Banach空間 $\oplus_{j\in J}\mathcal{H}_j$ 、$u,v\in\oplus_{j\in J}\mathcal{H}_j$とする。
このとき、$$(u,v)=\sum_{j\in J}(u_j,v_j)_j$$と定める。

    ・別に実数上でもいい。

- $\sum_{j\in J}|(u_j,v_j)|\le\|u\|\|v\|$、特に、$(u_j,v_j)_{j\in J}\in l^1(J)$
<br>

- $\oplus_{j\in J}\mathcal{H}_j$ はHilbert空間

---
---
---

# 最適近似

・ヒルベルト空間 $\mathcal{H}$、閉凸集合 $C$ 、$u\in\mathcal{H}$とする。
このとき、
$$\exist u_0\in C\text{ であって、}\|u-u_0\|=d(u,C)\\\ \\$$

    ・d(u,C)はCとのinf距離のこと。よって、infでなくてminでよい。

---

## 閉部分空間と最適近似

・ヒルベルト空間 $V$、閉部分空間 $M\sub V$、$u_0\in M$、$u\in V$ とする。
このとき、
$$\|u-u_0\|=d(u,M)\iff u=Pu\\\ \\$$

    ・Pは直交補空間との正射影。