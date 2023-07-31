
# 可測空間

##### ｓ

・$A$上の相対$\sigma$加法族：$\sigma(A)=\{A\cap E\ |\  E\in\mathfrak{M}\}$

    ・別にAは可測ではない

→Aに含まれる可測集合全体と等しい

---

・$I\subset 2^X$から生成される$\sigma-$加法族：$\sigma(I)$

    ・Iを含むσ加法族全体の共通部分

---

・直積σ加法族、直積可測空間（非可算無限）

    ・各射影は可測関数
    ・f可測⇔任意のπj◦f可測
    ・有限個のときは可測集合の直積から生成されたσ加法族と等しい（σ(A(M_1×...×M_N))）
    ・$l_k:X_k→X_1×...× X_N$は可測（一点以外を固定）

---

・自明な$\sigma$-加法族：$\{\phi,X\}$、$2^X$

---

##### Borel集合族$\mathfrak{B}$

・相対Borel集合族 $\mathfrak{B}(A)$

→部分集合による相対σ加法族 $\sigma(A)$に一致する

---

・直積Borel集合族

    ・第二可算空間の可算無限個の直積集合について、直積σ加法族＝直積位相のBorel集合族

##### 有限加法族 $\mathcal{F}$

・$\#\mathcal{F}<\infty$なる有限加法族

→このとき$\mathcal{F}$は$\sigma$-加法族



---

## Lebesgue測度

##### $\bm{R}$上のBorel集合 
$$\mathfrak{B}_{\bm{R}}=\sigma(\mathcal{O}_{\bm{R}})$$

→$\mathfrak{B}_{\bm{R}}=\sigma(\{開区間全体\})=\sigma(\{閉区間全体\})=\sigma(\{区間塊全体\})$

    ・開基の性質による

---

・$\bm{R}^n$上のBorel集合 
$$\mathfrak{B}_{\bm{R}^n}=\sigma(\mathcal{O}_{\bm{R}^n})$$

→$\mathfrak{B}_{\bm{R}^n}=\sigma(\{開区間全体\})=\sigma(\{閉区間全体\})=\sigma(\{区間塊全体\})$

    ・有限個の直積可測空間の性質

---

##### $\bm{R}$上の測度 
$$m:\mathfrak{B}_{\bm{R}}\to[0,\infty]$$

・Radon汎関数 
$$\Lambda :C_{c,\bm{R}}\to\bm{R},\quad \Lambda f=\int_I f(x)dx\quad(\mathrm{supp} f\subset I{なる任意の有界閉区間},\int{はRiemann積分})$$
に対して一意的に定まるRadon測度 $m$ のこと
