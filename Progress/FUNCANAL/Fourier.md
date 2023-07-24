# フーリエ解析

## フーリエ級数

・
$$f(x)=\sum c_ke^{ik\omega x},\quad c_k=\int_{-l}^{l}f(t)e^{-ik\omega t}dt \\\ \\ (\omega=\frac{\pi}{l},\ f{は}2l{周期})$$

##### 実関数でのフーリエ級数展開
$$f(x)=\frac{a_0}{2}+\sum_{k\ge 1}a_k\cos(k\omega x)+b_k\sin(k\omega x),\quad a_k=\frac{1}{l}\int_{-l}^lf(t)\cos k\omega t$$

---

・コサイン型：
$f(x)=C_0+\sum_{k\ge1}C_k\cos(k\omega x-\theta_k)\\\ \\
C_k=\sqrt{|a_k|^2+|b_k|^2},\ \cos\theta_k=\frac{a_k}{C_k}$

→サイン型：
$f(x)=C_0+\sum_{k\ge1}C_k\sin(k\omega x+\phi_k)\\\ \\
C_k=\sqrt{|a_k|^2+|b_k|^2},\ \sin\phi_k=\frac{a_k}{C_k}$

---


## $L^p(R^n)$、$L^p(\bm{T})$

#### フーリエ級数

##### フーリエ変換
$$F(k)=\int_{\bm{R}^n}f(x)e^{-ik\cdot x}dx$$


・逆変換：$f(x)=\frac{1}{(2\pi)^n}\int_{\bm{R}^n}F(k)e^{ik\cdot x}dk$