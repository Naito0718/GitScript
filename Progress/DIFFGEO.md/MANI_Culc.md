- [$C^{∞}$ 多様体から生成される多様体](#c-多様体から生成される多様体)
  - [$C^∞$ 写像](#c-写像)
  - [多様体 $M$ の開集合 $U$](#多様体-m-の開集合-u)
    - [包含写像](#包含写像)
    - [接空間 $Tp(U)$](#接空間-tpu)
  - [積多様体](#積多様体)
    - [定義](#定義)
    - [$C^∞$ 写像](#c-写像-1)
      - [微分](#微分)
  - [正則部分多様体](#正則部分多様体)
    - [定義](#定義-1)
      - [正則レベル集合](#正則レベル集合)
  - [部分多様体](#部分多様体)
- [$C^∞$ 多様体から生成される $C^∞$ 写像](#c-多様体から生成される-c-写像)
  - [チャート](#チャート)
    - [偏微分](#偏微分)
- [簡単な多様体](#簡単な多様体)
        - [$0$ 次元多様体](#0-次元多様体)
- [$C^∞$ 写像](#c-写像-2)
        - [$f:R^n→ R^m$](#frn-rm)
        - [$f:M→R$](#fmr)



# $C^{∞}$ 多様体から生成される多様体

## $C^∞$ 写像

・定値写像 $$f_{q_0}:M\to N,\quad f_{q_0}(p)=q_0$$は $C^{\infty}$。

---

## 多様体 $M$ の開集合 $U$

・$C^{\infty}n$ 次元多様体 $M$、開集合 $U\subset M$ とする。
 このとき、$U$ は $n$ 次元 $C^{\infty}$ 正則部分多様体。

- アトラス：$\{(U_{\alpha}\cap U,\phi_{\alpha}|_{U_{\alpha}\cap U})\}$
    
      ・閉集合だと無理

---

### 包含写像
$$i:U\to M$$

・$i$ は $C^{\infty}$ 写像。

・微分 $i_{*}$ は線形同型写像。よって、$i$ ははめ込みかつ沈め込み。

### 接空間 $Tp(U)$

・$p\in U$ に対して、
$$T_p(U)=T_p(M)$$

---



##  積多様体

### 定義

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ アトラス $\{(U_{\alpha},\phi_{\alpha})\},\ \{V_{\beta},\psi_{\beta}\}$ とする。
このとき、直積空間 $M\times N$ は $m+n$ 次元 $C^{\infty}$ 多様体。

- アトラス：$$\{U_{\alpha}\times V_{\beta},\phi_{\alpha}\times\psi_{\beta}\}$$

---

### $C^∞$ 写像

・射影 $\pi_1:M\times N\to M$ は $C^{\infty}$

- $f:M\to N_1\times N_2\text{ は }C^{\infty}\iff f^i:M\to N_i\text{ がともに }C^{\infty}$

- 包含 $$i_{q_0}:M\to M\times N,\quad i_{q_0}(p)=(p.q_0)$$は $C^{\infty}$

---

#### 微分

・$$\pi_{1,*}\left(\left.\frac{\partial}{\partial \overline {x}^i}\right|_{p,q}\right)=\left.\frac{\partial}{\partial x^i}\right|_p,\quad\pi_{1,*}\left(\left.\frac{\partial}{\partial \overline {y}^i}\right|_{p,q}\right)=0$$

    ・(x)^-は積空間の基底

- $$(\pi_{1,*},\pi_{2,*}):T_{p,q}(M\times N)\to T_pM\times T_qM$$は線形同型写像。

---

## 正則部分多様体

### 定義

・$m$ 次元 $C^{\infty}$ 多様体 $M$、$S\subset M$ とする。
このとき、$k$ 次元正則部分多様体 $S$：
$$\forall p\in S\text{ に対して、}\exist p\text{ 周りの $M$ のチャート }(U,\phi)\text{ であって、}\\\ \\
U\cap S=\{q\in U\ |\ \phi^{k+1}(q)=...=\phi^m(q)=0\}$$このとき、
$$(U\cap S,\phi_{S}),\quad\phi_S:U\cap S\to\bm{R}^k$$は $S$ のアトラス。

    ・Sの位相は部分空間位相：第二可算、Hausdorff。
    ・正則部分多様体はC^∞多様体
    ・MのチャートをSに適合するチャートという。
    ・余次元：n-k

---

#### 正則レベル集合

    ・レベル集合：あるcに対する原像F^{-1}(c) (cをレベルという。)
    ・正則値のレベル集合：正則レベル集合　（空集合またはすべての元が正則点）
    ・正則部分多様体は局所的に零点集合で表されるので、R^nのときはF^{-1}(0)を考えるとよい 

<dl><dt>

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $F:M\to N$ とする。

    ・正則レベル集合定理。
    ・逆関数定理が成り立つようなpにおいては、(V_p,F^1,...,F^n) はF^{-1}(p) に適合するチャート。

</dt><dd>

- 空でない正則レベル集合 $F^{-1}(q)$ は $n-m$ 次元正則部分多様体。
<br>

- 臨界値の集合は、ルベーグ測度 $0$
  
      ・???ルベーグ測度？
      ・サードの定理。

</dd></dl>

---

## 部分多様体

---
---
---

# $C^∞$ 多様体から生成される $C^∞$ 写像

## チャート

・$m$ 次元 $C^{\infty}$ 多様体 $M$、チャート $(U,\phi)$ とする。
このとき、$\phi:U\to \phi(U)$ は微分同相写像。 

    ・U,φ(U) は多様体

- $m$ 次元 $C^{\infty}$ 多様体 $M$、開集合 $U\subset M$、微分同相写像 $F:U\to F(U)\subset \bm{R}^m$ とする。
このとき、$(U,F)\subset M$ はチャートであって、ある極大アトラスに含まれる。

      ・結局任意の極大アトラスのチャートと両立することを言えばよい。

### 偏微分

<dl><dt>

・$m$ 次元 $C^{\infty}$ 多様体 $M$、チャート $(U,x^1,...,x^m)$ とする。

</dt><dd>

- $$\frac{\partial x^i}{\partial x^j}=\delta_{ij}$$

- $(U,x^1,...,x^m)$ と両立するチャート $(V,y^1,...,y^m)$ に対して、
$$\frac{\partial y^i}{\partial x^j}(p)=\frac{\partial(r^i\circ\psi\circ\phi^{-1})}{\partial r^j}(\phi(p))$$

</dd></dl>





---
---
---

# 簡単な多様体

##### $0$ 次元多様体

・$0$次元多様体：たかだか可算な集合で、離散位相が入る。

 - $\bm{R}^0=\{0\}$

---

# $C^∞$ 写像

##### $f:R^n→ R^m$

・開集合 $U_1\subset U_2\subset \bm{R}^n$、$C^{\infty}$ 写像 $f:U\to \bm{R}^m$ とする。
 このとき、$f|_{U_1}:U_1\to \bm{R}^n$ は $C^{\infty}$

        ・C^n、C^ωも同様。

- 開集合 $U_1\subset\bm{R}^m,\  U_2\subset \bm{R}^n$、$C^{\infty}$ 写像 $f:U_1\to \bm{R}^{n'},\ g:U_2\to\bm{R}^{m'}$ とする。
 このとき、$f\times g:U_1\times U_2\to \bm{R}^{n'+m'}$ は $C^{\infty}$

        ・C^n,C^mでは小さい方にまとめられる。
        ・C^ωでも同様に成り立つ。（関係ない引数の係数は0）

 ---

 ##### $f:M→R$

  ・

