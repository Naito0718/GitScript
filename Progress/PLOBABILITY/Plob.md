
- [第一章：確率モデル](#第一章確率モデル)
  - [定義と基本的な性質](#定義と基本的な性質)
    - [確率空間](#確率空間)
    - [条件付き確率](#条件付き確率)
      - [ベイズの定理](#ベイズの定理)
    - [分布](#分布)
      - [分布関数](#分布関数)
      - [ルベーグ-スティルチェス測度](#ルベーグ-スティルチェス測度)
      - [分布の種類](#分布の種類)
    - [完備確率空間](#完備確率空間)


# 第一章：確率モデル

## 定義と基本的な性質

### 確率空間

<dl><dt>

・確率空間 $(\Omega,\mathfrak{M},P)$：測度空間 $(\Omega,\mathfrak{M},P)$ であって、全確率：$P(\Omega)=1$

    ・全部が起きることは起こりうる。Aでないことも起こりうる。AまたはBまたは...も起こりうる。
    ・まず興味のある事柄が必ず入っている集合 Ω を決定し、その後細かさに応じて σ-加法族 を決定する。

</dt><dd>

- $$P(A)+P(A^c)=1\\\ \\
P(A\cup B)=P(A)+P(B)-P(A\cap B)\\\ \\$$

- 有限加法族 $\mathcal{F}\sub2^\Omega$、有限加法的確率 $P:\mathfrak{M}\to[0,1]$ とする。このとき、
$$P\text{ は }\sigma(\mathcal{F})\text{ 上の確率に一意拡張できる}\\\ \\
\iff\forall\text{ 非交叉列 }A_n\sub\mathcal{F},\ \bigcup A_n\in\mathcal{F}\text{ に対して、}P(\bigcup A_n)=\sum P(A_n)\\\ \\$$

- 可測空間 $\Omega$、有限加法的確率 $P:\mathfrak{M}\to[0,1]$ とする。
このとき、
$$P\text{ は確率 }\\\ \\
\iff\forall\text{ 単調増加列 }E_n\subset\mathfrak{M}\text{ に対し、}P(\bigcup E_n)=\lim P(E_n)\\\ \\
\iff\forall\text{ 単調減少列 }E_n\sub\mathfrak{M}\text{ に対し、}P(\bigcap E_n)=\lim P(E_n)$$

      ・一般の可測空間上でもμ(E_1)<∞にすれば成り立つ
      ・Pの連続性とも言える

</dd></dl>

---

### 条件付き確率

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

#### ベイズの定理

・確率空間 $(\Omega,\mathfrak{M},P)$、有限可測分割  $\Omega=\bigcup_i^n A_i$ が $P(A_i)>0$ を満たすとする。
このとき、$P(B)>0$ に対して、
$$P(A_i|B)=\frac{P(A_i)P(B|A_i)}{\sum_{j=1}^n P(A_j)P(B|A_j)}$$

    ・事象Bが起こったとき、その原因がA_iであった確率を得ることができる

---

### 分布

<dl><dt>

・確率空間 $(\Omega,\mathfrak{M},P)$ とする。
このとき、 $d$ 次元確率変数（ベクトル）：$\bm{R}^d$ 値可測関数 $X:\Omega\to\bm{R}^d$

    ・X_i も確率変数

</dt><dd>

- 確率空間 $(\Omega,\mathfrak{M},P)$、$d$ 次元確率変数 $X:\Omega\to\bm{R}^d$ とする。
このとき、
$$\mu:\mathfrak{B}_{\bm{R}^d}\to[0,1]\\\ \\
\mu(B)=P(X^{-1}(B))$$ は $(\bm{R}^d,\mathfrak{B}_{\bm{R}^d})$ 上の確率。
ここで、この $\mu$ を $X$ の分布という。

      ・確率空間を明示しなくても良くなる。
      ・X の法則ともいう。

</dd></dl>

#### 分布関数

・確率空間 $(\Omega,\mathfrak{M},P)$、$d$ 次元確率変数 $X:\Omega\to\bm{R}^d$、$X$ の分布 $\mu$ とする。
このとき、$X$ の分布関数：
$$F:\bm{R}^d\to[0,1]\\\ \\
F(x)=\mu((-\infty,x_1]\times...\times(-\infty,x_d])\\\ \\=P(X_1(\omega)\le x_1,...,X_d(\omega)\le x_d)$$

<dl><dt>

・確率変数 $X:\Omega\to\bm{R}$、$X$ の分布 $\mu$、分布関数 $F$ とする。

</dt><dd>

- $F$ は単調増加で右連続：
$$x\le y\Rightarrow F(x)\le F(y),\quad\lim_{y\to+x} F(y)=F(x)$$
- $$\lim_{x\to\infty} F(x)=1,\quad \lim_{x\to-\infty} F(x)=0$$
- 逆に、上記の $2$ つが成り立つような $F:\bm{R}\to[0,1]$ が与えられたとする。このとき、

   - $\mu_F((-\infty,x])=F(x)$ を満たす $(\bm{R},\mathfrak{B}_{\bm{R}})$ 上の確率 $\mu_F$ がただ一つ存在する。
  <br>
   - 確率空間 $(\bm{R},\mathfrak{B}_{\bm{R}},\mu_F)$ に対して、
  恒等写像 $id:\bm{R}\to\bm{R}$ の分布関数は $F(x)$
  <br>

         ・分布関数を「上記の2つ」が成り立つようなFとして定義してもよい。
         ・分布関数 F のみによって定義される確率 μ_F を Fの分布という。 

- $$\mu(\{x\})=F(x)-\lim_{y\to-x}F(y)\\\ \\$$

- $F$ の不連続点は高々可算個。

</dd></dl>

---

#### ルベーグ-スティルチェス測度

    ・結局実数値測度の積分のこと？
    ・ちょっと違うっぽい

・$f:\bm{R}\to\bm{R}$ とする。
このとき、総変動、有界変動、局所有界変動：
$$V(f)=\sup_{I\sub\bm{R}}\sup_{\Delta}\sum_{i\in\Delta}|f(x_i)-f(x_{i-1})|\\\ \\
V(f)<\infty\\\ \\
\forall\text{ 有界閉区間 }I\text{ で有界変動}$$

    ・閉区間では左端のsupは消せる。
    ・開区間、半開区間なども同様。
    ・閉区間上の関数なら、有界変動⇔局所有界変動


<dl><dt>

・確率変数 $X:\Omega\to\bm{R}$、$X$ の分布 $\mu$、分布関数 $F$ とする。

</dt><dd>

- 単調増加な有界関数は、有界変動関数。特に、分布関数は有界変動。
- 有界変動関数は有界関数。
- 有界変動関数 $f,g:\bm{R}\to\bm{R}$、$\alpha\in\bm{R}$ とする。このとき、
$$f+g,\ \alpha f,\ fg$$は有界変動関数。
- $f:\bm{R}\to\bm{R}$ とする。
このとき、
$$f\text{ は有界変動}\iff f_i\text{ は有界変動}\\\ \\$$

- $f:\bm{R}\to\bm{R}$ とする。
このとき、
$f\text{ は有界変動 }\iff\exist\text{ 有界単調増加関数 }\phi,\psi\text{ }$

</dd></dl>

---

#### 分布の種類

・確率空間 $(\Omega,\mathfrak{M},P)$、$d$ 次元確率変数 $X:\Omega\to\bm{R}^d$、$X$ の分布関数 $F:\bm{R}^d\to[0,1]$ とする。
このとき、$X$ が離散型、連続型、絶対連続型：
$$\exist\text{ 高々可算 }A\sub\bm{R}^d\text{ であって、}P(X^{-1}(A))=1\\\ \\
F\text{ が }\bm{R}^d\text{ 上連続}\\\ \\
\exist f\in\mathcal{L}^1_{\bm{R_+}}(\bm{R}^d),\ \int_{\bm{R}^d}f(x)dx=1\text{ であって、}\\F(x)=\int_{(-\infty,x_1]\times...\times[-\infty,x_d)} f(y)dy$$

    ・Xが絶対連続型のときに存在する f をXの密度関数という。

---

### 完備確率空間

・確率空間 $(\Omega,\mathfrak{M},P)$ とする。
このとき、完備確率空間 $(\Omega,\mathfrak{M},P)$：
$$A\sub \Omega,\ \exist N\sub\Omega\text{ であって、}P(N)=0\Rightarrow A\in\mathfrak{M}$$

