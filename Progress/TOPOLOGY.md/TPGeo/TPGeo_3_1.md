
    ・ベクトル空間でもやんなきゃなぁ。

- [チェイン複体](#チェイン複体)
  - [チェイン準同型](#チェイン準同型)
  - [部分チェイン](#部分チェイン)
    - [剰余チェイン複体](#剰余チェイン複体)
    - [チェイン完全系列](#チェイン完全系列)
- [完全系列](#完全系列)
  - [完全系列の準同型](#完全系列の準同型)
- [チェイン複体の完全系列](#チェイン複体の完全系列)
  - [境界準同型](#境界準同型)
  - [ホモロジー群完全系列](#ホモロジー群完全系列)





# チェイン複体

<dl><dt>

・加群列 $C_n\ \ (n\in\bm{Z})$、群準同型列 $\partial_n:C_n\to C_{n-1}$ とする。
このとき、チェイン複体 $\mathcal{L}$：
$$\forall n\in\bm{Z}\text{ に対して、}\partial_n\circ\partial_{n+1}=0$$
ここで、$C_n\in\mathcal{L}$ を $n$ チェイン群、$\partial_n$ を境界作用素、$Z_n=\ker\partial_n\sub C_n$ を $n$ サイクル群、$B_n=\mathrm{Im}\ \partial_{n+1}\sub C_n$ を $n$ 境界サイクル群という。
<br>

</dt><dd>

- $$\forall n\in\bm{Z}\text{ に対して、}B_n\sub Z_n$$
ここで、$H_n=Z_n/B_n$ を $n$ ホモロジー群といい、$[x]\in Z_n/B_n$ を $x$ にホモローグな $n$ サイクル、ホモロジー類という。
<br>

      ・加群だから問題ない。
      ・一応チェイン複体であることと同値。


</dd></dl>

---

## チェイン準同型

<dl><dt>

・チェイン複体 $\mathcal{L}_1,\mathcal{L}_2$、群準同型列 $f_n:C_{1,n}\to C_{2,n}$ とする。
このとき、チェイン準同型 $(f_n)$
$$\forall n\in\bm{Z}\text{ に対して、}\\\ \\
\partial_{2,n}\circ f_n=f_{n-1}\circ\partial_{1,n}\\\ \\$$

    ・いい感じに可換図式が書ける。
<br>

</dt><dd>

- $$\forall n\in\bm{Z}\text{ に対して、}\\\ \\
f_n(Z_{1,n})\sub Z_{2,n},\ f_n(B_{1,n})\sub B_{2.n}$$
したがって、
$$f_{n,*}:H_{1,n}\to H_{2,n}\\\ \\
f_{n,*}([x])=[f_n(x)]$$
はwell-definedな群準同型写像。
<br>

- チェイン準同型 $(f_n),(g_n)$ とする。
このとき、$(f_ng_n)$ はチェイン準同型であって、
$$\forall n\in \bm{Z}\text{ に対して、}(f_ng_n)_*=f_{n,*}g_{n,*}$$

</dd></dl>


---

## 部分チェイン

- チェイン複体  $\mathcal{L}_1,\mathcal{L}_2$ とする。
このとき、$\mathcal{L}_1$ が $\mathcal{L}_2$ の部分チェイン：
$$\forall n\in\bm{Z}\text{ に対して、}\\\ \\
C_{1,n}\sub C_{2,n}\text{ かつ、包含写像列 }i_n:C_{1,n}\to C_{2,n}\text{ がチェイン準同型}$$
このとき、明らかに $\partial_{1,n}=\partial_{2,n}|_{C_{1,n}}$

---

### 剰余チェイン複体

<dl><dt>

・チェイン複体 $\mathcal{L}_2$、部分チェイン複体 $\mathcal{L}_2$ とする。
このとき、
$$\partial_{n,/}:C_{2,n}/C_{1,n}\to C_{2,n-1}/C_{1,n-1}\\\ \\
\partial_{n,/}([x])=[\partial_n(x)]$$
と定めると、$(C_{2,n}/C_{1,n},\partial_{n,/})$ はチェイン複体。
ここで、$\mathcal{L}_2/\mathcal{L}_1=(C_{2,n}/C_{1,n},\partial_{n,/})$ を剰余チェイン複体という。
<br>

</dt><dd>

- 
$$p_n:C_{2,n}\to C_{2,n}/C_{1,n}\\\ \\
p_n(x)=[x]$$
と定めると、$(p_n):\mathcal{L}_2\to\mathcal{L}_2/\mathcal{L}_1$ はチェイン準同型。
<br>

- チェイン複体 $\mathcal{L}_1,\mathcal{L}_2$、部分チェイン複体 $\mathcal{M}_1\sub\mathcal{L}_1,\ \mathcal{M}_2\sub\mathcal{L}_2$、チェイン準同型 $(f_n):\mathcal{L}_1\to \mathcal{L}_2$ とする。
このとき、$f_n$ が $\mathcal{M}_1$ を $\mathcal{M}_2$ に移すならば、
$$f_{n,/}:C_{1,n}/D_{1,n}\to C_{2,n}/D_{2,n}\\\ \\
f_{n,/}([x])=[f(x)]$$
は $\mathcal{L}_1/\mathcal{M}\to\mathcal{L}_2/\mathcal{M}_2$ へのチェイン準同型。
<br>



</dd></dl>

---

### チェイン完全系列

・チェイン複体 $\mathcal{L}$、部分チェイン複体 $\mathcal{M}\sub\mathcal{L}$ とする。
このとき、
$$0\longrightarrow \mathcal{M}\overset{i_n}{\longrightarrow}\mathcal{L}\overset{p_n}{\longrightarrow}\mathcal{L}/\mathcal{M}\to 0\\\ \\
\text{ が完全系列}\\\ \\$$


---
---
---

# 完全系列

<dl><dt>

・加群列 $G_n\ \ (n\in\bm{Z})$、群準同型列 $f_n:G_n\to G_{n-1}$ とする。
このとき、完全系列 $(G_n,f_n)$：
$$\forall n\in\bm{Z}\text{ に対して、}\mathrm{Im}\ f_{n+1}=\mathrm{ker}\ f_{n}$$
明らかに、完全系列ならばチェイン複体。
<br>

</dt><dd>

- 
$$G_{n+1}=G_{n-1}=0\Rightarrow G_n=0\\\ \\
G_{n+1}=0\Rightarrow f_n\text{ は単射}\\\ \\
G_{n-2}=0\Rightarrow f_{n}\text{ は全射}$$


</dd></dl>

---

## 完全系列の準同型

<dl><dt>

・完全系列 $(G_{1,n},f_{1,n}),(G_{2,n},f_{2,n})$、群準同型列 $g_n:g_{1,n}\to G_{2,n}$ とする。
このとき、完全系列準同型 $(g_n)$
$$\forall n\in\bm{Z}\text{ に対して、}\\\ \\
f_{2,n}\circ g_n=g_{n-1}\circ f_{1,n}\\\ \\$$

    ・いい感じに可換図式が書ける。
<br>

</dt><dd>

- 
$$g_{n-1},g_{n+1}\text{ が全射、}g_{n-2}\text{ が単射}\Rightarrow g_{n}\text{ は全射}\\\ \\
g_{n+2}\text{ が全射},g_{n+1},g_{n-1}\text{ が単射}\Rightarrow g_n\text{ は単射}\\\ \\$$

- 完全系列準同型 $(g_n),(h_n)$ とする。
このとき、$(g_nh_n)$ は完全系列準同型。
<br>


</dd></dl>

---
---
---


# チェイン複体の完全系列

・チェイン複体 $\mathcal{L}_1,\mathcal{L}_2,\mathcal{L}_3$、チェイン準同型 $(f_n):\mathcal{L}_2\to\mathcal{L}_1,\ (g_n):\mathcal{L}_1\to\mathcal{L}_3$ とする。
このとき、チェイン複体の完全系列：
$$\forall n\in\bm{Z}\text{ に対して、}\\\ \\
0\longrightarrow C_{2,n}\overset{f_n}{\longrightarrow}C_{1,n}\overset{g_n}{\longrightarrow}C_{3,n}\to 0\\\ \\
\text{ が完全系列}\\\ \\$$

    ・端の写像は、0に行く定値写像と考える。

---

## 境界準同型

## ホモロジー群完全系列
