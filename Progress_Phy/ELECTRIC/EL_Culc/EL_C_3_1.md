
- [電気回路（準定常電流）](#電気回路準定常電流)
        - [直列$RL$回路](#直列rl回路)
        - [直列RLC回路](#直列rlc回路)
        - [平面に垂直な一様磁場内の導体棒](#平面に垂直な一様磁場内の導体棒)
        - [無限に長い直線電流と回路](#無限に長い直線電流と回路)
        - [平行版コンデンサー](#平行版コンデンサー)
- [運動する電気回路](#運動する電気回路)



# 電気回路（準定常電流）

・インダクタンス

    ・自己：自分が作る磁場が、自分を貫く磁束を求める
    ・相互：別の回路が作る磁場が、自分を貫く磁束を求める

- 一方の電流を $0\to I_2$ に増加させるために必要なエネルギー：$\frac{1}{2}L_2I_2^2$、電流を流し続けるために必要なエネルギー：$L_{12}I_1I_2$    

## 直列$RL$回路

・解くべき方程式
$L\frac{dI}{dt}(t)+RI(t)=V(t)$

→$V(t)=V_0,\ I(0)=0$のとき：
$$I(t)=\frac{LV_0}{R}(1-e^{-\frac{R}{L}}t)$$

→$V(t)=V_0e^{i\omega t},\ I(0)=0$のとき：
$$I(t)=\frac{V_0(R-iL\omega)}{R^2+\omega^2L^2}(e^{i\omega t}-e^{-\frac{R}{L}t})$$

    ・V_0cosωtとかのとき、V_0e^{iωt}として解いても答えは一致する


---

## 直列RLC回路

・強制振動：$L\frac{dI}{dt}+RI-\frac{Q}{C}=\tilde{\phi}e^{i\omega t}$ の特解 
$$I'(t)=\frac{\tilde{\phi}}{Z}e^{i(\omega t-\theta)}$$

- インピーダンス：$Z=\sqrt{R^2+(\omega L-\frac{1}{\omega C})}$
- 位相：$$\tan\theta=\frac{\omega L-\frac{1}{\omega C}}{R}$$

    ・強制振動の特解のこと


---

## 平面に垂直な一様磁場内の導体棒

    電子に働く力、誘導起電力

---

## 無限に長い直線電流と回路

・長方形回路の横辺が直線電流$I$に平行なとき（平行な辺の長さ$a$、もう一方の辺$b$、直線電流と辺の最短距離$h$）

→回路を貫く磁束：$N_s=-\frac{\mu_0I}{2\pi}a\log(\frac{b+h}{h})$
→相互インダクタンス：$L_{ls}=-\frac{\mu_0a}{2\pi}\log(\frac{b+h}{h})$
→回路に流れる電流：$I_s=0$

    ・回路は電流の右側に置いた

---

## 平行版コンデンサー

・面積$S$、間隔$d$、両端の電位差$V(t)$とする

→電束密度：$D=-\frac{Q(t)}{S}e_{z}=-\frac{V(t)}{\epsilon_0 d}e_{z}$
→静電容量：$C=\frac{\epsilon_0 S}{d}$
→導線に流れる電流：$I(t)=-\frac{\epsilon_0 S}{d}\frac{dV}{dt}$
→極版間の磁場：$B(x,t)=-\frac{\mu_0\epsilon_0r}{2d}\frac{dV}{dt}e_{\theta}$
→ポインティングベクトル：$S(\bm{x},t)=\frac{1}{4\epsilon_0S^2}(\frac{d}{dt}Q(t)^2)\bm{x}=\frac{\epsilon_0}{4d^2}(\frac{d}{dt}V(t)^2)\bm{x}$

    ・極版上で電荷密度σは一様とする（大きさ等しい）
    ・極版間で電場Eは位置によらないので、静電容量Cの定義は整合する
    ・磁場Bは電流密度i_eとの類似で求める
    ・電流の流れる向きを正とする


---


