
- [多様体がなす圏](#多様体がなす圏)
  - [束写像と共変関手](#束写像と共変関手)
- [$C^∞$ ベクトル束](#c-ベクトル束)
  - [部分集合と開集合](#部分集合と開集合)
  - [積束](#積束)
  - [正則部分多様体](#正則部分多様体)
- [判定](#判定)
  - [接束と $C^∞$ 切断の判定](#接束と-c-切断の判定)
  - [$C^{∞}$ 切断の判定](#c-切断の判定)
- [隆起関数](#隆起関数)



# 多様体がなす圏

## 束写像と共変関手

---
---
---


# $C^∞$ ベクトル束

## 部分集合と開集合

・ベクトル束 $(A,B,p,\bm{R}^r)$、部分集合 $W\sub B$ とする。
このとき、$(p^{-1}(W),W,p_{p^{-1}(W)},\bm{R}^r)$ はベクトル束。
<br>

- $C^{\infty}$ ベクトル束 $(A,B,p,\bm{R}^r)$、開集合 $U\sub B$ とする。
このとき、$(p^{-1}(U),U,p_{p^{-1}(U)},\bm{R}^r)$ は $C^{\infty}$ ベクトル束。

      ・開集合でないと多様体でない。

---

## 積束

・$m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、射影 $\pi:M\times\bm{R}^r\to M$ は $C^{\infty}$ 写像で、
$$\pi^{-1}(p)=\{p\}\times\bm{R}^r\\\ \\
\pi^{-1}(M)=M\times\bm{R}^r$$また、
$$id:M\times\bm{R}^r\to M\times\bm{R}^r\\\ \\$$と定めると、これは明らかに微分同相。
したがって、$(M\times\bm{R}^r,M,\pi,\bm{R}^r)$ は 階数 $r$ の $C^{\infty}$ ベクトル束。
これを積束という。

      ・円周S^1に対する円筒S^1×Rとか
<br>

- 
$$s_i:M\to M\times\bm{R}^r\\\ \\
s_i(p)=(p,e_i)$$
とする。
このとき、$s_1,...,s_r$ は積束 $(M\times\bm{R}^r,M,\pi,\bm{R}^r)$ の $C^{\infty}$ 枠。

---



## 正則部分多様体

- $m$ 次元 $C^{\infty}$ 多様体 $M$、$k$ 次元正則部分多様体 $S$ とする。
このとき、$(M,S,\pi)$ は $C^{\infty}$ ベクトル束。

      ・？？？横断性定理？

---

# 判定

## 接束と $C^∞$ 切断の判定

・判定：
$$\forall p\in M\text{ に対して、}p=\pi\circ s(p)\\\ \\
(\phi\circ\pi,c^1,...,c^m)\circ s\circ\phi^{-1}\text{ が }C^{\infty}$$
これは結局、ベクトル場 $X$ において、$X(p)=\sum a^i(p)\frac{\partial}{\partial x^i}|_p$ の各成分が $C^{\infty}$ であることと同値！

## $C^{∞}$ 切断の判定

・判定：
$$t_i:U\to\pi^{-1}(U)\quad(well-defined)\\\ \\
\pi\circ s_i(p)=p\\\ \\
t_i\text{ は }C^{\infty}\\\ \\
\forall p\in U\text{ に対して、}t_i(p)\in\pi^{-1}(p)\text{ の基底}$$

    ・ちゃんとr個あるか

---

# 隆起関数

・
$$f:(-1,1)\to\bm{R}\\\ \\
f(x)=\tan(\pi x/2)$$
に対して、$\mathrm{supp}f=(-1,1)$

    ・[-1,1]ではない。

