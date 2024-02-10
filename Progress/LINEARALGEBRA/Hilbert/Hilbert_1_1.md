
    ・折を見て位相群みたいなことしないといけない。T_1位相線形空間とか。

- [位相線形空間](#位相線形空間)
  - [コーシー列](#コーシー列)
  - [開集合](#開集合)
  - [閉包](#閉包)
  - [連続写像](#連続写像)
    - [演算](#演算)
  - [線形写像](#線形写像)
- [凸集合](#凸集合)
  - [Hahn-Banachの分離定理](#hahn-banachの分離定理)





# 位相線形空間

    ・T_1性を仮定してよい！つまり位相群でもある。

## コーシー列

・$\bm{R,C}$ 上位相線形空間 $V$、点列 $(x_n)\subset V$ とする。
このとき、コーシー列 $(x_n)$：
$$\forall N\in\mathcal{N}(0)\text{ に対して、}\exist n_0\in\bm{N}\text{ であって、}\\\ \\
n,m\ge n_0\Rightarrow x_n-x_m\in N$$ 

---

## 開集合

・$\bm{C,R}$ 上位相線形空間 $V$、開集合 $O\subset V$、$x\in O$ とする。
このとき、$$\exist \mu\in(0,1)\text{ であって、}\frac{1}{\mu}x\in O\\\ \\
\forall w\in V\text{ に対して、}\exist\delta>0\text{ であって、}x+\delta w\in O\\\ \\$$

- $\bm{C,R}$ 上位相線形空間 $V$、$0$ の開近傍 $0\in N\in\mathcal{N}(0)$、$x\in V$ とする。
このとき、$$\exist\delta>0\text{ であって、}\delta x\in N$$

---

## 閉包

・$\bm{C,R}$ 上位相線形空間 $V$、部分空間 $M\subset V$ とする。
このとき、$\overline{M}$ は $V$ の部分空間。

    ・？？？なんか近傍使って示した気がする。


---

## 連続写像

### 演算

・位相空間 $X$、$\bm{R,C}$ 上位相線形空間 $V$、連続写像 $f,g:X\to V$、$\alpha\in \bm{R,C}$ とする。
このとき、$f+g,\ \alpha f:X\to V$ は連続写像。

---

## 線形写像

・$\bm{C,R}$ 上位相線形空間 $V,W$、線形写像 $f:V\to W$、$x\in V$、$f(x)\in N_W(f(x))\in\mathcal{N}_W(f(x))$ とする。
このとき、$$f^{-1}(N_W(f(x)))=f^{-1}(N_V(0_V))+x$$となる $0_V\in N_V(0_V)\in\mathcal{N}_V(0_V)$ が存在する。

- $\bm{C,R}$ 上位相線形空間 $V,W$、線形写像 $f:V\to W$、$x\in V$ とする。
このとき、$f$ が $0_V\in V$ で連続ならば、$f$ は連続。
<br>



---

# 凸集合

・位相線形空間 $V$、凸集合 $C\sub V$ とする。
このとき、$C$ は弧状連結で、$0\in C^{\circ}$

---

- $\bm{R,C}$ 上ベクトル空間 $V$、絶対凸な集合 $C\sub V$ とする。
このとき、$\overline{C}$ は絶対凸。
<br>

## Hahn-Banachの分離定理

<dl><dt>

・$\bm{R,C}$ 上位相線形空間、$0\in C\subset V$ を $0$ の凸開近傍とする。
このとき、$$m:V\to[0,\infty)\\\ \\
m(x)=\inf\left\{\lambda\in(0,\infty)\ |\ \frac{1}{\lambda}x\in C\right\}$$と定めると、これはwell-definedなMinkowski汎関数。
<br>

    ・well-defined性は0開近傍による。
<br>

</dt><dd>

- 
$$C=\{x\in V\ |\ m(x)<1\}\\\ \\$$

- 凸集合 $A,B\subset V$ であって、$A$ は開集合かつ $A\cap B=\phi$ とする。
このとき、
$$\exist\text{ 連続写像 }\phi:V\to\bm{R,C},\ \exist t\in\bm{R}\text{ であって、}\\\ \\
\mathrm{Re}(\phi(x))< t\le\mathrm{Re}(\phi(y))\quad(\forall x\in A,\forall y\in B)$$
また、$\bm{C}$ 上においては、$\mathrm{Re}\ \phi,\mathrm{Im}\ \phi:V_{\bm{R}}\to\bm{R}$ は連続な線形写像。
<br>

      ・左側は真の不等式


</dd></dl> 

