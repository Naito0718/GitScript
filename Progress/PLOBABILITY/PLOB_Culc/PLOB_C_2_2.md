
- [一様分布 $U(a,b)$](#一様分布-uab)
  - [簡単な積分](#簡単な積分)
- [指数分布 $Exp(λ)$](#指数分布-expλ)
  - [簡単な積分](#簡単な積分-1)
- [両側指数分布 $WExp(a,λ)$](#両側指数分布-wexpaλ)
  - [簡単な積分](#簡単な積分-2)
- [ガンマ分布 $Γ(α,β)$](#ガンマ分布-γαβ)
  - [積分と正則性](#積分と正則性)
- [正規分布 $N(μ,σ^2)$](#正規分布-nμσ2)
  - [一次元熱核](#一次元熱核)
- [コーシー分布 $Ca(μ,σ^2)$](#コーシー分布-caμσ2)
  - [一次元コーシー核](#一次元コーシー核)




# 一様分布 $U(a,b)$

・$(a,b)\sub\bm{R}$ とし、
$$f:\bm{R}\to\bm{R}\\\ \\
f(x)=\frac{1}{b-a}\chi_{(a,b)}(x)$$
とする。このとき、
$$\mu:\mathfrak{B}_{\bm{R}}\to[0,1]\\\ \\
\mu(B)=\int_Bfdm=\frac{1}{b-a}\int_{B\cap(a,b)}dm$$
と定めると、これは $1$ 次元絶対連続分布。ここで、$\mu$ を一様分布という。

---

## 簡単な積分

・$c\in\bm{C}-\{0\}$ とする。
このとき、
$$\int_{\bm{R}}e^{cx}d\mu=\frac{e^{cb}-e^{ca}}{c(b-a)}\\\ \\$$

- 
$$\int_{\bm{R}}xd\mu=\frac{b+a}{2}\\\ \\
\int_{\bm{R}}x^2d\mu=\frac{a^2+ab+b^2}{3}\\\ \\$$

---

# 指数分布 $Exp(λ)$

・$\lambda>0$ とし、
$$f:\bm{R}\to\bm{R}\\\ \\
f(x)=\lambda e^{-\lambda x}\chi_{(0,\infty)}(x)$$
とする。このとき、
$$\mu:\mathfrak{B}_{\bm{R}}\to[0,1]\\\ \\
\mu(B)=\int_Bfdm=\lambda\int_{B\cap(0,\infty)}e^{-\lambda x}dm(x)$$
と定めると、これは $1$ 次元絶対連続分布。ここで、$\mu$ を指数分布という。

---

## 簡単な積分

・$c\in\bm{C}$ とする。
このとき、
$$\mathrm{Re}(c)<\lambda\\\ \\
\Rightarrow\int_{\bm{R}}e^{cx}d\mu=\frac{\lambda}{\lambda-c}\\\ \\$$

- $n\in\bm{N}$ とする。
このとき、[ガンマ関数](C:/Users/naitodaichi/GitScript/Progress/COMPANAL/CA_C/CA_C_3_2.md) より、
$$\int_{\bm{R}}t^nd\mu(t)=\frac{n!}{\lambda^{n+1}}\\\ \\$$



---

# 両側指数分布 $WExp(a,λ)$

・$a\in\bm{R},\ \lambda>0$ とし、
$$f:\bm{R}\to\bm{R}\\\ \\
f(x)=\frac{\lambda e^{-\lambda |x-a|}}{2}$$
とする。このとき、
$$\mu:\mathfrak{B}_{\bm{R}}\to[0,1]\\\ \\
\mu(B)=\int_Bfdm=\frac{\lambda}{2}\int_{B}e^{-\lambda |x-a|}dm(x)$$
と定めると、これは $1$ 次元絶対連続分布。ここで、$\mu$ を指数分布という。

---

## 簡単な積分

・$c\in\bm{C}$ とする。
このとき、
$$|\mathrm{Re}(c)|<\lambda\\\ \\
\Rightarrow\int_{\bm{R}}e^{cx}d\mu=\frac{\lambda^2e^{ca}}{\lambda^2-c^2}\\\ \\$$

- 
$$\int_{\bm{R}}xd\mu=a\\\ \\
\int_{\bm{R}}x^2d\mu=a^2+\frac{2}{\lambda^2}\\\ \\$$

---

# ガンマ分布 $Γ(α,β)$

・$\alpha,\beta>0$ とし、
$$f:\bm{R}\to\bm{R}\\\ \\
f(x)=\frac{\beta^{\alpha}}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x}\chi_{(0,\infty)}$$
とする。このとき、
$$\mu:\mathfrak{B}_{\bm{R}}\to[0,1]\\\ \\
\mu(B)=\int_Bfdm=\frac{\beta^{\alpha}}{\Gamma(\alpha)}\int_{B\cap(0,\infty)}x^{\alpha-1}e^{-\beta x}dm(x)$$
と定めると、これは $1$ 次元絶対連続分布。ここで、$\mu$ をガンマ分布といい、$\alpha$ を指数という。
<br>

- $\Gamma(1,\beta)=Exp(\beta)$, すなわち、ガンマ分布は指数分布の拡張であり、指数 $1$ のガンマ分布は指数分布である。
また、$n\in\bm{N}-\{0\}$ に対して、$\Gamma(n,\beta)=Erl(n,\beta)$ をアーラン分布といい、$\Gamma(\frac{n}{2},\frac{1}{2})$ を 自由度 $n$ の $\chi^2$ 分布という。

---

## 積分と正則性

<dl><dt>

ガンマ分布 $\Gamma(\alpha,\beta)$ としての $\mu$ とする。

</dt><dd>

|**$Plob-C-\Gamma- 1$** <br> ([$CompAnal-2-3$ 参照](Progress\COMPANAL\CompAnal_2_2.md))|
|:-|

$\mathrm{Re}(z)<\beta$ なる $z\in\bm{C}$ とする。
このとき、
$$\int_{\bm{R}}e^{zx}d\mu(x)=\frac{\beta^{\alpha}}{(\beta-z)^{\alpha}}\\\ \\$$
>qed,確率論p.37（岩田）

<br>

|**$Plob-C-\Gamma- 2$**|
|:-|

$n\in\bm{N}$ とする。
このとき、
$$\int_{\bm{R}}x^{n}d\mu(x)=\beta^{-n}\alpha(\alpha+1)...(\alpha+n-1)=\beta^{-n}\Pi_{k=0}^{n-1}(\alpha+k)\\\ \\$$
>qed,確率論p.37（岩田）


</dd></dl>


# 正規分布 $N(μ,σ^2)$

・$\mu,\sigma\in\bm{R}$ とし、
$$f:\bm{R}\to\bm{R}\\\ \\
f(x)=\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$
とする。このとき、
$$\mu:\mathfrak{B}_{\bm{R}}\to[0,1]\\\ \\
\mu(B)=\int_Bfdm=\frac{1}{\sqrt{2\pi\sigma^2}}\int_{B}e^{-\frac{(x-\mu)^2}{2\sigma^2}}dm(x)$$
と定めると、これは $1$ 次元絶対連続分布。ここで、$\mu$ を正規分布という。また、$N(0,1)$ を標準正規分布という。


---





---

## 一次元熱核

<dl><dt>

・$$f:(0,\infty)\times\bm{R}\to\bm{R}\\\ \\
f(\sigma,x)=\frac{1}{\sqrt{4\pi t}}e^{-\frac{x^2}{4t}}$$
と定めると、$t$ を固定した時、これは中心 $0$、幅 $\sqrt{2t}$ の正規分布 $N(0,\sqrt{2t}^2)$である。ここで、$f$ を一次元熱核という。
<br>

</dt><dd>



</dd></dl>


---

# コーシー分布 $Ca(μ,σ^2)$

・$\mu\in\bm{R},\sigma>0$ とし、
$$f:\bm{R}\to\bm{R}\\\ \\
f(x)=\frac{\sigma}{\pi}\frac{1}{(x-\mu)^2+\sigma^2}$$
とする。このとき、
$$\mu:\mathfrak{B}_{\bm{R}}\to[0,1]\\\ \\
\mu(B)=\int_Bfdm=\frac{\sigma}{\pi}\int_{B}\frac{1}{(x-\mu)^2+\sigma^2}dm(x)$$
と定めると、これは $1$ 次元絶対連続分布。ここで、$\mu$ をガンマ分布という。

---

## 一次元コーシー核

<dl><dt>

・$$f:(0,\infty)\times\bm{R}\to\bm{R}\\\ \\
f(\sigma,x)=\frac{\sigma}{\pi}\frac{1}{x^2+\sigma^2}$$
と定めると、$\sigma$ を固定した時、これは中心 $0$、幅 $\sigma$ のコーシー分布 $Ca(0,\sigma^2)$である。ここで、$f$ を一次元コーシー核という。
<br>

</dt><dd>



</dd></dl>


