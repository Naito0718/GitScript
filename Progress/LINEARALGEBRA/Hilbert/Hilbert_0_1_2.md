
- [凸集合 $C$](#凸集合-c)
  - [絶対凸](#絶対凸)
  - [フェイス](#フェイス)
- [独立性](#独立性)
  - [単体](#単体)
  - [一次写像](#一次写像)



# 凸集合 $C$

<dl><dt>

・$\bm{R,C}$ 上ベクトル空間 $V$、部分集合 $C\sub V$ とする。
このとき、凸集合 $C$：
$$x,y\in C\Rightarrow\forall t\in[0,1]\text{ に対して、}tx+(1-t)y\in C$$

</dt><dd>

- 凸集合族 $C_j\sub V$ とする。
このとき、$\bigcap C_j$ は凸集合。
<br>

- 部分空間 $W\sub V$ とする。
このとき、$W$ は凸集合。
<br>

- $x\in V$ とする。
このとき、$\{x\}$ は凸集合。
<br>

- 凸集合 $A,B\subset V$、$\alpha\in K$ とする。
このとき、$A+B,\ \alpha A$ は凸集合。

</dd></dl> 

---

## 絶対凸

<dl><dt>

・$\bm{R,C}$ 上ベクトル空間 $V$、凸集合 $C\sub V$ とする。
このとき、絶対凸 $C$：
$$x\in C\Rightarrow\forall\alpha\in\bm{R,C}\ |\alpha|\le1\text{に対して、}\alpha x\in C\\\ \\$$明らかに、$C$ が絶対凸ならば $0\in C$
<br>

</dt><dd>

- 絶対凸集合族 $C_j\sub V$ とする。
このとき、$\bigcap C_j$ は絶対凸。
<br>


- 部分空間 $W\sub V$ とする。
このとき、$W$ は絶対凸。
<br>

- 絶対凸集合 $A,B\subset V$、$\alpha\in\bm{R,C}$ とする。
このとき、$A+B,\ \alpha A$ は絶対凸。
<br>

- 絶対凸集合 $C_1\sub V,\ C_2\sub W$、線形写像 $f:V\to W$ とする。
このとき、$f(C_1),f^{-1}(C_2)$ は絶対凸。
<br>

・部分集合 $E\subset V$ とする。
このとき、
$$\mathrm{conv}(E)=\left\{\sum_{j=1}^n t_j x_j\ |\ n\in\bm{N},\ t_j\ge0,\ \sum_{j=1}^nt_j=1,\ x_j\in E\right\}$$
と定めると、これは $E$ を含む最小の凸集合。ここで、$\mathrm{conv}(E)$ を $E$ の凸包という。
<br>

    ・∩(Eを含む凸集合全体)と等しい。

</dd></dl> 

---

## フェイス

・$\bm{R,C}$ 上ベクトル空間 $V$、凸集合 $C\subset V$、部分集合 $F\sub C$ とする。
このとき、$C$ のフェイス $F$：
$$F\text{ は凸集合であって、}\\\ \\
\{(x,y)\in C\times C\ |\ \exist t\in(0,1)\text{ であって、}(1-t)x+ty\in F \}\subset F\times F$$
ここで、$\{x\}\sub C$ が $C$ のフェイスであるとき、$x$ を $C$ の端点といい、$C$ の端点全体を $\mathrm{ext}(C)$ と書く。
<br>

---

# 独立性

<dl><dt>

・$\bm{R,C}$ 上ベクトル空間 $V$、$v_0,...,v_p\in V$ とする。
このとき、$v_i$ が独立：
$$\sum_{i=0}^p\lambda_iv_i=0,\ \sum_{i=0}^p\lambda_i=0\Rightarrow \lambda_i=0\\\ \\
(\lambda_i\in\bm{R,C})$$
ここで、明らかに一次独立ならば独立。
<br>

</dt><dd>

- 独立な点 $v_0,...,v_p\in V$ とする。
このとき、$v_{i_1},...,v_{i_k}$ は独立。

</dd></dl> 

---

## 単体

<dl><dt>

・$\bm{R,C}$ 上ベクトル空間 $V$、独立な点 $v_1,...,v_p\in V$ とする。
このとき、$v_0,...,v_p$ を頂点とする $p$ 次元単体 $\sigma$：
$$\sigma=\mathrm{conv}\ \{v_0,...,v_p\}=\left\{x\in V\ \left|\ x=\sum_{i=0}^p\lambda_iv_i,\ \sum_{i=1}^p\lambda_i=1,\ \lambda_i\ge0\right.\right\}$$
ここで、$x\in\sigma$ に対する係数 $\lambda_i$ は一意的。
また、$x_G=\frac{1}{1+p}\sum_{i=0}^pv_i\in\sigma$ を重心という。
<br>

</dt><dd>

- $x\in\sigma$ とする。
このとき、
$$x\text{ は }\sigma\text{ の端点}\iff x\in\{v_0,...,v_p\}\\\ \\$$

- $\tau=\mathrm{conv}(\{v_{i_0},...,v_{i_q}\})$ は $\sigma$ のフェイス。
ここで、$\tau$ を $\sigma$ の $q$ 次元の辺といい、辺全体 $\bigcup_{q=0}^{p-1}\tau^q$ を $\partial\sigma$ と書く。
<br>

      ・図形の頂点とか辺とか。



</dd></dl> 

---

## 一次写像

<dl><dt>

・$\bm{R,C}$ 上ベクトル空間 $V,W$、$p$-単体 $\sigma\sub\bm{R}^n$、凸集合 $C\sub W$、$f:\sigma\to C$ とする。
このとき、一次写像 $f$：
$$\forall x,y\in \sigma,\ 0\le t\le 1\text{ に対して、}\\\ \\
f(tx+(1-t)y)=tf(x)+(1-t)f(y)\\\ \\$$

</dt><dd>

- 一次写像 $f:\sigma\to C$、$\sigma=[v_0,...,v_p]$ とする。
このとき、
$$\forall x=\sum_{i=0}^p\lambda_iv_i\in\sigma\text{ に対して、}\\\ \\f(x)=\sum_{i=0}^p\lambda_if(v_i)\\\ \\$$
逆に、$$f:\sigma\to C\\\ \\
f(x)=\sum_{i=0}^p\lambda_if(v_i)$$
と定めると、これはwell-definedな一次写像。
<br>

- $f:\sigma\to C$ が全単射な一次写像ならば、$f^{-1}$ は一次写像。

</dd></dl>

---



