
    ・真空中の静電磁場では電場と磁場が分離する！

- [静電場](#静電場)
  - [静電ポテンシャル $Φ$](#静電ポテンシャル-φ)
- [静磁場](#静磁場)
  - [ゲージ変換とベクトルポテンシャル $A$](#ゲージ変換とベクトルポテンシャル-a)
- [わからないこと](#わからないこと)



# 静電場

    ・現象論的近似が成り立つ場合も同様。

・真空中の静電場を記述する方程式：
$$\mathrm{rot}\ E(x)=0\\\ \\
\mathrm{div}\ E(x)=\frac{1}{\epsilon}\rho_e(x)$$

---

## 静電ポテンシャル $Φ$

・静電ポテンシャル $\phi(x)$ を用いると、真空中の静電場は以下の方程式に従う。
$$E(x)=-\mathrm{grad}\ \phi(x)\\\ \\
\Delta \phi(x)=-\frac{1}{\epsilon} \rho_e(x)\\\ \\$$したがって、グリーン関数解法より、
$$\phi(x)=\frac{1}{4\pi\epsilon}\int_{-\infty}^{\infty}\frac{\rho_e(x')}{|x-x'|}d^3x'\\\ \\
E(x)=\frac{1}{4\pi\epsilon}\int_{-\infty}^{\infty}\frac{\rho_e(x')}{|x-x'|^3}(x-x')d^3x'\\\ \\$$

      ・これはゲージ変換ない。
      ・積分と偏微分の交換？


---

# 静磁場

・真空中の静磁場を記述する方程式：
$$\mathrm{rot}\ B(x)=\mu i_e(x)\\\ \\
\mathrm{div}\ B(x)=0\\\ \\$$

---

## ゲージ変換とベクトルポテンシャル $A$

- ベクトルポテンシャル $A(x)$ を用いると、静磁場は、以下の方程式に従う。
$$B(x)=\mathrm{rot}\ A(x)\\\ \\
\Delta A(x)=-\mu i_e(x)\\\ \\
\mathrm{div}\ A(x)=0\\\ \\$$
ただし、$\mathrm{div} A=0$ はゲージ変換による。したがって、グリーン関数解法より、
$$A(x)=\frac{\mu}{4\pi}\int_{-\infty}^{\infty}\frac{i_e(x')}{|x-x'|}d^3x'\\\ \\
B(x)=\frac{1}{4\pi\epsilon}\int_{-\infty}^{\infty}\frac{\rho_e(x')}{|x-x'|^3}(x-x')d^3x'\\\ \\$$
<br>

      ・クーロンゲージ


# わからないこと

・パラメータに関するdivとかと、積分の交換。
・デルタ関数。
・発散定理。
・$\int\frac{1}{|x-x'|}dx'^3$ のラプラシアンが0であることと、デルタ関数を用いた$\Delta\frac{1}{|x-x'|}$ の記述。
・Dirichlet問題とNeumann問題。
・Green関数。