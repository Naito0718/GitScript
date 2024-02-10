
- [$L^1(R^N)$ 上のフーリエ変換](#l1rn-上のフーリエ変換)
  - [$L^1(R^N)$ 上のフーリエ逆変換](#l1rn-上のフーリエ逆変換)
  - [フーリエ逆変換が逆になるとき](#フーリエ逆変換が逆になるとき)
- [急減少関数 $S$ 上のフーリエ変換](#急減少関数-s-上のフーリエ変換)
  - [急減少関数 $S$ 上のフーリエ逆変換](#急減少関数-s-上のフーリエ逆変換)
  - [フーリエ変換,逆変換の関係](#フーリエ変換逆変換の関係)
- [緩増加超関数 $S'$ 上のフーリエ変換](#緩増加超関数-s-上のフーリエ変換)
- [$L^2(R^N)$ のフーリエ変換](#l2rn-のフーリエ変換)


# $L^1(R^N)$ 上のフーリエ変換

<dl><dt>

・$[f]\in L^1(\bm{R}^N)$ とする。
このとき、
$$\mathcal{F}_f:\bm{R}^N\to\bm{C}\\\ \\
\mathcal{F}_f(k)=\frac{1}{(2\pi)^{N/2}}\int_{\bm{R}^N}f(x)e^{-k\cdot x}dm(x)$$
と定めると、$\mathcal{F}_f$ はwell-defined、すなわち $f=g\quad(a.e.)$ ならば $\mathcal{F}_f=\mathcal{F}_g\quad(a.e.)$ である。さらに、$\mathcal{F}_f$ は連続関数であって、
$$\sup_{k\in\bm{R}^N}|\mathcal{F}_f(k)|\le\frac{1}{(2\pi)^{N/2}}\|f\|_{L^1}\\\ \\$$

</dt><dd>

- $[f],[g]\in L^1(\bm{R}^N)$ とする。
このとき、
$$\int_{\bm{R}^N}\mathcal{F}_f(x)g(x)dm=\int_{\bm{R}^N}f(x)\mathcal{F}_g(x)dm\\\ \\$$

      ・フビニの定理で順序クルクルするだけ。F_fg,F_gfが可積分なことにもよる。
<br>

- $y\in\bm{R}^N$ による平行移動 $T_y$ とし、
$$e_y:\bm{R}^N\to\bm{C}\\\ \\
e_y(x)=e^{ix\cdot y}$$
とする。
このとき、
$$\mathcal{F}_{f\circ T_y}=e_{-y}\mathcal{F}_{f},\quad\mathcal{F}_{e_yf}=\mathcal{F}_f\circ T_y\\\ \\$$

- 正則行列 $A\in GL(N,\bm{R})$ とする。
このとき、
$$\mathcal{F}_{f\circ A}=\frac{1}{|\det A|}\mathcal{F}_f\circ\ ^tA^{-1}\\\ \\$$

- $\mathcal{F}_f\in C_0(\bm{R}^N)$、すなわち、
$$\lim_{|k|\to\infty}\mathcal{F}_f(k)=0$$

</dd></dl>

---

## $L^1(R^N)$ 上のフーリエ逆変換

<dl><dt>

・$[f]\in L^1(\bm{R}^N)$ とする。
このとき、
$$\mathcal{F}^{\vee}_f:\bm{R}^N\to\bm{C}\\\ \\
\mathcal{F}^{\vee}_f(k)=\frac{1}{(2\pi)^{N/2}}\int_{\bm{R}^N}f(x)e^{ik\cdot x}dm(x)\\\ \\$$

と定めると、$\mathcal{F}^{\vee}_f$ はwell-defined、すなわち $f=g\quad(a.e.)$ ならば $\mathcal{F}^{\vee}_f=\mathcal{F}^{\vee}_g\quad(a.e.)$ である。さらに、$\mathcal{F}^{\vee}_f$ は連続関数であって、
$$\sup_{k\in\bm{R}^N}|\mathcal{F}^{\vee}_f(k)|\le\frac{1}{(2\pi)^{N/2}}\|f\|_{L^1}\\\ \\$$

</dt><dd>

- $[f],[g]\in L^1(\bm{R}^N)$ とする。
このとき、
$$\int_{\bm{R}^N}\mathcal{F}^{\vee}_f(x)g(x)dm=\int_{\bm{R}^N}f(x)\mathcal{F}^{\vee}_g(x)dm\\\ \\$$

      ・フビニの定理で順序クルクルするだけ。F_fg,F_gfが可積分なことにもよる。
<br>

- $y\in\bm{R}^N$ による平行移動 $T_y$ とし、
$$e_y:\bm{R}^N\to\bm{C}\\\ \\
e_y(x)=e^{ix\cdot y}$$
とする。
このとき、
$$\mathcal{F}^{\vee}_{f\circ T_y}=e_{y}\mathcal{F}^{\vee}_{f},\quad\mathcal{F}^{\vee}_{e_yf}=\mathcal{F}^{\vee}_f\circ T_{-y}\\\ \\$$

- 正則行列 $A\in GL(N,\bm{R})$ とする。
このとき、
$$\mathcal{F}^{\vee}_{f\circ A}=\frac{1}{|\det A|}\mathcal{F}^{\vee}_f\circ\ ^tA^{-1}\\\ \\$$

- $\mathcal{F}^{\vee}_f\in C_0(\bm{R}^N)$、すなわち、
$$\lim_{|k|\to\infty}\mathcal{F}^{\vee}_f(k)=0$$

</dd></dl>

---

## フーリエ逆変換が逆になるとき

    ・ここでのFの明確な写像の定義は難しい。
<br>

・$\mathcal{F}_f\in L^1(\bm{R}^N)$ を満たす有界連続な $f\in L^1(\bm{R}^N)$ とする。
このとき、
$$\forall x\in\bm{R}^N\text{ に対して、}f(x)=\frac{1}{(2\pi)^{N/2}}\int_{\bm{R}^{N}}\mathcal{F}_fe^{ik\cdot x}dm(k)\\\ \\
=\mathcal{F}^{\vee}_{\mathcal{F}_f}\\\ \\$$

- $\mathcal{F}^{\vee}_f\in L^1(\bm{R}^N)$ を満たす有界連続な $f\in L^1(\bm{R}^N)$ とする。
このとき、
$$\forall x\in\bm{R}^N\text{ に対して、}f(x)=\frac{1}{(2\pi)^{N/2}}\int_{\bm{R}^{N}}\mathcal{F}^{\vee}_fe^{-ik\cdot x}dm(k)\\\ \\
=\mathcal{F}_{\mathcal{F}^{\vee}_f}$$

---


# 急減少関数 $S$ 上のフーリエ変換

    ・SはL^1に含まれてる。
<br>

<dl><dt>

・$f\in\mathcal{S}_N$ とする。このとき、
$$id_j\mathcal{F}_f=-i\mathcal{F}_{\partial_jf},\text{ すなわち、}\forall k\in\bm{R}^N\text{ に対して、}k_j\mathcal{F}_f(k)=-i\mathcal{F}_{\partial_jf}(k)\\\ \\
\mathcal{F}_f\text{ は微分可能であって、}\partial_j\mathcal{F}_f=-i\mathcal{F}_{id_jf}\\\ \\$$

</dt><dd>

- $\mathcal{F}_f\in \mathcal{S}_N$ である。また、多重指数 $I$ とすると、
$$\partial^{I}\mathcal{F}_f=(-i)^{|I|}\mathcal{F}_{x^If},\quad id^I\mathcal{F}_f=(-i)^{|I|}\mathcal{F}_{\partial^I f}$$

</dd></dl>

---

## 急減少関数 $S$ 上のフーリエ逆変換

<dl><dt>

・$f\in\mathcal{S}_N$ とする。このとき、
$$id_j\mathcal{F}^{\vee}_f=i\mathcal{F}_{\partial_jf},\text{ すなわち、}\forall k\in\bm{R}^N\text{ に対して、}k_j\mathcal{F}_f(k)=i\mathcal{F}_{\partial_jf}(k)\\\ \\
\mathcal{F}_f\text{ は微分可能であって、}\partial_j\mathcal{F}_f=i\mathcal{F}_{id_jf}\\\ \\$$

</dt><dd>

- $\mathcal{F}^{\vee}_f\in \mathcal{S}_N$ である。また、多重指数 $I$ とすると、
$$\partial^{I}\mathcal{F}^{\vee}_f=(i)^{|I|}\mathcal{F}^{\vee}_{x^If},\quad id^I\mathcal{F}^{\vee}_f=(i)^{|I|}\mathcal{F}^{\vee}_{\partial^I f}$$

</dd></dl>

---

## フーリエ変換,逆変換の関係

・$$\mathcal{F}:\mathcal{S}_N\to\mathcal{S}_N,\quad\mathcal{F}^{\vee}:\mathcal{S}_N\to\mathcal{S}_N\\\ \\
\mathcal{F}\circ\mathcal{F}^{\vee}=\mathcal{F}^{\vee}\circ\mathcal{F}=id$$
であって、$\mathcal{F},\mathcal{F}^{\vee}$ は共に線形同型同相写像。さらに、
$$\forall f\in\mathcal{S}_N\text{ に対して、}\mathcal{F}\circ\mathcal{F}(f)=\mathcal{F}^{\vee}\circ\mathcal{F}^{\vee}(f)=f\circ S_{-1}\\\ \\
(f\circ S_{-1}(x)=f(-x))$$



---


# 緩増加超関数 $S'$ 上のフーリエ変換

<dl><dt>

・$\mathcal{S}'_N$ の元を、$\mathcal{S}_N$ 上の連続線形汎関数とみなす。
$$\mathcal{F},\mathcal{F}^{\vee}:\mathcal{S}'_N\to\mathcal{S}'_N\\\ \\
\mathcal{F}(u)(\phi)=u(\mathcal{F}_{\phi}),\quad\mathcal{F}^{\vee}(u)(\phi)=u(\mathcal{F}^{\vee}_{\phi})$$
と定めると、これはwell-definedであって、
$$\mathcal{F}\circ\mathcal{F}^{\vee}(u)=\mathcal{F}^{\vee}\circ\mathcal{F}(u)=u,\quad\mathcal{F}\circ\mathcal{F}(u)=\mathcal{F}^{\vee}\circ\mathcal{F}^{\vee}(u)=u\circ S_{-1}$$
ここで、$\mathcal{F}$ をフーリエ変換、$\mathcal{F}^{\vee}$ をフーリエ逆変換という。
<br>

</dt><dd>

- $[f]\in L^1(\bm{R}^N)$ とする。
このとき、
$$\forall\phi\in\mathcal{S}_N\text{ に対して、}\\\ \\
\mathcal{F}([f])(\phi)=\int_{\bm{R}^N}\mathcal{F}_f(x)\phi(x)dx=[\mathcal{F}_f](\phi),\quad\mathcal{F}^{\vee}([f])(\phi)=\int_{\bm{R}^N}\mathcal{F}^{\vee}_f(x)\phi(x)dx=[\mathcal{F}^{\vee}_f](\phi)$$
したがって、$\mathcal{S}_N'$ 上のフーリエ変換は、$L^1(\bm{R}^N)$ 上のフーリエ変換の定義と整合する。
<br>

    ・F_fとかは有界だから、L^1_loc(R^N)に属する。
<br>

- $u\in\mathcal{S}'_N$、多重指数 $I$ とする。
このとき、
$$\partial^I\{\mathcal{F}(u)\}=(-i)^{|I|}\mathcal{F}(id^Iu),\quad id^I\mathcal{F}(u)=(-i)^{|I|}\mathcal{F}(\partial^I u)\\\ \\
\partial^I\{\mathcal{F}^{\vee}(u)\}=i^{|I|}\mathcal{F}^{\vee}(id^Iu),\quad id^I\mathcal{F}^{\vee}(u)=i^{|I|}\mathcal{F}^{\vee}(\partial^I u)\\\ \\$$

</dd></dl>

---

# $L^2(R^N)$ のフーリエ変換

    ・一応急減少関数S上のフーリエ逆変換の後。
<br>

・$$\mathcal{F},\mathcal{F}^{\vee}:L^2(\bm{R}^N)\to L^2(\bm{R}^N)\\\ \\
\mathcal{F}(f)=\int_{\bm{R}^N}f(x)e^{ikx}dx,\quad\mathcal{F}^{\vee}(f)=\int_{\bm{R}^N}f(x)e^{ikx}dx$$
と定めると、$\mathcal{F},\mathcal{F}^{\vee}$ は値域がwell-definedなユニタリ作用素、すなわち 
$$\forall f\in L^2(\bm{R}^N)\text{ に対して、}\|\mathcal{F}(f)\|_{L^2}=\|\mathcal{F}^{\vee}(f)\|_{L^2}=\|f\|_{L^2}$$
で、
$$\mathcal{F}\circ\mathcal{F}^{\vee}=\mathcal{F}^{\vee}\circ\mathcal{F}=id\\\ \\
\overline{\mathcal{F}(f)}=\mathcal{F}^{\vee}(\overline{f}),\quad \overline{\mathcal{F}^{\vee}(f)}=\mathcal{F}(\overline{f})\\\ \\
(\mathcal{F}(f),\mathcal{F}(g))_{L^2}=(\mathcal{F}^{\vee}(f),\mathcal{F}^{\vee}(g))_{L^2}=(f,g)_{L^2}\\\ \\$$

    ・D(R^N)、S_Nが共にL^2(R^N)の稠密部分集合なことによる。
<br>

- $L^2(R^N)$ を $\mathcal{S}'_N$ の部分集合とみなす。
このとき、
$$\mathcal{F}',\mathcal{F}^{\vee'}:L^2(\bm{R}^N)\to L^2(\bm{R}^N)\\\ \\
\forall\phi\in\mathcal{S}_N\text{ に対して、}\mathcal{F}'([f])(\phi)=[f](\mathcal{F}(\phi)),\quad \mathcal{F}^{\vee'}([f])(\phi)=[f](\mathcal{F}^{\vee}(\phi))$$
と定めると、
$$\mathcal{F}'([f])=[\mathcal{F}(f)],\quad\mathcal{F}^{\vee'}([f])=[\mathcal{F}^{\vee}(f)]$$
すなわち、$\mathcal{S}'_N$ の部分集合と見た時のフーリエ変換と、普通の $L^2(\bm{R}^N)$ 上のフーリエ変換とは整合する。

<br>
      ・f∊L^2(R^N)に収束するS_Nの列と、φ∊S_Nにおいて、優収束定理が使える！

---

