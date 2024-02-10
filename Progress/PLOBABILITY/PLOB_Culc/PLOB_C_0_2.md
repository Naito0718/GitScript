
- [条件付き確率](#条件付き確率)
  - [ベイズの定理](#ベイズの定理)



# 条件付き確率

<dl><dt>

・確率空間 $(\Omega,\mathfrak{M},P)$、$B\in\mathfrak{M}$ は $P(B)>0$ を満たすとする。
このとき、
$$P(\cdot|B):\mathfrak{M}\to[0,1]\\\ \\
P(A|B)=\frac{P(A\cap B)}{P(B)}$$は確率。
よって、これを$B$ の下での条件付き確率という。

・確率空間 $(\Omega,\mathfrak{M},P)$、$A,B\in\mathfrak{M}$ とする。
このとき、$A,B$ が独立：
$$P(A\cap B)=P(A)P(B)\\\ \\$$

</dt><dd>

- $$P(A|B)+P(A^c|B)=1\\\ \\
P(A\cap B)=P(B)P(A|B)\\\ \\
P(A)>0,\ P(A|B)=P(A)\Rightarrow P(B|A)=P(B)\\\ \\$$

- $P(A),P(B)>0 $ならば、
$$A,B\text{ が独立}\iff P(A|B)=P(A)\\\ \\$$

- $P$-零集合は任意の事象と独立。

</dd></dl>

---

## ベイズの定理

・確率空間 $(\Omega,\mathfrak{M},P)$、有限可測分割  $\Omega=\bigcup_i^n A_i$ が $P(A_i)>0$ を満たすとする。
このとき、$P(B)>0$ に対して、
$$P(A_i|B)=\frac{P(A_i)P(B|A_i)}{\sum_{j=1}^n P(A_j)P(B|A_j)}$$

    ・事象Bが起こったとき、その原因がA_iであった確率を得ることができる
