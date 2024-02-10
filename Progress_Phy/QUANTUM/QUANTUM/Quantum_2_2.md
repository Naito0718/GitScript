
- [平行移動演算子と運動量演算子](#平行移動演算子と運動量演算子)
  - [ドブロイ波](#ドブロイ波)
  - [波動関数による表現](#波動関数による表現)
- [系の時間発展](#系の時間発展)
  - [時間発展演算子 $U(t)$](#時間発展演算子-ut)
  - [シュレディンガー方程式](#シュレディンガー方程式)
  - [ハミルトニアンの時間依存性](#ハミルトニアンの時間依存性)
    - [ハミルトニアンが時間に依存しないとき](#ハミルトニアンが時間に依存しないとき)
    - [ハミルトニアンが時間に依存するが交換するとき](#ハミルトニアンが時間に依存するが交換するとき)
    - [それ以外の時](#それ以外の時)
  - [時間依存しないハミルトニアン $H$](#時間依存しないハミルトニアン-h)
        - [エネルギー固有ケット](#エネルギー固有ケット)
        - [シュレディンガー表示とハイゼンベルグ表示](#シュレディンガー表示とハイゼンベルグ表示)
        - [ハミルトニアンと可換な演算子 $AH=HA$](#ハミルトニアンと可換な演算子-ahha)



# 平行移動演算子と運動量演算子
$$\bm{\mathcal{J}(x'),\ p}$$

・微小平行移動：$\mathcal{J}(dx')=1-i\frac{p_i}{\hbar}dx'_i$

→$\mathcal{J}(dx')\ket{x}=\ket{x+dx'}$

→$\bra{x'}\mathcal{J}(dx')\ket{\alpha}=\braket{x'-dx'|\alpha}$

→$\mathcal{J}(dx')^{\dag}\mathcal{J}(dx')=\mathcal{J}(dx')\mathcal{J}(dx')^{\dag}=1$

→$\mathcal{J}(-dx')=\mathcal{J}(dx')^{-1}$

→$\mathcal{J}(dx')\mathcal{J}(dx'')=\mathcal{J}(dx'')\mathcal{J}(dx')=\mathcal{J}(dx'+dx'')$

---

・交換関係：$[x_i,\mathcal{J}(dx'_j)]=dx_j\delta_{ij}$

→$[x_i,p_j]=i\hbar\delta_{ij}$

→$\braket{(\Delta x_i)^2}\braket{(\Delta p_i)^2}\ge\hbar^2/2$

→$[p_i,p_j]=0$

→$[p_i,\mathcal{J}(dx'_j)]=0$
特に、$\mathcal{J}(dx)\ket{p}=(1-\frac{ip_i}{\hbar}dx'_i)\ket{p}$

---

・有限平行移動：$\mathcal{J}(\Delta x_i)=\exp(-\frac{ip_i}{\hbar}\Delta x_i)$


---

## ドブロイ波

## 波動関数による表現
$$\bm{\psi(x)}$$


# 系の時間発展

## 時間発展演算子 $U(t)$

<dl><dt>

・状態 $\ket{\alpha}$ を時間発展させる時間発展演算子 $\ket{\alpha,t_0,t}=\mathcal{U}(t,t_0)\ket{\alpha,t_0}$ とする。
このとき、ハミルトニアン $H$：
$$\mathcal{U}(t_0+dt,t_0)=1-i\left(\frac{H}{\hbar}\right)dt\\\ \\$$

- 時間発展演算子 $\mathcal{U}(t,t_0)$ 全体の集合に対して、以下が成り立つことを要請する。
$$[\mathcal{U}(t,t_0)]^{\dag}\mathcal{U}(t,t_0)=1\\\ \\
\mathcal{U}(t_2,t_1)\mathcal{U}(t_1,t_0)=\mathcal{U}(t_2,t_0)\\\ \\$$

</dt><dd>

- $$\lim_{dt\to0}\mathcal{U}(t_0+dt,t_0)=1\\\ \\
[\mathcal{U}(t_0+dt,t_0)]^{\dag}\mathcal{U}(t_0+dt,t_0)=1\\\ \\
\mathcal{U}(t_0+dt_1+dt_2,,t_0+dt_1)\mathcal{U}(t_0+dt_1,t_0)=\mathcal{U}(t_0+dt_1+dt_2,t_0)\\\ \\$$

      ・こいつらはハミルトニアンのとこから導ける。

</dd></dl>

---

## シュレディンガー方程式

・
$$i\hbar\frac{\partial}{\partial t}\mathcal{U}(t,t_0)=H\mathcal{U}(t,t_0)$$
ここで、上式を時間発展演算子に対するシュレディンガー方程式という。
<br>

- $$i\hbar\frac{\partial}{\partial t}\ket{\alpha;t_0,t}=H\ket{\alpha;t_0,t}$$

---

## ハミルトニアンの時間依存性

### ハミルトニアンが時間に依存しないとき

・$H$ が時間に依存しないとする。
このとき、$$\mathcal{U}(t,t_0)=\exp\left(\frac{-iH(t-t_0)}{\hbar}\right)$$
特に、上記は $\mathcal{U}(t,t_0)$ に対するシュレディンガー方程式を満たし、
$$[\mathcal{U}(t,t_0)]^{\dag}\mathcal{U}(t,t_0)=1\\\ \\
\mathcal{U}(t_2,t_1)\mathcal{U}(t_1,t_0)=\mathcal{U}(t_2,t_0)\\\ \\
\lim_{t\to0}\mathcal{U}(t,t_0)=1$$
を満足する。

---

### ハミルトニアンが時間に依存するが交換するとき

- $[H(t'),H(t)]=0\ (\forall t,t')$のとき：
$$\mathcal{U}(t,t_0)=\exp\left(\frac{-i}{\hbar}\int_{t_0}^{t}H(t')dt'\right)$$

        ・偏微分すると[H(t),∫H(t')dt']みたいなのがでてくる

---

### それ以外の時

- $[H(t'),H(t)]\neq0$のとき：ダイソン級数

---
---
---

## 時間依存しないハミルトニアン $H$

- $[\mathcal{U}(t,t_0),H]=0$

##### エネルギー固有ケット
$$\ket{E_a}$$

・時間発展：
$$\ket{\alpha;t_0\to t}=\sum \ket{E_{a'}}\braket{E_{a'}|\alpha;t_0}\exp\left(\frac{-iE_{a'}t}{\hbar}\right)$$

- 定常状態の時間発展：$\ket{E_{a'};t_0\to t}=\ket{E_{a'};t_0}\exp\left(\frac{-iE_{a'}t}{\hbar}\right)$

        ・時間がたっても変化しない

---

・期待値の時間発展：$\braket{B}_{t}$

- 定常状態の期待値：$\braket{B}_{E_{a'},t}=\braket{B}_{E_{a'}}$

        ・定常状態において、任意の観測可能量の期待値は時間変化しない

- 一般の状態の期待値：
$$\braket{B}_{\alpha,t}=\sum c^*_{a'}c_{a''}\bra{E_{a'}}B\ket{E_{a''}}\exp\left(\frac{-it}{\hbar}(E_{a''}-E_{a'})\right)$$したがって、期待値を構成する各項は $\omega_{a''a'}=(E_{a''}-E_{a'})/\hbar$で振動する

    ・ボーアの振動数条件

---

##### シュレディンガー表示とハイゼンベルグ表示

・ハイゼンベルグ表示：観測可能量に対する演算子が時間変化し、状態ケットは変化しない

- $A^{(H)}(t)=\mathcal{U}^{\dag}(t)A^{(S)}\mathcal{U}(t),\quad \left(\mathcal{U}(t)=\exp\frac{-iHt}{\hbar}\right)$

- $A^{(H)}(0)=A^{(S)}$

・$t$秒後の固有ケット：$\ket{a',t}_H=\mathcal{U}^{\dag}\ket{a'}$

    ・シュレディンガー表示では変化しない
    ・固有値はどちらの表示でも変化しない

- $i\hbar\frac{\partial}{\partial t}\ket{a',t}_H=-H\ket{a',t}_H$

        ・シュレディンガー表示ではそもそも固有ケットを時間微分できない

---

・ハイゼンベルグの運動方程式：$\frac{d A^{(H)}}{d t}=\frac{1}{i\hbar}[A^{(H)},H]$

    ・全微分でいいのか気になるが、解析力学との対応を意識

---

・$t$秒後の期待値：$\braket{A^{H}(t)}_{\alpha}=\braket{A^{S}}_{\alpha,t}$

・$t$秒後の状態のフーリエ係数

---

##### ハミルトニアンと可換な演算子 $AH=HA$

・$A$の固有ケット$\ket{a_A}$は、時間発展しても再び固有ケット

- ハイゼンベルグ表示においては、$$\frac{dA^{H}}{dt}=0$$したがって、ハミルトニアンと可換な演算子は保存料であると言える

---

・対称性：ハミルトニアン $H$ がユニタリ作用素 $U$ に対して $[H,U]=0$ を満たすこと

    ・確率保存

- 系のハミルトニアン $H$ があるユニタリ作用素 $U$ に対して $[H,U]=0$ を満たすとする。
このとき、$\ket{\alpha;t}$がシュレディンガー方程式の解ならば、$U\ket{\alpha;t}$ も解である

        ・対称性の意味