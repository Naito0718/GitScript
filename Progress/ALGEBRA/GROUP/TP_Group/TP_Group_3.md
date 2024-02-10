
- [位相群の基本群](#位相群の基本群)
  - [位相群の道](#位相群の道)
    - [位相群とホモトープ](#位相群とホモトープ)
  - [基本群](#基本群)
- [連結位相群](#連結位相群)
  - [連結成分](#連結成分)
  - [連結位相群の性質](#連結位相群の性質)
    - [離散部分群](#離散部分群)
  - [剰余空間と連結性](#剰余空間と連結性)
- [弧状連結位相群](#弧状連結位相群)
  - [離散部分群 $Γ$](#離散部分群-γ)
- [リー群](#リー群)


# 位相群の基本群

## 位相群の道

・位相群 $G$、$G$ 上の道 $k,l$ とする。
このとき、$kl,\ k^{-1}$ は道。
ここで、$g\in G$ に対して、$gk=0_gk$ と書ける。
<br>

    ・逆の道はk^{inv}で書くようにする。

---

### 位相群とホモトープ

<dl><dt>

・位相群 $G$、$X$ の道 $m_1,m_2$、ホモトープな道 $k_1\sim k_2,\ l_1\sim l_2$ とする。
<br>

</dt><dd>

- 
$$k_1l_1\sim k_2l_2\\\ \\
k_1^{-1}\sim k_2^{-1}\\\ \\
l_i(1)=m_i(0)\Rightarrow (l_1m_1) (l_2m_2)= (l_1\vee m_1)(l_2\vee m_2)\\\ \\
0_{k_1(0)}\vee k_1\sim k_1,\quad k_1\vee 0_{k(1)}\sim k_1\\\ \\
m_1(0)=m_2(0)=e\Rightarrow m_1m_2\sim m_1\vee(m_1(1)m_2)\sim m_2\vee(m_1m_2(b))\\\ \\
m_1(0)=e\Rightarrow (m_1)^{-1}\sim m_1(1)^{-1}m_1^{inv}$$

- $\Omega(X,x)/\sim$ は演算 $[k]\vee[l]=[k\vee l]$ について群をなす。これを基本群 $\pi(X,x)$ という。
<br>

      ・閉じてないと単位元が定まらない。

</dd></dl>

---

## 基本群

・位相群 $G$ とする。
このとき、$\pi(X,e)$ は可換群であって、
$$[k]\vee[l]=[k][l],\quad [k]^{inv}=[k]^{-1}$$

---

# 連結位相群

## 連結成分

<dl><dt>

・位相群 $G$、単位元を含む連結成分 $e\in G^0$ とする。
このとき、$G^0$ は閉正規部分群。
<br>

</dt><dd>

- 位相群 $G$、連結成分 $C\sub G$ とする。
このとき、
$$\exist g\in G\text{ であって、}C=gG^0$$

</dd></dl>

---

## 連結位相群の性質

・連結位相群 $G$、単位元の開近傍 $e\in U\sub G$ とする。
このとき、
$$G=\lang U \rang$$

### 離散部分群

・連結位相群 $G$、離散正規部分群 $H$ とする。
このとき、$$H\sub Z(G)$$

    ・位相が結局部分空間位相なのでよい。


---

## 剰余空間と連結性

・位相群 $G$、閉部分群 $H\sub G$ とする。
このとき、$H$、$G/H$ が共に連結ならば、$G$ は連結。

    ・逆はよくわからん。
<br>


# 弧状連結位相群

## 離散部分群 $Γ$

・弧状連結位相群 $G$、離散正規部分群 $\Gamma\sub G$、中心 $Z(G)$ とする。
このとき、
$$\Gamma\sub Z(G)$$



---






# リー群


---