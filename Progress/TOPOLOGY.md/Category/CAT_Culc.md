

# 関手

## $K$-右加群

### 双対関手

<dl><dt>

・$K$ 右加群 $V,W$、右 $K$-線形写像 $L:V\to W$ とする。
このとき、双対 $L^{\vee}$：
$$L^{\vee}:W^{\vee}\to V^{\vee}\\\ \\
L^{\vee}(\alpha)=\alpha\circ L$$
はwell-definedな $K$-右線形写像。

</dt><dd>

- $K$ 右加群 $V$ とする。
このとき、
$$id^{\vee}=id_{V^{\vee}}\\\ \\$$

- $K$ 右加群 $V,W,X$、右 $K$-線形写像 $f:V\to W,\ g:W\to X$ とする。
このとき、
$$(g\circ f)^{\vee}=f^{\vee}\circ g^{\vee}$$
したがって、双対 $^{\vee}$ は反変関手。

      ・同型の双対は同型。

</dd></dl> 

---

### 多重コベクトル関手

<dl><dt>

・可換体 $K$ 加群 $V,W$、$K$-線形写像 $L:V\to W$ とする。
このとき、多重コベクトル関手 $A_k(L)$：
$$A_r(L):(\Lambda^r(W))^{\vee}\to (\Lambda^r(V))^{\vee}\\\ \\
A_r(L)(\xi)(v_1\wedge...\wedge v_r)=\xi(L(v_1)\wedge...\wedge L(v_r))$$
はwell-definedな $K$-線形写像。

      ・結局Λ^r(V) の元はr個のウェッジの有限和。
      ・r=1のとき、双対関手と一致する。

</dt><dd>

- 可換体 $K$ 加群 $V$ とする。
このとき、
$$A_r(id)=id_{(\Lambda^r(V))^{\vee}}\\\ \\$$

- 可換体 $K$ 加群 $V,W,U$、$K$-線形写像 $f:V\to W,\ g:W\to U$ とする。
このとき、
$$A_r(g\circ f)=A_r(f)\circ A_r(g)$$
したがって、双対多重コベクトル関手 $A_r$ は反変関手。

      ・同型fのA_k(f)は同型。
      ・A_k(V)=(Λ^r(V))^*




</dd></dl> 