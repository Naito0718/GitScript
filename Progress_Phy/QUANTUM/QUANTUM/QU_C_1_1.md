- [一次元ポテンシャルの一般的な性質](#一次元ポテンシャルの一般的な性質)
  - [対称なポテンシャル](#対称なポテンシャル)
- [段差ポテンシャルに向かって進む粒子](#段差ポテンシャルに向かって進む粒子)
  - [$E＞W, E＞0$ かつ物理的描像を考慮したとき](#ew-e0-かつ物理的描像を考慮したとき)
    - [反射率と透過率](#反射率と透過率)
  - [$E=W＞0$ のとき](#ew0-のとき)
  - [$0＜E＜W$ かつ束縛状態であるとき](#0ew-かつ束縛状態であるとき)
    - [反射率と透過率](#反射率と透過率-1)
- [対称ではない隆起型ポテンシャルに向かって進む粒子](#対称ではない隆起型ポテンシャルに向かって進む粒子)
  - [$E＞W,E＞0$ のとき](#ewe0-のとき)
    - [反射率と透過率](#反射率と透過率-2)
  - [$E=W＞0$ のとき](#ew0-のとき-1)
  - [$W＞E＞0$ のとき](#we0-のとき)
    - [反射率と透過率](#反射率と透過率-3)
- [有限深さの対称な井戸型ポテンシャル](#有限深さの対称な井戸型ポテンシャル)
  - [$0＞E＞-W$ かつ束縛状態であるとき](#0e-w-かつ束縛状態であるとき)
    - [偶パリティ解](#偶パリティ解)
      - [実際に取りうる値](#実際に取りうる値)
    - [奇パリティ解](#奇パリティ解)
- [崖にある井戸型型ポテンシャル](#崖にある井戸型型ポテンシャル)



# 一次元ポテンシャルの一般的な性質

    ・境界条件は、端での等号と微分値の等号！

<dl><dt>

・系を一次元とし、系のポテンシャル $V(x)$、系のエネルギー $E$ とする。また、粒子の質量 $m$、波動関数 $\phi(x)$ とする。
このとき、解くべき方程式：
$$\left\{-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V(x)\right\}\phi(x)=E\phi(x)$$


</dt><dd>

- エネルギー準位は縮退していない。すなわち、同じエネルギーをもつ波動関数 $\phi_1(x),\ \phi_2(x)$ に対して、$\exist C\in\bm{C}$ であって、
$$\phi_1(x)=C\phi_2(x)\\\ \\$$


<br>

- 

</dd></dl>

## 対称なポテンシャル

・系を一次元とし、系のポテンシャル $V(x)$、系のエネルギー $E$ とする。また、粒子の質量 $m$、波動関数 $\phi(x)$ とする。
このとき、
$$V(x)=V(-x)\Rightarrow\phi(x)=\phi(-x)\text{ または }\phi(-x)=-\phi(x)$$

    ・任意定数が実数でないと無理...別の量子力学の本に書いてあったはず。解析力学シリーズのやつ。
<br>

- 奇関数 $f$、$0$ で微分可能な偶関数 $g$ とする。
このとき、
$$f(0)=0,\quad f'(0)=0$$


---

# 段差ポテンシャルに向かって進む粒子

・ポテンシャル $V(x)$：$$V(x)=\begin{cases}
0 & (x<0)   \\
W & (x>0)\\
\end{cases}$$ とし、質量 $m$ の粒子が左から入射するとする。

## $E＞W, E＞0$ かつ物理的描像を考慮したとき

波動関数 $\psi:$
$$\psi(x,t)=\phi(x)e^{-i\frac{E}{\hbar}t}\\\ \\
\phi(x)=\begin{cases}
Ae^{ikx}+\frac{k-\kappa}{k+\kappa}Ae^{-ikx}   & (x<0) \\
\frac{2k}{k+\kappa}Ae^{i\kappa x}    & (x>0) \\
\end{cases}\\\ \\
k=\sqrt{\frac{2mE}{\hbar^2}},\ \kappa=\sqrt{\frac{2m(E-W)}{\hbar^2}}\\\ \\$$

- フラックス：
$$j(x,t)=\begin{cases}
\frac{\hbar k}{m}(|A|^2-|B|^2) & (x<0)    \\
\frac{\hbar\kappa}{m}|C|^2   & (x>0) \\
\end{cases}$$

      ・A,B,Cはそれぞれの項の任意定数。t成分は消える。

---

### 反射率と透過率

・反射率、透過率 $R,T$：
$$R=\frac{|B|^2}{|A|^2}=\frac{(k-\kappa)^2}{(k+\kappa)^2}\\\ \\
T=\frac{\kappa}{k}\frac{|C|^2}{|A|^2}=\frac{4k\kappa}{(k+\kappa^2)}\\\ \\
R+T=1$$

    ・透過率とかってちゃんとフラックス出さないといけない！？
    ・量子効果：反射率が0でない。

---

・$E>>W$ ならば、$\kappa\to k,\ R\to 0$
これは直感と一致する。
<br>

- $E\to W$ ならば、$\kappa\to 0,\ T\to 0$

---

## $E=W＞0$ のとき

・$x>0$ の範囲で波でなくなる。また、$E\to W$ からの推測より、$x>0$ で $\phi(x)=0$

    ・というか無限飛ばせば0になるから、定数でしかも $D=0$ か。
    ・しかも $A=B=0$ になっちゃうな。

---

## $0＜E＜W$ かつ束縛状態であるとき

波動関数 $\psi:$
$$\psi(x,t)=\phi(x)e^{-i\frac{E}{\hbar}t}\\\ \\
\phi(x)=\begin{cases}
Ae^{ikx}+\frac{k-i\kappa}{k+i\kappa}Ae^{-ikx}   & (x<0) \\
\frac{2k}{k+i\kappa}Ae^{-\kappa x}    & (x>0) \\
\end{cases}\\\ \\
k=\sqrt{\frac{2mE}{\hbar^2}},\ \kappa=\sqrt{\frac{2m(W-E)}{\hbar^2}}\\\ \\$$

- フラックス：
$$j(x,t)=\begin{cases}
\frac{\hbar k}{m}(|A|^2-|B|^2) & (x<0)    \\
0   & (x>0) \\
\end{cases}$$

      ・A,B,Cはそれぞれの項の任意定数。t成分は消える。

---

### 反射率と透過率

・反射率、透過率 $R,T$：
$$R=\frac{|B|^2}{|A|^2}=1\\\ \\
T=0\\\ \\
R+T=1$$

    ・染み出しはあるが、透過率は0。
    ・E=Wのときの極限の結果と整合する。

---

# 対称ではない隆起型ポテンシャルに向かって進む粒子

・ポテンシャル $V(x)$：$$V(x)=\begin{cases}
0 & (x<0)   \\
W & (0<x<a)\\
0 & (a<x)
\end{cases}$$ とし、質量 $m$ の粒子が左から入射するとする。

---

## $E＞W,E＞0$ のとき

このとき、波動関数 $\psi:$
$$\psi(x,t)=\phi(x)e^{-i\frac{E}{\hbar}t}\\\ \\
\phi(x)=\begin{cases}
Ce^{ika}\left(\left[\cos(\kappa a)-i\frac{k^2+\kappa^2}{2k\kappa}\sin(\kappa a)\right]e^{ikx}+\left[i\frac{(\kappa^2-k^2)}{2k\kappa}\sin(\kappa a)\right]e^{-ikx}\right) & (x<0)    \\
C\frac{e^{ika}}{2\kappa}\left(\frac{(\kappa+k)}{e^{i\kappa a}}e^{i\kappa x}+\frac{(\kappa-k)}{e^{-i\kappa a}}e^{-i\kappa x}\right) & (0<x<a)   \\
Ce^{ikx} & (a<x)   \\
\end{cases}\\\ \\
k=\sqrt{\frac{2mE}{\hbar^2}},\quad\kappa=\sqrt{\frac{2m}{\hbar^2}(E-W)}$$


- フラックス：
$$j(x)=\begin{cases}
\frac{\hbar k}{m}(|A|^2-|B|^2) & (x<0)    \\
\frac{\hbar \kappa}{m}(|C|^2-|D|^2)   & (0<x<a) \\
\frac{\hbar k}{m}|F|^2   & (x>0) \\
\end{cases}$$

      ・A,B,C,D,Fはそれぞれの項の任意定数。t成分は消える。

---

### 反射率と透過率

<dl><dt>

・反射率、透過率 $R,T$：
$$R=\frac{|B|^2}{|A|^2}=\frac{(\kappa^2-k^2)\sin^2(\kappa a)}{4k^2\kappa^2+(k^2-\kappa^2)^2\sin^2(\kappa a)}=\frac{W^2\sin^2(\kappa a)}{4E(E-W)+W^2\sin^2(\kappa a)}\\\ \\
T=\frac{|F|^2}{|A|^2}=\frac{4k^2\kappa^2}{4k^2\kappa^2+(k^2-\kappa^2)^2\sin^2(\kappa a)}=\frac{4E(E-W)}{4E(E-W)+W^2\sin^2(\kappa a)}\\\ \\
R+T=1$$

    ・フラックス的にこれで正しい。
    ・量子効果：反射率が0でない。

</dt><dd>

- $$R=0,T=1\iff \kappa a=n\pi>0\ \ (n=1,2,...)\\\ \\$$

- $E>>W$ ならば、$R\to 0$
これは直感と一致する。

      ・E→Wなら不定形になっちゃう。

</dd></dl>

---

## $E=W＞0$ のとき

---

## $W＞E＞0$ のとき

このとき、波動関数 $\psi:$
$$\psi(x,t)=\phi(x)e^{-i\frac{E}{\hbar}t}\\\ \\
\phi(x)=\begin{cases}
C\frac{e^{ika}}{ik\kappa}\left(\frac{(k^2-\kappa^2)\sinh(\kappa a)+2ik\kappa\cosh(\kappa a)}{2}e^{ikx}+\frac{(k^2+\kappa^2)}{2}\sinh(\kappa a)e^{-ikx}\right) & (x<0)    \\
C\frac{e^{ika}}{2\kappa}\left(\frac{(\kappa+ik)}{e^{\kappa a}}e^{\kappa x}+\frac{(\kappa-ik)}{e^{-\kappa a}}e^{-\kappa x}\right) & (0<x<a)   \\
Ce^{ikx} & (a<x)   \\
\end{cases}\\\ \\
k=\sqrt{\frac{2mE}{\hbar^2}},\quad\kappa=\sqrt{\frac{2m}{\hbar^2}(W-E)}$$

    ・a<x領域では左向きの波はない。
    ・Cは任意定数。連立方程式は上下の式を足し引きする！

- フラックス：
$$j(x)=\begin{cases}
\frac{\hbar k}{m}(|A|^2-|B|^2) & (x<0)    \\
\frac{\hbar \kappa}{m}(C\overline{D}-\overline{C\overline{D}})   & (0<x<a) \\
\frac{\hbar k}{m}|F|^2   & (x>0) \\
\end{cases}$$

      ・A,B,C,D,Fはそれぞれの項の任意定数。t成分は消える。

---

### 反射率と透過率


- 反射率 $R$、透過率 $T$ はそれぞれ、
$$R=\\\ \\
T=\frac{4k^2\kappa^2}{(k^2+\kappa^2)\sinh^2(\kappa a)+4k^2\kappa^2}$$

      ・絶対値を取る時分母にある複素数は、有理化して消す！

---

# 有限深さの対称な井戸型ポテンシャル

    ・井戸型ならE<0が許される！？

$$V=\begin{cases}
-W & (|x|< a)   \\
0 & (|x|>a)    \\
\end{cases}$$とし、質量 $m$ の粒子が左から入射するとする。

---

## $0＞E＞-W$ かつ束縛状態であるとき

### 偶パリティ解

・偶パリティ解：
$$\phi(x)=\begin{cases}
B\cos kx & (|x|<a)    \\
B\cos (ka)e^{\kappa a}e^{-\kappa|x|} & (|x|>a)    \\
\end{cases}\\\ \\
k=\sqrt{\frac{2m}{\hbar^2}(E+V_0)},\quad \kappa=\sqrt{-\frac{2m}{\hbar^2}E}\\\ \\
k\tan(ka)=\kappa\\\ \\$$

---

#### 実際に取りうる値

- $\xi=ka>0,\quad\eta=\kappa a>0$ とする。
このとき、
$$\xi^2+\eta^2=R^2,\ \eta=\xi\tan\xi\\\ \\
\left(R=\sqrt\frac{2mV_0a^2}{\hbar^2}\right)$$
したがって、上記の第一象限における円と $\tan$ 関数の交点における $(\xi,\eta)$ の交点が実際に取りうる値。
の交点で解が与えられる。

→$0<R<\pi k\quad(k=1,2,...)$に対して、
定常状態の数：$k$個、$k$番目の状態が$0$を切る点：$k-1$個

---

### 奇パリティ解

・奇パリティ解：
$$\phi(x)=\begin{cases}
-B\sin(ka)e^{\kappa a}e^{\kappa x} & (a<x)\\
B\sin kx & (|x|<a)    \\
B\sin(ka)e^{\kappa a}e^{-\kappa x} & (a<x)    \\
\end{cases}\\\ \\
k=\sqrt{\frac{2m}{\hbar^2}(E+V_0)},\quad \kappa=\sqrt{-\frac{2m}{\hbar^2}E}\\\ \\
\kappa\tan(ka)=-k$$




# 崖にある井戸型型ポテンシャル
$$V=\begin{cases}
\infty & (x=0)    \\
-V_0 & (0<x< a)   \\
0 & (x>a)    \\
\end{cases}$$

→$a<0$：$\phi(x)=0$

---
・解
$$\phi(x)=\begin{cases}
0 & (x<0)    \\
C\sin kx & (0<x<a)    \\
\phi(x)=De^{-\kappa x} & (a<x)  \\
\end{cases}\\\ \\
k^2=\frac{2m}{\hbar^2}(E+V_0),\quad \kappa^2=-\frac{2m}{\hbar^2}E\\\ \\
C\sin ka=De^{-\kappa a},\quad k\tan(ka+\frac{\pi}{2})=\kappa,\quad k^2+\kappa^2=\frac{2mV_0}{\hbar^2} $$

    ・規格化したら係数決定できそうではある

→$-V_0<E<0$

    ・有界条件

---

・別の形：$$\xi^2+\eta^2=R^2,\ \eta=\xi\tan(\xi+\frac{\pi}{2})\\\ \\
R=\sqrt\frac{2mV_0a^2}{\hbar^2},\ \xi=ka>0,\ \eta=\kappa a>0$$
の交点で解が与えられる。

→$R>\pi/2$：$V_0>\frac{1}{2m}(\frac{\hbar\pi}{2a})^2$を満たさないと解は存在しない

→$\frac{\pi}{2}<R<\frac{\pi}{2}(2k+1)\quad(k=1,2,...)$に対して、
定常状態の数：$k$個、$k$番目の状態が$0$を切る点：$k-1$個

    ・ノード、節点ともいう

---

