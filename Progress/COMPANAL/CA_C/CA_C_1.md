
- [複素数上の計算](#複素数上の計算)
  - [共役](#共役)
  - [自然数乗](#自然数乗)
  - [共役微分](#共役微分)
- [複素級数](#複素級数)
  - [広義一様収束](#広義一様収束)
  - [二重級数と広義一様収束](#二重級数と広義一様収束)
- [実 $n$ 重級数](#実-n-重級数)
  - [$∑x^I$](#xi)
  - [微分に使うやつ](#微分に使うやつ)

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





---

# 複素級数

・$$F(x)=\sum_ix^i\quad(x_i\in\bm{C})$$ とする。
このとき、$|x|<1$ なら $F(x)$ は絶対収束し、
$$F(x)=\frac{1}{(1-x_1)}$$

- 閉円板 $D(0,r)\subsetneq D(0,1)$ 上で、 $F(x)$ は正規収束する。

---

## 広義一様収束

・$a\in\bm{C}$、収束ベキ級数 $\sum_{n\in\bm{N}}a_n(z-a)^n$、収束半径 $\rho>0$ とする。
このとき、
$$\sum_{n\in\bm{N}}a_n(z-a)^n\text{ は }\{z\in\bm{C}\ |\ |z-a|<\rho\}\text{ 内で広義一様収束する}$$

---

## 二重級数と広義一様収束

・$a\in\bm{C}$、収束半径 $\rho_k>r>0$ の収束ベキ級数 $f_{k}=\sum_{n\in\bm{N}}a_{n,k}(z-a)^n$ とする。
このとき、
$$F_N:B(a,r)\to\bm{C},\quad F_N(z)=\sum_{k=0}^{N}f_n(z)\\\ \\
\text{ が }B(a,r)\text{ 上 }F(z)=\sum_{k=0}^{\infty}f_n(z)\text{ に広義一様収束 }\\\ \\
\Rightarrow F\text{ は }B(a,r)\text{ 上正則であって、}\forall n\in\bm{N}\text{ に対して、}A_n=\sum_{k\in\bm{N}}a_{n,k}\in\bm{C}\text{ であって、}\\\ \\
\forall z\in B(a,r)\text{ に対して、}F(z)=\sum_{n\in\bm{N}}A_n(z-a)^n$$

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



