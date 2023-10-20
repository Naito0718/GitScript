
- [リーマン積分](#リーマン積分)
  - [性質](#性質)
    - [連続関数](#連続関数)
  - [下積分と上積分](#下積分と上積分)
    - [可積分条件](#可積分条件)
- [広義積分](#広義積分)



# リーマン積分

## 性質

<dl><dt>

・有界閉区間 $I\sub\bm{R}^n$、$v(I)>0$、$f:I\to\bm{R}$ とする。
このとき、$f$ が $I$ 上可積分ならば、$f$ は $I$ 上有界。

    ・よって、だいたい可積分と言ったら有界性を仮定してよい。

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
$$\exist\mu\in\bm{R}\text{ であって、}\int_If=\mu v(I),\quad m\le\mu\le M$$
特に、$f$ が $I$ 上連続ならば、$\exist\xi\in I$ であって、$f(\xi)=\mu$

      ・第一平均値定理。

- 体積 $v(I)$ は平行移動 $T_c(x)=x+c$ で不変。
また、
$$\int_{T_c(I)} fdx=\int_I(f\circ T_c)dx$$


</dd></dl>

---

・$I=[a,b]\sub\bm{R}$、$I$ 上単調増加または単調減少な有界関数 $f$ とする。
このとき、$f$ は可積分。

---

### 連続関数

---

## 下積分と上積分


<dl><dt>

・有界閉区間 $I\sub\bm{R}^n$、有界関数 $f:I\to\bm{R}$、分割 $\Delta$、$M=\sup_{x\in I}f(x),m=\inf_{x\in I}f(x)$ とする。
このとき、振幅 $a(f,I)$、不足和 $s_{\Delta}$、過剰和 $S_{\Delta}$：
$$a(f,I)=\sup_{x,y\in I}|f(x)-f(y)|=M-m\\\ \\
s_{\Delta}=\sum_{k\in K(\Delta)}m_kv(I_k),\quad m_k=\inf_{x\in I_k}f(x)\\\ \\
S_{\Delta}=\sum_{k\in K(\Delta)}M_kv(I_k),\quad M_k=\sup_{x\in I_k}f(x)$$

    ・有界なので、上限、下限は存在する。また、一番上の等式は上限、下限の定義を適当に足せばよい。

- 
$$mv(I)\le s_{\Delta}\le S_{\Delta}\le Mv(I)\\\ \\
\Delta\sub\Delta'\Rightarrow s_{\Delta}\le s_{\Delta'}\le S_{\Delta'}\le S_{\Delta}\\\ \\
$$
したがって、分割全体 $\mathcal{D}$ に対して、
$$\underline{\int}_Ifdx=\sup_{\Delta\in\mathcal{D}}s_{\Delta}=s(f)\\\ \\
\overline{\int}_Ifdx=\inf_{\Delta\in\mathcal{D}}S_{\Delta}=S(f)$$
が意味を持つ。

    ・細分：大きい方が細かい。

</dt><dd>

- 
$$s(f)\ge S(f)\\\ \\
g(x)\le f(x)\ \ (\forall x\in I)\Rightarrow s(g)\le s(f),\ S(g)\le S(f)$$


</dd></dl>

---

### 可積分条件

・有界閉区間 $I\sub\bm{R}^n$、有界関数 $f:I\to\bm{R}$ とする。
このとき、
$$\lim_{d(\Delta)\to0}s_{\Delta}=s(f),\quad \lim_{d(\Delta)\to0}S_{\Delta}=S(f)$$

      ・ダルブーの定理。

- 有界関数 $f:I\to\bm{R}$ とする。
このとき、
$$f\text{ は }I\text{ 上可積分}\iff\lim_{d(\Delta)\to0}(S_{\Delta}-s_{\Delta})=0\\\ \\
\iff\lim_{d(\Delta)\to0}\sum_{k\in K(\Delta)}a(f,I_k)v(I_k)=0\\\ \\
\iff S(f)=s(f)\\\ \\
\forall\epsilon>0\text{ に対して、}\exist\text{ 分割 }\Delta\text{ であって、}S_{\Delta}-s_{\Delta}<\epsilon$$
さらに、上記が成り立つとき、$\int_Ifdx=s(f)=S(f)$

---


# 広義積分