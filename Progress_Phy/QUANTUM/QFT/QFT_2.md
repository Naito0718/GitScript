
- [クラインーゴルドン方程式](#クラインーゴルドン方程式)
  - [カレント](#カレント)
  - [非相対論的極限](#非相対論的極限)
- [ディラック方程式](#ディラック方程式)
  - [負エネルギー解](#負エネルギー解)




# クラインーゴルドン方程式 

・相対論的自由粒子は、次の微分方程式に従う。ここで、$\phi$ はスカラー関数。
$$(\partial_{\mu}\partial^{\mu}+m^2)\phi(x)=0$$
ここで、この微分方程式は相対論的不変である。これをクラインーゴルドン方程式という。
<br>

- アインシュタインの関係 $E^2=\bm{p}^2+m^2$ に対して、対応
$$p^{\mu}\to i\partial^{\mu}$$
によってクラインーゴルドン式が得られる。

      ・量子力学でのE=p^2/2mでの対応と完全に同じ。

- $c,\hbar$ を用いると、
$$\left(\partial_{\mu}\partial^{\mu}+\left(\frac{mc}{\hbar}\right)^2\right)\phi(x)=0$$

---

## カレント

・$\phi(x)$ をクラインーゴルドン方程式の解とする。
このとき、
$$\rho=\frac{i}{2m}(\phi^*\frac{\partial\phi}{\partial t}-\frac{\partial\phi^*}{\partial t}\phi)\\\ \\
\bm{j}=-\frac{i}{2m}(\phi^*\nabla\phi-(\nabla\phi^*)\phi)\\\ \\
j^{\mu}=\frac{i}{2m}\{\phi^*\partial^{\mu}\phi-(\partial^{\mu}\phi^*)\phi\}=(\rho,\bm{j})$$
とすると、
$$\partial_{\mu}j^{\mu}=0$$

    ・完全に連続の式。
    ・jは量子力学と完全に一致。ρは時間偏微分されてる。


- $$Q=\int_Vd^3\bm{x}\ \rho(t,x)$$
とする。
このとき、$$\frac{dQ}{dt}=0$$
ただし、$|\bm{x}|\to\infty$ で $\phi\to0$ とする。

      ・結局tにはよらない。

---

・こいつらって
$$j^{\mu}=\frac{i}{2m}\{\partial^{\mu}(\phi^{*}\phi)\}$$
で書けてるよね？これはシンプル！

---

## 非相対論的極限


<dl><dt>

・ある自由粒子に対して、クラインゴルドン式の解を $\phi(x,t)$、シュレディンガー式の解を $\psi(x,t)$ とする。
このとき、
$$\phi(x,t)=e^{-imt}\psi(x,t)$$
が成り立つとしてよい。
さらに、非相対論的極限：
$$|m\psi|>>\left|i\frac{\partial\psi}{\partial t}\right|$$
である。

      ・静止エネルギーm（\bm{p}=0）が非相対論的エネルギー、ポテンシャルエネルギーより十分大きい。

- クラインゴルドン解 $\phi$、波動関数 $\psi$ とする。
このとき、
$$\hat{H}\phi=\sqrt{\bm{p}^2+m^2},\quad\hat{H}\psi=\frac{\bm{p}^2}{2m}\psi$$
が成り立つとすると、
$$\phi(x,t)\sim e^{-imt}\psi(x,t)$$

      ・Eのテイラー展開で、ちょっと強引な近似ではあるが、納得できなくはない。


- 上記の関係において、負エネルギーに対応する波動関数を $\chi(x,t)$ とすると、
$$\phi(x,t)=e^{imt}\chi^*(x,t)$$
が成り立つとしてよい。

      ・まあ定義？

</dt><dd>

- 
$$\rho^+_{\phi}\sim \psi^{*}\psi\\\ \\
\rho^-_{\phi}\sim-\chi^*\chi$$

      ・相対論的極限！

</dd></dl>

---

# ディラック方程式

## 負エネルギー解










