
- [ガウス関数](#ガウス関数)
  - [ガウス関数とフーリエ変換](#ガウス関数とフーリエ変換)
- [超関数を考えるフーリエ変換](#超関数を考えるフーリエ変換)
  - [$f(x)=b$](#fxb)




# ガウス関数

<dl><dt>

・
$$g_N:\bm{R}^N\to(0,\infty)\\\ \\
g_N(x)=\exp\left(-\frac{|x|^2}{2}\right)$$
と定めると、$g_N$ は値域がwell-definedな $C^{\infty}$ 関数。
<br>

</dt><dd>

- $$\left(\int_{\bm{R}}g_1(x)dm(x)\right)^2=\int_{\bm{R}^2}g_2(x,y)dm(x)dm(y)=2\pi\\\ \\$$

      ・非負値Borel関数だから、可積分性は関係ない。
<br>

- $$\forall x\in\bm{R}\text{ に対して、}\frac{dg_1}{dx}+xg_1(x)=0\\\ \\$$

- $g_N\in\mathcal{S}_N$

</dd></dl>

---

## ガウス関数とフーリエ変換

・$$\mathcal{F}_{g_N}=\mathcal{F}^{\vee}_{g_N}=g_N\\\ \\$$

---

# 超関数を考えるフーリエ変換

## $f(x)=b$

    ・デルタ関数出てくる。

・$$\frac{1}{(2\pi)^{1/2}}\int be^{ikx}dk=\sqrt{2\pi}\delta(x)$$

    ・逆変換も同じっぽい？