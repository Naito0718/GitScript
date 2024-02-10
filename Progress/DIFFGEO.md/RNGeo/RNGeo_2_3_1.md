
- [Rieeman測度](#rieeman測度)
  - [局所座標 $(U,Φ)$ 上のRiemann測度](#局所座標-uφ-上のriemann測度)
  - [多様体上のRiemann測度](#多様体上のriemann測度)
    - [直積Riemann測度](#直積riemann測度)
- [ヤコビアン](#ヤコビアン)
  - [変数変換公式](#変数変換公式)



# Rieeman測度

## 局所座標 $(U,Φ)$ 上のRiemann測度

<dl><dt>

・$n$ 次元多様体 $M\sub\bm{R}^N$、局所座標 $(U,\phi)$ とする。
このとき、
$$\mu_{(U,\phi)}:\mathfrak{B}_U\to[0,\infty]\\\ \\
\mu_{(U,\phi)}(B)=\int_{\phi(B)}\sqrt{G_{(U,\phi)}}\circ\phi^{-1}dm$$
と定めると、これは測度。ここで、$\mu_{(U,\phi)}$ を $M$ の $(U,\phi)$ に関するRiemann測度という。
<br>

</dt><dd>

- 非負値Borel関数 $f:U\to[0,\infty]$ とする。
このとき、
$$\int_Ufd\mu_{(U,\phi)}=\int_{\phi(U)}\left(f\sqrt{G_{(U,\phi)}}\right)\circ\phi^{-1}dm\\\ \\$$

      ・実、複素可積分関数でも同様。
<br>

- $n$ 次元多様体 $M\sub\bm{R}^N$、局所座標 $(U,\phi),\ (V,\psi)$、$B\in\mathfrak{B}_{U\cap V}=\mathfrak{B}_U\cap\mathfrak{B}_V$ とする。
このとき、
$$\mu_{(U,\phi)}(B)=\mu_{(V,\phi)}(B)\\\ \\$$

- $n$ 次元多様体 $M\sub\bm{R}^N$、Borel集合 $B\in\mathfrak{B}_M$、可算なアトラス $\{(U_i,\phi_i)\}$ とする。
このとき、
$$\exist\text{ 非交叉列 }(B_n)\sub\mathfrak{B}_M\text{ であって、}\\\ \\
B=\bigcup_{n\in\bm{N}} B_n,\quad B_n\sub U_n\\\ \\$$

      ・この定理によって、積分は各チャート上の積分に分解できる。

</dd></dl>

---

## 多様体上のRiemann測度

<dl><dt>

・$n$ 次元多様体 $M\sub\bm{R}^N$ とする。
このとき、
$$\text{ ある測度 }\mu_M:\mathfrak{B}_M\to[0,\infty]\text{ が一意的に存在して、任意の局所座標 }(U,\phi),\ \forall B\in \mathfrak{B}_U\text{ に対して、}\\\ \\
\mu_M(B)=\mu_{(U,\phi)}(B)$$
ここで、$\mu_M$ を $M$ のRiemann測度という。また、これは $\bm{R}^N$ に対するLebesgue測度と整合する。
<br>

    ・Mは可測集合とは限らない。
<br>

</dt><dd>

- $k$ 次元部分多様体 $H\sub M$ とする。
このとき、$H\in\mathfrak{B}_M$ であって、
$$\mu_M(H)=0\\\ \\$$

      ・直積測度の性質による。
<br>

- $\mu_M$ は第二可算局所コンパクト空間 $M$ 上のRadon測度。
したがって、
$$\forall \text{ 開集合 }V\in\mathcal{O}_M\text{ に対して、}\\\ \\
\mu_M(V)=\sup\left\{\int_Mf(p)d\mu_M\ |\ f\in C_{c,+}^{\infty},\ \ \mathrm{supp}\ f\sub V,\ \ f(M)\sub[0,1]\right\}\\\ \\
\forall \text{ コンパクト集合 }K\sub M\text{ に対して、}\\\ \\
\mu_M(K)=\inf\left\{\int_Mf(p)d\mu_M\ |\ f\in C_{c,+}^{\infty},\ \ \forall x\in K\text{ に対して } f(x)=1,\ \ f(M)\sub[0,1]\right\}\\\ \\$$
また、$p\in[1,\infty)$、$f\in \mathcal{L}^p(M,\mathfrak{B}_M,\mu_M)$ とすると、
$$\exist\text{ 点列 }(f_n)\sub C_c^{\infty}(M)\text{ であって、}\\\ \\
\lim_{n\to\infty}\|f_n-f\|_{L^p}=0\\\ \\$$

      ・最後のは別にC_{c,+}^∞でもよい。
<br>

- $n$ 次元多様体 $M\sub\bm{R}^{N_1}$、$H\sub\bm{R}^{N_2}$、$C^1$ 写像 $f:M\to H$ とする。
このとき、$$\forall\sigma\text{-コンパクトな }\mu_M\text{-零集合 }B\in M\text{ に対して、}\\\ \\
f(B)\text{ は }\sigma\text{-コンパクトな}\mu_H\text{-零集合}$$

</dd></dl>

---

### 直積Riemann測度

・$n_i$ 次元多様体 $M_i\sub\bm{R}^{N_i}$ とする。
このとき、積多様体 $M_1\times...\times M_k$ は $\bm{R}^{N_1+...+N_k}$ 内の多様体。
<br>

- 積多様体 $M_1\times...\times M_k\sub\bm{R}^{N_1+...+N_k}$、チャート $(U_1\times...\times U_{k},\phi_1\times...\times\phi_k)$ とする。
このとき、
$$(g_{(\Pi\ U_i,\Pi\ \phi_i)}(p))_{\sum_{i=1}^lN_i+a,\ \ \sum_{i=1}^sN_i+b}=\delta_{ls} (g_{(U_i,\phi_i)}(p))_{ab}\quad(l,s=0,1,...,k-1,\ a=1,...,N_{l+1},\ b=1,...,N_{s+1})\\\ \\
G_{(\Pi\ U_i,\Pi\ \phi_i)}=G_{(U_1,\phi_1)}...G_{(U_k,\phi_k)}\\\ \\
\mu_{(\Pi\ U_i,\Pi\ \phi_i)}=\mu_{(U_1,\phi_1)}\otimes...\otimes\mu_{(U_k,\phi_k)}\\\ \\$$

      ・第二可算空間上のRadon測度はσ-有限測度。
<br>

- $$\mu_{M_1\times...\times M_k}=\mu_{M_1}\otimes...\otimes\mu_{M_k}$$

---

# ヤコビアン

<dl><dt>

・$n$ 次元多様体 $M,H\sub\bm{R}^N$、$C^1$ 写像 $\Phi:M\to H$、$M$ のアトラス $\{(U,\phi;x^1,...,x^n)\}$、$H$ のアトラス $\{(V,\psi,y^1,...,y^n)\}$ とする。
このとき、
$$J_{\Phi}:M\to [0,\infty)\\\ \\
J_{\Phi}(p)=\frac{\sqrt{G_{(V,\psi)}(\Psi(p))}}{\sqrt{G_{(U,\phi)}(p)}}\left|\det\left(\frac{\partial\Psi^i}{\partial x^j}(p)\right)_{i,j}\right|$$
と定めると、$J_{\Phi}$ はアトラスによらない連続写像。ここで、$J_{\Phi}$ を $\Phi$ のヤコビアンという。
<br>

</dt><dd>

- $p\in M$ とする。
このとき、
$$J_{\Phi}(p)>0\iff d\Phi_p\text{ が線形同型写像}$$

</dd></dl>

---

## 変数変換公式

<dl><dt>

・$n$ 次元多様体 $M,H\sub\bm{R}^N$、$C^1$ 微分同相？写像 $\Phi:M\to H$、非負値Borel関数 $f:H\to[0,\infty]$ とする。
このとき、
$$\int_Hfd\mu_H=\int_M(f\circ\Phi) J_{\Phi}d\mu_M\\\ \\$$


</dt><dd>

- $B\in\mathfrak{B}_M$、$B$ に含まれる、$B$ を含む開集合 $B_0\sub B\sub U\sub M$、$C^1$ 写像 $\Phi:U\to H$ とする。
このとき、
$$\begin{cases}
\Psi(B)\sub\mathfrak{B}_{H}\\
\Psi\text{ は }B_0\text{ 上単射で、 }\forall p\in B_0\text{ に対して }J_{\Phi}(p)>0\\
\exist\sigma\text{-コンパクトな }\mu_M\text{-零集合 }N\in\mathfrak{B}_{M}\text{ であって、}B-B_0\sub N\\
\end{cases}\\\ \\
\Rightarrow\forall\text{ 非負値Borel関数 }f:\Psi(B)\to[0,\infty]\text{ に対して、}\\\ \\
\int_{\Psi(B)}f(p)d\mu_H=\int_B(f\circ\Phi)(p)J_{\Phi}(p)d\mu_M$$


</dd></dl>




