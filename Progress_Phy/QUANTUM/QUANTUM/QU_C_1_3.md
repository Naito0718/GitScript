
- [自由粒子](#自由粒子)
  - [時間依存しない、束縛状態での一次元波動関数](#時間依存しない束縛状態での一次元波動関数)
    - [ロンスキアン：](#ロンスキアン)
        - [対称ポテンシャル $V(-x)=V(x)$](#対称ポテンシャル-v-xvx)
        - [振動定理](#振動定理)
- [デルタ関数型ポテンシャル](#デルタ関数型ポテンシャル)
- [ガウスの波束](#ガウスの波束)



# 自由粒子

・ポテンシャルなし（ハイゼンベルグ表示）

    ・古典粒子と同じ
    ・初期値とt秒後の位置に関する不確定性関係

・ポテンシャルあり（解析的関数）（ハイゼンベルグ表示）

    ・古典粒子と同じ、運動方程式、速度と運動量の関係
    ・期待値取ればシュレディンガー表示でも成り立つ（エーレンフェストの定理）

## 時間依存しない、束縛状態での一次元波動関数
$$\left(-\frac{\hbar^2}{2m}\frac{d}{dx}+V(x)\right)\phi(x,t)=E\phi(x)\\\ \\
\psi(x,t)=\phi(x)e^{-i\frac{E}{\hbar}t,},\quad \lim_{|x|\to\infty}|\phi(x)|=0$$

### ロンスキアン：
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


# デルタ関数型ポテンシャル

$$V(x)=-V_0\delta(x)$$

・解：$\phi(x)=\sqrt{\kappa}e^{-\kappa|x|}$

→$\lim_{\epsilon\to0}[\frac{d\phi}{dx}|_{\epsilon}-\frac{d\phi}{dx}|_{-\epsilon}]=-\frac{2mV_0}{\hbar^2}\phi(0)=-2C\kappa$

    ・φが偶関数であることはわかってる（0以外でφ計算）

---



# ガウスの波束 

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