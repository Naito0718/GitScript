

# 二変数

## 古典ディリクレ問題

・単位開円板 $D$、単位円周 $\Gamma$、$f\in C_{\#}(-\pi,\pi)$、$F\in C^2(D)\cap C^0(D\cup\Gamma)$ とする。
このとき、$L^2$ でのディリクレ問題：
$$\Delta F(x,y)=0\text{ であって、}F(e^{i\theta})=f(\theta)$$

    ・P_r*f,fは連続なので、a.e.でなく全体で等しくなる。

---

## $L^2$ ディリクレ問題

・単位開円板 $D$、$f\in L^2(-\pi,\pi)$、$F\in C^2(D)$ とする。
このとき、$L^2$ でのディリクレ問題：
$$\Delta F(x,y)=0\text{ であって、}\lim_{r\to1}\int_{-\pi}^{\pi}|F(re^{i\theta})-f(\theta)|^2d\theta=0$$

    ・結局古典的な場合を含む。

## $L^2$ ノイマン問題

・単位開円板 $D$、$f\in L^2(-\pi,\pi)$、$F\in C^2(D)$ とする。
このとき、$L^2$ でのディリクレ問題：
$$\Delta F(x,y)=0\text{ であって、}\lim_{r\to1}\int_{-\pi}^{\pi}\left|\frac{\partial}{\partial r}F(re^{i\theta})-f(\theta)\right|^2d\theta=0$$

    ・結局古典的な場合を含む。
    ・これは完全なPoisson積分ではない。


---

# 三変数

## rot $A=b$

・$b\in\bm{R}^3$ とする。
$$\mathrm{rot}A=b$$
としたとき、
一般解：
$$A=\mathrm{grad}\psi+b\times\bm{r}\quad(\psi\text{ は任意関数})$$

    ・解ける！


---

# 一般の $N$

## 熱伝導方程式

・$p\in[1,\infty]$、$f\in L^p(\bm{R}^N)$ とする。
