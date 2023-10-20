
- [複素数上の計算](#複素数上の計算)
  - [共役](#共役)
  - [自然数乗](#自然数乗)
  - [共役微分](#共役微分)
- [実点列](#実点列)
- [実級数](#実級数)
  - [$√1+x$](#1x)
  - [$1/√1+x$](#11x)
- [複素級数](#複素級数)
  - [項別線積分](#項別線積分)
- [実二重級数](#実二重級数)
- [実 $n$ 重級数](#実-n-重級数)
  - [$∑x^I$](#xi)
  - [微分に使うやつ](#微分に使うやつ)
- [実解析的関数](#実解析的関数)
  - [一変数](#一変数)
  - [多項式](#多項式)
  - [有理式](#有理式)

# 複素数上の計算

## 共役

・$\overline{z}=re^{-i\theta}$ とすることもできる。

## 自然数乗

・$$z^n=w\quad(n\in\bm{N},\ w\in\bm{C})$$ とする。
このとき、
$$r=^n\sqrt{|w|}\ge0,\quad\cos\theta=\frac{\mathrm{Re}(w)}{|w|},\ \sin\theta=\frac{\mathrm{Im}(w)}{|w|}\\\ \\
z=re^{i\theta}\\\ \\$$

- 
$$z^n=x\quad(n\in\bm{N},\ x\in\bm{R})$$
とすると、
$$z=re^{i\theta}\\\ \\
\begin{cases}
r=0,\ \theta\in[0,2\pi) &  (x=0) \\
r=^n\sqrt{x}>0,\ \theta=\frac{2\pi k}{n}\ (k=0,1,...,n-1) &  (x>0) \\
r=^n\sqrt{-x}>0, \ \theta=\frac{(2k+1)\pi}{n}\ (k=0,1,...,n-1)& (x<0) \\
\end{cases}$$

## 共役微分

・
$$\overline{\frac{\partial f}{\partial z}}=\frac{\partial\overline{f}}{\partial\overline{z}},\quad \overline{\frac{\partial f}{\partial \overline{z}}}=\frac{\partial\overline{f}}{\partial z}\\\ \\
\frac{\partial z}{\partial\overline{z}}=0,\quad\frac{\partial z}{\partial z}=1$$

---
---
---


# 実点列



---

# 実級数

・実級数$f(x)=\sum c_nx^n$に対して、定義域を複素数に拡張することができる
⇒というか複素数上の制限とみるのか？

    ・絶対収束する級数について、拡大前と拡大後の収束範囲は整合する。したがって実級数でも収束半径を考えることができる

---

## $√1+x$

・

---

## $1/√1+x$

---
---
---

# 複素級数

・$$F(x)=\sum_ix^i\quad(x_i\in\bm{C})$$ とする。
このとき、$|x|<1$ なら $F(x)$ は絶対収束し、
$$F(x)=\frac{1}{(1-x_1)}$$

- 閉円板 $D(0,r)\subsetneq D(0,1)$ 上で、 $F(x)$ は正規収束する。

## 項別線積分

    ・∫f(z(t))z'(t)dt のこと

・$$

---

# 実二重級数


---

# 実 $n$ 重級数

## $∑x^I$

  ・複素数でも同様。

・$$F(x)=\sum_Ix^I\quad(x_i\in\bm{R})$$ とする。
このとき、$|x_i|<1$ なら $F(x)$ は絶対収束し、
$$F(x)=\frac{1}{(1-x_1)...(1-x_n)}$$

- $Q=\{\bm{x}\ |\ |x_i|\le r_i<1 \}$ 上で、 $F(x)$ は正規収束する。

---

## 微分に使うやつ

    ・複素数でも同様。

・$$F(x)=\sum_{i_1,...,i_n=0,i_k=1}i_ka_{i_1,...,i_n}x_1^{i_1}...x^{i_k-1}...x^{i_n},\\\ \\
...\\\ \\
G(x)=\sum_{i_1,...,i_n=1}i_1...i_na_{i_1,...,i_n}x_1^{i_1-1}...x^{i_n-1}$$
とする。
このとき、$|x_i|<1$ なら $F(x),...,G(x)$ は絶対収束する。

---


# 実解析的関数

## 一変数

    ・sinとかもか

## 多項式

## 有理式



