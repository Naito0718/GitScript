

# 基礎的なこと

##### 自然単位系

・$c=\hbar=1$

- $c=1=LT^{-1},\quad\hbar=ML^2T^{-1}$

- $[Lenth]=[Time]=[Mass]^{-1}=[Energy]^{-1}=[momentum]^{-1}$

        ・m⇔mc^2
        ・mc/h⇔m （コンプトン波長の逆）

##### 計量

・時空の計量テンソル：
$$g_{\mu\nu}=g^{\mu\nu}=\begin{pmatrix}
1 & 0 & 0 & 0    \\
0 & -1 & 0 & 0    \\
0 & 0 & -1 & 0    \\
0 & 0 & 0 & -1    \\
\end{pmatrix}$$

- $(x^0,x^1,x^2,x^3)=(ct,x,y,z)$

- $ds^2=g_{\mu\nu}dx^{\mu}dx^{\nu}$

---

# クライン-ゴルドン方程式

## ガリレイ変換



<dl><dt>

・
$$\{(R,a,v,b)\ |\ R\in O(3),a,v\in\bm{R}^3,b\in\bm{R}\}=O(3)\times\bm{R}^3\times\bm{R}^3\times\bm{R}\\\ \\
(R_2,a_2,v_2,b_2)(R_1,a_1,v_1,b_1)=(R_2R_1,R_2a_1-v_2b_1+a_2,R_2v_1+v_2,b_2+b_1)$$と定めると、これは位相群をなす。

</dt><dd>

- 単位元：$(I,0,0,0)$、逆元：$(R^T,-R^T(a+vb),-R^Tv,-b)$
<br>

- $(x,t)\in\bm{R}^4$ に対して、
$$(R,a,v,b)(x,t)=(Rx-vt+a,t+b)$$と定めると、これは連続な作用。
<br>

- $(x'(t),t')=(R,a,v,b)(x(t),t)$ とすると、
$$m\frac{d^2x}{dt^2}=F(x)\\\ \\
\Rightarrow m\frac{d^2x'}{dt'^2}=F(x')\quad(F(x')=RF(x))\\\ \\$$

- $L=\frac{m}{2}\dot{x}^2$ とすると、
$$L'=L+\frac{d}{dt}(-(Rx,v)+v^2t+const)$$


</dd></dl>

