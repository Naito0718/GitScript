
- [数え上げ測度](#数え上げ測度)
- [完備測度空間](#完備測度空間)
  - [測度空間の完備化](#測度空間の完備化)
    - [$σ$-有限測度空間の完備化と外測度](#σ-有限測度空間の完備化と外測度)



# 数え上げ測度

・$X$ を空でない集合とする。
このとき、
$$\mu:2^X\to[0,\infty],\quad\mu(E)=\begin{cases}
0   & (E=\phi) \\
\# E & (E{は有限集合}) \\
\infty    & (E{は無限集合})
\end{cases}$$
と定めると、これは可測空間 $(X,2^X)$ 上の測度。


- 空でない集合 $X$、数え上げ測度 $\mu$、$f:X\to[0,\infty]$ とする。
このとき、$$\int fd\mu=\sum_{x\in X} f(x)$$

        ・右辺はネット的な総和

---

# 完備測度空間

・測度空間 $(X,\mathfrak{M},\mu)$ とする。
このとき、完備測度空間 $X$：
$$\forall\text{ 零集合 }N\in\mathfrak{M},\forall\text{ 部分集合 }A\sub N\text{ に対して、}A\in\mathfrak{M}$$


## 測度空間の完備化

<dl><dt>

・測度空間 $(X,\mathfrak{M},\mu)$ とする。
また、
$$\overline{\mathfrak{M}}=\{E\sub X\ |\ \exist B\in\mathfrak{M},\exist\text{ 零集合 }N\in\mathfrak{M}\text{ であって、}E\Delta B\sub N\}\\\ \\
\overline{\mu}:\overline{\mathfrak{M}}\to[0,\infty]\\\ \\
\overline{\mu}(E)=\mu(B)$$
と定めると、$\overline{\mathfrak{M}}$ は $\sigma$-加法族で、$\overline{\mu}$ はwell-defined。
<br>

</dt><dd>

- $E\in\overline{\mathfrak{M}}$、$E$ に対して存在する $B,N\in\mathfrak{M}$ とする。
このとき、$B_1=B\cup N,\ B_2=B-N$ とすると、
$$B_1,B_2\in\mathfrak{M},\\\ \\
B_1-B_2\sub N,\quad\mu(B_1-B_2)=0\\\ \\
B_2\sub E,B\sub B_1,\quad\mu(B_1)=\mu(B)=\mu(B_2)\\\ \\
E\Delta B_1,\ E\Delta B_2\sub N$$
したがって、
$$E\in \overline{\mathfrak{M}}\Rightarrow \exist B_1,B_2\in\mathfrak{M}\text{ であって、}\\\ \\
B_2\sub E\sub B_1,\quad \overline{\mu}(E)=\mu(B_1)=\mu(B_2),\quad\mu(B_1-B_2)=0\\\ \\$$

- $\overline{\mu}$ は $\overline{\mathfrak{M}}$ 上の測度であって、$(X,\overline{\mathfrak{M}},\overline{\mu})$ は完備測度空間。

</dd></dl>

---

### $σ$-有限測度空間の完備化と外測度

    ・いつもの(R^N,B,m)の完備化が、伊藤ルベーグのルベーグ可測集合とルベーグ測度。別にどっちでやっても、完備性を仮定しなければ影響はない。
<br>

<dl><dt>

・測度空間 $(X,\mathfrak{M},\mu)$ とする。
このとき、
$$\mu^*2^X\to[0,\infty]\\\ \\
\mu^*(E)=\inf\{\mu(B)\ |\ B\in\mathfrak{M}\text{ であって、} E\sub B\}$$
と定めると、これはカラテオドリ外測度のところの定義と一致する。ここで、
$$\mathfrak{M}_*=\{A\in2^X\ |\ \mu^*(E\cap A)+\mu^*(E\cap A^c)=\mu^*(E),\ \forall E\in2^X\}\\\ \\
\mu_*=\mu^*|_{\mathfrak{M}_*}$$
と定める。
<br>

</dt><dd>

- $(X,\mathfrak{M}_*,\mu_*)$ は完備測度空間。さらに、$\mu$ を $\sigma$-有限測度とすると、
$$\forall E\in\mathfrak{M}_*\text{ に対して、}\exist B_1,B_2\sub\mathfrak{M}\text{ であって、}\\\ \\
B_2\sub E\sub B_1,\quad\mu(B_1-B_2)=0,\quad\mu_*(E)=\mu(B_1)=\mu(B_2)\\\ \\$$

      ・別に拡張の一意性は関係ない。
<br>

- $\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$ の完備化 $(X,\overline{\mathfrak{M}},\overline{\mu})$ とする。
このとき、
$$\mathfrak{M}_*=\overline{\mathfrak{M}},\quad\mu_*=\overline{\mu}$$


</dd></dl>






