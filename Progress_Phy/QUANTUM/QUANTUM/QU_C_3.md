
- [外部磁場中にある電子（$1/2$スピン）](#外部磁場中にある電子12スピン)
  - [スピン歳差運動](#スピン歳差運動)
  - [回転と交換関係](#回転と交換関係)
  - [時間発展と期待値：](#時間発展と期待値)



# 外部磁場中にある電子（$1/2$スピン）

    ・フィルターに着く途中の位置を測定しようとすればまた変わる

・ヒルベルト空間は二次元：$\ket{\alpha}=c_+\ket{+}+c_-\ket{-}$

→$z$方向：
$$S_z=\frac{\hbar}{2}\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$$

- $\ket{+}=(1,0)$

---

・$x$方向：$\ket{S_x,\pm}=\frac{1}{\sqrt{2}}\ket{+}\pm\frac{1}{\sqrt{2}}\ket{-}$
- $$S_x=\frac{\hbar}{2}\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$$

- $y$方向：$\ket{S_y,\pm}=\frac{1}{\sqrt{2}}\ket{+}\pm\frac{i}{\sqrt{2}}\ket{-}$
- $$S_y=\frac{\hbar}{2}\begin{pmatrix}0 & -i \\ i & 0\end{pmatrix}$$

        ・右手系を用いた
        ・基準としてS_xの行列要素を正に指定した

---

・交換関係：$[S_i,S_j]=\epsilon_{ijk}i\hbar S_k$

- 反交換関係：$\{S_i,S_j\}=\frac{1}{2}\hbar^2\delta_{ij}$

- 二乗演算子 $S^2=S_{i}S_i=\frac{3}{4}\hbar^2$
-  $[S^2,S_i]=0$

---

・期待値：

---

・昇降演算子：$S_+=\hbar\ket{+}\bra{-},\ S_-=\hbar\ket{-}\bra{+}$

    ・スピンを上げ下げする

→$$S_+=\hbar\begin{pmatrix}0 & 1 \\ 0 & 0\end{pmatrix},\quad S_-=\hbar\begin{pmatrix}0 & 0 \\ 1 & 0\end{pmatrix}$$

→$S_{\pm}=S_x\pm iS_y$

---

## スピン歳差運動

・外部磁場 $B(x)$ 中の磁気モーメント $\frac{e\hbar}{2m_ec}$ を持つ一個のスピン$1/2$ 系

- ハミルトニアン：$H=-\frac{e}{m_ec}S\cdot B(x)$

    ・磁気回転比gが着くかもしれないが、定数倍の差しかしない
    ・普通に磁気モーメントから導ける式

---

・$B=Be_z$のとき：$H=\omega S_z,\quad \omega=\frac{|e| B}{m_ec},\quad(e<0)$

- エネルギー固有値：$E_{\pm}=\pm \omega\frac{\hbar}{2},\quad(\ket{\pm})$

- 明らかに $H$ と $S_z$ は交換する
- エネルギー固有値の差：$\hbar\omega$
- 時間発展演算子：$\mathcal{U}(t,0)=\exp(\frac{-i\omega S_zt}{\hbar})$

---

## 回転と交換関係

・$z$軸周りの回転 $\mathcal{D}_z(\phi)=\exp(\frac{-iS_z\phi}{\hbar})$

---

## 時間発展と期待値：
$$c_+\ket{+}+c_-\ket{-}\to c_+\exp\left(\frac{-i\omega t}{2}\right)\ket{+}+c_-\exp\left(\frac{i\omega t}{2}\right)\ket{-}$$

- $\ket{+}\to\exp(\frac{-i\omega t}{2})\ket{+}$ したがって $\ket{\pm}$ は向きを変えない

        ・定常状態だからそりゃそう

・$\ket{S_x;+}=\frac{1}{\sqrt{2}}\ket{+}+\frac{1}{\sqrt{2}}\ket{-}$

- 時間発展後に$\ket{S_x;\pm}$である確率：
$$|\braket{S_x;\pm|S_x;+;0\to t}|^2=\begin{cases}
\cos^2\frac{\omega t}{2} & \ket{S_x;+}   \\
\sin^2\frac{\omega t}{2} & \ket{S_x;-}   \\
\end{cases}$$

        ・z軸方向の磁場は+x方向のスピンを回転させた
        ・確かに全確率1

- $x$期待値 $\braket{S_x}_{S_x;+;t}=\frac{\hbar}{2}\cos\omega t$

        ・確かに(エネルギー差)/hで振動している

- $y$確率：$$|\braket{S_y;\pm|S_x;+;0\to t}|^2=\begin{cases}
\frac{1}{2}(1+\sin\omega t) & \ket{S_x;+}   \\
\frac{1}{2}(1-\sin\omega t) & \ket{S_x;-}   \\
\end{cases}$$
- $y$期待値 $\braket{S_y}_{S_x;+;t}=\frac{\hbar}{2}\sin\omega t$

- $z$確率：$|\braket{\pm|S_x;+;0\to t}|^2=\frac{1}{2}$
- $z$期待値：$\braket{S_z}_{S_x;+;t}=0$

---