
- [複素数値測度の積分](#複素数値測度の積分)



# 複素数値測度の積分

<dl><dt>

・可測空間 $(X,\mathfrak{M})$、複素数値測度 $\nu:\mathfrak{M}\to \bm{C}$、$\nu$ の全変動 $|\nu|$ に対するRadon-Nikodim微分 $h\in\mathcal{L}^1(X,|\nu|)$、$f\in\mathcal{L}^1(X,|\nu|)$ とする。
このとき、
$$\int_X fd\nu=\int_Xfhd|\nu|$$
と定めると、これはwell-defined。ここで、$\int_Xfd\nu$ を $f$ の $\nu$ による積分という。

</dt><dd>

- $|h(x)|=1\ \ (|\nu|-a.e.)$
<br>

- 測度空間 $(X,\mathfrak{M},\mu)$、非負値可測関数 $f,g:X\to[0,\infty]$とする。
このとき、
$$\int_Xgd\mu_f=\int_Xfgd\mu\\\ \\$$

      ・実数値、複素数値可積分関数でも同様で、可積分性の同値も以下と同じように成り立つ。

- 測度空間 $(X,\mathfrak{M},\mu)$、$f\in\mathcal{L}^1(X)$、複素数値可測関数 $g:X\to\bm{C}$ とする。
このとき、
$$g\in\mathcal{L}^1(X,|\mu_f|)\iff fg\in\mathcal{L}^1(X,\mu)\text{であって、}\\\ \\
\int_Xgd\mu_f=\int_Xfgd\mu\quad(\forall g\in\mathcal{L}^1(X,|\mu_f|))\\\ \\$$

      ・最後のgを含むLは、どうせ|h|=1だからこれでよい。
<br>

- 測度空間 $(X,\mathfrak{M},\mu)$、複素数値測度 $\nu:\mathfrak{M}\to\bm{C}$、$f\in\mathcal{L}^1(X)$、複素数値 $|\nu|-$可測関数 $g:X\to\bm{C}$ とする。
このとき、
$$\nu_f:\mathfrak{M}\to\bm{C}\\\ \\
\nu_f(E)=\int_Efd\nu$$
は複素数値測度で、
$$\nu_f(E)=|\nu|_{fh}(E)\quad(h:\nu\text{ の }|\nu|\text{ に関するRadon-Nikodim微分})\\\ \\
g\in\mathcal{L}^1(X,|\nu_f|)\iff fg\in\mathcal{L}^1(X,|\nu|)\\\ \\
\int_Xgd\nu_f=\int_Xfgd\nu\quad(\forall g\in\mathcal{L}^1(X,|\nu_f|))\\\ \\$$

      ・これはμ関係ない。
      ・最後のgを含むLは、どうせ|h|=1だからこれでよい。

</dd></dl>

---