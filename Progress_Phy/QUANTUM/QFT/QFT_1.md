
- [計量とLorentz変換](#計量とlorentz変換)
  - [計量](#計量)
  - [Lorentz変換](#lorentz変換)
    - [P,T,PT変換](#ptpt変換)
  - [反変、共変テンソル](#反変共変テンソル)
    - [相対論的不変性](#相対論的不変性)
    - [簡単なスカラー量](#簡単なスカラー量)
      - [体積要素](#体積要素)
      - [デルタ関数](#デルタ関数)
    - [簡単なベクトル量](#簡単なベクトル量)
      - [エネルギー運動量ベクトル](#エネルギー運動量ベクトル)
      - [時空座標の微分](#時空座標の微分)
    - [$LO(3,1)$ における不変テンソル](#lo31-における不変テンソル)
  - [スカラー関数、ベクトル関数](#スカラー関数ベクトル関数)
- [ガンマ行列](#ガンマ行列)




# 計量とLorentz変換

## 計量

・$x,y\in\bm{R}^4$ に対して、
$$\lang x,y\rang=c^2x_1y_1-x_2y_2-x_3y_3-x_4y_4$$と定めると、これは対称内積。

- $$x^{\mu}=(ct,x,y,z),\quad x_{\mu}=(ct,-x,-y,-z)$$とする。このとき、
$$ds^2=dx_{\mu}dx^{\mu}=dx^{\mu}dx_{\mu}$$

      ・こうやって考えるときは標準内積。定義からC抜き、正負も同じにすればClifford。

- 計量テンソル：
$$g_{\mu\nu}=g^{\mu\nu}=\begin{pmatrix}
1 & 0 & 0 & 0    \\
0 & -1 & 0 & 0    \\
0 & 0 & -1 & 0    \\
0 & 0 & 0 & -1    \\
\end{pmatrix}$$と定めると、
$$ds^2=g_{\mu\nu}dx^{\mu}dx^{\nu}$$

      ・こうやって考えるときは標準内積。dxからC抜き、gの左上にc追加すればClifford。ただしこのとき、逆行列の左上が1/cになる。
      ・どっちも上付きであることに注意。


## Lorentz変換

<dl><dt>

・$\Lambda\in M(4,\bm{R})$、$x^{\mu},a\in\bm{R}^4$ とする。
このとき、変換
$$x'{\mu}=\lambda^{\mu}_{\nu}x^{\mu}+a^{\mu}$$に対して、
$$ds'^2=ds^2\iff \eta_{\rho\lambda}\Lambda^{\rho}_{\mu}\Lambda^{\lambda}_{\nu}=\eta_{\mu\nu}\iff\Lambda^{T}\eta\Lambda=\eta$$このとき、$\Lambda$ をLorentz変換という。

    ・aは任意でよい。


</dt><dd>

- Lorentz変換 $\lambda\in M(4,\bm{R})$ に対して、
$$\Lambda^{-1}=\eta\Lambda^T\eta,$$ であって、$\Lambda^{-1}$ はLorentz変換。
<br>

- Lorentz変換 $\Lambda_1,\Lambda_2\in M(4,\bm{R})$ に対して、
$\Lambda_1\Lambda_2$ はLorentz変換。
<br>

- Lorentz変換 $\lambda\in M(4,\bm{R})$ に対して、
$$(\det\Lambda)^2=1,\quad(\Lambda^0_0)^2\ge1$$したがって、Lorentz変換群 $O(1,3)$ は $4$ つのクラスに分類され、それらは不連続的。

      ・それぞれ時間反転、空間反転を含むかどうかで分けられる。

</dd></dl>

---

### P,T,PT変換

<dl><dt>

・$$P=\eta=\begin{pmatrix}
1 & 0 & 0 & 0    \\
0 & -1 & 0 & 0    \\
0 & 0 & -1 & 0    \\
0 & 0 & 0 & -1    \\
\end{pmatrix},\quad T=-\eta=\begin{pmatrix}
-1 & 0 & 0 & 0    \\
0 & 1 & 0 & 0    \\
0 & 0 & 1 & 0    \\
0 & 0 & 0 & 1    \\
\end{pmatrix},\\\ \\
PT=-E=\begin{pmatrix}
-1 & 0 & 0 & 0    \\
0 & -1 & 0 & 0    \\
0 & 0 & -1 & 0    \\
0 & 0 & 0 & -1    \\
\end{pmatrix}$$ とする。また、単位行列 $E$ とする。
このとき、$E,P,T,PT\in O(3,1)$ であって、すべて異なるクラスに属する。ここで、$E$ が属するクラスを本義Lorentz変換という。

</dt><dd>

- Lorentz変換の $P,T,PT$ 変換は、それぞれ本義Lorentz変換と $P,T,PT$ の積で書ける。

      ・？？？

<br>

- 本義Lorentz変換 $\Lambda\in LO(3,1)$ とする。
このとき、
$$\Lambda^{-1}\in LO(3,1)$$

      ・QFTでは本義Lorentz変換以外のLorentz変換で不変でない事がある！
      ・積でも閉じてるのか？ちょっと証明できない。

- $S\in SO(3)$ とする。
このとき、
$$\begin{pmatrix}
1 & 0 \\
0 & S \\    
\end{pmatrix}\in LO(1,3)\\\ \\$$

- $$\gamma(v)=\frac{1}{\sqrt{1-(v/c)^2}}$$とする。
このとき、
$$\begin{pmatrix}
\gamma(v) & -\gamma(v)\frac{v}{c} & 0 & 0\\
-\gamma(v)\frac{v}{c} & \gamma(v) & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{pmatrix}\in LO(1,3)$$ここで、この形の変換を $x$ 軸方向のローレンツブーストという。また、$y,z$ 軸方向のローレンツブーストでも同じ結果が得られる。

      ・x軸方向の左上部分はSO(2)の要素ではない！

</dd></dl>

---

## 反変、共変テンソル

・$$x^{\mu}=\eta^{\mu\nu}x_{\nu},\quad x_{\mu}=\eta_{\mu\nu} x^{\nu}$$

    ・一般のテンソルでも成り立つ。

- $$T^{\mu\nu}=\eta^{\nu\lambda}T^{\mu}_{\lambda}=\eta^{\mu\rho}\eta^{\nu\lambda}T_{\rho\lambda}$$は定義っぽい。

- 反変ベクトル $A^{\mu}$、共変ベクトル $A_{\mu}$ とする。
このとき、
$$A^{\mu}B_{\mu}=A_{\mu}B^{\mu}$$

---

### 相対論的不変性

・スカラー $A,B$、反変（共変）ベクトル $A^{\mu},B^{\mu}$、二階反変（共変、混合）テンソル $A^{\mu\nu},B^{\mu\nu}$ とする。
このとき、以下の方程式
$$A=B\\\ \\
A^{\mu}=B^{\mu}\\\ \\
A^{\mu\nu}=A^{\mu\nu}$$は（本義）Lorentz変換で不変である。

    ・これがスカラーとか反変ベクトルとかを用いる理由の一つ。


---

### 簡単なスカラー量

#### 体積要素

・時空体積要素 $d^4x$
このとき、本義Lorentz変換 $x'^{\mu}=\Lambda^{\mu}_{\rho}x^{\rho}$ に対して、
$$dx'^{4}=dx^4$$したがって、$dx^4$ はスカラー。

    ・別に本義じゃなくてもよい。
    ・エネルギー運動量体積要素d^4pも同様。

---

#### デルタ関数

・今回は 
$$\int d^4x\ e^{ix_{\mu}p^{\mu}}=(2\pi)^4\delta^4(p)$$とする。
このとき、本義Lorentz変換 $x'^{\mu}=\Lambda^{\mu}_{\rho}x^{\rho},\ p'^{\mu}=\Lambda^{\mu}_{\rho}p^{\rho}$ に対して、
$$\delta^4(p')=\delta^4(p),\quad\delta(x'^4)=\delta(x^4)$$したがって、$\delta^4(x)$ はスカラー。

    ・別に本義じゃなくてもよい。

---

### 簡単なベクトル量

#### エネルギー運動量ベクトル

・エネルギー運動量ベクトル $p^{\mu}$：
$$p^{\mu}=\{E/c,p^x,p^y,p^z\}$$

- $p^2=p^{\mu}p_{\mu}$ とすると、
$$p^{2}=m^2c^2\iff E^2=\bm{p}^2c^2+m^2c^2$$

      ・アインシュタインの関係。

---

#### 時空座標の微分

・
$$\partial_{\mu}=\frac{\partial}{\partial x^{\mu}}=\left(\frac{1}{c}\frac{\partial}{\partial t},\frac{\partial}{\partial x},\frac{\partial}{\partial y},\frac{\partial}{\partial z}\right)\\\ \\
\partial^{\mu}=\frac{\partial}{\partial x_{\mu}}=\left(\frac{1}{c}\frac{\partial}{\partial t},-\frac{\partial}{\partial x},-\frac{\partial}{\partial y},-\frac{\partial}{\partial z}\right)$$と定めると、これらはともに反変、共変ベクトル。
<br>

- $\partial_{\mu}\partial^{\mu}$ はダランベルシャンのこと。これはスカラー。

---

### $LO(3,1)$ における不変テンソル

・$v\in\bm{R}^4$ とする。
このとき、
$$\forall \Lambda\in LO(3,1)\text{ に対して }\Lambda v=v\iff v=0$$したがって、不変ベクトルは $0$ のみである。

    ・実数上で固有ベクトルが存在しないこと。

- 対称行列 $A\in M(4,\bm{R})$ とする。
このとき、
$$\forall \Lambda\in LO(3,1)\text{ に対して }\Lambda A\Lambda^T=A\iff A=\alpha \eta\ (\alpha\in\bm{R})$$したがって、$2$ 階の反変な対称不変テンソルは、$P$ 変換 $\eta$ の定数倍のみである。

      ・対称行列！
      ・？？？

---

・$\eta^{\mu\nu},\eta_{\mu\nu},\delta_{\mu\nu}$ はそれぞれ二階の反変、共変、混合不変テンソル。

---

## スカラー関数、ベクトル関数

・関数 $\phi:\bm{R}^4\to\bm{R}$、$x^{\mu}$、Lorentz変換 $x'^{\mu}=\Lambda^{\mu\nu}x^{\nu}$ とする。
このとき、スカラー関数 $\phi$ の変換性：
$$\phi'(x')=\phi(x)$$

- 反変ベクトル関数、共変ベクトル関数の変換性：
$$A'^{\mu}(x')=\Lambda^{\mu}_{\nu}A^{\nu}(x),\quad A'_{\mu}(x')=(\Lambda^{-1})_{\mu}^{\nu}A_{\nu}(x)$$
したがって、$\partial^{\mu}\phi(x),\partial_{\mu}\phi(x)$ は共に反変、共変ベクトル関数。

---
---
---

# ガンマ行列

    ・有限群の表現論！？

・$\gamma\in M(D,\bm{R})$ とする。
このとき、$D$ 次元ガンマ行列：
$$\gamma^{\mu}\gamma^{\nu}+\gamma^{\mu}\gamma^{\nu}=2\eta^{\mu\nu}I_D\\\ \\
\eta=\begin{pmatrix}
1    \\
& -1 \\
& & -1 \\
& & & \ddots \\
\end{pmatrix}\in M(D,\bm{R})$$

- $\gamma^{i}\to i\gamma^i\quad(i=1,2,...)$ と定義しなおすと、
$$\gamma^{\mu}\gamma^{\nu}+\gamma^{\mu}\gamma^{\nu}=
\delta^{\mu\nu}I_D$$
よって、以降常にこの形で考える。このとき、$(\gamma^{\mu})^2=I_D$
<br>

      ・形式的に言えば、もとのやつとδ_{ij}のやつの間に全単射があるので、これを考えればよい。

<br>

