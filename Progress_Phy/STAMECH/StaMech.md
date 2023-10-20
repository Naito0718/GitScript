
- [基本原理](#基本原理)
  - [分配関数](#分配関数)
    - [エントロピーとか](#エントロピーとか)
- [分布関数 $f(q,p,t)$](#分布関数-fqpt)
  - [ミクロカノニカル分布](#ミクロカノニカル分布)
  - [カノニカル分布](#カノニカル分布)
  - [グランドカノニカル分布](#グランドカノニカル分布)
  - [平衡状態](#平衡状態)
- [密度行列](#密度行列)
  - [経路積分](#経路積分)
- [スピン、超伝導（300ページ！？）](#スピン超伝導300ページ)


# 基本原理

・等確率の原理：微視的状態はすべて同じ確率で起こる。
このとき、確率はエネルギーの関数：$P(E)$

    ・同じエネルギーを持った違う状態。

・時間平均と集団平均は等しい。：$\lang A\rang=\frac{\int Afdpdq}{\int fdpdq}$

---

## 分配関数

・ある平衡系に対して、温度 $T$ とする。
このとき、$N$ 個の取りうる状態のうちその $1$ つの状態を取る時、系がエネルギー $E_n$ の状態を占める確率 $P$：
$$P_n=\frac{1}{Q}e^{-\frac{E_n}{kt}}\\\ \\
Q=\sum_n^Ne^{-\frac{E_n}{kT}}$$
ここで、$Q$ を分配関数という。

---

### エントロピーとか


<dl><dt>

・ある平衡系に対して、温度 $T$、分配関数 $Q$、エネルギー $E_n$ の確率 $P_n$ とする。
このとき、エントロピー $S$、Helmholtzエネルギー $F$：
$$S=-k\sum P_n\log P_n\\\ \\
F=-kT\log Q$$

</dt><dd>



</dd></dl>

---

# 分布関数 $f(q,p,t)$

    ・時刻tにおける、系を特徴づける(p,q)において、その系と巨視的に見て同じである代表点の密度。

・$v=(\dot{q},\dot{p})$ とすると、
$$\frac{\partial }{\partial t}\int_G fdpdq=\int_G \frac{\partial f}{\partial t}dpdq=-\int_{\partial G}n\cdot vfdS$$が成り立つ。
すなわち、$\frac{\partial \dot{p}_i}{\partial p_i}+\frac{\partial\dot{q}_i}{\partial q_i}=0\ \ (\forall i)$ より、
$$-\frac{\partial f}{\partial t}=\sum \frac{\partial f}{\partial p_i}\dot{p}_i+\frac{\partial f}{\partial q_i}\dot{q}_i\\\ \\
\frac{df}{dt}=0\\\ \\
\frac{\partial f}{\partial t}=i\mathcal{L}f=\lang H,f\rang_{poison}$$

    ・これは代表点が非圧縮性流体のように時間発展することを意味する？？？

---

## ミクロカノニカル分布

・$$f(p,q)=\begin{cases}
1 & (E<H(p,q)<E+\delta E)   \\
0 & (\text{それ以外})\\
\end{cases}$$

    ・必要があれば、V=V_0とかN_0<N(p,q)<N_0+δとかも条件に加える。

## カノニカル分布

## グランドカノニカル分布

## 平衡状態

<dl><dt>

・$$\frac{\partial f}{\partial t}=0,\quad\frac{\partial H}{\partial t}=0$$

    ・各系でエネルギーは一定！

</dt><dd>

- $$\lang H,f\rang_{poison}=0$$

</dd></dl>

---

# 密度行列

## 経路積分

---

# スピン、超伝導（300ページ！？）