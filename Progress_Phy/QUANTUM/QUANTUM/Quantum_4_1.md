

- [摂動](#摂動)
  - [縮退のないとき](#縮退のないとき)
  - [$k$ 重縮退のあるとき](#k-重縮退のあるとき)
- [時間依存する摂動論](#時間依存する摂動論)




# 摂動

    ・数学的には解けない！
<br>

<dl><dt>

・時間に依存しないハミルトニアン $H=\frac{1}{2}m\hat{\dot{x}}^2+V(\hat{x})$ とする。
このとき、摂動ハミルトニアン $H'$：
$$\exist \text{ エルミート演算子 }H_0\text{ であって、}H'=H-H_0\\\ \\
H_0\ket{n^0}=E_{n}^{(0)}\ket{n^0},\quad\ket{n^0}\text{ は可算完全系をなす}$$
このとき、$H_0$ を非摂動ハミルトニアンという。
<br>

    ・可算基底？時間に依存しないから？
<br>

- 時間に依存しないハミルトニアン $H=\frac{1}{2}m\hat{\dot{x}}^2+V(\hat{x})$、摂動、非摂動ハミルトニアン $H',H_0$、$\lambda\in\bm{R}$ とする。
このとき、固有値 $E_0$ に対する固有ケット $\ket{n^0}$ に関する摂動展開：
$$H_{\lambda}=H_0+\lambda H',\quad H_{\lambda}\ket{n}_{\lambda}=E_{n,\lambda}\ket{n}_{\lambda}\\\ \\
E_{n,\lambda}=\sum_{k\in\bm{N}} \lambda^kE_{n}^{(k)},\quad \ket{n}_{\lambda}=\sum_{k\in\bm{N}} \lambda^k\ket{n^k}$$
このとき、$\lim_{\lambda\to0}E_{n,\lambda}=E^{(0)}_n,\ \lim_{\lambda\to 0}\ket{n}_{\lambda}=\ket{n^0}$
<br>

      ・E_n^{(k)}とか|n_k>は適当な点列で、k=0のとき非摂動ハミルトニアンのやつになる。
      ・H(λ)としてλの関数とみるべきかも。
<br>

</dt><dd>

- 
$$(H_0-E_n^{(0)})\ket{n^0}=0\\\ \\
(H_0-E_n^{(0)})\ket{n^1}=(E_n^{(1)}-H')\ket{n^0}\\\ \\
(H_0-E_n^{(0)})\ket{n^2}=(E_n^{(1)}-H')\ket{n^1}+E_n^{(2)}\ket{n^0}\\\ \\
\cdots\\\ \\
(H_0-E_n^{(0)})\ket{n^k}=(E_n^{(1)}-H')\ket{n^{k-1}}+E_n^{(2)}\ket{n^{k-2}}...+E_n^{(k)}\ket{n^0}$$


</dd></dl>

---

## 縮退のないとき

    ・別にm_0で縮退しててもよい。
<br>

<dl><dt>

・時間に依存しないハミルトニアン $H=\frac{1}{2}m\hat{\dot{x}}^2+V(\hat{x})$、摂動、非摂動ハミルトニアン $H',H_0$ とし、$E_n^{(0)}$ を固有値とする $\ket{n_0}$ には縮退がないとする。
このとき、$$E_{n}^{(1)}=\bra{n_0}H'\ket{n_0}\\\ \\
\ket{n^1}=\sum_{k\in\bm{N}}c_k^1\ket{k^0},\quad \forall k\in\bm{N}-\{n_0\}\text{ に対して、}c_k^1=\frac{\bra{k^0}H'\ket{n^0}}{E_n^{(0)}-E_k^{(0)}}$$
ここで、決定できないので、$c^1_{n}=0$、すなわち $\braket{n_0|n_1}=0$ と定める。
<br>

</dt><dd>

- $$E_2^{(0)}=\bra{n^0}H'\ket{n^1}=\sum_{m\in\bm{N}-\{n_0\}}\frac{|\bra{m^0}H'\ket{n^0}|^2}{E_n^{(0)}-E_m^{(0)}}\\\ \\$$

- $\braket{n_0|n_2}=0$ と定める。
このとき、
$$\ket{n_2}=\sum_{k\in\bm{N}}c_k^2\ket{k_0},\quad \forall k\in\bm{N}-\{n_0\}\text{ に対して、}c_k^2=\frac{-E_n^{(1)}c_k^1+\bra{k_0}H'\ket{n_1}}{E_n^{(0)}-E_k^{(0)}}\\\ \\$$

- 第一近似において、$\braket{n|n}=1$

<br>

- 第二近似において、$$\braket{n|n}=1+\braket{n_1|n_1}=1+\sum_{k\in\bm{N}-\{n_0\}}\frac{\bra{k^0}H'\ket{n^0}}{(E_n^{(0)}-E_{k}^{(0)})^2}$$
特に、
$$E_n=E_n^{(0)}+\bra{n^0}H'\ket{n^0}+\sum_{k\in\bm{N}-\{n_0\}}\frac{|\bra{k^0}H'\ket{n^0}|^2}{E_n^{(0)}-E_m^{(0)}}\\\ \\
\ket{n}=\ket{n^0}+\sum_{k\in\bm{N}-\{n_0\}}\ket{k^0}\frac{\bra{k^0}H'\ket{n^0}}{E_n^{(0)}-E_{k}^{(0)}}+\sum_{k,m\in\bm{N}-\{n_0\}}\ket{k^0}\frac{\bra{k^0}H'\ket{m^0}\bra{m^0}H'\ket{n^0}}{(E_n^{(0)}-E_{k}^{(0)})(E_n^{(0)}-E_m^{(0)})}-\sum_{k\in\bm{N}-\{n_0\}}\ket{k^0}\frac{\bra{n^0}H'\ket{n^0}\bra{k^0}H'\ket{n^0}}{(E_n^{(0)}-E_{k}^{(0)})^2}$$

</dd></dl>

---

## $k$ 重縮退のあるとき

<dl><dt>

・時間に依存しないハミルトニアン $H=\frac{1}{2}m\hat{\dot{x}}^2+V(\hat{x})$、摂動、非摂動ハミルトニアン $H',H_0$ とし、$E_n^{(0)}$ を固有値とする $\ket{n_0}$ は $k$ 重縮退しているとする。
このとき、$E_n^{0}$ に属する一次独立な固有ケット $\ket{\phi_{0n1}},...,\ket{\phi_{0nk}}$、$E_n^{(0)}$ に属する正規直交固有ケット $\ket{n_{01}},...,\ket{n_{0k}}$ とすると、
$$(\tilde{H}-E_{nl}^{(1)})\bm{c}^l=0\\\ \\
\tilde{H}_{ij}=\bra{n_{0i}}H'\ket{n_{0j}},\quad\ket{\phi_{0nl}}=\sum_{i=1}^kc_{i}^l\ket{n_{0i}},\quad\bm{c}^l=(c_1^l,...,c_k^l)$$
したがって、$E^{(1)}_{nl}$ 及び $\bm{c}^l$ を求めるには $\det(\tilde{H}-E^{(1)}_{nl}I)=0$ を解けばよいが、これは、$\tilde{H}$ に関する固有値方程式である。また、$\bm{c}$ を規格化しておけば、各 $\ket{\phi_{0ni}}$ も規格化される。
<br>

    ・各|Φ_0ni>でE_n^(0)は等しいが、E_n^(1)が等しいわけではない。

</dt><dd>





</dd></dl>

---

# 時間依存する摂動論

<dl><dt>

・時間に依存するハミルトニアン $H=\frac{1}{2}m\hat{\dot{x}}^2+V(\hat{x},t)$、摂動、非摂動ハミルトニアン $H',H_0$、$\lambda\in\bm{R}$ とする。
このとき、固有値 $E_n^{(0)}$ に属する固有関数 $\psi_n=e^{-iE_0t/\hbar}\phi_n$ に関する摂動展開：
$$H_{\lambda}=H_0+\lambda H',\quad H_{\lambda}\Psi=i\hbar\frac{\partial}{\partial t}\Psi\\\ \\
E_{n,\lambda}=\sum_{k\in\bm{N}} \lambda^kE_{n}^{(k)},\quad \ket{n}_{\lambda}=\sum_{k\in\bm{N}} \lambda^k\ket{n^k}$$
このとき、$\lim_{\lambda\to0}E_{n,\lambda}=E^{(0)}_n,\ \lim_{\lambda\to 0}\ket{n}_{\lambda}=\ket{n^0}$
<br>

      ・E_n^{(k)}とか|n_k>は適当な点列で、k=0のとき非摂動ハミルトニアンのやつになる。
      ・H(λ)としてλの関数とみるべきかも。
<br>

</dt><dd>

- 
$$(H_0-E_n^{(0)})\ket{n^0}=0\\\ \\
(H_0-E_n^{(0)})\ket{n^1}=(E_n^{(1)}-H')\ket{n^0}\\\ \\
(H_0-E_n^{(0)})\ket{n^2}=(E_n^{(1)}-H')\ket{n^1}+E_n^{(2)}\ket{n^0}\\\ \\
\cdots\\\ \\
(H_0-E_n^{(0)})\ket{n^k}=(E_n^{(1)}-H')\ket{n^{k-1}}+E_n^{(2)}\ket{n^{k-2}}...+E_n^{(k)}\ket{n^0}$$


</dd></dl>

---


