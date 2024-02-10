
- [微小回転演算子と角運動量](#微小回転演算子と角運動量)
  - [角運動量の性質](#角運動量の性質)
  - [全角運動量とはしご演算子](#全角運動量とはしご演算子)
    - [同次固有ケット](#同次固有ケット)
      - [角運動量の固有ケットの性質のまとめ](#角運動量の固有ケットの性質のまとめ)
- [スピン角運動量を無視できるとき](#スピン角運動量を無視できるとき)
  - [波動関数表示の直接的な計算](#波動関数表示の直接的な計算)
    - [固有状態における波動関数 $Y](#固有状態における波動関数-y)





# 微小回転演算子と角運動量


<dl><dt>

・単位ベクトル $\bm{n}$ 方向まわりの微小回転演算子 $\mathcal{D}(\hat{\bm{n}},d\phi)$ とする。
このとき、角運動量演算子 $J$：
$$\mathcal{D}(\hat{\bm{n}},d\phi)=1-i\left(\frac{J\cdot \hat{\bm{n}}}{\hbar}\right)d\phi\\\ \\$$

- 回転演算子 $\mathcal{D}(R)$ 全体の集合に対して、合成に関して群をなすことを要請する。
ただし、
$$I_{\mathcal{D}}=\mathcal{D}(I),\quad\mathcal{D}(R)^{-1}=\mathcal{D}(R^{-1})\\\ \\
$$

</dt><dd>

- $\bm{n}$ 方向に $\phi$ 回転させる演算子 $\mathcal{D}(\hat{\bm{n}},\phi)$ とする。
このとき、$$\mathcal{D}(\hat{\bm{n}},\phi)=\exp\left(\frac{-iJ\cdot \hat{\bm{n}}\phi}{\hbar}\right)$$

- $$\mathcal{D}(\hat{x}_i,d\phi_1)\mathcal{D}(\hat{x}_j,d\phi_2)=\epsilon_{ijk}(\mathcal{D}(\hat{x}_k,(d\phi_3)^2)-\mathcal{D}(I))$$


</dd></dl>

---

## 角運動量の性質

・$$[J_i,J_j]=\epsilon_{ijk}i\hbar J_k$$


---

## 全角運動量とはしご演算子

<dl><dt>

・$$\bm{J}^2=J_x^2+J_y^2+J_z^2\\\ \\
J_+=J_x+iJ_y,\quad J_-=J_+^{\dag}=J_x-iJ_y$$
と定めると、$\bm{J}^2$ は物理量であって、$J_{\pm}$ は物理量でない。ここで、$\bm{J}^2$ を全角運動量、$J_{\pm}$ をはしご演算子という。

<br>

</dt><dd>

- $$\forall k=1,2,3\text{ に対して、}[\bm{J}^2,J_k]=0$$
ここで、同時に対角化できるような $J_k$ として、慣習として $J_z$ を選ぶ。
<br>

- $$[J_+,J_-]=2\hbar J_z,\quad [J_z,J_{\pm}]=\pm \hbar J_{\pm}\\\ \\
[\bm{J}^2,J_{\pm}]=0\\\ \\$$

- $$\bm{J}^2-J_z^2=\frac{1}{2}(J_+J_-+J_-J_+)\\\ \\
J_{-}J_+=\bm{J}^2-J_z^2-\hbar J_z\quad J_{+}J_-=\bm{J}^2-J_z^2+\hbar J_z$$

</dd></dl>

---

### 同次固有ケット

<dl><dt>

・$\bm{J}^2$ と $J_z$ の同次固有ケット $\ket{a,b}$ とする。ただし、$\bm{J}^2\ket{a,b}=a\ket{a,b},\quad J_z\ket{a,b}=b\ket{a,b}$ とする。
<br>

    ・観測可能量J_zと物理量J^2。
<br>

</dt><dd>

- $$J_z(J_{\pm}\ket{a,b})=(b\pm\hbar)(J_{\pm}\ket{a,b}),\quad\bm{J}^2(J_{\pm}\ket{a,b})=a(J_{\pm}\ket{a,b})$$
したがって、$J_{\pm}^n\ket{a,b}$ は同次固有ケットであって、$\bm{J}^2$ の固有値 $a$、$J_z$ の固有値 $b\pm n\hbar$ である。
<br>

- $$|J_{\pm}\ket{a,b}|^2=a^2-b^2\mp\hbar b\\\ \\$$

- $$a\ge b^2$$
したがって、
$$\forall J^2\text{ の固有値 }a\text{ に対して、}\exist \bm{J}_z\text{ の固有値 }b_M,b_m\text{ であって、}\\\ \\
J_+\ket{a,b_M}=0,\ J_-\ket{a,b_m}=0,\ b_m\le b_M$$
このとき、上記の $|J_{\pm}\ket{a,b}|$ の式より、
$$(b_M+b_m)(b_M-b_m+\hbar)=0$$
が出るので、$b_M=-b_m,\quad b_m\le 0\le b_M$

<br>

- $b\neq B$ なる固有ケット $\ket{a,b},\ket{a,B}$ とする。
このとき、
$$\text{ある }n_b,n_B\in\bm{N}\text{ がただ一つ存在して、}\\\ \\
b_M=b+n_b\hbar,\quad B_M=B+n_B\hbar,\quad(B_M-b_M)(B_M+b_M+\hbar)=0$$
したがって、$B_M=b_M$、すなわち $B-b$ は $\hbar$ の整数倍で書ける。

</dd></dl>

---

#### 角運動量の固有ケットの性質のまとめ

<dl><dt>

・$\bm{J}^2$ と $J_z$ の同次固有ケット $\ket{a,b}$ とする。ただし、$\bm{J}^2\ket{a,b}=a\ket{a,b},\quad J_z\ket{a,b}=b\ket{a,b}$ とする。
このとき、
$$\exist n_0\in\bm{N}\text{ であって、}b=\frac{\hbar }{2}n_0,\ \frac{\hbar}{2}n_0-\hbar,\ ...,\ -\frac{\hbar}{2}n_0+\hbar,\ -\frac{\hbar}{2}n_0\quad(n_0+1\text{ 個})\\\ \\
a=\hbar^2\frac{n_0}{2}\left(\frac{n_0}{2}+1\right)$$
ここで、$$j=\frac{n_0}{2},\ m=\frac{b}{\hbar}$$ とおくと、
$$a=\hbar^2j(j+1)\\\ \\
m=j,\ j-1,\ ...,\ -j+1,\ -j\quad(2j+1\text{ 個})\\\ \\$$
<br>

</dt><dd>

- $$\bra{j',m'}\bm{J}^2\ket{j,m}=j(j+1)\hbar^2\delta_{j'j}\delta_{mm'}\\\ \\$$

- $$\bra{j',m'}J_z\ket{j,m}=m\hbar\delta_{j'j}\delta_{mm'}\\\ \\$$

- $$J_+\ket{j,m}=\sqrt{(j-m)(j+m+1)}\hbar\ket{j,m+1}\\\ \\$$

- $$J_-\ket{j,m}=\sqrt{(j+m)(j-m+1)}\hbar\ket{j,m-1}\\\ \\$$

</dd></dl>

---

# スピン角運動量を無視できるとき

    ・さっきの半整数のjがlになる。
<br>+

<dl><dt>

・$\hat{L}=\hat{x}\times\hat{p}$ と定める。
<br>

</dt><dd>

- $$[L_i,L_j]=i\hbar\epsilon_{ijk}L_k\\\ \\$$

- $$[L_i,\hat{p}_j]=\epsilon_{ijk}i\hbar\hat{p}_k,\quad[L_i,\hat{x}_j]=\epsilon_{ijk}i\hbar\hat{x}_k\\\ \\
[L_i,\hat{\bm{p}}^2]=0,\quad[L_i,\hat{\bm{x}}^2]=0\\\ \\
[\bm{L}^2,\hat{x}_i]=0,\quad[\bm{L}^2,\hat{p}_i]=0$$


</dd></dl>

---

## 波動関数表示の直接的な計算

・$$\hat{L}\cdot\hat{L}=(\hat{x}\cdot\hat{x})(\hat{p}\cdot\hat{p})-(\hat{x}\cdot\hat{p})(\hat{x}\cdot\hat{p})+i\hbar\hat{x}\cdot\hat{p}\\\ \\$$

- $$\bra{\bm{x}'}\hat{x}\cdot\hat{p}\ket{\alpha}=-i\hbar\bm{x}'\cdot\nabla'\braket{\bm{x}'|\alpha}\\\ \\
=-i\hbar r'\frac{\partial}{\partial r'}\braket{\bm{x}'|\alpha}\\\ \\
\bra{\bm{x}'}(\hat{x}\cdot\hat{p})(\hat{x}\cdot\hat{p})\ket{\alpha}=-\hbar^2\left(r'^2\frac{\partial^2}{\partial r'^2}+r'\frac{\partial}{\partial r'}\right)\braket{\bm{x}'|\alpha}\\\ \\$$

- $$\bra{\bm{x}'}\hat{L}\cdot\hat{L}\ket{\alpha}=-\hbar^2r'^2\nabla'^2\braket{\bm{x}'|\alpha}+\hbar^2\left(r'^2\frac{\partial^2}{\partial r'^2}+2r'\frac{\partial}{\partial r'}\right)\braket{\bm{x}'|\alpha}$$
したがって、
$$\nabla'^2\braket{\bm{x}'|\alpha}=\left(\frac{\partial^2}{\partial r'^2}+\frac{2}{r'}\frac{\partial}{\partial r'}\right)\braket{\bm{x}'|\alpha}-\frac{1}{\hbar^2r'^2}\bra{\bm{x'}}\hat{L}\cdot\hat{L}\ket{\alpha}$$
より、$\bra{\bm{x'}}\hat{L}\cdot\hat{L}\ket{\alpha}$ は球座標あるいは円柱座標のラプラシアンの角度成分を用いて与えられることが分かる。

---

### 固有状態における波動関数 $Y

・方向固有ケット $\ket{\bm{n}}$ を、
$$\ket{\bm{n}}=\ket{\theta,\phi}$$
で定める。また、
$$Y_l^m(\theta,\phi)=\bra{\bm{n}}\ket{l,m}$$
で定める。
<br>

    ・まあ角度演算子の固有ケットってとこか。
    ・結局ただの球面調和関数。




