調和数列の冪の積に関する部分分数分解
==========================================

分母が等差数列の冪の積である有理関数の部分分数分解を考える。

公式
~~~~

.. prf:theorem:: 一般化された Melzak の公式
    :label: melzak_pow

    複素数 :math:`w,z` と非負整数 :math:`K`、正の整数 :math:`N` と高々 :math:`N(K+1)-1` 次の多項式 :math:`P(z)` について、

    .. math::
        P(z+w) \prod_{k=0}^K \frac{1}{(z+k)^N} = \sum_{k=0}^K \sum_{n=1}^N \frac{ a_k^{\langle n \rangle} }{(z+k)^n}

    が成り立つ。ここで、

    .. math::
        :label: melzak_pow_coef

        a_k^{\langle n \rangle} \triangleq \frac{C_{K,k}^N}{(N-n)!} \sum_{\nu=0}^{N-n} \binom{N-n}{\nu} P^{(N-n-\nu)} (w-k)
        B_\nu \qty(
        0! N \bar{H}_{K,k}^{(1)},1! N \bar{H}_{K,k}^{(2)},\dots,
        (\nu-1)! N \bar{H}_{K,k}^{(\nu)})

    であり、:math:`\binom{N-n}{\nu}` は二項係数であり、

    .. math::
        C_{K,k} \triangleq \frac{(-1)^k}{K!} \binom{K}{k}

    と定義する。また、:math:`B_\nu` は :math:`\nu` 次 :prf:ref:`完全 Bell 多項式 <complete_bell_polynomial>` である。

    :math:`H_k^{(\nu)}` は :math:`k` 番目の :math:`\nu` 次一般化調和数、すなわち、

    .. math::
        H_k^{(\nu)} \triangleq \sum_{i=1}^k \frac{1}{i^\nu}

    と定義したうえで :math:`\bar{H}_{K,k}^{(\nu)}` を、

    .. math::
        \bar{H}_{K,k}^{(\nu)} \triangleq H_k^{(\nu)} + (-1)^\nu H_{K-k}^{(\nu)}

    と定義する。

.. prf:proof::
    左辺は、:math:`z` について分母が :math:`N(K+1)` 次で分子が高々 :math:`N(K+1)-1` 次であり、:prf:ref:`pfd_theorem` より、

    .. math::
        P(z+w) \prod_{k=0}^K \frac{1}{(z+k)^N} = \sum_{k=0}^K \sum_{n=1}^N \frac{ a_k^{\langle n \rangle} }{(z+k)^n}

    と部分分数分解できる。

    :prf:ref:`Heaviside の方法 <heaviside_method>` より、:math:`k=h,n=m` のときの :math:`1/(z+h)^m` の係数 :math:`a_h^{\langle m \rangle}` は、

    .. math::
        :label: melzak_pow_temp_1

        a_h^{\langle m \rangle} = \frac{1}{(N-m)!} \eval{ \dv[N-m]{z} P(z+w) \qty[ (z+h) \prod_{k=0}^K \frac{1}{z+k} ]^N }_{z=-h}

    と表せることがわかる。

    ここで、

    .. math::
        f(z) \triangleq (z+h) \prod_{k=0}^K \frac{1}{z+k}

    と定義すると、:eq:`melzak_pow_temp_1` は :prf:ref:`一般の Leibniz 則 <leibniz_rule_general>` により、

    .. math::
        :label: melzak_pow_temp_2

        \begin{align}
        a_h^{\langle m \rangle}
        &= \frac{1}{(N-m)!} \eval{ \dv[N-m]{z} P(z+w) (f(z))^N }_{z=-h} \\
        &= \frac{1}{(N-m)!} \sum_{\nu=0}^{N-m} \binom{N-m}{\nu} {P^{(N-m-\nu)} (w-h)} \eval{ [(f(z))^N]^{(\nu)} }_{z=-h}
        \end{align}

    と書き直すことができる。

    いま、

    .. math::
        g(z) \triangleq N \log f(z)

    と定義すると、

    .. math::
        \begin{align}
        e^{g(z)}
        &= e^{N \log f(z)} \\
        &= (f(z))^N
        \end{align}

    であり、:prf:ref:`Faà di Bruno の公式の系 <faa_di_bruno_cor>` より、

    .. math::
        [(f(z))^N]^{(\nu)} = (f(z))^N B_\nu \qty(g'(z),g''(z),\dots,g^{(\nu)}(z))

    が成り立つから、:eq:`melzak_pow_temp_2` は、

    .. math::
        :label: melzak_pow_temp_3

        a_h^{\langle m \rangle}
        = \frac{(f(-h))^N}{(N-m)!} \sum_{\nu=0}^{N-m} \binom{N-m}{\nu} {P^{(N-m-\nu)} (w-h)}
        B_\nu \qty(g'(-h),g''(-h),\dots,g^{(\nu)}(-h))

    となる。

    さらに、調和数列の積の部分分数分解の場合 :eq:`hp_prod_pfd_coef` と同様に、

    .. math::
        \begin{align}
        f(-h)
        &= \eval{ (z+h) \prod_{k=0}^K \frac{1}{z+k} }_{z=-h} \\
        &= \frac{1}{K!} (-1)^h \binom{K}{h} \\
        &= C_{K,k}
        \end{align}

    であるから、:eq:`melzak_pow_temp_3` は、

    .. math::
        :label: melzak_pow_temp_4

        a_h^{\langle m \rangle}
        = \frac{C_{K,k}^N}{(N-m)!} \sum_{\nu=0}^{N-m} \binom{N-m}{\nu} {P^{(N-m-\nu)} (w-h)}
        B_\nu \qty(g'(-h),g''(-h),\dots,g^{(\nu)}(-h))

    となる。

    また、:math:`\nu>0` について、:math:`\log f(z)` の :math:`\nu` 階導関数は、

    .. math::
        \begin{align}
        \dv[\nu]{z} \log f(z)
        &= \dv[\nu]{z} \log \prod_{k=0,k \neq h}^K \frac{1}{z+k} \\
        &= \dv[\nu]{z} \sum_{k=0,k \neq h}^K \log \frac{1}{z+k} \\
        &= (-1)^\nu (\nu-1)! \sum_{k=0,k \neq h}^K \frac{1}{(z+k)^\nu}
        \end{align}

    となるから、:math:`\log f(z)` の :math:`z=-h` における :math:`\nu` 階微分係数は、

    .. math::
        \begin{align}
        \dv[\nu]{\log f}{z} (-h)
        &= (-1)^\nu (\nu-1)! \sum_{k=0,k \neq h}^K \frac{1}{(k-h)^\nu} \\
        &= (-1)^\nu (\nu-1)! \qty[ \sum_{k=0}^{h-1} \frac{1}{(k-h)^\nu} + \sum_{k=h+1}^K \frac{1}{(k-h)^\nu} ] \\
        &= (-1)^\nu (\nu-1)! \qty[ \sum_{k=-h}^{-1} \frac{1}{k^\nu} + \sum_{k=1}^{K-h} \frac{1}{k^\nu} ] \\
        &= (-1)^\nu (\nu-1)! \qty[ \sum_{k=1}^h \frac{(-1)^\nu}{k^\nu} + \sum_{k=1}^{K-h} \frac{1}{k^\nu} ] \\
        &= (\nu-1)! \qty[ \sum_{k=1}^h \frac{1}{k^\nu} + (-1)^\nu\sum_{k=1}^{K-h} \frac{1}{k^\nu} ] \\
        &= (\nu-1)! \qty[ H_h^{(\nu)} + (-1)^\nu H_{K-k}^{(\nu)} ] \\
        &= (\nu-1)! \bar{H}_{K,h}^{(\nu)}
        \end{align}

    となり、

    .. math::
        g^{(\nu)} (-h) = (\nu-1)! N \bar{H}_{K,h}^{(\nu)}

    であるから、
    :eq:`melzak_pow_temp_4` は、

    .. math::
        a_h^{\langle m \rangle}
        = \frac{C_{K,h}^N}{(N-m)!} \sum_{\nu=0}^{N-m} \binom{N-m}{\nu} {P^{(N-m-\nu)} (w-h)}
        B_\nu \qty( 0! N \bar{H}_{K,h}^{(1)},1! N \bar{H}_{K,h}^{(2)},\dots,(\nu-1)! N \bar{H}_{K,h}^{(\nu)})

    となるがゆえ、示された。

系
~~

.. prf:corollary:: 調和数列の積の冪の部分分数分解
    :label: hp_prod_pow_pfd

    とくに、:math:`P(w) \triangleq 1` のとき、

    .. math::
        \prod_{k=0}^K \frac{1}{(z+k)^N} = \sum_{k=0}^K \sum_{n=1}^N \frac{ a_k^{\langle n \rangle} }{(z+k)^n}

    が成り立ち、係数は、

    .. math::
        a_k^{\langle n \rangle}
        = \frac{C_{K,k}^N}{(N-n)!}
        B_{N-n} \qty( 0! N \bar{H}_{K,k}^{(1)},1! N \bar{H}_{K,k}^{(2)},\dots,(N-n-1)! N \bar{H}_{K,k}^{(N-n)})

    となる\ :footcite:ps:`Chu2005,Zhu2021`。

.. prf:proof::
    係数 :eq:`melzak_pow_coef` は、:math:`\nu \neq N-n` のとき :math:`P^{(N-n-\nu)} = 0` となることに注意すると、

    .. math::
        a_k^{\langle n \rangle} = \frac{C_{K,k}^N}{(N-n)!} \binom{N-n}{N-n} P^{(0)} (w-k) B_{N-n} (\dots )

    すなわち、

    .. math::
        a_k^{\langle n \rangle} = \frac{C_{K,k}^N}{(N-n)!}
        B_{N-n} (\dots)

    となり、示された。

例
~~

.. prf:example:: Melzak の公式
    :label: melzak_rev

    :prf:ref:`melzak_pow` において :math:`N \triangleq 1` としたとき、:math:`B_0 = 1` であることを考慮すると、

    .. math::
        a_k^{\langle 1 \rangle} = C_{K,k} P(w-k)

    となるから、

    .. math::
        \begin{align}
        P(z+w) \prod_{k=0}^K \frac{1}{z+k}
        &= \sum_{k=0}^K \frac{C_{K,k} P(w-k)}{z+k} \\
        &= \frac{1}{K!} \sum_{k=0}^K (-1)^k \binom{K}{k} \frac{P(w-k)}{z+k}
        \end{align}

    となり、:prf:ref:`Melzak の公式 <melzak>` となる。

.. prf:example:: 調和数列の積の 2 乗の部分分数分解
    :label: hp_prod_sq_pfd_rev

    :prf:ref:`hp_prod_pow_pfd` において :math:`N \triangleq 2` としたとき、:math:`B_1(x_1) = x_1` であることを考慮すると、

    .. math::
        B_1 \qty(2 \bar{H}_{K,k}^{(1)}) = 2 (H_k - H_{K-k})

    であり、:math:`B_0 = 1` であったから、

    .. math::
        \begin{empheq}[left=\empheqlbrace]{align}
        a_k^{\langle 2 \rangle} &= C_{K,k}^2 \\
        a_k^{\langle 1 \rangle} &= C_{K,k}^2 \cdot 2 (H_k - H_{K-k})
        \end{empheq}

    となるがゆえ、

    .. math::
        \prod_{k=0}^K \frac{1}{(z+k)^2} = \frac{1}{(K!)^2} \sum_{k=0}^K \binom{K}{k}^2 \qty[ \frac{1}{(z+k)^2} + \frac{2 (H_k-H_{K-k})}{z+k} ]

    となる。

.. footbibliography::
