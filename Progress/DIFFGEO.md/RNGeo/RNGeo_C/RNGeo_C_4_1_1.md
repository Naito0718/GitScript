
- [$R^3$ 正則曲線と弧長パラメータ表示](#r3-正則曲線と弧長パラメータ表示)
  - [曲率 $κ$ と捩率 $τ$](#曲率-κ-と捩率-τ)
    - [曲線論の基本定理](#曲線論の基本定理)
    - [曲率半径](#曲率半径)



# $R^3$ 正則曲線と弧長パラメータ表示

    ・単射、C^∞、一階導関数が0でないなら、(φ(U),φ^{-1})は1次元局所座標（とみなしてよい。）
    ・正則曲線は、正則でないパラメータ表示も可能。

<dl><dt>

・正則曲線 $\bm{p}:(a,b)\to\bm{R}^3$、$t_0\in(a,b)$ とする。
このとき、
$$s_{t_0}:I\to(0,\infty)\\\ \\
s_{t_0}(t)=\int_{t_0}^t|\dot{\bm{p}}(t)|dm\\\ \\
\psi_{t_0}:(s_{t_0}(a),s_{(t_0)}(b))\to\bm{R}^3\\\ \\
\psi_{t_0}(l)=(\bm{p}\circ s_{t_0}^{-1})(l)$$
と定めると、$s_{t_0}$ は $C^{\infty}$ 狭義単調増加関数、特に微分同相写像であって、$\psi_{t_0}$ は
$$|\dot{\psi}(l)|=1$$
を満たすwell-definedな正則曲線。したがって、任意の正則曲線は、$|\dot{\bm{p}}|=1$ を満たす別の正則曲線表示を持つ。
ここで、$|\dot{\bm{p}}|=1$ を満たす正則曲線表示を弧長パラメータ表示といい、$e_1(s)=\dot{\bm{p}}(s)$ と書く。
<br>

</dt><dd>

- 正則弧長パラメータ曲線 $\bm{p}:(a,b)\to\bm{R}^3$ とする。
このとき、
$$\forall s\in(a,b)\text{ に対して、}|e_1(s)|=1,\quad\dot{e_1}(s)\cdot e_1(s)=0$$


</dd></dl>

---

## 曲率 $κ$ と捩率 $τ$

<dl><dt>

・正則弧長パラメータ曲線 $\bm{p}:(a,b)\to\bm{R}^3$ とする。
このとき、曲率 $\kappa$：
$$\kappa:(a,b)\to[0,\infty)\\\ \\
\kappa(s)=|\dot{e_1}(s)|,\quad e_1(s)=\dot{\bm{p}}(s)$$
さらに、$\forall s\in(a,b)$ で $\kappa(s)>0$ の時、捩率 $\tau$：
$$\tau:(a,b)\to\bm{R}\\\ \\
\tau(s)=\dot{e}_2(s)\cdot e_3(s),\quad e_3(s)=e_1(s)\times e_2(s),\quad e_2(s)=\frac{1}{\kappa(s)}\dot{e_1}(s)\\\ \\$$
明らかに、$$\forall s\in(a,b)\text{ に対して }\kappa(s)>0\\\ \\
\Rightarrow\forall s\in(a,b)\text{ に対して、}(e_1(s),e_2(s),e_3(s))\text{ が正規直交基底かつ、}\kappa\text{ が }C^{\infty}\text{ 写像} \\\ \\$$
明らかに、$\tau$ が定義されれば $C^{\infty}$ である。ここで、この正規直交基底をFrenet標構といい、$e_2$ を主法線、$e_3$ を従法線という。
<br>

</dt><dd>

- 曲率 $\kappa>0$ の正則弧長パラメータ曲線 $p:(a,b)\to\bm{R}^3$ とする。
このとき、
$$\forall s\in(a,b)\text{ に対して、}\\\ \\
(\dot{e_1}(s),\dot{e_2}(s),\dot{e_3}(s))=(e_1(s),e_2(s),e_3(s))\begin{pmatrix}
0 & -\kappa(s) & 0 \\
\kappa(s) & 0 & -\tau(s) \\
0 & \tau(s) & 0  \\
\end{pmatrix}$$
ここで、
$$\bm{b}:(a,b)\to\bm{R}^3,\quad\bm{b}(s)=(\tau(s),0,\kappa(s))\text{ とおくと、}\\\ \\
\widetilde{b(s)}=\begin{pmatrix}
0 & -\kappa(s) & 0 \\
\kappa(s) & 0 & -\tau(s) \\
0 & \tau(s) & 0  \\
\end{pmatrix}\\\ \\$$

      ・直線は常に曲率0


</dd></dl>

---

### 曲線論の基本定理

・$C^{\infty}$ 写像 $\kappa:(a,b)\to(0,\infty)$、$C^{\infty}$ 写像 $\tau:(a,b)\to\bm{R}$ とする。
このとき、
$$\exist\kappa_p>0\text{ の正則弧長パラメータ曲線 }p:(a,b)\to\bm{R}^3\text{ であって、}\forall s\in(a,b)\text{ に対して、}\\\ \\
\kappa_p(s)=\kappa(s),\quad\tau_p(s)=\tau\\\ \\$$ 

- $C^{\infty}$ 写像 $\kappa:(a,b)\to(0,\infty)$、$C^{\infty}$ 写像 $\tau:(a,b)\to\bm{R}$ とする。
このとき、
$$\forall\text{ 曲率 }\kappa>0,\ \text{ 捩率 }\tau\text{ の正則弧長パラメータ曲線 }p_1,p_2:(a,b)\to\bm{R}^3\text{ に対して、}\exist A\in SO(3),\ \exist b\in \bm{R}^3\text{ であって、}\\\ \\
\forall s\in(a,b)\text{ に対して、}p_1(s)=Ap_2(s)+b\\\ \\$$

      ・適当な点s_0において、p_1(s_0)=p_2(s_0)（平行移動）、(e_1(s_0),...,e_3(s_0))=(e_1'(s_0),...,e_3'(s_0))（回転）で一致させれば全部一致する。

---

### 曲率半径

・

---


