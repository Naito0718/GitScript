
- [片側に $2π$ 因子を押し付けるとき](#片側に-2π-因子を押し付けるとき)
  - [逆変換の定義](#逆変換の定義)



# 片側に $2π$ 因子を押し付けるとき

・$$\sup_{k\in\bm{R}^N}|\mathcal{F}'_f(k)|\le\|f\|_{L^1}$$

---

## 逆変換の定義

・$\mathcal{F}_f\in L^1(\bm{R}^N)$ を満たす有界連続な $f\in L^1(\bm{R}^N)$ とする。
このとき、
$$\forall x\in\bm{R}^N\text{ に対して、}f(x)=\frac{1}{(2\pi)^{N/2}}\int_{\bm{R}^{N}}\mathcal{F}_fe^{ik\cdot x}dm(k)\\\ \\
=\frac{1}{(2\pi)^{N}}\int_{\bm{R}^{N}}\mathcal{F}'_fe^{ik\cdot x}dm(k)\\\ \\$$
よって、逆変換は上記のように定義しなおしておく必要がある。すなわち、
$$\mathcal{F}'_f=(\sqrt{2\pi})^N\mathcal{F}_f,\quad\mathcal{F}^{\vee'}_{f}=\frac{1}{(\sqrt{2\pi})^N}\mathcal{F}^{\vee}_f\\\ \\$$

- $\mathcal{F}^{\vee}_f\in L^1(\bm{R}^N)$ を満たす有界連続な $f\in L^1(\bm{R}^N)$ とする。
このとき、
$$\forall x\in\bm{R}^N\text{ に対して、}f(x)=\frac{1}{(2\pi)^{N/2}}\int_{\bm{R}^{N}}\mathcal{F}^{\vee}_fe^{-ik\cdot x}dm(k)\\\ \\
=\int_{\bm{R}^{N}}\mathcal{F}^{\vee'}_fe^{-ik\cdot x}dm(k)\\\ \\$$