

- [剛体球](#剛体球)
  - [衝突](#衝突)
    - [衝突角が与えられてるとき](#衝突角が与えられてるとき)
    - [弾性衝突](#弾性衝突)




# 剛体球

## 衝突

<dl><dt>

・質量 $m_1,m_2$、半径 $R_1,R_2$ の $2$ つの剛体球を考える。各球の中心を $\bm{x}_1,\bm{x}_2$ とする。

</dt><dd>

・拘束力 $\bm{f}^c_i$、外力 $\bm{f}_i$ とする。
このとき、拘束条件 $G(\bm{X})$ と運動方程式：
$$G(\bm{X})=|\bm{x}_1-\bm{x}_2|-(R_1+R_2)\ge0\\\ \\
\begin{pmatrix}
m_1 & 0 & \cdots\\
0 & m_1 &\ddots\\
\\
0 & \cdots & m_2\\    
\end{pmatrix}\begin{pmatrix}
\ddot{\bm{x}}_1    \\
\ddot{\bm{x}}_1    \\
\end{pmatrix}=\begin{pmatrix}\bm{f}_1    \\
\bm{f}_1    \\\end{pmatrix}+\begin{pmatrix}\bm{f}^c_1    \\
\bm{f}^c_1    \\\end{pmatrix}\\\ \\$$
ここで、衝突時には $f_i=0$ としてよい。

- ダランベールの原理、作用反作用より、
$$\bm{f}_1^c=\lambda_1\nabla_1 G(\bm{x}_1,\bm{x}_2)=\lambda_1\frac{\bm{x}_1-\bm{x}_2}{|\bm{x}_1-\bm{x}_2|}\\\ \\
\bm{f}_2^c=\lambda_2\nabla_2 G(\bm{x}_1,\bm{x}_2)=-\lambda_2\frac{\bm{x}_1-\bm{x}_2}{|\bm{x}_1-\bm{x}_2|}\\\ \\
\lambda_1=\lambda_2$$

      ・ダランベールの原理：拘束力は衝突面に垂直。確かに偏微分したやつは=cに垂直。
<br>

- 外力は無視できるので、重心 $\bm{x}_G$ は等速度運動する。
したがって、衝突前の重心座標での速度 $\dot{\bm{x}}_{i,in}'$、重心座標での衝突後の速度 $\dot{\bm{x}}_{i,out}'$ とすると、
$$\frac{|\dot{\bm{x}}_{1,out}'|}{|\dot{\bm{x}}_{1,in}'|}=\frac{|\dot{\bm{x}}_{2,out}'|}{|\dot{\bm{x}}_{2,in}'|}=e=(const)\\\ \\$$

- $$\bm{x}_{1,out}=\bm{x}_{1,in}+\frac{\Lambda}{m_1}\frac{\bm{x}_1-\bm{x}_2}{|\bm{x}_1-\bm{x}_2|}\\\ \\
\bm{x}_{2,out}=\bm{x}_{2,in}-\frac{\Lambda}{m_2}\frac{\bm{x}_1-\bm{x}_2}{|\bm{x}_1-\bm{x}_2|}\\\ \\
\Lambda=-\frac{m_1m_2}{m_1+m_2}\left((\dot{\bm{x}}_{1,in}-\dot{\bm{x}}_{2,in})^T\frac{\bm{x}_1-\bm{x}_2}{|\bm{x}_1-\bm{x}_2|}\pm\sqrt{\left((\dot{\bm{x}}_{1,in}-\dot{\bm{x}}_{2,in})^T\frac{\bm{x}_1-\bm{x}_2}{|\bm{x}_1-\bm{x}_2|}\right)^2-(1-e^2)(\dot{\bm{x}}_{1,in}-\dot{\bm{x}}_{2,in})^2}\right)$$

</dd></dl>

---

### 衝突角が与えられてるとき

・


### 弾性衝突

<dl><dt>

・弾性衝突条件は、$e=1$、すなわち、
$$|\bm{x}_{1,out}-\bm{x}_{2,out}|=|\bm{x}_{1,in}-\bm{x}_{2,in}|$$
のことである。

</dt><dd>



</dd></dl>