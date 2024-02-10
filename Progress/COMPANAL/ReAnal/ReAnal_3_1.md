
- [リーマン積分](#リーマン積分)
  - [性質](#性質)
    - [性質 $2$](#性質-2)
  - [下積分と上積分](#下積分と上積分)
    - [可積分条件](#可積分条件)
- [ベクトル値関数の積分](#ベクトル値関数の積分)
  - [性質](#性質-1)
    - [性質 $2$](#性質-2-1)
  - [可積分条件](#可積分条件-1)
  - [複素数値関数の積分](#複素数値関数の積分)
- [広義積分](#広義積分)



# リーマン積分

・有界閉区間 $I\sub\bm{R}^n$、$f:I\to\bm{R}$ とする。
このとき、$$\int_Ifdx=J\in\bm{R}\iff\\\ \\
\forall\epsilon>0\text{ に対して、}\exist\delta>0\text{ であって、}\forall\ I\text{ の分割 }\Delta,\ d(\Delta)<0,\ \forall\text{ 代表点 }\xi_k\in I_k\text{ に対して、}\\\ \\
\left|\sum_kf(\xi_k)v(I_k)-J\right|<\epsilon$$
と定める。明らかに、$f$ がリーマン可積分ならば、その積分値 $J$ は一意的に定まる。

---

## 性質

<dl><dt>

・有界閉区間 $I\sub\bm{R}^n$、$v(I)>0$、$f:I\to\bm{R}$ とする。
このとき、$f$ が $I$ 上可積分ならば、$f$ は $I$ 上有界。
<br>

</dt><dd>

- $I$ 上可積分関数 $f,g$、$c\in\bm{R}$ とする。
このとき、$f+g,cf$ は $I$ 上可積分で、
$$\int_I (f+g)dx=\int_Ifdx+\int_Igdx\\\ \\
\int_I(cf)dx=c\int_Ifdx\\\ \\$$

- $I$ 上可積分関数 $f,g$ が $f(x)\ge g(x)\ \ (\forall x\in I)$ を満たすとする。
このとき、
$$\int_Ifdx\ge\int_Igdx\\\ \\$$

- $I$ 上有界可積分関数 $f$、$I$ における上限、下限を $m,M$ とする。
このとき、
$$\exist\mu\in\bm{R}\text{ であって、}\int_Ifdx=\mu v(I),\quad m\le\mu\le M$$
特に、$f$ が $I$ 上連続ならば、$\exist\xi\in I$ であって、$f(\xi)=\mu$
<br>

      ・第一平均値定理。
<br>

- 体積 $v(I)$ は平行移動 $T_c(x)=x+c$ で不変。
また、
$$\int_{T_c(I)} fdx=\int_I(f\circ T_c)dx$$


</dd></dl>

---

### 性質 $2$

<dl><dt>

・有界閉区間 $I\sub\bm{R}^n$、$I$ 上可積分関数 $f:I\to\bm{R}$ とする。
<br>

</dt><dd>

- $|f|$ は可積分で、$$\left|\int_If(x)dx\right|\le\int_I|f(x)|dx$$


</dd></dl>

---

## 下積分と上積分


<dl><dt>

・有界閉区間 $I\sub\bm{R}^n$、有界関数 $f:I\to\bm{R}$、分割 $\Delta$、$M=\sup_{x\in I}f(x),m=\inf_{x\in I}f(x)$ とする。
このとき、
$$a(f,I)=\sup_{x,y\in I}|f(x)-f(y)|=M-m\\\ \\
s_{\Delta}=\sum_{k\in K(\Delta)}m_kv(I_k),\quad m_k=\inf_{x\in I_k}f(x)\\\ \\
S_{\Delta}=\sum_{k\in K(\Delta)}M_kv(I_k),\quad M_k=\sup_{x\in I_k}f(x)$$
と定めると、これらはwell-defined。ここで、$a(f,I)$ を振幅、$s_{\Delta}$ を不足和、$S_{\Delta}$ を過剰和という。

    ・一番上の等式は上限、下限の定義を適当に足せばよい。

- 
$$mv(I)\le s_{\Delta}\le s(f,\Delta,\xi)\le S_{\Delta}\le Mv(I)\\\ \\
\Delta\sub\Delta'\Rightarrow s_{\Delta}\le s_{\Delta'}\le S_{\Delta'}\le S_{\Delta}\\\ \\
\forall\Delta_1,\Delta_2\in\mathcal{D}\text{ に対して、}s_{\Delta_1}\le S_{\Delta_2}$$
したがって、分割全体 $\mathcal{D}$ に対して、
$$\underline{\int}_Ifdx=\sup_{\Delta\in\mathcal{D}}s_{\Delta}=s(f)\\\ \\
\overline{\int}_Ifdx=\inf_{\Delta\in\mathcal{D}}S_{\Delta}=S(f)$$
はwell-defined、すなわちただ一つの実数。
<br>

    ・Δの分割は有限個であること、Iの分割では、軸に沿って全部同じ形に分割しないといけないことに注意。
<br>

</dt><dd>

- 
$$s(f)\le S(f)\\\ \\
g(x)\le f(x)\ \ (\forall x\in I)\Rightarrow s(g)\le s(f),\ S(g)\le S(f)$$


</dd></dl>

---

### 可積分条件

・有界閉区間 $I\sub\bm{R}^n$、有界関数 $f:I\to\bm{R}$ とする。
このとき、
$$\lim_{d(\Delta)\to0}s_{\Delta}=s(f),\quad \lim_{d(\Delta)\to0}S_{\Delta}=S(f)\\\ \\$$

- 有界関数 $f:I\to\bm{R}$ とする。
このとき、
$$f\text{ は }I\text{ 上可積分}\iff\lim_{d(\Delta)\to0}(S_{\Delta}-s_{\Delta})=0\\\ \\
\iff\lim_{d(\Delta)\to0}\sum_{k\in K(\Delta)}a(f,I_k)v(I_k)=0\\\ \\
\iff S(f)=s(f)\\\ \\
\forall\epsilon>0\text{ に対して、}\exist\text{ 分割 }\Delta\text{ であって、}S_{\Delta}-s_{\Delta}<\epsilon$$
さらに、上記が成り立つとき、
$$\int_If(x)dx=s(f)=S(f)$$

---

# ベクトル値関数の積分

<dl><dt>

・有界閉区間 $I\sub\bm{R}^n$、$f:I\to\bm{R}^m$、$J\in\bm{R}^m$ とする。
このとき、$$\int_Ifdx=J\iff\\\ \\
\forall\epsilon>0\text{ に対して、}\exist\delta>0\text{ であって、}\forall  d(\Delta)<\delta\text{ なる }I\text{ の分割 }\Delta,\ \forall\text{ 代表点 }\xi_k\in I_k\text{ に対して、}\\\ \\
\left|\sum_kf(\xi_k)v(I_k)-J\right|<\epsilon$$
と定める。明らかに、$f$ がリーマン可積分ならば、その積分値 $J$ は一意的に定まる。
<br>

</dt><dd>

- $$\sum_kf(\xi_k)v(I_k)=\left(\sum_kf_1(\xi_k)v(I_k),\ ...,\ \sum_kf_m(\xi_k)v(I_k)\right)$$
したがって、
$$f\text{ が }I\text{ 上可積分}\iff \text{すべての }f_i\text{ が }I\text{ 上可積分}$$
であって、このとき
$$\int_If(x)dx=\left(\int_If_1(x)dx,\ ...,\ \int_If_m(x)dx\right)$$


</dd></dl>

---

## 性質

<dl><dt>

・有界閉区間 $I\sub\bm{R}^n$、$v(I)>0$、$f:I\to\bm{R}^m$ とする。
このとき、$f$ が $I$ 上可積分ならば、$f$ は $I$ 上有界。
<br>

</dt><dd>

- $I$ 上可積分関数 $f,g$、$c\in\bm{R}$ とする。
このとき、$f+g,cf$ は $I$ 上可積分で、
$$\int_I (f+g)dx=\int_Ifdx+\int_Igdx\\\ \\
\int_I(cf)dx=c\int_Ifdx\\\ \\$$

- 平行移動 $T_c(x)=x+c$ とする。
このとき、
$$\int_{T_c(I)} fdx=\int_I(f\circ T_c)dx$$

</dd></dl>

---

### 性質 $2$

<dl><dt>

・有界閉区間 $I\sub\bm{R}^n$、$I$ 上可積分関数 $f:I\to\bm{R}^m$ とする。
<br>

</dt><dd>

- 
$$\text{すべての }k\in K(\Delta)\text{ に対して、}a(|f|,I_k)\le a(f_1,I_k)+...+a(f_m,I_k)$$
すなわち、$|f|$ は可積分で、
$$\left|\int_If(x)dx\right|\le\int_I|f(x)|dx$$


</dd></dl>

---

## 可積分条件

<dl><dt>

・有界閉区間 $I\sub\bm{R}^n$、有界関数 $f:I\to\bm{R}^m$、分割 $\Delta$、$M=\sup_{x\in I}f(x),m=\inf_{x\in I}f(x)$ とする。
このとき、
$$s_{\Delta}(f)=(s_{\Delta}(f_1),...,s_{\Delta}(f_m))\\\ \\
S_{\Delta}(f)=(S_{\Delta}(f_1),...,S_{\Delta}(f_m))\\\ \\
s(f)=(s(f_1),...,s(f_m))\\\ \\
S(f)=(S(f_1),...,S(f_m))$$
と定めると、これらはwell-defined。ここで、$a(f,I)$ を振幅、$s_{\Delta}$ を不足和、$S_{\Delta}$ を過剰和。$s(f)$ を下積分、$S(f)$ を上積分という。
<br>

</dt><dd>

- 有界閉区間 $I\sub\bm{R}^n$、有界関数 $f:I\to\bm{R}$ とする。
このとき、
$$\lim_{d(\Delta)\to0}s_{\Delta}=s(f),\quad \lim_{d(\Delta)\to0}S_{\Delta}=S(f)\\\ \\$$

- 有界関数 $f:I\to\bm{R}$ とする。
このとき、
$$f\text{ は }I\text{ 上可積分}\iff\lim_{d(\Delta)\to0}(S_{\Delta}-s_{\Delta})=0\\\ \\
\iff\text{ すべての }i\text{ に対して、}\lim_{d(\Delta)\to0}\sum_{k\in K(\Delta)}a(f_i,I_k)v(I_k)=0\\\ \\
\iff S(f)=s(f)\\\ \\
\forall\epsilon>0\text{ に対して、}\exist\text{ 分割 }\Delta\text{ であって、}|S_{\Delta}-s_{\Delta}|<\epsilon$$
さらに、上記が成り立つとき、
$$\int_If(x)dx=s(f)=S(f)$$

</dd></dl>

---





## 複素数値関数の積分

    ・性質とかはベクトル値と同じ。
<br>

<dl><dt>

・有界閉区間 $I\sub\bm{R}^n$、$f:I\to\bm{C}$、$J\in\bm{C}$ とする。
このとき、$$\int_Ifdx=J\iff\\\ \\
\forall\epsilon>0\text{ に対して、}\exist\delta>0\text{ であって、}\forall d(\Delta)<\delta\text{ なる }I\text{ の分割 }\Delta,\ \forall\text{ 代表点 }\xi_k\in I_k\text{ に対して、}\\\ \\
\left|\sum_kf(\xi_k)v(I_k)-J\right|<\epsilon$$
と定める。明らかに、$f$ がリーマン可積分ならば、その積分値 $J$ は一意的に定まる。
<br>

</dt><dd>

- $$\sum_kf(\xi_k)v(I_k)=\sum_k\mathrm{Re}[f](\xi_k)v(I_k)+i\sum_k\mathrm{Im}[f](\xi_k)v(I_k)$$
したがって、
$$f\text{ が }I\text{ 上可積分}\iff \mathrm{Re}[f],\ \mathrm{Im}[f]\text{ が }I\text{ 上可積分}$$
であって、このとき
$$\int_If(x)dx=\int_I\mathrm{Re}[f](x)dx+i\int_I\mathrm{Im}[f](x)dx\\\ \\$$

- 積分の線形性、


</dd></dl>


# 広義積分