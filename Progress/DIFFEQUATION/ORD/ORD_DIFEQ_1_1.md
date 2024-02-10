

- [一階正規型方程式](#一階正規型方程式)
  - [ベクトル値微分方程式](#ベクトル値微分方程式)
    - [行列値微分方程式](#行列値微分方程式)
  - [初期値,パラメータによる連続性への影響](#初期値パラメータによる連続性への影響)
    - [微分可能性](#微分可能性)
  - [解析的微分方程式](#解析的微分方程式)
- [最高階の係数 $1$ の線形微分方程式](#最高階の係数-1-の線形微分方程式)
  - [ロンスキアン](#ロンスキアン)



# 一階正規型方程式

・
$$\exist K>0\text{ であって、}\forall t\in[a,b],\ \forall x_1,x_2\in[c,d]\text{ に対して、}\\\ \\
|f(t,x_1)-f(t,x_2)|\le K|x_1-x_2|$$
を満たす連続関数 $f:[a,b]\times[c,d]\to\bm{R}$、$(t_0,x_0)\in[a,b]\times[c,d]$ とする。
このとき、
$$x_0(t)=x_0,\quad x_n(t)=x_0+\int_{t_0}^tf(\tau,x_{n-1}(\tau))d\tau$$
と定めると、$x_n(t)$ はある $C^1$ 関数 $x(t)$ に一様収束し、
$$\exist\delta>0\text{ であって、}[t_0-\delta,t_0+\delta]\text{ 上で }\\\ \\
\frac{dx(t)}{dt}=f(t,x(t)),\quad x(t_0)=x_0$$
さらに、$f$ が $C^k$ ならば解 $x(t)$ は $C^{k+1}$ であり、上記の微分方程式を満たす解 $x(t)$ は一意的。
<br>

    ・一意性を満たすfは第二引数でリプシッツ。


---

## ベクトル値微分方程式

・閉領域 $D\sub\bm{R}^n$、
$$\exist K>0\text{ であって、}\forall t\in[a,b],\ \forall x_1,x_2\in D\text{ に対して、}\\\ \\
|f(t,x_1)-f(t,x_2)|\le K|x_1-x_2|$$
を満たす連続関数 $f:[a,b]\times D\to\bm{R}^n$、$(t_0,x)\in[a,b]\times D$ とする。
このとき、
$$x_0(t)=x_0,\quad x_n(t)=x_0+\int_{t_0}^tf(\tau,x_{n-1}(\tau))d\tau$$
と定めると、$x_n(t)$ はある $C^1$ 関数 $x(t)$ に一様収束し、
$$\exist\delta>0\text{ であって、}[t_0-\delta,t_0+\delta]\text{ 上で }\\\ \\
\frac{dx}{dt}=f(t,x),\quad x(t_0)=x_0$$
さらに、$f$ が $C^k$ ならば解 $x(t)$ は $C^{k+1}$ であり、上記の微分方程式を満たす解 $x(t)$ は一意的。

<br>

    ・閉集合の任意直積は閉集合。
    ・複素でも同様だが、tは実数。
    ・n階のこと。
<br>

---

### 行列値微分方程式

・閉領域 $D\sub M(n,\bm{R})$、
$$\exist K>0\text{ であって、}\forall t\in[a,b],\ \forall x_1,x_2\in D\text{ に対して、}\\\ \\
|f(t,x_1)-f(t,x_2)|\le K|x_1-x_2|$$
を満たす連続関数 $f:[a,b]\times D\to\bm{R}^n$、$(t_0,x_0)\in[a,b]\times M(n,\bm{R})$ とする。
このとき、
$$x_0(t)=x_0,\quad x_n(t)=x_0+\int_{t_0}^tf(\tau,x_{n-1}(\tau))d\tau$$
と定めると、$x_n(t)$ はある $C^1$ 関数 $x(t)$ に一様収束し、
$$\exist\delta>0\text{ であって、}[t_0-\delta,t_0+\delta]\text{ 上で }\\\ \\
\frac{dx}{dt}=f(t,x),\quad x(t_0)=x_0$$
さらに、$f$ が $C^k$ ならば解 $x(t)$ は $C^{k+1}$ であり、上記の微分方程式を満たす解 $x(t)$ は一意的。
<br>

    ・||はR^nの拡張。
<br>

- 閉領域 $D\sub GL(n,\bm{R})$、
$$\exist K>0\text{ であって、}\forall t\in[a,b],\ \forall x_1,x_2\in D\text{ に対して、}\\\ \\
|f(t,x_1)-f(t,x_2)|\le K|x_1-x_2|$$
を満たす連続関数 $f:[a,b]\times D\to\bm{R}^n$、$(t_0,x_0)\in[a,b]\times M(n,\bm{R})$ とする。
このとき、
$$x_0(t)=x_0,\quad x_n(t)=x_0+\int_{t_0}^tf(\tau,x_{n-1}(\tau))d\tau$$
と定めると、$x_n(t)$ はある $C^1$ 関数かつ逆行列を持つ $x(t)$ に一様収束し、
$$\exist\delta>0\text{ であって、}[t_0-\delta,t_0+\delta]\text{ 上で }\\\ \\
\frac{dx}{dt}=f(t,x),\quad x(t_0)=x_0$$
さらに、$f$ が $C^k$ ならば解 $x(t)$ は $C^{k+1}$ であり、上記の微分方程式を満たす解 $x(t)$ は一意的。
<br>

      ・GL(n,R)が開集合であることによる。

---


## 初期値,パラメータによる連続性への影響

### 微分可能性

## 解析的微分方程式

    ・重要！これ使って級数解法してる！
<br>



# 最高階の係数 $1$ の線形微分方程式

## ロンスキアン