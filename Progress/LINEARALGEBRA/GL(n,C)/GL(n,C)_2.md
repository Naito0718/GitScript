
- [エルミート行列 $H(n)$ と準代数群](#エルミート行列-hn-と準代数群)
  - [位相的性質](#位相的性質)
  - [性質](#性質)
    - [次元、固有値](#次元固有値)
    - [指数写像](#指数写像)
  - [正値エルミート行列](#正値エルミート行列)
    - [位相的性質](#位相的性質-1)
    - [性質](#性質-1)
    - [極分解](#極分解)
  - [対角エルミート行列](#対角エルミート行列)
  - [$C^n$ への作用](#cn-への作用)
- [反射行列](#反射行列)
  - [性質](#性質-2)



# エルミート行列 $H(n)$ と準代数群

## 位相的性質

・$H(n)$ は $M(n,\bm{R,C,H})$ の閉集合。

---

## 性質

### 次元、固有値

<dl><dt>

・$$H(n)=\{A\in M(\bm{R,C,H})\ |\ A^{\dag}=A\}$$は $\bm{R}$ 加群。ここで、$H(n)$ の元をエルミート行列という。

    ・C,H加群ではない。

</dt><dd>

- $$\dim H_{\bm{R}}(n)=\frac{n(n+1)}{2},\quad\dim H_{\bm{C}}(n)=n^2,\\\ \\
\dim H_{\bm{H}}(n)=n(2n-1)$$特に、対角成分はすべて実数。
さらに、距離空間として $\bm{R}^{\dim H(n)}$ と同型である。

      ・n+k(n(n-1)/2)

- $$\forall A\in H(n)\text{ に対して、}\exist\lambda\in\bm{R},\exist x\in\bm{R,C,H}^n\backslash\{0\}\text{ であって、}\\\ \\
Ax=\lambda x\\\ \\$$

      ・四元数体Hでは、エルミート行列以外の固有値は定義できない。（っぽい）

- $$\forall A\in H(n)\text{ に対して、}\exist X\in G(n,\bm{R,C,H})\text{ であり }\\\ \\
\text{さらに }\lambda_1,...,\lambda_n\in\bm{R}\text{ が順序を除いてただ一つ存在して、}\\\ \\
X^{-1}AX=\begin{pmatrix}
\lambda_1 & \\
 & \ddots & \\
 & & \lambda_n\\
\end{pmatrix}\\\ \\
\mathrm{Tr}(X^k)=\sum_{i=1}^n\lambda_i^k\quad(k=1,...,n)$$が成り立つ。


</dd></dl> 

---

### 指数写像

・$A\in G(n,\bm{R,C,H}),\ X\in H(n)$ とする。
このとき、
$$A\exp X=\exp X\ A$$ならば、
$$AX=XA\\\ \\$$

- $$\exp:H(n)\to H_+(n)$$は同相写像。したがって、$\bm{R}^{\dim H(n)}$ と同相。



---

## 正値エルミート行列

### 位相的性質

・$H_+(n)$ は $GL(n,\bm{R,C,H})$ の閉集合。

---

### 性質

<dl><dt>

・エルミート行列 $A\in H(n)$ に対して、
正値エルミート行列 $A$：固有値がすべて $>0$
ここで、正値エルミート行列全体を $H_{+}(n)$ と書く。

    ・別にR上のベクトル空間ではない。

</dt><dd>

- $H_+(n)\sub GL(n)$
<br>

- エルミート行列 $A\in H(n)$ とする。このとき、
$$A\in H_{+}(n)\\\ \\
\iff\exist B\in H_+(n)\text{ であって、}A=B^2\\\ \\
\iff\forall x\in \bm{R,C,H}\text{ に対して、}(Ax,x)>0\\\ \\$$

- $P,Q\in H_+(n)$ とする。
このとき、$$P^n=Q^n\ (n=1,2,...)\iff P=Q$$

- 
$$f:H_+(n)\to H_+(n)\\\ \\
f(P)=\sqrt{P}=\exp\left(\frac{1}{2}\log P\right)$$ はwell-definedで連続。

</dd></dl> 

--- 

### 極分解

・$A\in GL(n,\bm{R,C,H})$ とする。
このとき、$$\exist! U\in G(n,\bm{R,C,H}),\ \exist! P\in H_+(n)\text{ であって、} H=UP$$ 

    ・一意的に成り立つ。

- 
$$f:G(n,\bm{R,C,H})\times H_+(n)\to GL(n,\bm{R,C,H})\\\ \\
f(u,P)=UP$$は同相写像。




---

## 対角エルミート行列

<dl><dt>

・対角エルミート行列：$DH(n)=\{A\in H(n)\ |\ A\text{ は対角行列 }\}$
<br>

</dt><dd>

- $$DH(n)=\{A\in M(n,\bm{R})\ |\ A\text{ は対角行列 }\}$$

- $$\exp:DH(n)\to DH_+(n)$$ は同相写像。
<br>

- 点列 $D_n\sub DH(n)$ とする。
このとき、$\exp D_n$ が $GL(n,\bm{R,C,H})$ 内に収束するならば、：$\lim \exp D_n=P\in GL(n,\bm{R,C,H})$
$D_n$ は収束し、
$$P\in DH_+(n),\ \lim D_n=D\in DH(n),\ P=\exp D$$


</dd></dl> 

---

## $C^n$ への作用

・$N$ 次元 $\bm{R,C,H}$ 内積右加群 $V$、$A:V\to V$ とする。
このとき、Hermite変換 $A$：
$$(u,Av)=(Au,v)$$

- $N$ 次元 $\bm{C,H}$ 内積右加群 $V$、$A:V\to V$ とする。
このとき、
$$A\text{ がHermite}\iff\forall v\in V\text{ に対して }(v,Av)\in\bm{R}$$

      ・有限次元C,H右加群のとき、正規直交基底の存在より、内積が実数値だけになることはありえない。


---
---
---

# 反射行列

## 性質

<dl><dt>

・$a\in S_{\bm{R,C,H}}^{n-1}$、$D\in M(n,\bm{R,C,H})$ とする。
このとき、$a$ に関する反射行列 $D$：
$$Da=-a\\\ \\
\forall x\in (\bm{R,C,H})^n\text{ に対して、}(x,a)=0\Rightarrow Dx=x\\\ \\$$

</dt><dd>

- 


</dd></dl> 


---