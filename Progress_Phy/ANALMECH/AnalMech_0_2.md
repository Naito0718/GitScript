

- [単位球面](#単位球面)
- [極座標写像 $Ψ$](#極座標写像-ψ)
  - [極座標チャート $(Ω,φ)$](#極座標チャート-ωφ)
  - [$S^N$ の局所座標 $(S^{N}\_0,Θ)$](#sn-の局所座標-sn_0θ)
  - [極座標変換](#極座標変換)


# 単位球面

・$$f:\bm{R}^N\to\bm{R}\\\ \\
f(x)=|x|^1-1\\\ \\$$
と定める。このとき、
$$S^{N-1}=\{x\in\bm{R}^N\ |\ |x|=1\}=f^{-1}(0)\text{ であって、}\\\ \\
\forall x\in S^{N-1}\text{ に対して、}df_x\neq0$$
したがって、$S^{N-1}$ は $\bm{R}^N$ の $N-1$ 次元部分多様体。

---


# 極座標写像 $Ψ$

<dl><dt>

・
$$\Psi:\bm{R}^N\to\bm{R}^N\\\ \\
\Psi(x)=\begin{pmatrix}
x_1\cos x_2\\  x_1\sin x_2\cos x_3 \\
x_1\sin x_2\sin x_3\cos x_4 \\ ... \\
x_1\sin x_2...\sin x_{N-1}\cos x_N\\ x_1\sin x_2...\sin x_{N-1}\sin x_N    
\end{pmatrix}\\\ \\$$
<br>

</dt><dd>

- 
$$\Psi_1:[0,\pi]\times...\times[0,\pi]\times[0,2\pi)\to S^{N-1}\\\ \\
\Psi_1(x_1,...,x_{N-1})=\Psi(1,x_1,...,x_{N-1})$$
と定めると、$\Psi_1$ は $[0,\pi]\times...\times[0,\pi]\times[0,2\pi)$ 上全射であって、$(0,\pi)\times...\times(0,\pi)\times(0,2\pi)$ 上全単射。
<br>

- 
$$\forall x\in\bm{R}^N\text{ に対して、}\\\ \\
\det(\Psi'(x))=x_1^{N-1}(\sin x_2)^{N-2}(\sin x_3)^{N-3}...\sin x_{N-1}$$
特に、
$$\forall x\in(0,\infty)\times(0\times\pi)\times...\times(0,\infty)\text{ に対して、}\\\ \\
\det(\Psi'(x))>0$$

</dd></dl>

---

## 極座標チャート $(Ω,φ)$

    ・多様体としてはR^Nがあって、そこの局所座標ってこと。
<br>

<dl><dt>

・$$\Omega_N=\Psi((0,\infty)\times(0,\pi)\times...\times(0,2\pi))\\\ \\
\varphi:\Omega_N\to(0,\infty)\times(0,\pi)\times...\times(0,2\pi)\\\ \\
\varphi(x)=\Psi^{-1}(x)$$
と定める。
<br>

</dt><dd>

- $\Omega_N\sub\bm{R}^N$ は開集合であって、$(\Omega,\varphi)$ は $\bm{R}^N$ の局所座標。
<br>

- $$i\neq j\text{ ならば、}\forall p\in\Omega_N\text{ に対して、}\left(\frac{\partial}{\partial x^i}p,\frac{\partial}{\partial x^j}p\right)=0\\\ \\
\left|\frac{\partial}{\partial x^1}p\right|=1,\quad i\ge1\text{ に対して、}\left|\frac{\partial}{\partial x^i}p\right|=[\Psi^{-1}(p)]_1\Big(\sin [\Psi^{-1}(p)]_2\Big)...\Big(\sin [\Psi^{-1}(p)]_i\Big)$$
特に、$(\Omega,\varphi)$ は $\bm{R}^N$ の正の向きの直交局所座標であって、
$$\forall x\in\Omega_N\text{ に対して、}\sqrt{G_{(\Omega_N,\varphi)}(x)}=\det\Psi'(\Psi^{-1}(x))$$

</dd></dl>

---

## $S^N$ の局所座標 $(S^{N}_0,Θ)$

<dl><dt>

・
$$S^{N-1}_0=S^{N-1}\cap\Omega=\Psi(\{1\}\times(0,\pi)\times...\times(0,\pi)\times(0,2\pi))\\\ \\
\Theta:S^{N-1}_0\to(0,\pi)...\times(0,\pi)\times(0,2\pi)\\\ \\
\forall x\in S^{N-1}_0\text{ に対して、}\Psi^{-1}(x)=(1,\Theta(x))$$
と定める。

</dt><dd>

- $(S^{N-1}_{0},\Theta)$ は $S^{N-1}$ の局所座標。特に、$\Theta^{-1}=\Psi$ でよい。
<br>

- $$i\neq j\text{ ならば、}\forall p\in S_0^{N-1}\text{ に対して、}\left(\frac{\partial}{\partial x^i}p,\frac{\partial}{\partial x^j}p\right)=0\\\ \\
\left|\frac{\partial}{\partial x^i}p\right|=\Big(\sin [\Theta(p)]_1\Big)\Big(\sin[\Theta(x)]_2\Big)...\Big(\sin [\Theta(p)]_i\Big)$$
特に、$(S^{N-1}_0,\Theta)$ は $S^{N-1}$ の正の向きの直交局所座標であって、
$$\forall x\in S^{N-1}_0\text{ に対して、}\sqrt{G_{(S_0^{N-1},\Theta)}(x)}=\Big(\sin[\Theta(x)]_1\Big)^{N-2}\Big(\sin[\Theta(x)]_2\Big)^{N-3}...\Big(\sin[\Theta(x)_{N-2}]\Big)\\\ \\$$

- 
$$\mu_{S^{N-1}}(S^{N-1}-S^{N-1}_0)=0\\\ \\
\mu_{S^{N-
1}}(S^{N-1})=2\pi\int_0^{\pi}...\int_0^{\pi}\Big[(\sin\theta_1)^{N-2}(\sin\theta_2)^{N-1}...\sin\theta_{N-2}\Big]d\theta_1...d\theta_{N-2}$$


</dd></dl>


---

## 極座標変換

・$a\in\bm{R}^N$、$R>0$、非負値Borel関数 $f:B(a,R)\to[0,\infty]$ とする。
このとき、
$$\int_{B(a,r)}f(x)dm=\int_0^R\int_{S^{N-1}}f(a+r\omega)r^{N-1}d\mu_{S^{N-1}}(\omega)dr\\\ \\$$

    ・このωって立体角か！


