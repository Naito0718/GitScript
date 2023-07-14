# 複素解析

##### 除去可能特異点

##### 無限遠点

・$\infty$で正則、$g(z)=f(\frac{1}{z})$が$z=0$で正則

    ・有理式Q=P/Qは、degQ≧degPならば∞で正則

##### 回転数$n(C,z)$

・円板$D(a,R)>0$の正の向きの周

    ・円板でn(C,z)=1、円外部でn(C,z)=0

・領域$D$を囲むサイクル$C:n(C,a)=(1\ (a\in D),0\ (a\in D^c-C))$かつ$C\cap D=\phi$

    ・円板、長方形領域はその周で囲まれる
    ・囲まれるとき、$D^b\subset S_pC$、等号は一般に成り立たない

・回転数計算は分割して考えてよい！

---
## ローラン展開

## コーシーの定理

・領域$D$上で正則な$f:D\to\bm{C}$において、任意の$D$内のホモローグ$0$のサイクル$C$に対して、$\int_Cfdz=0$
・このとき、$n(C,a)f(a)=\frac{1}{2\pi i}\int_C \frac{f(z)}{z-a}dz\ (\forall a\in D-C)$


・領域$D$上で正則な$f:D\to\bm{C}$において、$D$が単一連結ならば、任意の$D$内の区分的$C^1$閉曲線$C$に対して、$\int_Cfdz=0$

    ・$D$が単一連結：D内の任意の区分的C^1閉曲線がホモローグ0
    ・単一連結⇔単連結

## 留数定理

### 種々の表示

・$\int_{0}^{2\pi}\log(1-2r\cos t+r^2)dt=(0\ (0\le r\le1),4\pi\log r\ (1<r))$

    ・0~πまでの積分値の2倍
・$\int_0^{\pi/2}\log\sin\theta d\theta=-\frac{\pi}{2}\log2$

#### 特殊関数

##### エルミート多項式　$H_n(x)=(-1)^ne^{x^2}\frac{d^n}{dx^n}(e^{-x^2})\quad (x\in\bm{R})$

・$H_n(x)=\sum_{n=0}^{[N/2]}(-1)^n\frac{N!}{n!(N-2n)!}(2x)^{N-2n}$

・母関数$F(t,x)=e^{2tx-t^2}$

---
・$H_n''(x)-2xH_n'(x)+2nH_n(x)=0+$
・$H_{n+1}'(x)=2(n+1)H_n(x)$
・$H_n'(x)=2xH_n(x)-H_{n+1}(x)$

・$\frac{d}{dx}(e^{-x^2}\frac{d}{dx}H_n(x))+2ne^{-x^2}H_n(x)=0$

---
・$H_{n+2}(x)-2xH_{n+1}(x)+2nH_n(x)=0$

---
・$\int_{-\infty}^{\infty}H_m(x)H_m(x)e^{-x^2}dx=\sqrt{\pi}2^nn!\delta_{mn}$

---
・$H_n(-x)=(-1)^nH_n(x)$

・$H_0(x)=1$
・$H_1(x)=2x$
・$H_2(x)=4x^2-2$
・$H_3(x)=8x^3-12x$
・$H_4(x)=16x^4-48x^2+12$


---

##### 第一種チェビシェフ多項式　$T_n(x)=\cos (n\cos^{-1}x)\quad (x\in[-1,1])$

・$\cos n\theta=\cos^n\theta-\binom{n}{2}\cos^{n-2}\sin^2\theta+\binom{n}{4}\cos^{n-4}\sin^4\theta-...$
・$\cos(n+2)\theta=2\cos\theta\cos (n+1)\theta-\cos n\theta$
・$\cos^{-1}(-x)=\pi-x$

---

・母関数$F(t,x)=\frac{1-tx}{1-2tx+t^2}$
・$\frac{1-r^2+2i\sin\theta}{1-2r\cos\theta+r^2}=1+2\sum_{n\ge1}r^n(\cos n\theta+i\sin n\theta)\quad (|z|<1,z=re^{i\theta})$

---

・$(1-x^2)T''_n(x)-xT_n'(x)+n^2T_n(x)=0$

---

・$T_{n+2}-2xT_{n+1}+T_n(x)=0$

---

・$\int_{-1}^{1}\frac{T_m(x)T_n(x)}{\sqrt{1-x^2}}dx=(0\ (m\neq n)),\ \pi/2\ (m=n>0),\ \pi\ (n=m=0)$

---
・$T_n(-x)=(-1)^nT_n(x)$

・$T_0(x)=1$
・$T_1(x)=x$