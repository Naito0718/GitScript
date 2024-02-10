
- [電荷](#電荷)
  - [対称性を含む系](#対称性を含む系)
    - [テクニック](#テクニック)
    - [球対称な電荷分布](#球対称な電荷分布)
    - [円周 $a$ 上の一様電荷分布](#円周-a-上の一様電荷分布)
    - [ポテンシャルから電荷密度を決定する問題](#ポテンシャルから電荷密度を決定する問題)







# 電荷

## 対称性を含む系

### テクニック



・球対称ラプラシアン：
$$\Delta\phi(r)=\frac{1}{r}\frac{d^2}{dr^2}\left(r\phi(r)\right)=\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{d}{dr}\phi(r)\right)$$

---

### 球対称な電荷分布 

$$\bm{\rho(r)}$$

・半径$r$内の全電荷：$e(r)=4\pi\int_0^r\rho_e(r')r'^2 dr'$

→静電ポテンシャル：
$$\phi(r)=\frac{e(r)}{4\pi\epsilon_0 r}+\frac{1}{\epsilon_0}\int_r^{\infty}r'\rho_e(r)dr'$$

---


・電荷密度が半径$a$の球領域に含まれるとき

→静電ポテンシャル：$\phi(r)=\begin{cases}
\phi(r)=\frac{e(r)}{4\pi\epsilon_0 r}+\frac{1}{\epsilon_0}\int_r^{a}r'\rho_e(r)dr'  & (r<a)  \\
\frac{e(a)}{4\pi\epsilon_0 r}  & (r\ge a)  \\
\end{cases}$

→$E(r)=\begin{cases}
\frac{e(r)}{4\pi\epsilon_0 r^2}\bm{e_r}  & (r<a)  \\
\frac{e(a)}{4\pi\epsilon_0 r^2}\bm{e_r}  & (r\ge a)  \\
\end{cases}$

---

### 円周 $a$ 上の一様電荷分布

・静電ポテンシャル：：$\phi=\frac{\lambda}{4\pi\epsilon_0}\int_0^{2\pi}\frac{a}{\sqrt{r^2+a^2+z^2-2ar\cos\theta}}d\theta$

- 電場 $E=\frac{\lambda}{4\pi\epsilon_0}\int_0^{2\pi}\frac{1}{|x-x'|^3}(x-x')ad\theta$

---
・$z$ 軸上の電場：$E=\frac{\lambda}{2\epsilon_0}\frac{az}{(\sqrt{z^2+a^2})^3}$

    ・磁場とはちょっと違う

・解くべき方程式：$$\phi=\frac{\lambda}{4\pi\epsilon_0}\sqrt{\frac{a}{2r}}\alpha(R),\quad \alpha(R)=\int_0^{2\pi}\frac{1}{\sqrt{R^2-\cos\theta}}d\theta\\\ \\
R=\sqrt\frac{r^2+a^2+z^2}{2ar}>1$$

- $$\alpha(R)=\frac{4}{\sqrt{R^2-1}}\int_0^{\frac{\pi}{2}}\frac{1}{\sqrt{1-m\sin^2\psi}}d\psi,\quad m=-\frac{2}{R^2-1}<0$$

        ・第一種完全楕円積分？

---

・この円環を角速度 $\omega (e_z)$ で回転させたとき

- 電流密度：$i_e=\lambda a\omega e_{\theta}$

---

### ポテンシャルから電荷密度を決定する問題

→ $\Delta\phi=0$になるときもある

    ・一様な電場とか

・$$\phi(r)=\frac{q}{4\pi\epsilon_0}\frac{e^{-\lambda r}}{r}$$

    ・湯川ポテンシャル

→$\rho_e(r)=q\delta(r)-\frac{q}{4\pi}\frac{\lambda^2 e^{-\lambda r}}{r}$

    ・第一項は後ろの項がr→0で発散してしまうため必要、(～)1/rのラプラシアン取った

---
---
---

