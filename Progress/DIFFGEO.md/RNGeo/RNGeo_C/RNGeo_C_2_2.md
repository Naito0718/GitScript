
- [線積分](#線積分)
  - [線積分の性質](#線積分の性質)
  - [一次元チェイン上の線積分](#一次元チェイン上の線積分)



# 線積分

・区分的 $C^1$ 曲線 $f:[a,b]\to\bm{R}^n$、開集合 $f(I)\sub U$、連続関数 $F:U\to\bm{R}^n$ とする。
このとき、$$\int_CF=\int_a^b(F(f(t))\cdot f'(t))dt$$
と定めると、これはwell-defined、すなわち区分的 $C^1$ 同値類 $(f)$ によらない。

---

## 線積分の性質

<dl><dt>

・区分的 $C^1$ 曲線 $C$、$C$ 上で定義されている連続関数 $F_1,F_2:C\to \bm{R^n}$、$\alpha\in\bm{R}$ とする。
<br>

</dt><dd>

- $$\int_C(F_1+F_2)=\int_CF_1+\int_CF_2,\quad\int_C(\alpha F_1)=\alpha\int_CF_1\\\ \\$$

- $$\int_{-C}F=-\int_CF\\\ \\$$

- $C$ の弧長 $l(C)$ とする。
このとき、
$$\left|\int_CF\right|\le\sup_{x\in C}|F(x)|l(C)$$

</dd></dl>

---

## 一次元チェイン上の線積分

<dl><dt>

・区分的 $C^1$ 曲線 $C_1,...,C_k$、$D_1,...,D_l$ とする。
このとき、
$$(C_1,...,C_k)\sim(D_1,...,D_l)\\\ \\
\iff(C_1,...,C_k)\text{ は、順序の入れ替え、曲線の分割または始点と終点の結合、互いに逆向きである曲線の組の除去および挿入によって }(D_1,...,D_l)\text{ に移る}$$
と定めると、これは同値関係。
ここで、組 $(C_1,...,C_k)$ を一次元チェインという。
<br>

</dt><dd>

- $\bm{R}^n$ 内の一次元チェイン $(C_1,...,C_k)$、$C=\bigcup_{i=1}^k C_i$ 上連続な $F:C\to \bm{R}^n$ とする。
このとき、$$\int_CF=\sum_{i=1}^k\int_{C_i}F$$
と定めると、これはwell-defined、すなわち等しいチェインによらない。さらに、
$$\int_C(F_1+F_2)=\int_CF_1+\int_CF_2,\quad\int_C(\alpha F_1)=\alpha\int_CF_1\\\ \\
\int_{-C}F=-\int_CF\\\ \\
\left|\int_CF\right|\le\sup_{x\in C}|F(x)|l(C)$$
もまったく同様に成り立つ。
<br>

- $A\in O(n)$、$b\in\bm{R}^n$ とする。
このとき、
$$T_{A,b}:\bm{R}^n\to\bm{R}^n\\\ \\
T_{A,b}(x)=Ax+b$$
と定めると、
$$\int_{T_{A,b}(C)}F=\int_CF\\\ \\$$

      ・リーマン幾何の、積分の変数変換で示すべきかもしれない。
      ・というかベクトル場の変換が意味不明だな。

</dd></dl>


