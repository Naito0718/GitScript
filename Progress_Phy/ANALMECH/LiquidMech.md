# 流体力学

## 流体の性質

    ・流体の運動は、すべての点における速度u、圧力p、密度ρ、温度T、その他の熱力学関数を、時間の関数として与えることで完全に決定される

---

##### 流体の記述

・Lagrange記述 $\frac{D}{Dt}$

    ・流体を微小部分に分けて（流体粒子）、それぞれの運動を追跡する
    ・流体粒子は、時刻が変化しても、大きさや形は変わるがやはり一つの流体粒子

→時刻$t$における位置座標$x$、速度$u$：
$$x=x(x_0,t),\quad u=\frac{\partial}{\partial t}x(x_0,t)\\\ \\
x_0=x(x_0,0)$$

    ・初期位置と時間の関数
    ・初期位置$x_0$は広がっていることに注意
    ・関数x(x_0,t)を決めれば流体のすべての場所の運動は決まる

---

・Euler記述 $\frac{d}{dt}$

    ・∂A/∂tは流体粒子の時間変化ではなく、空間内の一点における時間変化を表す（一点における水の流れ）

→時刻$t$における速度$u$：
$$u=u(x,t)$$

    ・初期位置と時間の関数
    ・初期位置$x_0$は広がっていることに注意
    ・関数x(x_0,t)を決めれば流体のすべての場所の運動は決まる

・Euler記述とLagrange記述の関係：
$$\frac{D}{Dt}A(x_0,t)=\left\{\frac{\partial }{\partial t}+(u\cdot\mathrm{grad})\right\}A(x,t)$$

→変形：$$\frac{D}{Dt}A=\frac{\partial A}{\partial t}+\frac{1}{2}\{\mathrm{grad}(u\cdot A)+\mathrm{rot}u\times A \\\ \\
+\mathrm{rot}A\times u-\mathrm{rot}(u\times A)+u\mathrm{div}A-A\mathrm{div}\ u\}$$

    ・曲線座標への書き換えで使う

→加速度：$$a=\frac{D}{Dt}u=\frac{\partial u}{\partial t}+(u\cdot \mathrm{grad})u\\\ \\
=\frac{\partial u}{\partial t}+\frac{1}{2}\mathrm{grad}(|u|^2)-u\times\mathrm{rot}\ u$$

---

##### 流線と流管、流跡線、流脈線

・流線 $c(s,t)$

    ・各点の接ベクトル=uとなるような曲線
    ・多様体論における積分曲線

→ベクトル場が与えられた空間を積分曲線で満たすことができる❓
→もし流線が交わる点が得られたら、その点は流れの外にあることになる❓
→よどみ点$u=0$では複数の流線が交わる❓

---

・流管 $S''(t)$

    ・閉曲線Sに対して、その線上の各点を通る流線によって作られる曲面、適当な閉曲線S'で打ち切る

→流管$S''$上で、$n\cdot u=0$

---

・流跡線 $d(t)$：流体粒子の軌跡

    ・普通にパラメータがtの曲線、d/dt d(t)=u(x,t),d(0)=x_0

---

・流脈線

    ・固定点x_0を時刻tまでに通過したすべての流体粒子がtまでに描いた軌跡全体

→それぞれの状態は、一気に粉末をばらまいて短い動画を撮る、一点に粉を落として長時間動画を撮る、一点に粉末を落とし続けて動画を撮る、として実現できる


---


#### 流体の局所的な記述

##### ひずみ速度

・$\delta u$の対称部分 
$$e_{ij}=\frac{1}{2}\left(\frac{\partial u_i}{\partial x_j}+\frac{\partial u_i}{\partial x_j}\right)$$

→伸縮ひずみ速度

→ずれひずみ速度

→体積ひずみ速度：$\frac{1}{\delta V}\frac{D \delta V}{Dt}=\mathrm{tr}\ e=\mathrm{div}u$

・座標変換に対して

    ・任意のひずみ速度は主軸系における伸縮ひずみ速度のみで表現できる

→任意の座標系において、$\mathrm{div}\ u=\mathrm{tr}\  e,\ \det e$は不変



---

##### 渦度 $\omega$

・渦度 $\omega=\mathrm{rot}\  u=(\delta u{の反対称部分}\times 2)$

---

・渦線

---

・循環

---

・渦管

---

##### 応力と応力テンソル

・ある体積$V$に働く体積力：$F=\int_V\rho KdV$

    ・Kは重力とか

・応力 $p(n)$

    ・向き：面の法ベクトルと逆向き

→面積力：$F=\int_Sp(n)dS$

---

・応力テンソル $P_{ij}=p_i(e_j)$

    ・対角成分が法線応力、非対角成分が接線応力

→応力$p(n)$との関係：$p(n)=Pn$ 

→$P$は対称テンソル：$P_{ij}=P_{ji}$

→座標変換$x'=Ax$に対して、応力テンソルは$$と変換される

    ・任意の応力は主軸系における法線応力のみで表現できる

→任意の座標系において、$\mathrm{tr} P,\ \det P$は不変


---

#### 基礎方程式

・連続方程式
$$\frac{\partial \rho}{\partial t}+\mathrm{div}(\rho u)=0$$

    ・任意の流体で成り立つ
    ・質量保存則による

→ラグランジュ記述： $\frac{D\rho}{Dt}+\rho\ \mathrm{div}u=0$
または： $\frac{D}{Dt}(\rho\ \delta V)=0$

    ・最後の式は確かに質量保存則

---

・運動方程式
$$\frac{\partial}{\partial t}(\rho u_i)=\frac{\partial}{\partial x_j}(P_{ij}-\rho u_iu_j)+\rho K$$

    ・運動方程式による
    ・まとめて書けなさそう？

→ラグランジュ記述： $\frac{Du_i}{Dt}=\frac{1}{\rho}\frac{\partial P_{ij}}{\partial x_j}+K_i$
または： $\frac{D}{Dt}(\rho u_i\ \delta V)=\frac{\partial P_{ij}}{\partial x_j}\delta V+\rho K_i\delta V$

    ・最後の式は確かに運動方程式（Pは無視）

---

・エネルギー方程式
$$\frac{\partial}{\partial t}\left\{\rho\left(\frac{1}{2}|u|^2+U\right)\right\}\\\ \\
=\frac{\partial}{\partial x_i}\left\{p_{ij}u_j-\rho\left(\frac{1}{2}|u|^2+U\right)u_i-\theta_i\right\}+\rho Ku_i$$

    ・熱量θ、Uは単位質量当たり
    ・単一相だけを考える：相変化、化学反応、解離、電離などは考えない
    ・放射によるエネルギー伝達は考えない
    ・流体は電気的に不導体であるとする：電磁場との相互作用は考えない

→ラグランジュ記述：
$$\frac{D}{Dt}\left(\frac{1}{2}|u|^2+U\right)\\\ \\
=\frac{1}{\rho}\frac{\partial}{\partial x_i}(p_{ij}u_j-\theta_i)+K_iu_i$$

→運動エネルギーについて（単位質量）：
$$\frac{D}{Dt}\left(\frac{1}{2}|u|^2\right)=\frac{1}{\rho}\frac{\partial p_{ij}}{\partial x_i}u_j+K_iu_i$$

→内部エネルギーについて（単位質量）：
$$\frac{D}{Dt}U=\frac{p_{ij}}{\rho}\frac{\partial u_j}{\partial x_i}-\frac{1}{\rho}\frac{\partial}{\partial x_i}\theta_i$$
または：
$$\frac{D}{Dt}(\rho\ U\delta V)=p_{ij}\frac{\partial u_j}{\partial x_i}\delta V-\frac{\partial}{\partial x_i}\theta_i\delta V$$

    ・最後の式は熱力学第一法則のこと


#### 流体の特性

・密度の定義：$\frac{dm}{dV}$ではない

    ・マクロ特有の量

---

・単相流と多相流

    ・単相流：一つの相だけ考える系
    ・多相流：気体、液体、固体をすべて考える系

---

・弾性

    ・レオロジー

---

・熱伝導性

---

・熱膨張性

---

・電気伝導性

---

#### 流体力学における熱力学

・物質量$N$と質量$m$と密度$\rho$

    ・そもそもmは流体力学では現れない（非圧縮では別？）

→すべて単位質量当たりで考えることになるが、このとき熱力学で言ってたことはすべて同様に成り立つ

    ・圧力が問題なくなる代わりに、化学ポテンシャルがよく分からんくなる

→基本的に科学ポテンシャルは無視するし、自然変数は$2$つだけだとして考えるし、相転移も考えない

---

・熱平衡状態

→流体が静止しているときは、外部境界の温度が一定ならば熱平衡にあるとしてよい

    ・熱以外やり取りできない壁ならば、熱力学より従う

→流体が運動しているときは、温度$T$と圧力$p$を気にすればよい
温度一様な粘性流体ならば、熱平衡の時の関係式をそのまま使ってよい。
温度変化が小さい圧力が熱平衡と同じ系ならば、熱平衡の時の関係式をそのまま使ってよい。


---

・
$d'Q=dU+pd(\frac{1}{\rho})$
$dU=TdS-pd(\frac{1}{\rho})$

---

・状態方程式：$f(p,T,\rho)=0$

    ・まあ物質量の代わり？

---

・比熱 $c$


---

## 定常流：すべての物理量が時間変化しない

・流線 $c(s)$、流管 $S''$

    ・空間に固定された曲線群、曲面になる

→流管$S''$に対する不変量：$\int_S\rho u\cdot ndS$

    ・流管を一つ定めた時、これは断面によらない
    ・質量保存則による

→流線$c(s)$は流跡線$d(t)$、流脈線と一致する

---
## 非圧縮性流体

    ・圧縮率、熱膨張率0

・密度が運動で一定：$\frac{D}{Dt}\rho=0$

    ・空間で一定というわけではない

→質量保存則 $\mathrm{div}\ u=0$
→空間内のある時間$t$の流管$S''$に対する流量 $Q(t)=\int_{S(t)}(u\cdot n)dS$

---

##### 定常流

・流線$c(s)$と流管$S''$

→流管$S''$に対する流量$Q=\int_Su\cdot ndS$

    ・流管を一つ定めた時、これは流管の断面によらない

→流管の強さ：$Q=uS=const$

    ・断面において$u$が一定とみなせるほど断面を小さくとる
    ・このとき、速度が大きいほど流感の断面積が小さくなる
    ・空間はこの流管の集合からなるとみなされる



##### 圧縮率
$$\frac{1}{\rho}\frac{\partial\rho}{\partial p}$$

    ・外的条件の取り方により異なる（等温、断熱）
    
・非圧縮性との境界

    ・音速を超えると圧縮性流体になる

---

## 完全流体

---

## 圧縮性流体


---

## 粘性流体

    ・速い粘性流体は境界層とウエーク以外は完全流体と一致する

・解くべき方程式：
$$\frac{\partial \rho}{\partial t}+\mathrm{div}(\rho u)=0\\\ \\
\frac{Du_i}{Dt}-\frac{1}{\rho}\frac{\partial p}{\partial x_i}+\frac{\partial}{\partial x_i}(\chi\mathrm{div}u)+\frac{1}{\rho}\frac{\partial}{\partial x_i}\left\{\mu\left(\frac{\partial u_i}{\partial x_j}+\frac{\partial u_j}{\partial x_i}-\frac{2}{3}\mathrm{div}\ u\ \delta_{ij}\right)\right\}+K_i$$

→一般に体積粘性率$\chi$、粘性率$\mu$を外に出して、以下のnavier-stokes方程式を解く：
$$\frac{Du}{Dt}=-\frac{1}{\rho}\mathrm{grad}\ p+\frac{1}{\rho}\left(\chi+\frac{\mu}{3}\right)\mathrm{grad\ div}u+\frac{\mu}{\rho}\Delta u+K$$

    ・温度T、圧力pの辺か範囲が小さいとき



### 粘性かつ非圧縮

・解くべき方程式：
$$\frac{\partial \rho}{\partial t}+\mathrm{div}(\rho u)=0\\\ \\
\frac{\partial u}{\partial t}+(u\cdot\mathrm{grad})u=-\frac{1}{\rho}\mathrm{grad}\ p+\nu\Delta u+K$$

    ・運動体積率ν=μ/ρ
    ・順に、非定常項、移流項、圧力項、粘性項、外力項




---

## 乱流

