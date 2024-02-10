
- [$D(R^N)$ と $ε(R^N)$](#drn-と-εrn)
  - [コンパクト台超関数空間 $ε'(R^N)$](#コンパクト台超関数空間-εrn)
  - [Diracのデルタ超関数](#diracのデルタ超関数)
- [緩増加関数空間 $T$](#緩増加関数空間-t)
  - [多項式空間 $P$](#多項式空間-p)
  - [多項式的に増加する関数](#多項式的に増加する関数)
- [急減少関数空間 $S$](#急減少関数空間-s)
  - [同値性いろいろ](#同値性いろいろ)
  - [緩増加関数と急減少関数](#緩増加関数と急減少関数)
  - [急減少関数空間上の連続線形写像](#急減少関数空間上の連続線形写像)
  - [急減少関数と $L^p$ 空間](#急減少関数と-lp-空間)
- [超関数と急減少関数](#超関数と急減少関数)
  - [緩増加超関数空間 $S'$](#緩増加超関数空間-s)
  - [緩増加超関数空間 $S'$ の性質](#緩増加超関数空間-s-の性質)


# $D(R^N)$ と $ε(R^N)$

・
$$D(\bm{R}^N)\sub\epsilon(\bm{R}^N),\quad\overline{D(\bm{R}^N)}=\epsilon(\bm{R}^N)$$

---

## コンパクト台超関数空間 $ε'(R^N)$

<dl><dt>

・$$\epsilon'(\bm{R}^N)=\{u'\in D'(\bm{R}^N)\ |\ \mathrm{supp}\ u\sub\bm{R}^N\text{ はコンパクト}\}$$
と定める。ここで、$\epsilon(\bm{R}^N)$ をコンパクト台超関数空間という。
<br>

</dt><dd>

- 線形汎関数 $u:D(\bm{R}^N)\to\bm{C}$ とする。
このとき、
$$u\in\epsilon'(\bm{R}^N)\iff u\text{ は }\epsilon(\bm{R}^N)\text{ の位相で連続}\iff u\in D'(\bm{R}^N)\text{ かつ、}\exist h\in D(\bm{R}^N)\text{ であって、}u=hu$$
特に、$u\in D'(\bm{R}^N)$ とすると、
$$\mathrm{supp}\ u\text{ がコンパクトでない}\\\ \\
\Rightarrow \forall n\in\bm{N}\text{ に対して、}\exist\phi_n\in D(\bm{R}^N)\text{ であって、}\\\ \\
u(\phi_n)=1,\quad\mathrm{supp}\ \phi_n\sub\{x\in\bm{R}^N\ |x|>n\}$$
さらに、上記の同値な命題が成り立つとき、
$$\text{ある }\tilde{u}:\epsilon(\bm{R}^N)\to\bm{C}\text{ が一意的に存在して、}\forall \phi\in D(\bm{R}^N)\text{ に対して、}\\\ \\
\tilde{u}(\phi)=u(\phi)$$
ここで、$\epsilon'(\bm{R}^N)$ は $\epsilon(\bm{R}^N)$ 上の連続線形汎関数と一対一に対応するので、$\epsilon'(\bm{R}^N)$ を $\epsilon(\bm{R}^N)$ 上の連続線形汎関数全体とみなす。
<br>

      ・hu(φ)=u(hφ)
<br>

- $$\epsilon'(\bm{R}^N)\sub\mathcal{S}'_N$$
すなわち、$\phi_n\in D(\bm{R}^N)$ が $\mathcal{S}_N$ の位相で収束するならば、$\lim_{n\to\infty}u(\phi_n)=u(\lim_{n\to\infty}\phi_n)$


</dd></dl> 


---

## Diracのデルタ超関数

・$x\in\bm{R}^N$ とする。
このとき、
$$\delta_x:\epsilon(\bm{R}^N)\to\bm{C}\\\ \\
\delta_x(f)=f(x)$$
と定めると、$\delta_x\in\epsilon'(\bm{R}^N)$ であって、
$$\mathrm{supp}\ \delta_x=\{x\}$$
ここで、$\delta_x$ を $\{x\}$ を台とするDiracのデルタ関数という。

---

# 緩増加関数空間 $T$

<dl><dt>

・$$\mathcal{T}_N=\{f\in C^{\infty}(\bm{R}^N)\ |\ \forall\text{ 多重指数 }I\text{ に対して、}\exist M>0,\ \exist n\in\bm{N}\text{ であって、}\forall x\in\bm{R}^N\text{ に対して、}|\partial^If(x)|\le M(1+|x|^2)^n\}$$
と定めると、$\mathcal{T}_N$ は $\bm{C}$ 上ベクトル空間。ここで、$\mathcal{T}_N$ を緩増加関数空間という。
<br>

</dt><dd>

- $f\in \mathcal{T}_N$、多重指数 $I$ とする。
このとき、$\partial^If\in \mathcal{T}_N$。
<br>

- $1$ 階以上の偏導関数がすべて有界な $C^{\infty}$ 関数 $\Psi:\bm{R}^N\to\bm{R}^N$、$f\in\mathcal{T}_N$ とする。
このとき、$f\circ\Psi\in\mathcal{T}_N$


</dd></dl> 

---

## 多項式空間 $P$

<dl><dt>

・多重指数 $I$ とする。
このとき、
$$id^I:\bm{R}^N\to\bm{R}\\\ \\
id^I(x)=x_1^{I_1}...x_N^{I_N}\\\ \\
\mathcal{P}_N=\mathrm{span}\{id^J\ |\ J\text{ は多重指数}\}$$
と定めると、$\mathcal{P}_N$ は $\bm{C}$ 上ベクトル空間であって、$\forall x\in\bm{R}^N$ に対して $id^I(x)=x^I$ である。ここで、$\mathcal{P}$ を多項式空間という。
<br>

</dt><dd>

- $f\in \mathcal{P}_N$、多重指数 $I$ とする。
このとき、$\mathcal{P}_N\sub C^{\infty}(\bm{R}^N)$ であって、$\partial^If\in \mathcal{P}_N$。したがって、$\mathcal{P}_N\sub\mathcal{T}_N$
<br>

- $$\mathcal{P}_N\mathcal{T}_N\sub\mathcal{T}_N$$

</dd></dl> 

---

## 多項式的に増加する関数

<dl><dt>

・$$P=\{f:\bm{R}^N\to\bm{C}\ |\ \exist M>0,\ \exist n\in\bm{N}\text{ であって、}\forall x\in\bm{R}^N\text{ に対して、}|f(x)|\le M(1+|x|^2)^n\}$$
と定めると、$P$ は $\bm{C}$ 上ベクトル空間。ここで、$f\in P$ を多項式的に増加する関数という。
<br>

</dt><dd>

- $f,g\in P$ とする。また、$|\alpha|\le1\text{  なる }\alpha\in\bm{C}$ とし、
$$\alpha:\bm{R}^N\to\bm{C}\\\ \\
\alpha(x)=\alpha$$
と定める。
このとき、$|f|,fg,\alpha\in P$。特に、$\forall n\in\bm{N}\text{ に対して、}(1+|f|^2)^n\in P$
<br>

- 有界関数 $F_1:\bm{R}^N\to\bm{C},\ F_2:\bm{R}^N\to\bm{R}^m$、$f\in P$ とする。
このとき、$F_1f,\ |F_2|f\in P$
<br>

- $1$ 階偏導関数がすべて有界な $C^1$ 関数 $\Psi:\bm{R}^N\to\bm{R}^N$、$f\in P$ とする。
このとき、$|\Psi|,f\circ\Psi\in P$
<br>

      ・有限増分の定理！
<br>

</dd></dl> 

---

# 急減少関数空間 $S$

<dl><dt>

・
$$\mathcal{S}_N=\left\{f\in C^{\infty}(\bm{R}^N)\ |\ \forall\text{ 多重指数 }I,J\text{ に対して、}\sup_{x\in\bm{R}^N}|x^I\partial^Jf(x)|<\infty\right\}\\\ \\
p_{n,I},p_n:\mathcal{S}_N\to[0,\infty)\\\ \\
p_{n,I}(f)=\sup_{x\in\bm{R}^N}\Big\{(1+|x|^2)^n|\partial^If(x)|\Big\}\\\ \\
p_n(f)=\max_{|I|\le n}p_{n,I}(f)\\\ \\
\mathcal{P}=\{p_n\ |n\in\bm{N}\},\quad\mathcal{P}_I=\{p_{n,I}\ |\ n\in\bm{N},\ I\text{ は多重指数}\}$$
と定めると、$\mathcal{S}_{\bm{N}}$ は $\bm{C}$ 上ベクトル空間で、$\forall n\in\bm{N},\forall\text{ 多重指数 }I$ に対して、$p_{n,I}$ は $\mathcal{S}_N$ 上のセミノルム、$\forall n\in\bm{N}$ に対して $p_n$ は $\mathcal{S}_N$ 上のノルム。
さらに、$\mathcal{P},\ \mathcal{P}_I$ は共にセミノルムの分離族。
ここで、$\mathcal{P}$ をセミノルムの分離族とする セミノルム空間 $\mathcal{S}_N$ を $\bm{R}^N$ 上の急減少関数空間と言う。
<br>

    ・Nはいつも0含む。
<br>

</dt><dd>

- $$\forall x\in\bm{R}^N\text{ に対して、}|x|\le(1+|x|^2)\\\ \\$$

- $f\in\mathcal{S}_N$ とする。
このとき、$f$ は有界であって、
$$\forall k\in\bm{N},\ \forall\text{ 多重指数 }I\text{ に対して、}\lim_{|x|\to\infty}|x|^k\partial^If(x)=0,\quad\partial^If\in\mathcal{S}_N\\\ \\$$

- $$f\in C_0(\bm{R}^N)\iff\lim_{|x|\to\infty}f(x)=0$$
特に、$\mathcal{S}_N\sub C_0(\bm{R}^N)$
<br>

- 点列 $(f_n)\sub\mathcal{S}_N$、$f\in\mathcal{S}_N$ とする。
このとき、
$$f_n\to f\iff\forall\text{ 多重指数 }I,J\text{ に対して、}\sup_{x\in\bm{R}^N}|x^I\partial^Jf_n-x^I\partial^J f|=0\\\ \\$$

- $\mathcal{S}_N$ はFrechet空間。

</dd></dl> 

---

## 同値性いろいろ

<dl><dt>

・$u\in C^{\infty}(\bm{R}^N)$ とする。

</dt><dd>

・$$\forall N\in\bm{N},\forall\text{ 多重指数 }I\text{ に対して、}\lim_{|x|\to\infty}(1+|x|)^N|\partial^Iu(x)|=0\\\ \\
\iff\forall N\in\bm{N},\forall\text{ 多重指数 }I\text{ に対して、}\exist M>0\text{ であって、}\forall x\in\bm{R}^N\text{ に対して、}(1+|x|)^N|\partial^Iu(x)|<M\\\ \\$$

- 点列 $(f_n)\sub\mathcal{S}_N$、$f\in\mathcal{S}_N$ とする。
このとき、
$$f_n\to f\quad(\mathcal{P}_I\text{ によるセミノルム位相})\iff\forall\text{ 多重指数 }I,J\text{ に対して、}\sup_{x\in\bm{R}^N}|x^I\partial^Jf_n-x^I\partial^J f|=0$$
特に、$\mathcal{P}_I$ をセミノルムの分離族とするセミノルム空間 $\mathcal{S}_{N,I}$ はFrechet空間。

</dd></dl> 

---

## 緩増加関数と急減少関数

・$$D(\bm{R}^N)\sub\mathcal{S}_N\sub\mathcal{T}_N,\ \quad\mathcal{S}_N\mathcal{T}_N\sub\mathcal{T}_N\\\ \\$$

- $\Psi,\Psi^{-1}$ の $1$ 階以上の偏導関数がすべて有界な $C^{\infty}$ 微分同相写像 $\Psi:\bm{R}^N\to\bm{R}^N$、$f\in\mathcal{S}_N$ とする。
このとき、$f\circ\Psi\in\mathcal{S}_N$

---

## 急減少関数空間上の連続線形写像

・多重指数 $I$、$g\in\mathcal{T}_N$、$\Psi,\Psi^{-1}$ の $1$ 階以上の偏導関数がすべて有界な $C^{\infty}$ 微分同相写像 $\Psi:\bm{R}^N\to\bm{R}^N$ とする。
このとき、
$$\partial^I,\ \times g,\ \circ\Psi:\mathcal{S}_N\to\mathcal{S}_N\\\ \\
\partial^I(f)=\partial^If\\\ \\
\times g(f)=fg\\\ \\
\circ\Psi(f)=f\circ\Psi\\\ \\$$
と定めると、これらはすべて連続線形写像。
<br>

- $f\in L^{\infty}(\bm{R}^n)\cap C(\bm{R}^N)$ とする。
このとき、$$\|f\|_{L^{\infty}}=\sup_{x\in\bm{R}^n}|f(x)|<\infty\\\ \\$$

---

## 急減少関数と $L^p$ 空間

・$p\in[1,\infty]$  とする。
このとき、
$$[]_p:\mathcal{S}_N\to L^p(\bm{R}^N)\\\ \\
[]_p(f)=[f]$$
と定めると、これは連続線形写像。特に、$\mathcal{S}_N\sub L^p(\bm{R}^N)$ とみなせる。
<br>

      ・極座標変換！

---

# 超関数と急減少関数

・$$D(\bm{R}^N)\sub\mathcal{S}_N,\quad\overline{D(\bm{R}^N)}=\mathcal{S}_N$$
すなわち、テスト関数空間は急減少関数空間において稠密。
<br>

- 線形汎関数 $u:D(\bm{R}^N)\to\bm{C}$ とする。
このとき、$$u\text{ は }\mathcal{S}_N\text{ の相対位相で連続 }\\\ \\
\iff\exist \mathcal{S}_N\text{ のセミノルム分離族のノルム } p_n\in\mathcal{P}_{\mathcal{S}_N},\exist M>0\text{ であって、}\forall \phi\in D(\bm{R}^N)\text{ に対して、}\\\ \\
|u(\phi)|\le Mp_n(\phi)$$
さらに、上記が満たされるとき、
$$\text{ある連続線形汎関数 }\tilde{u}:\mathcal{S}_N\to\bm{C}\text{ が一意的に存在して、}\forall \phi\in D(\bm{R}^N)\text{ に対して、}\\\ \\
\tilde{u}(\phi)=u(\phi)\\\ \\$$

- 線形汎関数 $u:D(\bm{R}^N)\to\bm{C}$、コンパクト集合 $K\sub\bm{R}^N$、点列 $(\phi_i)\sub D(\bm{R}^N)$、$\phi\in D_K(\bm{R}^N)$ とする。
このとき、$$(\phi_i)\text{ は }\phi\text{ に }D_K(\bm{R}^N)\text{ の位相で収束}\Rightarrow(\phi_i)\text{ は }\phi\text{ に }\mathcal{S}_N\text{ の位相で収束}\\\ \\
u\text{ が }\mathcal{S}_N\text{ の位相で連続}\Rightarrow u\in D'(\bm{R}^N)$$

---

## 緩増加超関数空間 $S'$

・$$\mathcal{S}'_N=\{u:D(\bm{R}^N)\to\bm{C}\ |\ u\text{ は線形汎関数であって、}\mathcal{S}_N\text{ の位相で連続 }\}$$
と定めると、$\mathcal{S}'_N$ は $\bm{C}$ 上ベクトル空間であって、$D'(\bm{R}^N)$ の部分空間。
ここで、$\mathcal{S}'_N$ を緩増加超関数空間という。また、$\mathcal{S}_N$ 上の連続線形汎関数と一対一に対応するので、$\mathcal{S}'_N$ を $\mathcal{S}_N$ 上の連続線形汎関数全体とみなす。
<br>

    ・超関数空間D'(R^N)の部分空間であるためにはD(R^N)上の関数でなければならない。

---

## 緩増加超関数空間 $S'$ の性質

<dl><dt>

・$u\in S'_N$、多重指数 $I$、$g\in\mathcal{T}_N$、$\Psi,\Psi^{-1}$ の $1$ 階以上の偏導関数がすべて有界な $C^{\infty}$ 微分同相写像 $\Psi:\bm{R}^N\to\bm{R}^N$ とする。
このとき、
$$\partial^Iu,\ fu,\ u\circ\Psi\in S'(N)$$
ここで、$u:D(R^N)\to\bm{C}$ ならば、$\partial^IU,\ fu,\ u\circ\Psi$ もすべて定義域は $D(\bm{R}^N)$ 。

    ・全部超関数の意味。
<br>

</dt><dd>

- $p\in[1,\infty]$  とする。
このとき、$$L^p(\bm{R}^N)\sub\mathcal{S}'_N\\\ \\$$

      ・超関数空間の意味。S_Nの位相でも収束する。
<br>

- 多項式的に増加するBorel関数 $f\in P$ とする。このとき、
$$f\in L^1_{loc}(\bm{R}^N),\quad [f]\in \mathcal{S}'_N$$
特に、$\mathcal{T}_N\sub\mathcal{S}'_N$

</dd></dl> 




