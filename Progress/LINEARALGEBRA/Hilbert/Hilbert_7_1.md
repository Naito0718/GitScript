
- [直交補空間](#直交補空間)
- [Hilbert空間上の有界線形作用素](#hilbert空間上の有界線形作用素)
  - [有界準双線形写像と有界線形写像](#有界準双線形写像と有界線形写像)
  - [共役作用素](#共役作用素)
    - [共役作用素の演算](#共役作用素の演算)
  - [線形変換の時](#線形変換の時)
- [CONS](#cons)
  - [Hilbert空間とONS](#hilbert空間とons)
  - [CONS](#cons-1)
  - [可算なCONS](#可算なcons)



# 直交補空間

<dl><dt>

・ヒルベルト空間 $V$、部分空間 $M,N\sub V$ とする。
このとき、
$$M^{\perp}=(\overline{M})^{\perp}\\\ \\
M^{\perp\perp}=\overline{M}\\\ \\
V=N\oplus M\text{ かつ }M\perp N\\
\Rightarrow M,N\text{ は閉部分空間}\\\ \\$$

</dt><dd>

- 
$$V=M\oplus M^{\perp}\\\ \\
M\neq V\text{ ならば、}M^{\perp}\neq\{0\}\\\ \\
V=N\oplus M\text{ かつ }M\perp N\\
\Rightarrow M=N^{\perp}$$

</dd></dl>

---

# Hilbert空間上の有界線形作用素

## 有界準双線形写像と有界線形写像

<dl><dt>

・$\bm{C}$ 上Hilbert空間 $\mathcal{H_1,H_2}$、有界準双線形汎関数 $\Phi:\mathcal{H}_1\times \mathcal{H}_2\to\bm{C,R}$ とする。
このとき、
$$\text{ある }T\in B(\mathcal{H}_2,\mathcal{H}_1)\text{ がただ一つ存在して、}\forall u\in\mathcal{H}_1,\ \forall v\in\mathcal{H}_2\text{ に対して、}\\\ \\
\Phi(u,v)=(u,T v)_1,\quad \|\Phi\|=\|T\|\\\ \\$$

    ・R上でも同様。
<br>

</dt><dd>

- $T\in B(\mathcal{H}_1,\mathcal{H}_2)$ とする。
このとき、
$$\Phi:\mathcal{H}_1\times\mathcal{H}_2\to\bm{R,C}\\\ \\
\Phi(u,v)=(Tu,v)_2$$
と定めると、これは $\|\Phi\|=\|T\|$ を満たす有界準双線形汎関数。


</dd></dl>

---

## 共役作用素

・$\bm{R,C}$ 上Hilbert空間 $\mathcal{H_1,H_2}$、$T\in B(\mathcal{H}_1,\mathcal{H}_2)$ とする。
このとき、
$$\text{ある } T^*\in B(\mathcal{H}_2,\mathcal{H}_1)\text{ がただ一つ存在して、}\\\ \\
\|T\|=\|T^*\|,\quad (Tu,v)_{2}=(u,T^*v)_1\quad(\forall u\in\mathcal{H}_1,\forall v\in\mathcal{H}_2)$$
ここで、$T^*$ を $T$ の自己共役作用素という。

---

### 共役作用素の演算

<dl><dt>

・$\bm{R,C}$ 上Hilbert空間 $\mathcal{H}_1,\mathcal{H}_2,\mathcal{H}_3$、$T_1,T_2\in B(\mathcal{H}_1,\mathcal{H}_2),\ S\in B(\mathcal{H}_2,\mathcal{H}_3)$、$\alpha\in\bm{R,C}$ とする。
<br>

</dt><dd>

- $$(T_1+T_2)^*=T_1^*+T_2^*,\quad (\alpha T_1)^*=\overline{\alpha}T^*\\\ \\$$

- $$(S\circ T_1)^{*}=T_1^*\circ S^*\\\ \\$$

- $$(T_1^*)^*=T_1\\\ \\$$

- $$\|T_1^*\circ T_1\|=\|T_1\|^2\\\ \\$$

- $$(\mathrm{Im}\ T)^{\perp}=\ker T^*$$


</dd></dl>

---

## 線形変換の時

・$\bm{R,C}$ 上Hilbert空間 $\mathcal{H}$ とする。
このとき、$B(\mathcal{H})$ は共役演算に対して $C^*$-環。


  
---
---
---

# CONS

## Hilbert空間とONS

・Hilbert空間 $\mathcal{H}$、$J$ によって添え字付けられた $\mathcal{H}$ のONS $e_j\in B_0$、$v\in \overline{\mathrm{span}B_0}$ とする。
このとき、$$\|v\|^2=\sum_{j\in J}|(e_j,v)|^2,\quad v=\sum_{j\in J}(e_j,v)e_j\\\ \\
(u,v)=\sum (u,e_k)\overline{(v,e_k)}$$が成り立つ。
さらに、
$$U:\overline{\mathrm{span}B_0}\to l^2(J)\\\ \\
U(v)=(e_j,v)_{j\in J}$$
と定めると、これはユニタリ作用素。
<br>

    ・ユニタリ作用素：全射な等長写像。

---

## CONS

<dl><dt>

・Hilbert空間 $\mathcal{H}$、ONS $B\sub\mathcal{H}$ とする。
このとき、CONS $B$：
$$\overline{\mathrm{span}\ B}=\mathcal{H}\\\ \\$$

</dt><dd>

- $J$ によって添え字付けられた CONS を持つHilbert空間 $\mathcal{H}$ とする。
このとき、
$$\mathcal{H}\cong l^2(J)\quad(\text{ユニタリ同型})\\\ \\$$


・Hilbert空間 $\mathcal{H}$、$\mathcal{H}$ のONS $B_0$ とする。
このとき、$$\exist\text{ CONS } B\sub\mathcal{H}\text{ であって、}B_0\subset B\\\ \\$$

    ・B_0を含むONS全体の集合は帰納的順序集合
<br>

- Hilbert空間 $\mathcal{H}$、$\mathcal{H}$ のCONS $B_1,B_2$ とする。
このとき、$B_1$ と $B_2$ の濃度は等しい。

</dd></dl> 

---

## 可算なCONS

・Hilbert空間 $\mathcal{H}$ とする。
このとき、
$$\mathcal{H}{は可分}\iff \mathcal{H}{のCONSは可算}$$

