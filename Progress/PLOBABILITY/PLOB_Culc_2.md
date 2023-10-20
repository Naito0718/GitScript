


# 有限な標本空間

## いつもの

・有限（実）標本空間 $\Omega_N$ とする。
このとき、単純平均、単純分散 $m(\bm{x}),\ s^2(\bm{x})$
$$m,s^2:\Omega_N\to\bm{R}\\\ \\
m(\bm{x})=\frac{1}{N}\sum x_i\\\ \\
s(\bm{x})^2=\frac{1}{N}\sum (x_i-\overline{\bm{x}})^2\\\ \\$$

    ・全部をまとめたベクトル：x

- $a\in\bm{R},\ \bm{b}=(b_1,...,b_N)\in\bm{R}^N$ とする。
このとき、
$$m(\bm{ax+b})=am(\bm{x})+b\\\ \\
s^2(a\bm{x}+\bm{b})=a^2s^2(\bm{x})$$

      ・標本空間でスカラー倍と和が定義されてる場合。

---

・標準化：
$$\bm{z}=\frac{\bm{x}-\overline{\bm{x}}}{s(\bm{x})}$$
とする。このとき、
$$\overline{\bm{z}}=0\\\ \\
s^2(\bm{z})=1$$

---

# 二次元データ

    ・データの数は同じ

## 共分散

・共分散 
$$s^2(\bm{x},\bm{y})=\frac{1}{N}\sum(x_i-m(\bm{x}))(y_i-m(\bm{y}))\\\ \\
=m((...,x_iy_i,...))-m(\bm{x})m(\bm{y})$$

## 相関係数

・相関係数：$$r(\bm{x},\bm{y})=\frac{s(\bm{x},\bm{y})}{s(\bm{x})s(\bm{y})}$$

- $\bm{x},\bm{y}\in\bm{R}^N$ とする。
このとき、
$$r(\bm{x},\bm{y})=\frac{(\bm{x}-m(\bm{x}))\cdot(\bm{y}-m(\bm{y}))}{|\bm{x}-m(x)||\bm{y}-m(y)|}$$

      ・cosθみたいなもん。

$r(\bm{x},\bm{y})^2$：決定係数

---

## 最小二乗法

・$$y=r(\bm{x},\bm{y})\frac{s(\bm{y})}{s(\bm{x})}(x-m(\bm{x}))+m(y)$$
とすると、残差平方和：
$$\sum (y_i-(ax_i+b))^2=Ns^2(\bm{y})(1-r(\bm{x},\bm{y})^2)$$
であって、これは最小値。？？？最後はまだ。

    ・偏微分で導ける。
    ・標準化と角度cosθとも見れる。標準化しても角度は変わらない！
    ・残差平方和：y_i-yのこと。


