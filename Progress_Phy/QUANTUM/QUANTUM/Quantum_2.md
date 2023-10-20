- [量子力学](#量子力学)
  - [有用な公式](#有用な公式)
        - [諸々の位置固有ケット、波動関数表示](#諸々の位置固有ケット波動関数表示)
        - [テクニック](#テクニック)
  - [状態と演算子](#状態と演算子)
  - [有用な関係式](#有用な関係式)
  - [位置演算子、運動量演算子](#位置演算子運動量演算子)
        - [位置演算子 $x$](#位置演算子-x)
        - [平行移動演算子と運動量演算子](#平行移動演算子と運動量演算子)
        - [波動関数による表現](#波動関数による表現)
- [系の時間発展](#系の時間発展)
  - [時間発展演算子](#時間発展演算子)
  - [時間依存しないハミルトニアン $H$](#時間依存しないハミルトニアン-h)
        - [エネルギー固有ケット](#エネルギー固有ケット)
        - [シュレディンガー表示とハイゼンベルグ表示](#シュレディンガー表示とハイゼンベルグ表示)
        - [ハミルトニアンと可換な演算子 $AH=HA](#ハミルトニアンと可換な演算子-ahha)
    - [波動関数表示](#波動関数表示)
        - [束縛状態](#束縛状態)
    - [曲線座標での波動関数表示](#曲線座標での波動関数表示)
- [回転演算子と角運動量](#回転演算子と角運動量)
  - [二次までの微小回転](#二次までの微小回転)
        - [微小回転演算子と角運動量](#微小回転演算子と角運動量)


# 量子力学

・ブラケット記法の意味

    ・並進、回転、時間発展は物理的空間全体を変換する→どんな系でも有効！
    ・基本位置空間で考えたいが、運動量空間、スピン空間で考えたり、基底をちょっと変えてみたりしたいことがある→ヒルベルト空間は抽象的で、系の自由度を決めて初めて空間の次元が定まる！
    ・内積で波動関数になるのは、|x>が連続固有値だから！

・波動関数 $\psi(x)$ は位置固有ケット $\ket{x}$ のフーリエ係数

・純粋アンサンブルと混合アンサンブル：純粋なら初めから出てきたものが決まっていて、混合は測定して初めて決定される

    ・両者が同じ結果を与えることもある

---

## 有用な公式

・$$[x_i,F(p)]=i\hbar\frac{\partial F}{\partial p_i},\quad [p_i,G(x)]=-i\hbar\frac{\partial G}{\partial x_i}\\\ \\(F(p),G(x){は解析的})$$

---

##### 諸々の位置固有ケット、波動関数表示

・$\braket{\alpha|\beta}=\int dx'\psi_{\beta}^*(x')\psi_{\alpha}(x')$

・$\bra{\beta}A\ket{\alpha}=\int dx'dx''\psi_{\beta}^*(x')\bra{x'}A\ket{x''}\psi_{\alpha}(x'')$

- 線形演算子$U$に対して、
$U$ はユニタリー$\iff\bra{x'}U^{\dag}U\ket{x''}=\delta(x'-x'')\ (\forall x',x'')$

- 線形演算子 $A,B$ に対して、
$A=B\iff A\ket{x}=B\ket{x}\ (\forall x)$

---

##### テクニック

・古典論との対応で$xp$が出てきたら、$(xp+px)/2$とするべき

---
---
---

## 状態と演算子
$$\bm{\ket{\alpha},\ A}$$

・交換関係
・不確定性関係

    ・時間に依存しないことに注意

・演算子の次元が合わないやつはテンソルで表現する？固有値がうまくいきそう

## 有用な関係式 

---

## 位置演算子、運動量演算子

##### 位置演算子 $x$

・$[x_i,x_j]=0$

---

##### 平行移動演算子と運動量演算子
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

##### 波動関数による表現
$$\bm{\psi(x)}$$



---
---
---

# 系の時間発展

## 時間発展演算子 
$$\bm{\mathcal{U}(t_0+dt,t_0)=1-\frac{iH}{\hbar}dt}$$

・微小時間発展：$\mathcal{U}(t_0+dt,t_0)\ket{\alpha;t_0}=\ket{\alpha;t_0+dt}$

- $[\mathcal{U}(t,t_0)]^{\dag}\mathcal{U}(t,t_0)=1$
- $\mathcal{U}(t_2,t_1)\mathcal{U}(t_1,t_0)=\mathcal{U}(t_2,t_0)\quad(t_2>t_1>t_0)$
- $\lim_{dt\to0}\mathcal{U}(t_0+dt,t_0)=1$

        ・これらは定義
        ・t_0+dtにおいて、これらがすべて満たされていることが分かる

---

・時間発展演算子に対するシュレディンガー方程式：
$$i\hbar\frac{\partial}{\partial t}\mathcal{U}(t,t_0)=H\mathcal{U}(t,t_0)$$

- $i\hbar\frac{\partial}{\partial t}\ket{\alpha;t_0\to t}=H\ket{\alpha;t_0\to t}$

---

・時間発展演算子に対するシュレディンガー方程式の形式解

- $H$が時間依存しないとき：
$$\mathcal{U}(t,t_0)=\exp\left(\frac{-iH(t-t_0)}{\hbar}\right)$$

- $[H(t'),H(t)]=0\ (\forall t,t')$のとき：
$$\mathcal{U}(t,t_0)=\exp\left(\frac{-i}{\hbar}\int_{t_0}^{t}H(t')dt'\right)$$

        ・偏微分すると[H(t),∫H(t')dt']みたいなのがでてくる

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

##### ハミルトニアンと可換な演算子 $AH=HA
$

・$A$の固有ケット$\ket{a_A}$は、時間発展しても再び固有ケット

- ハイゼンベルグ表示においては、$$\frac{dA^{H}}{dt}=0$$したがって、ハミルトニアンと可換な演算子は保存料であると言える

---

・対称性：ハミルトニアン $H$ がユニタリ作用素 $U$ に対して $[H,U]=0$ を満たすこと

    ・確率保存

- 系のハミルトニアン $H$ があるユニタリ作用素 $U$ に対して $[H,U]=0$ を満たすとする。
このとき、$\ket{\alpha;t}$がシュレディンガー方程式の解ならば、$U\ket{\alpha;t}$ も解である

        ・対称性の意味

---
---
---


### 波動関数表示

    ・すべてL^2(X)の元、すなわち有限値しかとらないし、積分も有限

・解くべき方程式
$$\left(-\frac{\hbar^2}{2m}\Delta+V(x)\right)\phi(x)=E\phi(x)\\\ \\
\psi(x,t)=\phi(x)e^{-i\frac{E}{\hbar}t}$$

→フラックス

→確率密度が時間変化しないこと

    ・定常状態

##### 束縛状態

→$\lim_{|x|\to\infty}|\phi(x)|=0$

---

・$V(r)\le V_0$ならば、$E>V_0$

→$\nabla\phi(r)\neq0$

    ・発散しない

→$\braket{E}=E,\ \braket{T}>0,\ \braket{V}\ge V_0$

---

・このとき、取りうる$E$の値は離散的

    ・偏微分方程式論による

### 曲線座標での波動関数表示

---
---
---

# 回転演算子と角運動量

## 二次までの微小回転
$$\bm{R(\epsilon_0),R(\epsilon)}$$

→ 任意の軸周りの一次の微小回転行列$R(\epsilon_0)$は交換する
→ 任意の軸周りの回転行列$R(\theta)$に対して、$R(0)=I$
→ $$R_z(\epsilon)= \
\begin{pmatrix} \
1-\frac{\epsilon^2}{2} & -\epsilon & 0 \\   \
\epsilon &  1-\frac{\epsilon^2}{2} & 0 \\   \
 0 & 0 & 1   \
\end{pmatrix},\quad R_x(\epsilon)\
\begin{pmatrix} \
1 & 0 & 0 \\   \
0 &  1-\frac{\epsilon^2}{2} & -\epsilon \\   \
 0 & \epsilon & 1-\frac{\epsilon^2}{2}   \
\end{pmatrix},\quad R_y(\epsilon)\\
\begin{pmatrix} \
1-\frac{\epsilon^2}{2} & 0 & \epsilon \\   \
0 &  1 & 0 \\   \
 -\epsilon & 0 &  1-\frac{\epsilon^2}{2}  \
\end{pmatrix},\quad \\$$
→ $[R_x(\epsilon),R_y(\epsilon)]=R_z(\epsilon^2)-R(0)$

---

##### 微小回転演算子と角運動量
$$\mathcal{D}(n,d\phi)=1-i\left(\frac{J\cdot n}{\hbar}\right)d\phi$$

    ・x×pと定義するわけではない！後で特別な場合に一致するのを見る

・$D_n(\phi)=\exp(\frac{-iJ\cdot n\phi}{\hbar})$
→ $D_{n_1}(\phi_1)D_{n_2}(\phi_2)=D_{n_3}(\phi_3)$
→ $(D_{n_1}(\phi_1)D_{n_2}(\phi_2))D_{n_3}(\phi_3)=D_{n_1}(\phi_1)(D_{n_2}(\phi_2)D_{n_3}(\phi_3))$
→ $D_{x_i}(d\phi_1)D_{x_j}(d\phi_2)=\epsilon_{ijk}(D_{x_k}(d^2\phi_3)-1)$

---

・正準交換関係：$[J_i,J_j]=\epsilon_{ijk}i\hbar J_kS$


---


