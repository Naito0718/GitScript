# 特殊関数

## シュツルムーリウビル型微分方程式

---

##### エルミート多項式　$H_n(x)=(-1)^ne^{x^2}\frac{d^n}{dx^n}(e^{-x^2})\quad (x\in\bm{R})$

・$H_n(x)=\sum_{n=0}^{[N/2]}(-1)^n\frac{N!}{n!(N-2n)!}(2x)^{N-2n}$

・母関数$F(t,x)=e^{2tx-t^2}$

---
・$H_n''(x)-2xH_n'(x)+2nH_n(x)=0+$
・$H_{n+1}'(x)=2(n+1)H_n(x)$
・$H_n'(x)=2xH_n(x)-H_{n+1}(x)$

・$\frac{d}{dx}(e^{-x^2}\frac{d}{dx}H_n(x))+2ne^{-x^2}H_n(x)=0$

---
・$H_{n+2}(x)-2xH_{n+1}(x)+2(n+1)H_n(x)=0$

---
・$\int_{-\infty}^{\infty}H_m(x)H_m(x)e^{-x^2}dx=\sqrt{\pi}2^nn!\delta_{mn}$

---
・$H_n(-x)=(-1)^nH_n(x)$
・$H_{n}(x)$は、$n$が偶数ならば偶数乗からなる多項式で、奇数ならば奇数乗からなる多項式

・$H_0(x)=1$
・$H_1(x)=2x$
・$H_2(x)=4x^2-2$
・$H_3(x)=8x^3-12x$
・$H_4(x)=16x^4-48x^2+12$


---

##### ルジャンドル多項式$P_n(x)=\frac{1}{2^nn!}\frac{d^n}{dx^n}(x^2-1)^n\quad (x\in[-1,1])$

・$P_n(x)=\sum_{n=0}^{[N/2]}(-1)^n\frac{(2N-2n)!}{n!(N-2n)!(N-n)!2^N}x^{N-2n}$

・母関数$F(t,x)=\frac{1}{\sqrt{1-2tx+t^2}}$

---
・$(1-x^2)P_n'(x)=(n+1)xP_n(x)-(n+1)P_{n+1}(x)$
・$(1-x^2)P_n'(x)=-nxP_n(x)+nP_{n-1}(x)$

    ・(1-x^2)d/dx-(n+1)x　は上昇演算子→(-n+1)P_{n+1}
    ・(1-x^2)d/dx+nx　は下降演算子→nP_{n-1}

・$\frac{d}{dx}((1-x^2)\frac{d}{dx}P_n(x))+n(n+1)P_n(x)=0$

---
・$(n+2)P_{n+2}(x)-(2n+3)xP_{n+1}(x)+(n+1)P_n(x)=0$

---
???・$\int_{-\infty}^{\infty}H_m(x)H_m(x)e^{-x^2}dx=\sqrt{\pi}2^nn!\delta_{mn}$

---
・$P_n(-x)=(-1)^nP_n(x)$
・$P_{n}(x)$は、$n$が偶数ならば偶数乗からなる多項式で、奇数ならば奇数乗からなる多項式

・$P_0(x)=1$
・$P_1(x)=x$
・$P_2(x)=\frac{1}{2}(3x^2-1)$
・$P_3(x)=8x^3-12x$
・$P_4(x)=\frac{1}{8}(35x^4-30x^2+3)$

・$P_n(1)=1,\ P_n(-1)=(-1)^n$
・$P_n'(1)=$

---

##### ルジャンドル陪関数$P_{l}^m(x)=\frac{1}{2^ll!}(1-x^2)^{m/2}\frac{d^{l+m}}{dx^{l+m}}(x^2-1)^l\quad(-l \le m\le l)$

    ・mが範囲外だと意味がない式になる

・$$P_l^m(x)=\begin{cases}P_l(x) & (m=0) \\ \frac{(l+m!)}{2^ll!}(1-x^2)^{m/2}\sum_{l\ge r\ge m}\binom{l}{r}\binom{l}{r-m}(x+1)^{r-m}(x-1)^{l-r} & (m>0) \\ P_l^m(x)=(1-x)^{m/2}\frac{d^m}{dx^m}P_l(x) & (m<0) \end{cases}$$

---
・$(1-x^2)P_l^{m'}(x)=-mxP_l^m(x)+\sqrt{1-x^2}P_l^{m+1}(x)$
・$(1-x^2)P_l^{m'}(x)=mxP_n(x)-(l+m)(l-m+1)\sqrt{1-x^2}P_l^{m-1}(x)$

    ・(1-x^2)d/dx+mx　は上昇演算子→√[1-x^2]P_l^{m+1}
    ・(1-x^2)d/dx-mx　は下降演算子→-(l+m)(l-m+1)√[1-x^2]P_l^{m-1}

・$\frac{d}{dx}((1-x^2)\frac{d}{dx}P_l^m(x))+[l(l+1)-\frac{m^2}{1-x^2}]P_l^m(x)=0$
・$[\frac{1}{\sin\theta}\frac{d}{d\theta}(\sin\theta)\frac{d}{d\theta}+l(l+1)-\frac{m^2}{\sin^2\theta}]P_l^m(\cos\theta)=0$

---
・$(n+2)P_{n+2}(x)-(2n+3)xP_{n+1}(x)+(n+1)P_n(x)=0$

---
???・$\int_{-\infty}^{\infty}H_m(x)H_m(x)e^{-x^2}dx=\sqrt{\pi}2^nn!\delta_{mn}$

---
・$P_l^m(-x)=(-1)^{l+m}P_l^m(x)$

・$P_l^{l}(x)=\frac{(2l)!}{2^ll!}(1-x^2)^{l/2},\ P_l^{-l}=\frac{(-1)^l}{2^ll!}(1-x^2)^{l/2}$

・$l=0$
$P_0^0(x)=1$

・$l=1$
$P_1^0(x)=x$
$P_1^1(x)=\sqrt{1-x^2}$

・$l=2$
$P_2^0(x)=\frac{1}{2}(3x^2-1)$
$P_2^1(x)=3x\sqrt{1-x^2}$
$P_2^2(x)=3(1-x^2)$

・$l=3$
$P_3^0(x)=8x^3-12x$

・$l=4$
$P_4^0(x)=\frac{1}{8}(35x^4-30x^2+3)$

・$P_n(1)=1,\ P_n(-1)=(-1)^n$
・$P_n'(1)=$

---

##### ラゲール多項式$L_n(x)=e^x\frac{d^n}{dx^n}(x^ne^{-x})\quad (x\in[0,\infty))$

---

##### ソニン多項式

---

##### ラゲール陪多項式

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

---

## 球面調和関数 
##### $$Y_{lm}(\theta,\phi)=(-1)^m\sqrt{\frac{2l+1}{4\pi}\frac{(l-m)!}{(l+m)!}}P_{l}^m(\cos\theta)e^{im\phi}$$
$(P_l^m{はルジャンドル陪関数},\theta\in[0,\pi],\phi\in[0,2\pi],\ -m\le l\le m\  {は整数},\ l=0,1,2,...)$

---
・$Y_{l,-m}(\theta,\phi)=(-1)^mY_{lm}(\theta,\phi)^*$
・$Y_{lm}(\pi-\theta,\phi+\pi)=(-1)^lY_{lm}(\theta,\phi)$

    ・ベクトルを反転

・$l=1$
$Y_{00}=\frac{1}{\sqrt{4\pi}}$

・$l=1$
$Y_{11}=-\sqrt{\frac{3}{8\pi}}\sin\theta\  e^{i\phi}$
$Y_{10=}=\sqrt{\frac{3}{4\pi}}\cos\theta$
$Y_{1,-1}=\sqrt{\frac{3}{8\pi}}\sin\theta\  e^{-i\phi}$

・$l=2$
$Y_{22}=\sqrt{\frac{5}{96\pi}}3\sin^2\theta \ e^{2i\phi}$
$Y_{21=}=-\sqrt{\frac{5}{24\pi}}3\sin\theta\cos\theta\  e^{i\phi}$
$Y_{20=}=\sqrt{\frac{5}{4\pi}}\frac{1}{2}(3\cos^2\theta-1)$
$Y_{2,-1}=$
$Y_{2,-2}=$
