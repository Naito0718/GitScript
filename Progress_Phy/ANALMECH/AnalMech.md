# 解析力学

## ベクトル場と座標変換

    ・時間軸も加えた4次元ベクトルを考えるとよい

・ガリレイ変換

・空間反転

・時間反転 $t'=t_0-t,\quad t'=t_1-t$

    ・原点を一致させるか、経路の逆走か

## ラグランジュ形式

・

### 剛体

## ハミルトン形式
$H(q,p,t)=p_i\dot{q}_i-L(q,\dot{q},t)$

    ・ルジャンドル変換のこと、基本ラグランジアンは凸なので問題ない

→ハミルトンの運動方程式：
$$\frac{\partial H}{\partial p_i}=\dot{q}_i,\quad\frac{\partial H}{\partial q_i}=-\dot{p}_i$$

    ・ハミルトニアンが陽に時間依存しないなら、その時間微分は常に消える（エネルギー）

→ 
ハミルトンの運動方程式$\iff$作用$S[q,p]=\int_{t_0}^{t_1}p_i\dot{q}_i-H(q,p,t)\quad(q(t_0)=q_0,q(t_1)=q_1)$ の停留条件

→$$\frac{d}{dt}H=\frac{\partial H}{\partial t}=\frac{\partial L}{\partial t}$$

##### 相空間 $(q,p)$

・相空間軌跡：$\gamma(t)=(q(t),p(t))$

→軌跡の接ベクトル：$\frac{d}{dt}\gamma(t)=(\frac{\partial H}{\partial p},-\frac{\partial H}{\partial q})$


→陽に時間によらないハミルトニアン $H(q,p)$に対して、相空間軌跡は異なる接ベクトルをもつ軌跡を描かない

---


・母関数

・量子力学、幾何光学、解析力学の対応

## 正準変換 $Q_i,P_i$

##### Poisson括弧 $\{f,g\}$

・双線形、交代性
・$\{f,a\}=0$
・$\{fg,h\}=f\{g,h\}+\{f,g\}h$

・$\frac{d}{dt}f(q(t),p(t),t)=\{f,H\}+\frac{\partial f}{\partial t}$
・$\{q_i,f\}=\frac{\partial f}{\partial p_i},\ \{p_i,f\}=-\frac{\partial f}{\partial q_i}$
・$\{q_i,p_j\}=\delta_{ij},\ \{q_i,q_j\}=\{p_i,p_j\}=0$

・$\{f,g\}_{q,p}=\{f,g\}_{Q,P}$
・$\{Q_i,P_j\}_{q,p}=0,\ \{Q_i,Q_j\}_{q,p}=\{P_i,P_j\}_{q,p}=0$

---

##### Lagrange括弧 $\braket{f,g}$

---

##### 正準交換関係

・
$$[q_i,q_j]=[p_i,p_j]=0\\\ \\
[q_i,p_j]=\delta_{ij}$$

・三次元において、
$$[L_i,L_j]=\epsilon_{ijk}L_k\\\ \\
[x_i,L_j]=\epsilon_{ijk}x_k,\quad[p_i,L_j]=\epsilon_{ijk}p_k$$


---




