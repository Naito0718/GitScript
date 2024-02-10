
- [半加群](#半加群)
  - [半加群準同型](#半加群準同型)
  - [普遍加群](#普遍加群)
- [単位的可換半環](#単位的可換半環)
  - [単位的可換半環準同型](#単位的可換半環準同型)
  - [普遍環](#普遍環)
- [](#)


# 半加群

    ・可換モノイドのこと

## 半加群準同型

・半加群 $A,B$、$f:A\to B$ とする。
このとき、
$$f(0_A)=0_B\\\ \\
f(a\oplus b)=f(a)\oplus f(b)\\\ \\$$

- 全単射な半加群準同型 $f$ とすると、$f^{-1}$ は半加群準同型。

---

## 普遍加群

    ・Grothendieck加群

<dl><dt>

・半加群 $M$ とする。
このとき、
$$\exist \text{ 加群 }A(M),\exist\text{ 半加群準同型 }\tau:M\to A(M)\text{ であって、}\\\ \\
\forall\text{ 加群 }A,\forall\text{ 半加群準同型 }\phi:M\to A\text{ に対して、}\exist\ !\text{ 加群準同型 }\psi:A(M)\to A\\\ \\
\phi=\psi\circ\tau$$ここで、$(A(M),\tau)$ を普遍化群という。

    ・τは準同型！

</dt><dd>

- 普遍加群 $(A(M)_1,\tau_1),(A(M)_2,\tau_2)$ とする。
このとき、$\tau_2=f\circ \tau_1$ を満たす加群同型
$$f:A(M)_1\to A(M)_2$$がただ一つ存在する。 

- $$\tau(a\oplus b)=\tau(a)+\tau(b)\\\ \\$$

- 加群 $A$、$\phi:M\to A$ とする。
このとき、$\phi$ が単射ならば、$\psi$ は単射。
<br>

- 半加群同型な半加群 $M,N,\ M\cong N\ (\text{半加群同型})$、普遍加群 $A(M),A(N)$ とする。
このとき、$A(M)\cong A(N)\ \text{加群同型}$ であり、$A(N)$ は $M$ の普遍加群。
<br>

- - $$A(M)=M\times M/\sim,\quad (a_1,b_1)\sim (a_2,b_2)\iff\exist x,y\in M\text{ であって、}a_1\oplus x=a_2\oplus x,\ b_1\oplus y=b_2\oplus y\\\ \\
\tau(a)=[a,0]\\\ \\
\psi([a,b])=\phi(a)-\phi(b)$$と定めると、$(A(M),\tau)$ は普遍加群。
<br>

  - 上記の普遍加群 $A(M)$ において、
  $$0_{A(M)}=[0,0]\\\ \\
  -[a,b]=[b,a]\\\ \\
  \forall x\in A(M)\text{ に対して、}\exist a,b\in M\text{ であって、} x=\phi(a)-\phi(b)$$ 

- - $F(M)$ を $M$ から生成される自由化群とする。このとき、
$$A(M)=F(M)/I(M),\quad I(M)=\lang\{a\oplus b-a-b\ |\ a,b\in M\}\rang\sub F(M)\\\ \\
\tau(a)=[a]\\\ \\
\psi([m_1a_1+...+m_na_n])=m_1\phi(a_1)+...+m_n\phi(a_n)$$ は普遍加群。

        ・可換モノイドなら自然数倍とかが存在する。

  - 上記の普遍加群 $A(M)$ において、
  $$0_{A(M)}=[0]=I(M)\\\ \\
  -[x]=[-x]\\\ \\
  [a\oplus b]=[a+b]
  \forall x\in A(M)\text{ に対して、}\exist a,b\in M\text{ であって、} x=\phi(a)-\phi(b)$$ 

        ・可換モノイドなら自然数倍とかが存在する。

</dd></dl>

---

# 単位的可換半環

・$0=0\otimes0=0\otimes1=0\otimes(1\oplus 1)=...$

    ・0×a=0は言えないっぽい

## 単位的可換半環準同型

・単位的可換半環 $M,N$、$f:M\to N$ とする。
このとき、半環準同型：
$$f(1_M)=1_N\\\ \\
f(a\otimes b)=f(a)\otimes f(b)\\\ \\$$

- 全単射な半環準同型 $f$ とすると、$f^{-1}$ は半環準同型。

---

## 普遍環

    ・Grothendieck環

<dl><dt>

・単位的可換半環 $M$ とする。
このとき、
$$\exist \text{ 単位的可換環 }R(M),\exist\text{ 半環準同型 }\tau:M\to R(M)\text{ であって、}\\\ \\
\forall\text{ 単位的可換環 }A,\forall\text{ 半環準同型 }\phi:M\to A\text{ に対して、}\exist\ !\text{ 環準同型 }\psi:R(M)\to A\text{ であって、}\\\ \\
\phi=\psi\circ\tau$$ここで、$(R(M),\tau)$ を普遍環という。

    ・τは半環準同型！

</dt><dd>

- 普遍環 $(R(M)_1,\tau_1),(R(M)_2,\tau_2)$ とする。
このとき、$\tau_2=f\circ \tau_1$ を満たす環同型
$$f:A(M)_1\to A(M)_2$$がただ一つ存在する。 

- $$\tau(a\otimes b)=\tau(a)\times\tau(b)\\\ \\$$

- 半環同型な単位的可換半環 $M,N,\ M\cong N\ (\text{半環同型})$、普遍環 $A(M),A(N)$ とする。
このとき、$A(M)\cong A(N)\ (\text{環同型})$ であり、$A(N)$ は $M$ の普遍環。
<br>

- - $$R(M)=M\times M/\sim,\quad (a_1,b_1)\sim (a_2,b_2)\iff\exist x,y\in M\text{ であって、}a_1\oplus x=a_2\oplus x,\ b_1\oplus y=b_2\oplus y\\\ \\
[a,b]\times[c,d]=[(a\otimes c)\oplus(b\otimes d),(b\otimes c)\oplus(a\otimes d)]\\\ \\
\tau(a)=[a,0]\\\ \\
\psi([a,b])=\phi(a)-\phi(b)$$と定めると、$(A(M),\tau)$ は普遍環。
<br>

  - 上記の普遍環 $R(M)$ において、
  $$1_{R(M)}=[1,0]\\\ \\
  [a\otimes0,0]=[a\otimes 0,b\otimes 0]=[0,0]=0_{R(M)}$$ 

</dd></dl>

---

# 