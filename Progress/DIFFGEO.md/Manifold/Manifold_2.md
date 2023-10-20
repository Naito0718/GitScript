
- [ベクトル束と接束](#ベクトル束と接束)
  - [接束 $TM$](#接束-tm)
    - [チャートによる接束の位相](#チャートによる接束の位相)
    - [接束の位相](#接束の位相)
    - [接束の多様体構造](#接束の多様体構造)
  - [$C^∞$ ベクトル束](#c-ベクトル束)
    - [ファイバー写像](#ファイバー写像)
    - [ベクトル束](#ベクトル束)
      - [束写像](#束写像)
  - [切断とベクトル場](#切断とベクトル場)
  - [枠](#枠)
- [$1$ の分割](#1-の分割)
  - [隆起関数](#隆起関数)
  - [$1$ の分割](#1-の分割-1)
- [ベクトル場](#ベクトル場)
  - [積分曲線](#積分曲線)
    - [局所フロー](#局所フロー)
  - [リー括弧](#リー括弧)
  - [関係にあるベクトル場](#関係にあるベクトル場)
    - [押し出し](#押し出し)



# ベクトル束と接束

    ・すべてのチャートは、ある極大アトラスに含まれているとしている！

## 接束 $TM$

・$C^{\infty}$ 多様体 $M$ とする。
このとき、接束
$$TM=\bigcup_{p\in M} T_pM$$

    ・これは非交和。直積ではないので、各TpMは部分集合。

- 自然な射影：
$$\pi:TM\to M\\\ \\
\pi(v)=p$$

- $M$ のチャート $(U,\phi)$ に対して、
$$TU=\bigcup_{p\in U}T_pM$$また、チャート $(U,\phi),(V,\psi)$ に対して、
$$TU\cap TV=T(U\cap V)$$

      ・チャート以外でTUを考えることは特にない。

---

### チャートによる接束の位相




<dl><dt>

・チャート $(U,\phi)$、$p\in U$、$v=\sum c^i\frac{\partial}{\partial x^i}_p\in T_pM$ とする。
このとき、
$$\tilde{\phi}:TU\to\phi(U)\times\bm{R}^m\\\ \\
\tilde{\phi}(v)=(\pi(v),c^1,...,c^n)$$ と定めると、これは全単射。
したがって、この写像によって $TU$ の位相を誘導する。
      
</dt><dd>

- $TU\cong \phi(U)\times R^m\\\ \\$

- $U$ の開集合 $V\sub U$ とする。このとき、$V$ はチャートであり、
$$TV\text{ の相対位相}=\tilde{\phi}_{TV}\text{ によって誘導される位相}$$

- チャート $U$ に対して、$\phi,\psi$ をともにざひょう


</dd></dl>
  
---

### 接束の位相

<dl><dt>

・$$\mathcal{B}=\{A\ |\ \exist\text{ チャート }U\text{ であって、}A\text{ は }TU\text{ の開集合 }\}$$は $TM$ の開基となる。

    ・各チャートUに対して、TUは開。
      
</dt><dd>

- $m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、$M$ はチャートからなる可算開基を持つ。
<br>

- 接束 $TM$ は第二可算である。また、Hausdorff空間でもある。
<br>

</dd></dl>

---

### 接束の多様体構造

・$m$ 次元 $C^{\infty}$ 多様体 $M$、アトラス $\{(U_{\alpha},\phi_{\alpha})\}$ とする。
このとき、$\{(TU_{\alpha},\tilde{\phi}_{\alpha})\}$ は $TM$ のアトラス。
したがって、$TM$ は $2m$ 次元 $C^{\infty}$ 多様体。

---

## $C^∞$ ベクトル束

### ファイバー写像

・ファイバー空間 $(A,B,p,F),(A',B,p',F')$、$\psi:A\to A'$ とする。
このとき、ファイバー写像 $\psi$：
$$\forall b\in B\text{ に対して、}\psi(p^{-1}(b))\sub p'^{-1}(b)$$

- ファイバー空間 $(A,B,p,F),(A',B,p',F')$、$\psi:A\to A'$ とする。
このとき、
$$\psi\text{ はファイバー写像}\iff p=p'\circ\psi\\\ \\$$

- 自明化写像 $\phi_U$ は全単射なファイバー写像。

---

### ベクトル束

<dl><dt>

・ファイバー空間 $(A,B,p,\bm{R}^r)$ とする。
このとき、階数 $r$ のベクトル束 $(A,B,p,\bm{R}^r)$：
$$\forall b\in B\text{ に対して、}p^{-1}(b)\text{ は }r\text{ 次元 }\bm{R}\text{ 上ベクトル空間}\\\ \\
p^{-1}(b)\cong \bm{R}^r\ (\text{線形同相})$$ここで、$A,B$ が 有限次元 $C^{\infty}$ 多様体、$p$ が $C^{\infty}$ 写像、各自明化写像 $\phi_U$ が微分同相写像であれば、階数 $r$ の $C^{\infty}$ ベクトル束という。

    ・p^{-1}(x) の位相が部分空間位相なので、FとR^rの同相が言えない気がする。あと演算も未知だし。
<br>

</dt><dd>

- $m$ 次元 $C^{\infty}$ 多様体 $M$、接束 $TM$ とする。
このとき、$\pi$ は $C^{\infty}$ 写像で、
$$\pi^{-1}(p)=T_pM\\\ \\
\text{極大アトラス} \{(U_{\alpha},\phi_{\alpha})\}\text{ に対して、 }\\
\pi^{-1}(U_{\alpha})=TU_{\alpha}$$また、
$$\psi:TU_{\alpha}\to U_{\alpha}\times\bm{R}^m\\\ \\
\psi(v)=(\pi(v),c^1,...,c^m)$$と定めると、これは明らかに微分同相。
したがって、$(TM,M,\pi,\bm{R}^m)$ は 階数 $m$ の $C^{\infty}$ ベクトル束。

</dd></dl>

---

#### 束写像

<dl><dt>

・階数 $r,s$ のベクトル束 $(A_1,B_1,\pi_1,\bm{R}^r),(A_2,B_2,\pi_2,\bm{R}^s)$、$f:B_1\to B_2,g:A_1\to A_2$ とする。
このとき、束写像 $(f,g)$：
$$\pi_2\circ g=f\circ\pi_1\\\ \\
\forall b_1\in B_1\text{ に対して、}g:\pi_1^{-1}(b_1)\to \pi_2^{-1}(f(b_1))\text{ は線形写像}$$

    ・二つ目の条件で、写像はwell-defined。
<br>

- $E,F$ を $M$ 上のベクトル束とする。
このとき、$M$ 上 $E$ から $F$ への束写像：$(f,g)=(id,g)$
これが成り立つとき、$g$ はファイバー写像。
<br>

- 多様体 $M$、$C^{\infty}$ ベクトル束 $E$ とする。
このとき、自明束 $E$：???積束と同型？？？
<br>


</dt><dd>

- $m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $f:M\to N$ とする。
このとき、
$$g:TM\to TN\\\ \\
g(p,v)=(f(p),f_{*}(v))$$
と定めると、$(f,g)$ は束写像。

      ・共変関手？
<br>

</dd></dl>

---

## 切断とベクトル場

<dl><dt>

・階数 $r$ のベクトル束 $(A,B,p,\bm{R}^r)$ とする。
このとき、切断 $s:B\to A$
$$p\circ s=1_{M}$$
これが成り立つとき、$$s(p)\in\pi^{-1}(p)$$
すなわち、各点 $p$ をその上のファイバーへ移す。
さらに、$s$ が $C^{\infty}$ 写像ならば、$C^{\infty}$ 切断という。

    ・ファイバーが縦線なら、sは断面。
<br>

- $C^{\infty}$ 多様体 $M$、$C^{\infty}$ 写像 $X:M\to TM$ とする。
このとき、
$$X\text{ は }C^{\infty}\text{ ベクトル場 }\iff X\text{ は }C^{\infty}\text{ 切断}$$

      ・各点pにTpMの元を割り当てる。
<br>

- $C^{\infty}$ ベクトル束 $(A,B,p,\bm{R}^r)$、$C^{\infty}$ 切断 $s:B\to A$、自明化 $\phi_U:p^{-1}(U)\to U\times\bm{R}^r$ とする。
このとき、
$$\phi_U\circ s(q)=(q,...)$$

      ・第一成分だけ分かる。
<br>

</dt><dd>

- $C^{\infty}$ ベクトル束 $(A,B,p,\bm{R}^r)$、$C^{\infty}$ 切断 $s,t:B\to A$、$C^{\infty}$、$\alpha\in \bm{R}$、 写像 $f:B\to\bm{R}$ とする。
このとき、$$s+t,\alpha s,fs$$
は $C^{\infty}$ 切断。
したがって、$A$ の $C^{\infty}$ 切断全体 $\Gamma(A)$ は 単位的可換環 $C^{\infty}(B)$ 上 $\bm{R}$ー加群。これを大域切断という。
<br>

- 開集合 $U\sub B$ とする。
このとき、$\Gamma(p^{-1}(U))$ は単位的可換環 $C^{\infty}(U)$ 上 $\bm{R}$ー加群。

</dd></dl>

---


## 枠

<dl><dt>

・階数 $r$ のベクトル束 $(A,B,p,\bm{R}^r)$、開集合 $U\sub B$ とする。
このとき、枠 $s_1,...,s_r$：
$$s_1,...,s_r\in\Gamma(p^{-1}(U))\text{ であって、}\\
\forall b\in U\text{ に対して }s_1(b),...,s_r(b)\text{ が }p^{-1}(b)\text{ の基底}$$
さらに、$s_1,...,s_r$ が $C^{\infty}$ 写像ならば、$C^{\infty}$ 枠という。

- $C^{\infty}$ ベクトル束 $(A,B,\pi,\bm{R}^r)$、自明化 $\phi_U:\pi^{-1}(U)\to U\times\bm{R}^r$、積束 $(U\times\bm{R}^r,U,\pi_{\times},\bm{R}^r)$ 上の $C^{\infty}$ 枠 $s_i$ とする。
このとき、
$$t_i:U\to\pi^{-1}(U)\\\ \\
t_i(p)=\phi^{-1}\circ s_i(p)$$
と定めると、$t_i$ は $A$ の $U$ 上 $C^{\infty}$ 枠。
したがって、自明化 $\phi^{-1}_U$ は $C^{\infty}$ 枠同士を移しあっており、この $t_i$ を自明化 $\phi_U$ の $U$ 上 $C^{\infty}$ 枠という。

<br>

</dt><dd>

- $C^{\infty}$ ベクトル束 $(A,B,p,\bm{R}^r)$、開集合 $U\sub B$、$A$ の $U$ 上 $C^{\infty}$ 枠 $s_i$ とする。
このとき、$s(p)=\sum c^i(p)s_i(p)$ は $U$ 上切断で、
$$s(p)=\sum c^i(p)s_i(p)\text{ が }C^{\infty}\text{ 切断}\iff c^{i}(p)\text{ が }U\text{ 上 }C^{\infty}$$

      ・自明化の枠であるときの拡張。

</dd></dl>

---
---
---


# $1$ の分割

## 隆起関数

<dl><dt>

・$$f(t)=\begin{cases}
e^{-\frac{1}{t}} & (t>0) \\
0 & (t\le0) \\
\end{cases}$$
として、
$$g(t)=\frac{f(t)}{f(t)+f(1-t)}\\\ \\
h(x)=g\left(\frac{x-a^2}{b^2-a^2}\right),\quad(0<a<b)\\\ \\
k(x)=h(x^2)\\\ \\
\rho(x)=1-k(x)$$
としていくと、$\rho$ は原点 $0$ における $y$ 軸対称な $C^{\infty}$ 写像で、$[-a,a]$ で $1$、$\mathrm{supp} f=[-b,b]$
さらに、$\rho(x-q)$ は $q$ における $C^{\infty}$ 隆起関数。

    ・q∊Uにおける隆起関数：連続非負値で、qのある近傍で値が1でsuppρ⊂U
<br>

</dt><dd>

- 
$$\sigma:\bm{R}^n\to\bm{R}\\\ \\
\sigma(x)=\rho(\|x\|)$$
とする。
このとき、$\sigma$ は $C^{\infty}$ 写像で、$\overline{U(\bm{0},a)}$ で $1$、$\mathrm{supp} f=\overline{U(0,b)}$
さらに、$\sigma(x-q)$ は $q$ における $C^{\infty}$ 隆起関数。
<br>

- 
$m$ 次元 $C^{\infty}$ 多様体 $M$、$q\in M$、開集合 $q\in U\sub M$ とする。
このとき、
$$\rho:M\to [0,1]\\\ \\
\mathrm{supp}\rho\sub U$$ なる $U$ に台を持つ $q$ における $C^{\infty}$ 隆起関数が存在する。

    ・（チャートの部分空間位相における）閉集合A⊂U上で1で、そもそも1以下。
    ・コンパクトの部分は無理かも？
---

- 
$m$ 次元 $C^{\infty}$ 多様体 $M$、$q\in M$、開集合 $q\in U\sub M$、$C^{\infty}$ 写像 $f:U\to\bm{R}$ とする。
このとき、$q$ の十分小さい近傍 $V\sub U$ 上で $f$ と一致するような $C^{\infty}$ 写像 $g:M\to\bm{R}$ が存在する。

</dd></dl>

---

## $1$ の分割

・$m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、$C^{\infty}1$ の分割 $\{\rho_{\alpha}:M\to\bm{R}\}_{\alpha\in A}$：
$$\rho_{\alpha}\text{ は非負の }C^{\infty}\text{ 写像}\\\ \\
\{\mathrm{supp}\ \rho_{\alpha}\}_{\alpha\in A}\text{ は局所有限}\\\ \\
\sum\rho_{\alpha}=1$$ 
ここで、位相空間 $X$ の部分集合族 $\{S_{\alpha}\}$ が局所有限：
$$\forall x\in X\text{ に対して }\exist\text{ 開近傍 }q\in U\text{ であって、}\\
\text{たかだか有限個を除いて}U\cap S_{\alpha}=\phi$$
また、開被覆 $M=\bigcup_{\alpha\in A}U_{\alpha}$ に対して、$\mathrm{supp}\ \rho_{\alpha}\sub U_{\alpha}$ が成り立つとき、$1$ の分割は開被覆に従属するという。

    ・∑ρ=1が無くても、∑ρはC^∞ではある。
<br>

- $m$ 次元 $C^{\infty}$ 多様体 $M$、開被覆 $M=\bigcup_{\alpha\in A}U_{\alpha}$ とする。
このとき、
$$\exist C^{\infty}1\text{ の分割 }\{\phi_n\}_{n\in\bm{N}}\text{ であって、}\\
\mathrm{supp}\ \phi_n\text{ はコンパクトで、 }\\
\forall n\text{ に対して }\exist\alpha\in A\text{ であって }\mathrm{supp}\ \phi_n\sub U_{\alpha}\\\ \\
\exist C^{\infty}1\text{ の分割 }\{\phi_\alpha\}_{\alpha\in A}\text{ であって、}\\
\{\phi_\alpha\}_{\alpha\in A}\text{ は }\{U_{\alpha}\}_{\alpha\in A}\text{ に従属する}$$

      ・???

---
---
---

# ベクトル場

<dl><dt>

・$m$ 次元 $C^{\infty}$ 多様体 $M$、ベクトル場 $X:M\to TM$ とする。
このとき、
$$X\text{ が }C^{\infty}\\\ \\
\iff\exist\text{ アトラス }\{U_{\alpha},\phi_{\alpha}\}\text{ であって、}\\
\forall\text{ チャート }(U_{\alpha},\phi_{\alpha})\text{ 上で枠 }\partial/\partial x^i\text{ の係数 }a^i\text{ が }C^{\infty}\\\ \\
\iff\forall\text{ チャート }(U_{\alpha},\phi_{\alpha})\text{ に対して、枠 }\partial/\partial x^i\text{ の係数 }a^i\text{ が }C^{\infty}\\\ \\
\iff\forall C^{\infty}\text{ 写像 }f:M\to\bm{R}\text{ に対して、}Xf:M\ni p\mapsto X_pf\in\bm{R}\text{ が }C^{\infty}$$

    ・最後の同値は、隆起関数のとこの拡大を使って示す。
<br>

- $C^{\infty}$ ベクトル場 $X:M\to TM$、$f,g\in C^{\infty}(M)$、$\alpha\in\bm{R}$ とする。
このとき、$Xf\in C^{\infty}(M)$ であって、
$$X(f+g)=Xf+Xg,\quad X(\alpha f)=\alpha Xf\\\ \\
X(fg)=(Xf)g+f(Xg)$$
したがって、$X$ は単位的可換 $\bm{R}$-多元環 $C^{\infty}(M)$ 上導分。

      ・TpMの元が点導分なのは定義。
      ・二つの記述は同値？p.265
<br>

</dt><dd>

- $m$ 次元 $C^{\infty}$ 多様体 $M$、$p\in M$、開集合 $p\in U\sub M$、$C^{\infty}$ ベクトル場 $X:U\to TU$ とする。
このとき、$p$ の十分小さい近傍 $V\sub U$ 上で $X$ と一致するような $C^{\infty}$ ベクトル場 $Y:M\to TM$ が存在する。
<br>

- ベクトル場 $X,Y:M\to T_M$ とする。
このとき、
$$X=Y\iff \forall f\in C^{\infty}\text{ に対して }Xf=Yf$$


</dd></dl>

---

## 積分曲線

・$m$ 次元 $C^{\infty}$ 多様体 $M$、$C^{\infty}$ ベクトル場 $X:M\to TM$、$p\in M$ とする。
このとき、積分曲線 $c$：
$$C^{\infty}\text{ 写像 }c:\bm{R}\sup(a,b)\to M\\\ \\
\forall t\in (a,b)\text{ に対して }c'(t)=X_{c(t)}$$

    ・普通0∊(a,b)
    ・始点だけ合わせればよいなら存在する。
    ・定義域をそれ以上拡張できないとき極大であるという。

### 局所フロー

---

## リー括弧

・$m$ 次元 $C^{\infty}$ 多様体 $M$、開集合 $U\sub M$、$C^{\infty}$ ベクトル場 $X,Y:U\to TU$、$p\in U$ とする。
このとき、
$$[X,Y](f)=(XY-YX)f\\\ \\
[X,Y]_pf=(X_pY-Y_pX)f$$
はそれぞれ $U$ 上の $C^{\infty}$ ベクトル場、$T_pM$ の元である。
ここで、$M$ 上の $C^{\infty}$ ベクトル場全体からなるベクトル場 $\mathfrak{X}(M)$ は、リー括弧積を括弧積とする実リー代数。

---

## 関係にあるベクトル場


<dl><dt>

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $F:M\to N$、ベクトル場 $X:M\to TM,Y:N\to TN$ とする。
このとき、$F$ 関係にあるベクトル場 $(X,Y)$：
$$\forall p\in M\text{ に対して、}F_{*,p}(X_p)=Y_{F(p)}$$

    ・ベクトル場は滑らかでなくてもよい。
<br>

</dt><dd>

- $m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $F:M\to N$、ベクトル場 $X:M\to TM,Y:N\to TN$ とする。
このとき、
$$(X,Y)\text{ は }F\text{ 関係}\iff\forall f\in C^{\infty}(M)\text{ に対して、}X(g\circ F)=(Yg)\circ F$$
<br>

- $m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $F:M\to N$、$F$ 関係にあるベクトル場 $(X_1,Y_1),(X_2,Y_2)$ とする。
このとき、$([X_1,X_2],[Y_1,Y_2])$ は $F$ 関係にあるベクトル場。

</dd></dl>

---

### 押し出し

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $F:M\to N$、$X_p\in T_pM$ とする。
このとき、押し出し：
$$F_*(X_p)\in T_{F(p)}N$$

    ・ただの微分の像。接ベクトルに注目した。


- $F$ を微分同相写像とする。
このとき、
$$F_{*}X:N\to TN\\\ \\
F_*X(q)=F_{*}\circ X\circ F^{-1}(q)$$
と定めると、これは $C^{\infty}$ 写像で、$F$ 関係にあるベクトル場 $(X,F_*X)$ である。
これをベクトル場 $X$ の押し出しという。

      ・ベクトル場には拡張できない。M→TNなら可能。




