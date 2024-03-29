
- [直積空間と連結性](#直積空間と連結性)
  - [道](#道)
  - [基本群](#基本群)
- [弧状連結空間の具体例](#弧状連結空間の具体例)
  - [簡単な弧状連結空間](#簡単な弧状連結空間)
- [簡単なホモトピー](#簡単なホモトピー)
  - [固定ホモトピー](#固定ホモトピー)
- [簡単なファイバー空間](#簡単なファイバー空間)
  - [部分集合](#部分集合)
  - [直積空間](#直積空間)



# 直積空間と連結性

・位相空間 $X,Y$ とする。
このとき、
$$X,Y\text{ は弧状連結}\iff X\times Y\text{は弧状連結}$$

---

## 道

・位相空間 $X,Y$、ホモトープな $X$ の道 $k_1\sim k_2$、ホモトープな $Y$ の道 $l_1\sim l_2$ とする。
このとき、
$$k_1\times l_1\sim k_2\sim l_2$$

---

## 基本群

・位相空間 $X,Y$、$(x,y)\in X\times Y$、射影 $p_{X}:X\times Y\to X$ とする。
このとき、
$$(p_X)_*\times (p_Y)_*:\pi(X\times Y,(x,y))\to\pi(X,x)\times\pi(Y,y)$$
と定めると、これは群同型写像。
<br>

- 単連結空間 $X,Y$ に対して、$X\times Y$ は単連結。

---

# 弧状連結空間の具体例

## 簡単な弧状連結空間

・一点集合 $\{x\}$ は弧状連結。

- 離散空間 $X$ の弧状連結成分は、一点集合 $\{x\}$ からなる。

      ・離散空間の語源？

---


# 簡単なホモトピー

## 固定ホモトピー

・位相空間 $X,Y$、$A\subset X$、部分集合 $A$ 上で一致する連続写像 $f,g:X\to Y$ とする。
このとき、$A$ を固定したホモトピー：
$$f\sim g\\\ \\
\iff\exist\text{ 連続写像かつ $f,g$ のホモトピー }H:X\times I\to X\text{ であって、}\\\ \\
H(a,t)=f(a)=g(a)\quad(\forall (a,t)\in A\times I)$$は同値関係。

    ・道のホモトピーは端点固定ホモトピー。



---


# 簡単なファイバー空間

## 部分集合

・ファイバー空間 $(A,B,p,F)$、$W\sub B$ とする。
このとき、$(p^{-1}(W),W,p_{p^{-1}(W)},F)$ はファイバー空間。

    ・結局制限するだけ。

## 直積空間

・位相空間 $X,Y$、射影 $p_X:X\times Y\to X$ とする。
このとき、$(X\times Y,X,p_X,Y;\{e\})$ はファイバー束であって、
自明化：$$U=X,\ \phi(x,y)=(x,y)$$

