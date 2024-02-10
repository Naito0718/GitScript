
- [真空中の電磁波（なにもない）](#真空中の電磁波なにもない)
  - [不変デルタ関数](#不変デルタ関数)
  - [真空中](#真空中)
  - [回折現象](#回折現象)
  - [散乱現象](#散乱現象)
- [一般の電磁波](#一般の電磁波)
  - [関数の特殊関数表示](#関数の特殊関数表示)
  - [真空中](#真空中-1)
  - [多重極放射](#多重極放射)
- [物質中の電磁波](#物質中の電磁波)
  - [誘電体中の電磁波](#誘電体中の電磁波)
  - [電磁波の反射と屈折](#電磁波の反射と屈折)
  - [導体中の電磁波](#導体中の電磁波)





# 真空中の電磁波（なにもない） 
$$\bm{\rho(x,t)=i(x,t)=0}$$

## 不変デルタ関数
・$$D(x,t)=\frac{i}{2(2\pi)^3}\int_{-\infty}^{\infty}\frac{d^3k}{\omega(k)}[e^{i(k\cdot x-\omega(k)t)}-e^{i(k\cdot x-\omega(k) t)}]$$

→$\frac{\partial D}{\partial t}(x,t)=\frac{1}{2(2\pi)^3}\int_{-\infty}^{\infty}d^3k[e^{i(k\cdot x-\omega(k)t)}+e^{i(k\cdot x-\omega(k) t)}]$

→$\frac{\partial D}{\partial t}(x,0)=\delta(x),\ D(x,0)=0$

→$(\Delta-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}) D(x,t)=0$

    ・初期条件として、0,δ(x)を与えた時の斉次波動方程式の解

---

・$$D(x,t)=\frac{1}{4\pi c}\frac{1}{r}[\delta(r-ct)-\delta(r+ct)]$$
よって、$$D_{ret}(x-x',t-t')=\frac{1}{4\pi c}\frac{1}{|x-x'|}\delta(|x-x'|-c(t-t'))\\ \
D_{adv}(x-x',t-t')=\frac{1}{4\pi c}\frac{1}{|x-x'|}\delta(|x-x'|+c(t-t'))$$

とおくと、$D(x-x',t-t')=D_{ret}(x-x',t-t')-D_{adv}(x-x',t-t')$

    ・空間積分において、実際に現れるのは|x-x'|=c(t-t')の部分：ret、advのどちらか！

---

・$D_{ret}(x,t)=\theta(t)D(x,t)$
→$$\left(\Delta-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right)D_{ret}(x,t)=-\frac{1}{c^2}\delta(t)\delta^3(x)$$


    ・θはヘビサイドの階段関数
    ・δ(t)f(x,t)=δ(t)f(x,0)でよい

---

## 真空中 
$$\bm{\epsilon_0,\mu_0}$$

・解くべき方程式$$\left(\Delta-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right)A(x,t)=0\\ \
A(x,t_0)=f(x,t_0)\\ \
\frac{\partial A}{\partial t}(x,t_0)=g(x,t_0)$$

    ・解の導出の際、実関数なのでフーリエ逆変換するとき複素共役を足してよい
    ・デルタ関数はフーリエ逆変換での積分の交換で使う！

---

・一般解$$A(x,t)=\int_{-\infty}^{\infty}d^3x'\left[\frac{\partial D}{\partial t}(x-x',t-t_0)f(x',t_0)\right] +D(x-x',t-t_0)g(x',t_0)$$

    ・D(x,t)は不変デルタ関数
    ・A(x,t)は実関数
    ・このとき、tについてフーリエ積分する必要はない！

---

## 回折現象

・Kirchhoffの積分表示
$$\psi(x,t)=\int_Vd^3x[D_{ret}(x-x',t-t_0)\frac{\partial\psi}{\partial t'}(x',t_0)+\psi(x',t_0)\frac{\partial}{\partial t}D_{ret}(x-x',t-t_0)]\\\ \\
+\frac{1}{4\pi}\oint_SdS'n'\cdot\left(\frac{\nabla'\psi(x',t')}{R}-\frac{\bm{R}}{R^3}\psi(x',t')-\frac{\bm{R}}{cR^2}\frac{\partial\psi}{\partial t}(x',t')\right)\\\ \\
(c(t-t_0)\ge|x-x'|)$$


    ・Ψは任意の波動方程式の解
    ・Vは任意領域、R=x-x',t'=t-R/c

→第一項について

    ・初期条件を与えた時の、波動方程式の解（t>t_0）と同じ形（積分範囲が小さい）
    ・$t_0$のとき、（外部）領域内に波動が存在しなければ第一項は消える：表面から発信するときなど

---

・Huygensの原理

---

・小孔による解析


---

## 散乱現象

---



# 一般の電磁波
$$\bm{\rho_e(x,t),i_e(x,t)}\\\bm{{近似：電荷、電流が半径}a{球面内に限られているとし、}}\\\bm{\omega a/c<<1\iff cT>>a}$$

    ・近似の物理的意味：放射電磁波の波長λが電荷、電流領域より十分大きい
    ・このとき、電磁波は放射する

---

## 関数の特殊関数表示



---

## 真空中 
$$\bm{\epsilon_0,\mu_0}$$

・解くべき方程式
$$\Delta A(x,\omega)+\frac{\omega^2}{c^2}A(x,\omega)=-\mu_0i_e(x,\omega)\\ \
\Delta \phi(x,\omega)+\frac{\omega^2}{c^2}\phi(x,\omega)=-\frac{1}{\epsilon_0}\rho_e(x,\omega)$$

    ・時間に対するフーリエ変換によって求まる
    ・非斉次ヘルムホルツ方程式

---

・ヘルムホルツ方程式のグリーン関数：
$$G_{ret}(x)=\frac{1}{4\pi}\frac{e^{i|x|\frac{\omega}{c}}}{|x|}\\ \
G_{adv}(x)=\frac{1}{4\pi}\frac{e^{-i|x|\frac{\omega}{c}}}{|x|}$$

---

・一般解：
$$A(x,t)=\mu_0c^2\int_Vd^3x'\int_{-\infty}^{\infty}dt'D_{ret(adv)}(x-x',t-t')i_e(x',t) \\ \
\phi(x,t)=\frac{c^2}{\epsilon_0}\int_Vd^3x'\int_{-\infty}^{\infty}dt'D_{ret(adv)}(x-x',t-t')\rho_e(x',t)$$

    ・c^2 D_{ret}は多分波動方程式のグリーン関数

---

・別の遅延ポテンシャル表示
$$A(x,t)=\frac{\mu_0}{4\pi}\int_Vd^3x'\frac{i_e(x',t-\frac{|x-x'|}{c})}{|x-x'|}\\ \
\phi(x,t)=\frac{1}{4\pi\epsilon_0}\int_Vd^3x'\frac{\rho_e(x',t-\frac{|x-x'|}{c})}{|x-x'|}$$

    ・先進は被積分関数内のtに足す
    ・時間の初期値を決めて正方向に進める場合、考えるのは遅延だけになる

→遅延、先進ともに$\mathrm{div} A+\frac{1}{c^2}\frac{\partial \phi}{\partial t}=0$を満たす

---

## 多重極放射 
$$\bm{{分布が半径}a{内に限られているとし、}}\\\bm{cT>>a{または}\frac{\omega a}{c}<<1}$$

    ・放射電磁波の波長が存在領域より十分大きいとき
    ・このとき、積分で出てくる r'→0　とできる

・多重極展開：
$$\phi(x,t)=\frac{1}{4\pi\epsilon_0}\sum_{l=0}\frac{(2l+1)}{(2l+1)!!}(-r)^l\left(\frac{1}{r}\frac{d}{dr}\right)^l\left(\frac{1}{r}<\rho^l(t-\frac{r}{c})>\right) \\\ \\
A(x,t)=\frac{\mu_0}{4\pi}\sum_{l=1}\frac{(2l-1)}{(2l-1)!!}(-r)^{l-1}\left(\frac{1}{r}\frac{d}{dr}\right)^{l-1}\left(\frac{1}{r}<i^{(l-1)}(t-\frac{r}{c})>\right) \\\ \\
<\rho^{(l)}(t)>=\int_Vd^3x'\ r'^lP_l(\cos\theta')\rho_e(x',t),\quad <i^{(l)}(t)>=\int_Vd^3x'\ r'^lP_l(\cos\theta')i_e(x',t)$$

    ・t-r/cは原点における発信時刻
    ・遅延ポテンシャルを展開している
    ・A_0=0は定義

---

# 物質中の電磁波


## 誘電体中の電磁波

・特徴：$\epsilon(\omega),\ \mu(\omega)$
分散公式$n=n(\omega)=c\sqrt{\epsilon(\omega)\mu(\omega)}$

    ・誘電体中の誘電率とかは、tのωでのフーリエ逆変換において、ωの関数になってる

---

・解くべき方程式：$$\mathrm{rot}E(x,t)+\frac{\partial B}{\partial t}=0\\ \
\mathrm{div}B(x,t)=0\\ \
\int d\omega e^{i\omega t}\frac{1}{\mu(\omega)}\left(\mathrm{rot}B(x,\omega)-\frac{i\omega}{v^2(\omega)}E(x,\omega)\right)=0\\ \
\int d\omega e^{i\omega t}\epsilon(\omega)\mathrm{div}E(x,\omega)=0$$

---

・ゲージ変換

→ ポテンシャル：$$E(x,\omega)=-i\omega A(x,\omega)-\mathrm{grad}\phi(x,\omega)\\ \
B(x,\omega)=\mathrm{rot}A(x,\omega)$$

→ Lorentzゲージ：$(\Delta+\frac{\omega^2}{v(\omega)^2})\chi(x,\omega)=-\mathrm{div}A(x,\omega)-\frac{i\omega}{v(\omega)^2}\phi(x,\omega)$
→ クーロンゲージ：$i\omega\chi_0(x,\omega)=\phi(x,\omega)$

→ 変換された方程式：$$E(x,\omega)=-i\omega A(x,\omega)\\
B(x,\omega)=\mathrm{rot}A(x,\omega)\\ \
\int d\omega e^{i\omega t}\frac{1}{\mu(\omega)}\left(\Delta A(x,\omega)-\frac{\omega^2}{v^2(\omega)}A(x,\omega)\right)=0\\ \
\mathrm{div}A(x,\omega)=0$$

    ・時間に関する式と、そのフーリエ変換から導出できる

---

・$A(x,\omega)$の一般解$$A(x,t)=\int_{-\infty}^{\infty}d^3k[a(k)e^{i(k\cdot x-\omega(k)t)}+a(k)^*e^{-i(k\cdot x-\omega(k) t)}]$$
→ $\omega=v(\omega)k$
→ 位相速度：$v_p=\frac{\omega(k)}{k}=\frac{c}{n(\omega)}=v(\omega)$

    ・A(x,ω)をフーリエ変換して、A(x,t)をフーリエ積分してる
    ・ωをkの逆関数として解いてる
    ・位相速度v_pは光速を超えうる

---

・群速度 $v_g=\mathrm{grad}_k\omega(k_0)$

    ・信号の速さ
    ・光速を超えてはならない

→ $a(k)$はある波数$k_0$を中心として$\Delta k$なる狭い領域以外$0$で、波束は十分広がっているとする

→この場合の一般解と振幅：$$A(x,t)=a(x-v_g t)e^{i(k_0\cdot x-\omega(k_0)t)}\\\
a(x-v_gt)=\int_{\Delta k}d^3k'a(k_0+k')e^{ik'\cdot(x-v_g t)}$$

    ・一般解的には後ろに複素共役が足される



→群速度の別の表示：$v_g=\frac{c}{n(\omega)+\omega\frac{dn}{d\omega}(\omega)}$

    ・n(ω)≧0だが、異常分散があるときは第二項が大きく負になることがある：群速度自体が定義できる状態にない
    

---

## 電磁波の反射と屈折

---

## 導体中の電磁波

---