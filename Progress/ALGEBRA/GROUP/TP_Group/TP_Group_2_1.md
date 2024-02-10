
- [既約表現](#既約表現)
  - [不変部分空間](#不変部分空間)
  - [既約表現](#既約表現-1)
  - [無限次元](#無限次元)
- [指標](#指標)
  - [トレース $tr$](#トレース-tr)
  - [指標](#指標-1)



# 既約表現

## 不変部分空間

<dl><dt>

・$G-K$ 加群 $V$、部分空間 $W$、$g\in G$ とする。
このとき、$$\pi(g)W=\{\pi(g)w\ |\ w\in W\}$$
は $V$ の部分空間。
<br>

- $G-K$ 加群 $V$、閉部分空間 $W$、$g\in G$ とする。
このとき、不変部分空間 $W$：
$$\forall g\in G\text{ に対して、}\pi(g)W\sub W$$

      ・π(g)W=Wと同値。
<br>

</dt><dd>

- $G-K$ 加群 $V$、不変部分空間 $W$、$g\in G$ とする。
このとき、
$$\pi_W:G\to GL_K(W),\quad\pi_W(g)=\pi(g)|_W$$
と定めると、これは表現。

</dd></dl> 

---

## 既約表現

## 無限次元





# 指標

    ・無限次元表現でも存在する？

## トレース $tr$

・可換体 $K$、$A,B\in M(n,K)$ とする。
このとき、
$$\mathrm{tr}(A+B)=\mathrm{tr}A+\mathrm{tr}B,\quad \mathrm{tr}(A\alpha)=(\mathrm{Tr}A)\alpha\\\ \\
\mathrm{tr}(AB)=\mathrm{tr}(BA)\\\ \\
\forall P\in GL(n,K)\text{ に対して、}\mathrm{tr}(P^{-1}AP)=\mathrm{tr}A\\\ \\
\mathrm{tr}A^T=\mathrm{tr}A,\quad\mathrm{tr}\overline{A}=\overline{\mathrm{tr}A}\\\ \\$$

    ・結構可換体上でないと成り立たないものも多い。

- 可換体 $K$、$A\in M(n,K)$、$B\in M(m,K)$ とする。
このとき、
$$\mathrm{tr}(A\oplus B)=\mathrm{tr}A+\mathrm{tr}(B)\\\ \\
\mathrm{tr}(A\otimes B)=(\mathrm{tr}A)(\mathrm{tr}B)$$

      ・これは斜体上でもよい。

---

## 指標

・位相群 $G$、可換体 $K$、有限次元 $G-K$ 加群 $V$、基底 $\{u_i\}$、$gu_i=\sum u_ja_{ji}(g)$ とする。
このとき、指標 $\chi_V$：
$$\chi_V:G\to K\\\ \\
\chi(g)=\sum a_{ii}(g)$$
このとき、$\chi$ は連続で、well-defined、すなわち基底によらない。

    ・0次元G-K加群の指標は0と定める。
<br>

- 位相群 $G$、可換体 $K$、表現 $A:G\to GL(n,K)$ とする。
このとき、指標 $\chi$：
$$\chi_A:G\to K\\\ \\
\chi(g)=\mathrm{tr}(A(g))$$
このとき、$\chi$ は連続。

