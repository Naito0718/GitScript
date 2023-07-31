- [量子力学的な系、計算](#量子力学的な系計算)
  - [自由粒子](#自由粒子)
  - [時間依存しない、束縛状態での一次元波動関数](#時間依存しない束縛状態での一次元波動関数)
        - [ロンスキアン：](#ロンスキアン)
        - [対称ポテンシャル $V(-x)=V(x)$](#対称ポテンシャル-v-xvx)
        - [振動定理](#振動定理)
  - [一次元の簡単なポテンシャル](#一次元の簡単なポテンシャル)
        - [崖にある井戸型型ポテンシャル](#崖にある井戸型型ポテンシャル)
        - [対称な井戸型ポテンシャル](#対称な井戸型ポテンシャル)
        - [デルタ関数型ポテンシャル](#デルタ関数型ポテンシャル)
  - [一次元でのポテンシャル散乱](#一次元でのポテンシャル散乱)
        - [階段型ポテンシャル](#階段型ポテンシャル)
        - [非対称な井戸型ポテンシャル](#非対称な井戸型ポテンシャル)
  - [一次元調和振動子](#一次元調和振動子)
        - [演算子法](#演算子法)
        - [波動関数表示（Hermite多項式）](#波動関数表示hermite多項式)
  - [二次元調和振動子](#二次元調和振動子)
  - [外部磁場中にある電子（$1/2$スピン）](#外部磁場中にある電子12スピン)
    - [スピン歳差運動](#スピン歳差運動)
        - [回転と交換関係](#回転と交換関係)
        - [時間発展と期待値：](#時間発展と期待値)
  - [ガウスの波束](#ガウスの波束)


# 量子力学的な系、計算

## 自由粒子

・ポテンシャルなし（ハイゼンベルグ表示）

    ・古典粒子と同じ
    ・初期値とt秒後の位置に関する不確定性関係

・ポテンシャルあり（解析的関数）（ハイゼンベルグ表示）

    ・古典粒子と同じ、運動方程式、速度と運動量の関係
    ・期待値取ればシュレディンガー表示でも成り立つ（エーレンフェストの定理）

## 時間依存しない、束縛状態での一次元波動関数
$$\left(-\frac{\hbar^2}{2m}\frac{d}{dx}+V(x)\right)\phi(x,t)=E\phi(x)\\\ \\
\psi(x,t)=\phi(x)e^{-i\frac{E}{\hbar}t,},\quad \lim_{|x|\to\infty}|\phi(x)|=0$$

##### ロンスキアン：
$$W=\begin{vmatrix}
\phi_1 & \frac{d\phi_1}{dx} \\
\phi_2 & \frac{d\phi_2}{dx} \\
\end{vmatrix}
=const=0$$

→縮退は存在しない

    ・もし同じエネルギー固有値を持つならば同じ状態

→$\phi(x)$は実関数に取ることができる

    ・規格化定数に吸収できる

→$d\phi/dx,\phi$は常に連続

    ・V(x)は有界とした

---

##### 対称ポテンシャル $V(-x)=V(x)$

・このとき、$\phi(-x)$も解となる

→$\phi(-x)=\pm\phi(x)$：よって、必ず解は偶関数または奇関数

    ・φ(-x)も実関数


##### 振動定理

・

---

## 一次元の簡単なポテンシャル

##### 崖にある井戸型型ポテンシャル
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

##### 対称な井戸型ポテンシャル
$$V=\begin{cases}
-V_0 & (|x|< a)   \\
0 & (|x|>a)    \\
\end{cases}$$

---

・偶パリティ解：
$$\phi(x)=\begin{cases}
B\cos kx & (|x|<a)    \\
Ce^{-\kappa|x|} & (|x|>a)    \\
\end{cases}\\\ \\
k^2=\frac{2m}{\hbar^2}(E+V_0),\quad \kappa^2=-\frac{2m}{\hbar^2}E\\\ \\
B\cos ka=Ce^{-\kappa a},\quad k\tan(ka)=\kappa$$

→別の形：
$$\xi^2+\eta^2=R^2,\ \eta=\xi\tan\xi\\\ \\
R=\sqrt\frac{2mV_0a^2}{\hbar^2},\ \xi=ka>0,\ \eta=\kappa a>0$$
の交点で解が与えられる。

→$0<R<\pi k\quad(k=1,2,...)$に対して、
定常状態の数：$k$個、$k$番目の状態が$0$を切る点：$k-1$個

---

・奇パリティ解

---

##### デルタ関数型ポテンシャル
$$V(x)=-V_0\delta(x)$$

・解：$\phi(x)=\sqrt{\kappa}e^{-\kappa|x|}$

→$\lim_{\epsilon\to0}[\frac{d\phi}{dx}|_{\epsilon}-\frac{d\phi}{dx}|_{-\epsilon}]=-\frac{2mV_0}{\hbar^2}\phi(0)=-2C\kappa$

    ・φが偶関数であることはわかってる（0以外でφ計算）

---

## 一次元でのポテンシャル散乱

##### 階段型ポテンシャル

##### 非対称な井戸型ポテンシャル

---

## 一次元調和振動子

##### 演算子法

    ・ハミルトニアンH
    ・消滅演算子、生成演算子、個数演算子、H=hω(N+1/2)

---

##### 波動関数表示（Hermite多項式）



---

## 二次元調和振動子



---

## 外部磁場中にある電子（$1/2$スピン）

    ・フィルターに着く途中の位置を測定しようとすればまた変わる

・ヒルベルト空間は二次元：$\ket{\alpha}=c_+\ket{+}+c_-\ket{-}$

→$z$方向：
$$S_z=\frac{\hbar}{2}\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$$

- $\ket{+}=(1,0)$

---

・$x$方向：$\ket{S_x,\pm}=\frac{1}{\sqrt{2}}\ket{+}\pm\frac{1}{\sqrt{2}}\ket{-}$
- $$S_x=\frac{\hbar}{2}\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$$

- $y$方向：$\ket{S_y,\pm}=\frac{1}{\sqrt{2}}\ket{+}\pm\frac{i}{\sqrt{2}}\ket{-}$
- $$S_y=\frac{\hbar}{2}\begin{pmatrix}0 & -i \\ i & 0\end{pmatrix}$$

        ・右手系を用いた
        ・基準としてS_xの行列要素を正に指定した

---

・交換関係：$[S_i,S_j]=\epsilon_{ijk}i\hbar S_k$

- 反交換関係：$\{S_i,S_j\}=\frac{1}{2}\hbar^2\delta_{ij}$

- 二乗演算子 $S^2=S_{i}S_i=\frac{3}{4}\hbar^2$
-  $[S^2,S_i]=0$

---

・期待値：

---

・昇降演算子：$S_+=\hbar\ket{+}\bra{-},\ S_-=\hbar\ket{-}\bra{+}$

    ・スピンを上げ下げする

→$$S_+=\hbar\begin{pmatrix}0 & 1 \\ 0 & 0\end{pmatrix},\quad S_-=\hbar\begin{pmatrix}0 & 0 \\ 1 & 0\end{pmatrix}$$

→$S_{\pm}=S_x\pm iS_y$

---

### スピン歳差運動

・外部磁場 $B(x)$ 中の磁気モーメント $\frac{e\hbar}{2m_ec}$ を持つ一個のスピン$1/2$ 系

- ハミルトニアン：$H=-\frac{e}{m_ec}S\cdot B(x)$

    ・磁気回転比gが着くかもしれないが、定数倍の差しかしない
    ・普通に磁気モーメントから導ける式

---

・$B=Be_z$のとき：$H=\omega S_z,\quad \omega=\frac{|e| B}{m_ec},\quad(e<0)$

- エネルギー固有値：$E_{\pm}=\pm \omega\frac{\hbar}{2},\quad(\ket{\pm})$

- 明らかに $H$ と $S_z$ は交換する
- エネルギー固有値の差：$\hbar\omega$
- 時間発展演算子：$\mathcal{U}(t,0)=\exp(\frac{-i\omega S_zt}{\hbar})$

---

##### 回転と交換関係

・$z$軸周りの回転 $\mathcal{D}_z(\phi)=\exp(\frac{-iS_z\phi}{\hbar})$

---

##### 時間発展と期待値：
$$c_+\ket{+}+c_-\ket{-}\to c_+\exp\left(\frac{-i\omega t}{2}\right)\ket{+}+c_-\exp\left(\frac{i\omega t}{2}\right)\ket{-}$$

- $\ket{+}\to\exp(\frac{-i\omega t}{2})\ket{+}$ したがって $\ket{\pm}$ は向きを変えない

        ・定常状態だからそりゃそう

・$\ket{S_x;+}=\frac{1}{\sqrt{2}}\ket{+}+\frac{1}{\sqrt{2}}\ket{-}$

- 時間発展後に$\ket{S_x;\pm}$である確率：
$$|\braket{S_x;\pm|S_x;+;0\to t}|^2=\begin{cases}
\cos^2\frac{\omega t}{2} & \ket{S_x;+}   \\
\sin^2\frac{\omega t}{2} & \ket{S_x;-}   \\
\end{cases}$$

        ・z軸方向の磁場は+x方向のスピンを回転させた
        ・確かに全確率1

- $x$期待値 $\braket{S_x}_{S_x;+;t}=\frac{\hbar}{2}\cos\omega t$

        ・確かに(エネルギー差)/hで振動している

- $y$確率：$$|\braket{S_y;\pm|S_x;+;0\to t}|^2=\begin{cases}
\frac{1}{2}(1+\sin\omega t) & \ket{S_x;+}   \\
\frac{1}{2}(1-\sin\omega t) & \ket{S_x;-}   \\
\end{cases}$$
- $y$期待値 $\braket{S_y}_{S_x;+;t}=\frac{\hbar}{2}\sin\omega t$

- $z$確率：$|\braket{\pm|S_x;+;0\to t}|^2=\frac{1}{2}$
- $z$期待値：$\braket{S_z}_{S_x;+;t}=0$

---

## ガウスの波束 
$$\psi(x)=\braket{x'|\alpha}=\frac{1}{\pi^{1/4}\sqrt{d}}\exp(ikx'-\frac{x'^2}{2d^2})$$

→位置の確率密度：$|\braket{x'|\alpha}|^2=\frac{1}{d\sqrt{\pi}}\exp(-\frac{x'^2}{d^2})$

→位置の期待値：$\braket{x}=0$

→$\braket{x^2}=\frac{d^2}{2}$、よって分散$\braket{(\Delta x)^2}=\frac{d^2}{2}$

---

・運動量の期待値：$\braket{p}=\hbar k,\ \braket{p^2}=\frac{\hbar^2}{2d^2}+\hbar^2k^2$、よって分散$\braket{(\Delta p)^2}=\frac{h^2}{2d^2}$

・最小不確定波束：$\braket{(\Delta x)^2}\braket{(\Delta p)^2}=\frac{\hbar^2}{4}$

---

運動量空間$\braket{p'|\alpha}=$

---