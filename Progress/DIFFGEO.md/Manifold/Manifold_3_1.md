
- [外微分](#外微分)
  - [微分形式全体 $Ω'(M)$](#微分形式全体-ωm)
    - [局所作用素](#局所作用素)
  - [外微分](#外微分-1)
  - [外微分の引き戻し](#外微分の引き戻し)
    - [$k$ 形式の引き戻し](#k-形式の引き戻し)
- [リー微分と内部積](#リー微分と内部積)


# 外微分

## 微分形式全体 $Ω'(M)$

・$m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、
$$\Omega^*(M)=\bigoplus_{k=0}^m\Omega^k(M)$$
は、ウェッジ積について $\bm{R}$ 上次数付き単位的多元環。

    ・非可換で、連結でない。
    ・一個づつでなく、多項式で出てくることに注意。

---

### 局所作用素

・$m$ 次元 $C^{\infty}$ 多様体 $M$、反導分 $D:\Omega^*(M)\to\Omega^*(M)$ とする。
このとき、
$$\forall k,\ \forall\omega\in\Omega^k(M),\ \forall\text{ 開集合 }U\sub M\text{ に対して、}\\\ \\
\omega(p)=0\ \ (\forall p\in M)\text{ ならば、}D\omega=0$$
ここで、この性質を持つ線形写像を局所作用素という。

    ・導分でも成り立つ。

- $m$ 次元 $C^{\infty}$ 多様体 $M$、$\bm{R}$ 線形写像 $D:\Omega^*(M)\to\Omega^*(M)$ とする。
このとき、
$$D\text{ は局所作用素}\\\ \\
\iff\forall k,\ \forall\omega_1,\omega_2\in\Omega^k(M),\ \forall\text{ 開集合 }U\sub M\text{ に対して、}\\\ \\
\omega_1(p)=\omega_2(p)\ \ (\forall p\in M)\text{ ならば、}D\omega_1=D\omega_2$$

---

## 外微分

<dl><dt>

・$m$ 次元 $C^{\infty}$ 多様体 $M$、微分形式全体 $\Omega^*(M)$ とする。
このとき、外微分 $D$：
$$D:\Omega^*(M)\to \Omega^*(M)\\\ \\
D\text{ は }\bm{R}\text{ 線形で、次数 }1\text{ の反導分}\\\ \\
D^2=0,\quad\forall f\in \Omega^0(M)\text{ に対して、}Df=df\\\ \\$$

</dt><dd>

- $m$ 次元 $C^{\infty}$ 多様体 $M$、チャート $(U,\phi)$ とする。
このとき、
$$d_U:\Omega^*(U)\to \Omega^*(U)\\\ \\
d_U(\omega)=d_U\left(\sum a_Idx^I\right)=\sum da_I\wedge dx^I$$
と定めると、これは一意的に定まる外微分。
<br>

- $m$ 次元 $C^{\infty}$ 多様体 $M$、微分形式全体 $\Omega^*(M)$ とする。
このとき、
$$d:\Omega^*(M)\to\Omega^*(M)\\\ \\
\forall p\in M\text{ に対して、}\text{適当なチャート }p\in (U,\phi)\text{ を取って、}\\\ \\
(d\omega)(p)=(d_U\omega)(p)\\\ \\
$$
と定めると、これはwell-defined、すなわちチャートによらず、さらに一意的に定まる外微分。

</dd></dl>

---

## 外微分の引き戻し

### $k$ 形式の引き戻し

<dl><dt>

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $F:M\to N$ とする。
このとき、余微分 $F^*$：
$$F^*_p:A_k(T_{F(p)}N)\to A_k(T_pM)\\\ \\
F^*_p(\omega_{F(p)})(v_{1,p}\wedge...\wedge v_{k,p})=\omega_{F(p)}(F_{*,p}(v_{1,p})\wedge...\wedge F_{*,p}(v_{k,p}))$$
はwell-definedな線形写像。
ここで、$F^*_p(\omega_p)$ を $F$ によるコベクトル $\omega_{F(p)}$ の引き戻しという。

    ・多重コベクトル関手のこと。CAT_Culc参照。
<br>

</dt><dd>

- $k$ 形式 $\omega:N\to \Lambda^k(T^*N)$ とする。
このとき、
$$F^*\omega:M\to \Lambda^k(T^*M)\\\ \\
(F^*\omega)(p)=F^*_p(\omega_{F(p)})$$
は $M$ 上の $k$ 形式。
特に、この定義は一形式の引き戻しと整合する。

      ・k=0のときは余微分が定義できないので、関数の引き戻しは前出てきたやつが定義。

<br>

- $m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $F:M\to N$、$k$ 形式 $\omega,\tau:N\to\Lambda^k(T^*N)$、$g\in C^{\infty}(N)$ とする。
このとき、
$$F^*(\omega+\tau)=F^*(\omega)+F^*(\tau)\\\ \\
F^{*}(g\omega)=(F^*g)(F^*\omega)$$

      ・別にgはC^∞でなくてもよい。
<br>

- $m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $F:M\to N$、$k$ 形式 $\omega:N\to\Lambda^k(T^*N)$、$l$ 形式 $\tau:N\to\Lambda^l(T^*N)$ とする。
このとき、
$$F^*(\omega\wedge\tau)=(F^*\omega)\wedge (F^*\tau)$$

---

- $m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $F:M\to N$、$C^{\infty}$ $k$ 形式 $\omega\in\Omega^k(N)$ とする。
このとき、$F^*\omega\in \Omega^k(M)$ で、
$F^*\omega=$

      ・C^∞写像gなら、F^*(gω)もC^∞。


</dd></dl>

---


# リー微分と内部積

    ・外微分をチャートによらずに定義できる！？