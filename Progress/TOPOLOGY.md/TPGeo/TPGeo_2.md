
- [ファイバー束](#ファイバー束)
- [レトラクト](#レトラクト)
  - [強変位レトラクション](#強変位レトラクション)
- [局所連結](#局所連結)


# ファイバー束

・位相空間 $A,B,F$、位相群 $G$、連続な全射 $p:A\to B$ とする。
このとき、ファイバー束 $(A,B,p,F;G)$：
$$G\text{ は }F\text{ に効果的に作用していて、}\\\ \\
\exist\text{ 開被覆 }B=\bigcup U_{\lambda}\text{ であって、}U_{\lambda}\text{ 上で自明化が与えられていて、}\\
F_{\lambda}\cong F\ \ (\text{同相})\\\ \\
\phi_{\lambda,x}:F\to p^{-1}(x),\quad\phi_{\lambda,x}(y)=\phi_{\lambda}(x,y)\text{ と定めると、}\\
U_{\lambda}\cap U_{\mu}\neq\phi\text{ ならば、}\forall x\in U_{\lambda}\cap U_{\mu}\text{ に対して、}\exist g\in G\text{ であって、}\\\ \\
\phi_{\lambda,x}^{-1}\circ\phi_{\mu,x}=T_g\ \ (:F\to F)\\\ \\
\text{さらに、}g_{\lambda\mu}:U_{\lambda}\cap U_{\mu}\to G,\quad g_{\lambda\mu}(x)=\phi_{\lambda,x}^{-1}\circ\phi_{\mu,x}\text{ に対して一意的に定まる }g\\\ \\
\text{は連続}$$
ここで、ファイバー束は明らかにファイバー空間。また、$G$ を構造群、$U_{\lambda}$ を座標近傍、$\phi_{\lambda}$ をzahyouka、$g_{\lambda\mu}$ を座標変換という。
<br>

    ・効果的なので、作用として定まるgは一意的。また、g_{λμ}(x)^{-1}=g_{μλ}(x)
    ・なんか多様体みたい？
<br>

- 
$$\forall x\in U_{\lambda}\text{ に対して、}g_{\lambda\lambda}(x)=e\\\ \\
\forall x\in U_{\lambda}\cap U_{\mu}\text{ に対して、}g_{\lambda\mu}(x)^{-1}=g_{\mu\lambda}(x)\\\ \\$$

- ファイバー束 $(A,B,p,F;G)$ とする。 
このとき、主ファイバー束 $(A,B,p,G;G)$：
$$F=G\text{ かつ作用が群の積 }$$

---

# レトラクト

・位相空間 $X$、部分空間 $A\sub X$、包含 $i:A\to X$、$r:X\to A$ とする。
このとき、レトラクション $r$：$$r\text{ は連続写像であって、}r\circ i=1_A$$
ここで、$A$ を $X$ のレトラクトであるという。
<br>

- 位相空間 $X$、$X$ のレトラクト $(A,r)$ とする。
このとき、
$$\forall\text{ 位相空間 }Y,\ \forall\text{ 連続写像 }f:A\to Y\text{ に対して、}\\\ \\
\exist\text{ 連続写像 }\tilde{f}:X\to Y\text{ であって、}\tilde{f}(x)=f(x)\quad(\forall x\in A)$$

      ・f◦rしただけ。

---

## 強変位レトラクション

<dl><dt>

・位相空間 $X$、部分空間 $A\sub X$、$F:X\times[0,1]\to X$ とする。
このとき、強変位レトラクション $F$：$$F\text{ は連続写像であって、}\begin{cases}
F(x,0)=x & (\forall x\in X)    \\
F(x,1)\in A & (\forall x\in X) \\
F(a,s)=a & (\forall a\in A,\ \forall s\in [0,1]) \\
\end{cases}$$
ここで、$A$ を $X$ の強変位レトラクトであるという。

</dt><dd>

- 位相空間 $X$、強変位レトラクト $(A,F)$ とする。
このとき、$(A,F(x,1))$ は $X$ のレトラクト。
<br>

- 位相空間 $X$、強変位レトラクト $(A,F_1)$、$A$ の強変位レトラクト $(B,F_2)$ とする。
このとき、
$$F:X\times[0,1]\to X\\\ \\
F(x,s)=\begin{cases}
F_1(x,2s) & (0\le s\le 1/2)    \\
F_2(F_1(x,1),2s-1) & (1/2\le s\le1)    \\
\end{cases}$$と定めると、$(B,F)$ は $X$ の強変位レトラクト。

</dd></dl>


# 局所連結

・位相空間 $X$ とする。
このとき、局所連結、局所弧状連結、局所単連結な $X$：
$$\exist\text{ 基本近傍系 }\mathcal{V}\text{ であって、}\forall x\in X,\ \forall V\in\mathcal{V}(x)\text{ に対して、}\\\ \\
V\text{ は連結、弧状連結、単連結}$$
明らかに、局所単連結 $\Rightarrow$ 局所弧状連結 $\Rightarrow$ 局所連結。

- 局所連結空間 $X$ とする。
このとき、$X$ の任意の連結成分は開集合。