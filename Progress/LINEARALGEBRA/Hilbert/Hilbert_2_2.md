
- [有界線形作用素](#有界線形作用素)
  - [等長写像](#等長写像)
  - [線形変換のとき](#線形変換のとき)
  - [値域がBanach空間のとき](#値域がbanach空間のとき)
  - [定義域がBanach空間のとき](#定義域がbanach空間のとき)
- [有界双線形写像](#有界双線形写像)



# 有界線形作用素

<dl><dt>

・$\bm{R,C}$ 上ノルム空間 $X,Y$ とする。
このとき、
$$L(X,Y)=\{f:X\to Y\ |\ f{は線形作用素}\}\\\ \\
\|T\|=\sup\{\|T(x)\|_Y\ |\ x\in X,\ \|x\|_X\le1\}\\\ \\
B(X,Y)=\{T\in L(X,Y)\ |\ \|T\|<\infty\}\\\ \\ $$
と定めると、$L(X,Y)$ は $\bm{R,C}$ 上ベクトル空間で、$B(X,Y)$ は $\bm{R,C}$ は $L(X,Y)$ の部分空間で、$\|\cdot\|$ は $B(X,Y)$ 上のノルム。
<br>
  
</dt><dd>

- 
$$\|T\|=\sup\{\|T(x)\|\ |\ x\in X,\ \|x\|_X=1\}\\\ \\
=\sup\left\{\left.\frac{\|T(x)\|_Y}{\|x\|_X}\ \right|\ x\in X-\{0\}\right\}\\\ \\$$

- 
$$\forall x\in X,\ \forall T\in B(X,Y)\text{ に対して、}\\\ \\
\|T(x)\|_Y\le\|T\|\|x\|_X\\\ \\$$

- $T\in L(X,Y)$ とする。
このとき、
$$T\in B(X,Y)\iff T{\text は一様連続}\\\ \\
\iff T\text{ は }\ 0\in X\text{ で連続}\\\ \\$$

- $\bm{R,C}$ 上ノルム空間 $X,Y,Z$、$T\in B(X,Y),\ S\in B(Y,Z)$ とする。
このとき、$$S\circ T\in B(X,Z)\\\ \\$$

- ノルム空間 $X,Y$、$T_1,T_2\in B(X,Y)$、稠密な部分集合 $M\sub X,\ \overline{M}=X$ とする。
このとき、
$$\forall x\in M\text{ に対して、}T_1(x)=T_2(x)\\\ \\
\Rightarrow T_1=T_2\ \ (\forall x\in X)$$

</dd></dl> 

---

## 等長写像

<dl><dt>

・$\bm{R,C}$ 上ノルム空間 $X,Y$、線形写像 $T:X\to Y$ とする。
このとき、等長写像 $T$：
$$\|u\|_X=\|T(u)\|_Y\quad(\forall u\in X)$$
このとき、$T$ は単射。
<br>  

- $\bm{R,C}$ 上ノルム空間 $X,Y$、全射な等長写像 $T:X\to Y$ とする。
このとき、$T\in B(X,Y)$ であって、$T^{-1}$ は等長写像。

</dt><dd>


ここで、ノルム空間 $X,Y$ に対して、全射な等長写像が存在するとき、$V$ と $W$ はノルム同型といい、$T$ をユニタリ作用素という。


     ・Banach空間でも同じ。完備性が保たれる。
     ・内積空間でも同じ。内積を保つ。


</dd></dl> 

---

## 線形変換のとき

<dl><dt>

・$\bm{R,C}$ 上ノルム空間 $X$ とする。
このとき、$$L(X)=\{f:X\to X\ |\ f{は線形作用素}\}\\\ \\
\|T\|=\sup\{\|T(x)\|\ |\ x\in X,\ \|x\|\le1\}\\\ \\
B(X)=\{T\in L(X)\ |\ \|T\|<\infty\}\\\ \\ $$
と定めると、$L(X)$ は合成によって $\bm{R,C}$ 上単位的多元環、$B(X)$ は $\|\cdot\|$ をノルムとする $\bm{R,C}$ 上単位的ノルム環かつ、$L(X)$ の部分空間。
<br>

</dt><dd>

- $S,T\in B(X)$ とする。
このとき、$$\|ST\|\le \|S\|\|T\|$$

       ・ノルム環のこと。

</dd></dl> 

---

## 値域がBanach空間のとき

・ノルム空間 $X$ 、Banach空間 $Y$ とする。 
このとき、$B(X,Y)$ はBanach空間

- ノルム空間 $X$、Banach空間 $Y$、部分空間 $M\subset X$、$T\in B(X,Y)$とする。
このとき、
$$\text{ある }\overline{T}:\overline{M}\to Y\text{ がただ一つ存在して、}\\\ \\
\overline{T}|_M=T,\quad\|\overline{T}\|=\|T\|\\\ \\$$ 
特に、$M$ を稠密な部分空間とすると、$T$ は $X$ 上に一意的に拡張される。

---

## 定義域がBanach空間のとき

・Banach空間 $X$、ノルム空間 $Y$、閉部分空間 $M\sub X$、等長写像 $T:M\to Y$ とする。
このとき、$Im(T)$ は閉部分空間。

---
---
---

# 有界双線形写像

<dl><dt>

・$\bm{R,C}$ 上ノルム空間 $V,W,U$、双線形写像 $\Phi:V\times W\to U$ とする。
このとき、有界双線形写像 $\Phi$： 
$$\|\Phi\|<\infty\\\ \\
\text{ ただし、}\|\Phi\|=\sup\{\|\Phi(u,v)\|_U\ |\ \|u\|_V,\|v\|_W\le1\}\\\ \\$$

      ・準双線形写像でも同様。
<br>

</dt><dd>

- 
$$\|\Phi\|=\sup\{\|\Phi(u,v)\|_U\ |\ \|u\|_V,\|v\|_W=1\}\\\ \\
=\sup\left\{\left.\frac{\|\Phi(u,v)\|_U}{\|u\|_V\|v\|_W}\ \right|\ u\in V-\{0\},\ v\in W-\{0\}\right\}\\\ \\$$

- $u\in V$、$w\in W$ とする。
このとき、$$\|\Phi(u,v)\|_U\le\|\Phi|\|u\|_V\|v\|_W\\\ \\$$

- 有界双線形写像 $\Phi:V\times W\to U$ とする。
このとき、$\Phi$ は連続写像。
<br>

      ・準双線形も同様。
      ・逆は知らない。

</dd></dl>