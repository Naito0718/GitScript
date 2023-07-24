# 関数解析的な具体例、計算例

## デルタ関数

##### 関係式

・$\delta(x-x')=\frac{1}{2\pi}\int e^{ik(x-x')}dk$

→$\frac{2}{\pi}\int_0^{\infty}\cos kx\cos kx'dk=\delta(x-x')+\delta(x+x')$

→$\frac{2}{\pi}\int_0^{\infty}\sin kx\sin kx'dk=\delta(x-x')-\delta(x+x')$

## フーリエ変換

### 級数展開

##### テクニック

・実関数は$\cos,\sin$で考えてよい

→偶関数→$\cos$部分、奇関数→$\sin$部分

---

##### $f(x)=x^{2p}$

→ $a^{2p}_0=\frac{2}{2p+1}\pi^{2p}$

→ $a^{2p}_k=4(-1)^k\frac{\pi^{2p-2}}{k^2}-\frac{2p(2p-1)}{k^2}a^{2p-2}_k$

---

・$p=0$

→$a_0=2,\quad a_k=0$

→フーリエ変換：$1$

---

・ $p=1$

→$a_0=\frac{2}{3}\pi^{2},\quad a_k=4(-1)^k\frac{1}{k^2}$

→フーリエ変換：$\frac{1}{3}\pi^2-4\cos x+2\cos 2x-\frac{4}{9}\cos 3x+...$


