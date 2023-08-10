- [写像](#写像)
        - [演算](#演算)
        - [連続性](#連続性)
- [同値関係](#同値関係)
        - [射影と断面](#射影と断面)
        - [誘導された写像](#誘導された写像)
  - [種々の同値関係](#種々の同値関係)
        - [直積と射影](#直積と射影)
- [ネット](#ネット)
- [フィルター](#フィルター)
- [距離空間](#距離空間)
        - [集合の性質](#集合の性質)
- [$R$](#r)
        - [連結性](#連結性)
    - [写像 $f$](#写像-f)
        - [$C,R$ への写像](#cr-への写像)
        - [区間の同値類別と円周 $S^1$](#区間の同値類別と円周-s1)




# 写像

##### 演算

集合 $X,Y$、写像 $f:X\to Y,\ g:Y\to X$ とする。
このとき、$g\circ f=1_X$ ならば、$f$ は単射で $g$ は全射 

##### 連続性

・位相空間 $X,Y$、$y_0\in Y$ に対して、
$f(x)=y_0$ は連続写像

- 連続写像 $f;X\to Y$ に対して、
$$f(\overline{A})\subset \overline{f(A)}$$

---
---
---

# 同値関係

 ##### 射影と断面

 ・集合 $X$、同値関係 $\sim$ とする。
 このとき、$$\pi:X\to X/\sim,\quad \pi(x)=[x]$$は全射。

 - 断面：$$s:X/\sim\to X,\quad s([x])=x\ (x{は代表元})$$
 <br>

 - 集合 $X$、同値関係 $\sim$ とすると、
            $s$ が断面$\iff p\circ s=1_{X/\sim}$

 - 断面 $s$ は単射。

---

 ##### 誘導された写像

 集合 $X,Y$、同値関係 $\sim_X$、$x\sim x'\Rightarrow f(x)=f(x')$ なる写像 $f:X\to Y$ とする。
 このとき、$$\tilde{f}:X/\sim\ \to Y,\quad \tilde{f}([x])=f(x)$$はwell-defined

    ・誘導された写像

 - $f=\tilde{f}\circ \pi$ 
 <br>

 - $f$ が全射ならば、誘導された写像 $\tilde{f}$ も全射
 <br>

 - 集合 $X,Y$、写像 $f:X\to Y$ に対して、
 $$x\sim x'\iff f(x)=f(x')$$は同値関係であって、誘導された写像 $\tilde{f}$ は単射。

  
 ---

 ## 種々の同値関係

 ##### 直積と射影

 ・直積集合 $X\times Y$ に対して、
 $$(x,y)\sim(x',y')\iff x=x'$$は同値関係。

 - 射影：$\pi(x,y)=x\times Y$、断面：$s(x\times Y)=(x,y_0)\ (y_0\in Y)$

 - $X/\sim\ \cong X,\quad(x\times Y)\leftrightarrow x\ ({濃度})$

 - 断面は包含写像 $i:X\to X\times Y,\ i(x)=(x,y_0)$ とみなせる。
  また、射影は $\pi':X\times Y\to X,\ \pi'(x,y)=x$ とみなせる。

 ---
 ---
 ---



# ネット的な性質の具体例

##### 有向集合

・自然数 $\bm{N}$ は、通常の大小関係で有向集合。

・位相空間 $\bm{X}$ の点 $x$ に対して、
$x$ の近傍全体 $\mathcal{N}(x)$ は逆包含関係により有向集合。

---

##### eventually in, frequently in

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

# 距離空間

##### 集合の性質

・開球 $B(x,r)=\{y\in X\ |\ d(x,y)<r\}$ は開集合

- 閉球 $\overline{B(x,r)}$ は閉集合

---
---
---
# $R$

    ・R^nは微分幾何

## 連結性

・空でない凸集合は弧状連結

→開球体、閉球体も弧状連結



---

## 写像 $f$

##### $C,R$ への写像

・絶対値とか和の連続性

---

##### 区間の同値類別と円周 $S^1$

・区間 $[0,1]$ に対する同値関係：
$$x\sim y\iff x=y\ or\ (x,y)=(1,0),(0,1)$$

- 同値類全体の集合：$I/\sim\ \cong[0,1)$。
さらに、$I/\sim\ \cong S^1,\quad f(t)=(\sin2\pi t,\cos2\pi t)$

        ・集合として、位相でない、近くとみなしたいならS^1
        ・できるだけ似ているように同値類別の代表元を選びたい！→胞体分割


---

# 単位球面

・$(\bm{R,C,H})^n$ に対して、
