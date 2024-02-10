
- [一次元調和振動子](#一次元調和振動子)
  - [波動関数表示](#波動関数表示)
    - [束縛条件](#束縛条件)
  - [演算子法](#演算子法)
  - [個数演算子 $N$ の固有ケット](#個数演算子-n-の固有ケット)
      - [位置空間での波動関数表示](#位置空間での波動関数表示)
  - [波動関数表示（Hermite多項式）](#波動関数表示hermite多項式)
- [二次元調和振動子](#二次元調和振動子)




# 一次元調和振動子

・質量 $m$、角運動量 $\omega$ とする。
このとき、系のハミルトニアン $\tilde{H}$：$$\tilde{H}=\frac{1}{2m}\tilde{p}^2+\frac{m\omega^2}{2}\tilde{x}^2$$

---

## 波動関数表示

・角振動数 $\omega>0$、ポテンシャル $V(x)$：$$V(x)=\frac{1}{2}m\omega^2x^2$$ とし、質量 $m$ の粒子がエネルギー $E$ を持つとする。
このとき、
$$\xi=\sqrt{\frac{m\omega}{\hbar}}x,\quad\epsilon=\frac{2E}{\hbar\omega}$$ とおくと、シュレディンガー方程式：
$$\frac{d}{d\xi^2}\phi+(\epsilon-\xi^2)\phi=0$$

---

### 束縛条件

---

## 演算子法


<dl><dt>

・
$$a=\sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x}+\frac{i}{m\omega}\hat{p}\right)\\\ \\
a^{\dag}=\sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x}-\frac{i}{m\omega}\hat{p}\right)\\\ \\
N=a^{\dag}a$$
とする。明らかに、$N$ は物理量である。

<br>

</dt><dd>

- $$[a,a^{\dag}]=1,\quad H=\hbar\omega\left(N+\frac{1}{2}\right)$$

- $[N,H]=0$ 。したがって、$N$ は保存量。
<br>

- $$[N,a]=-a,\ \  [N,a^{\dag}]=a^{\dag}$$

</dd></dl>


---

## 個数演算子 $N$ の固有ケット


<dl><dt>

・$N\ket{n}=n\ket{n}$ とする。
<br>

</dt><dd>

- $$n\ge0$$

- 
$$Na\ket{n}=(n-1)a\ket{n}\\\ \\
Na^{\dag}\ket{n}=(n+1)a^{\dag}\ket{n}$$
であって、規格化条件より
$$a\ket{n}=\sqrt{n}\ket{n-1},\quad a^{\dag}\ket{n}=\sqrt{n+1}\ket{n+1}$$
特に、$a\ket{n},a^{\dag}\ket{n}$ は $N$ の固有ケットであって、$n\in\bm{N}\cup\{0\}$  
<br>

- $$H\ket{n}=\hbar\omega\left(n+\frac{1}{2}\right)\ket{n}$$
特に、エネルギー固有値は離散的であって、基底状態 $\ket{0}$ において最小値 $\hbar\omega/2$ を取る。
<br>

- $$\ket{n}=\frac{(a^{\dag})^n}{\sqrt{n!}}\ket{0}$$


</dd></dl>

---

#### 位置空間での波動関数表示

<dl><dt>

・$$\hat{x}=\sqrt{\frac{\hbar}{2m\omega}}(a+a^{\dag}),\quad\hat{p}=i\sqrt{\frac{m\omega\hbar}{2}}(-a+a^{\dag})\\\ \\$$

</dt><dd>

- $$\left(x'+x_0^2\frac{d}{dx'}\right)\braket{x'|0}=0\\\ \\
x_0^2=\frac{\hbar}{m\omega}$$
を満たす。したがって、規格化条件より、
$$\braket{x'|0}=\frac{1}{\pi^{1/4}\sqrt{x_0}}\exp\left[-\frac{1}{2}\left(\frac{x'}{x_0}\right)^2\right]\\\ \\$$

      ・確かにx_0は長さの次元を持つ。
<br>

- $$\braket{x'|n}=\left(\frac{1}{\pi^{1/4}\sqrt{2^nn!}}\right)\left(\frac{1}{x_0^{n+1/2}}\right)\left(x'-x_0^2\frac{d}{dx'}\right)^n\exp\left[-\frac{1}{2}\left(\frac{x'}{x_0}\right)^2\right]$$ 

<br>

---

- $$\bra{n}\hat{x}^2\ket{n}=(2n+1)\frac{\hbar}{2m\omega},\quad\bra{n}\hat{p}^2\ket{n}=(2n+1)\frac{\hbar m\omega}{2}$$

- $$\bra{n}\hat{x}^4\ket{n}=3(2n^2+2n+1)\left(\frac{\hbar}{2m\omega}\right)^2$$


</dd></dl>


---


## 波動関数表示（Hermite多項式）



---

# 二次元調和振動子



---