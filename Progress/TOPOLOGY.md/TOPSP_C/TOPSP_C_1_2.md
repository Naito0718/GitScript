
- [ネット的な性質の具体例](#ネット的な性質の具体例)
  - [有向集合](#有向集合)
  - [eventually in, frequently in](#eventually-in-frequently-in)
- [フィルター的な性質の具体例](#フィルター的な性質の具体例)
  - [フィルターから生成されるフィルター](#フィルターから生成されるフィルター)
        - [有限交叉族 $F$ が生成するフィルター](#有限交叉族-f-が生成するフィルター)
        - [フィルターの制限と拡張](#フィルターの制限と拡張)
        - [写像によるフィルターの像](#写像によるフィルターの像)
  - [具体的なフィルター](#具体的なフィルター)
        - [Frechetフィルター](#frechetフィルター)
        - [近傍フィルター](#近傍フィルター)



# ネット的な性質の具体例

## 有向集合

・自然数 $\bm{N}$ は、通常の大小関係で有向集合。

・位相空間 $\bm{X}$ の点 $x$ に対して、
$x$ の近傍全体 $\mathcal{N}(x)$ は逆包含関係により有向集合。

---

## eventually in, frequently in

    ・全体集合Xはfrequently in

・点列

    ・自然数Nを添え字集合とするネット
    ・部分列は部分ネット、点列の部分ネットは部分列とは限らない。

・部分ネット$\forall,\exist,\ge,\Rightarrow,\ge$
    ・普遍部分ネット、任意のネットに対して普遍部分ネットが存在する

---
---
---

# フィルター的な性質の具体例

## フィルターから生成されるフィルター

##### 有限交叉族 $F$ が生成するフィルター

・集合 $X$、有限交叉族$\mathcal{F}$ に対して、
$$\lang\mathcal{F}\rang=\{G\subset X\ |\ \exist F_1,...,F_n\ {であって、}F_1\cap...\cap F_n\subset G\}$$はフィルター。

- 生成されるフィルター $\lang\mathcal{F}\rang$ は $\mathcal{F}$ を含む最小のフィルター。

--- 

・ 集合 $X$、$x\in X$ に対して、
一点集合 $\{x\}$ は有限交叉族。
したがって、$x$ が生成する単項フィルター $\lang\{x\}\rang$ が定まる。 

---

・フィルター $\mathcal{F},\mathcal{G}$ に対して、
 $$\mathcal{F},\mathcal{G}\ {は両立する}\ \iff\mathcal{F},\mathcal{G}\ {は共通の細分を持つ}$$

 - 両立するフィルター $\mathcal{F},\mathcal{G}$ に対して、
 $$\mathcal{F}\cup\mathcal{G}=\{A\ |\ A\in\mathcal{F}\text{ または }A\in\mathcal{G}\}$$は有限交叉族。
 <br>

 - 両立するフィルター $\mathcal{F},\mathcal{G}$ に対して、
 $$\lang\mathcal{F}\cup\mathcal{G}\rang=\mathcal{F}\vee\mathcal{G}=\{F\cap G\ |\ F\in\mathcal{F},\ G\in\mathcal{G}\}$$は $\mathcal{F},\mathcal{G}$ に共通する最小の細分。

---

##### フィルターの制限と拡張

・集合 $X$、フィルター $\mathcal{F}$、$A\subset X$ とする。
このとき、$A$ への制限：
$$\mathcal{F}|_A=\{F\cap A\ |\ F\in\mathcal{F}\}$$は $A$ 上のフィルター

- 集合 $X$、$A\subset X$、$A$ 上のフィルター $\mathcal{F}_A$ とする。
このとき、$$\mathcal{F}_X=\{G\subset X\ |\ \exist F\in\mathcal{F}_A\ {であって}\ F\subset G\}$$は $X$ 上のフィルター。

- $A\in \mathcal{F}$ となる $X$ 上のフィルター全体と、$A$ 上のフィルター全体は、
制限と拡大によって一対一に対応する。

---

##### 写像によるフィルターの像

・集合 $X,Y$、フィルター $\mathcal{F}_X$、$f:X\to Y$ に対して、
$$f[\mathcal{F}]=\{G\subset Y\ |\ f^{-1}(G)\in\mathcal{F}\}$$は $Y$ 上のフィルター。

- 超フィルター $\mathcal{U}$ の像 $f[\mathcal{U}]$ は超フィルター。

---

## 具体的なフィルター

##### Frechetフィルター

・無限集合 $X$ に対して、
$$\mathcal{F}=\{A\subset X\ |\ \#A^c<\infty\}$$はフィルター。

    ・（無限集合Xの補有限部分集合全体）

##### 近傍フィルター

・位相空間 $X$、$x\in X$ に対して、
$$\mathcal{F}=\mathcal{N}(x)$$はフィルター。


---
---
---

