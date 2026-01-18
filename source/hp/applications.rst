応用
====

二項係数の逆数の部分分数分解
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. prf:definition:: 一般二項係数
    :label: binom_general

    複素数 :math:`z` と非負整数 :math:`K` について、一般二項係数 :math:`\binom{z}{K}` を、

    .. math::
        \binom{z}{K}
        &\triangleq \frac{z (z-1) \cdots (z-K+1)}{K!} \\
        &= \frac{1}{K!} \prod_{k=0}^{K-1} (z-k)

    と定義する。

.. tip::
    :math:`z` が :math:`K` 以上の整数であれば通常の二項係数と同じである。

.. prf:example::
    :label: binom_inv_pfd_1

    :prf:ref:`melzak_gen_hp` より、

    .. math::
        \frac{1}{\binom{z}{K}}
        &= K! \prod_{k=0}^{K-1} \frac{1}{z-k} \\
        &= K! \cdot \frac{1}{(K-1)! (-1)^{K-1}} \sum_{k=0}^{K-1} (-1)^k \binom{K-1}{k} \frac{1}{z-k} \\
        &= K! \cdot \frac{1}{(K-1)! (-1)^{K-1}} \sum_{k=0}^{K-1} (-1)^k \frac{(K-1)!}{k! ((K-1)-k)!} \cdot \frac{1}{z-k} \\
        &= \sum_{k=0}^{K-1} (-1)^{K+k-1} \frac{K!}{k! (K-k)!} \cdot \frac{K-k}{z-k} \\
        &= \sum_{k=0}^{K-1} (-1)^{K-1-k} \binom{K}{k} \frac{K-k}{z-k}

    となる。

.. prf:example::
    :label: binom_inv_pfd_2

    :prf:ref:`binom_inv_pfd_1` において :math:`z` を改めて :math:`z+K` とおくと、

    .. math::
        \frac{1}{\binom{z+K}{K}}
        &= \sum_{k=0}^{K-1} (-1)^{K-1-k} \binom{K}{k} \frac{K-k}{z+K-k} \\
        &= \sum_{k=-K}^{-1} (-1)^{-k-1} \binom{K}{K+k} \frac{-k}{z-k} \\
        &= \sum_{k=1}^K (-1)^{k-1} \binom{K}{K-k} \frac{k}{z+k} \\
        &= \sum_{k=1}^K (-1)^{k-1} \binom{K}{k} \frac{k}{z+k} \\

    となる。


等差数列が分母・分子に交互に来る積の部分分数分解
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. prf:example::
    :label: ap_hp_prod_pfd

    複素数 :math:`z` と非負整数 :math:`K` について、

    .. math::
        \prod_{k=0}^{2K} (z+k)^{(-1)^{k+1}}
        = \qty[ \prod_{k=0}^{K-1} (z+2k+1) ] \qty[ \prod_{k=0}^K \frac{1}{z+2k} ]

    の部分分数分解を考える。

    まず、

    .. math::
        P(z) \triangleq \prod_{i=0}^{K-1} (z+2i+1)

    と定義すると、

    .. math::
        P(-2k)
        &= \prod_{i=0}^{K-1} (-2k+2i+1) \\
        &= \prod_{i=-k+1}^{K-k} (2i-1) \\
        &= \qty[ \prod_{i=-k+1}^0 (2i-1) ] \qty[\prod_{i=1}^{K-k} (2i-1) ] \\
        &= \qty[ \prod_{i=0}^{k-1} (-2i-1) ] \qty[\prod_{i=1}^{K-k} (2i-1) ] \\
        &= \qty[ (-1)^k \prod_{i=0}^{k-1} (2i+1) ] \qty[\prod_{i=1}^{K-k} (2i-1) ] \\
        &= (-1)^k (2k-1)!! (2(K-k)-1)!! \\
        &= (-1)^k \frac{(2k)!}{2^k k!} \cdot \frac{(2(K-k))!}{2^{K-k} (K-k)!} \\
        &= (-1)^k \frac{(2k)!(2(K-k))!}{2^K k!(K-k)!}

    となり、

    .. math::
        \frac{1}{K! 2^K} (-1)^k \binom{K}{k} P(-2k)
        &= \frac{1}{K! 2^K} (-1)^k \binom{K}{k} \cdot (-1)^k \frac{(2k)!(2(K-k))!}{2^K k!(K-k)!} \\
        &= \frac{1}{K!} \cdot \frac{K!}{k!(K-k)!} \cdot \frac{(2k)!(2(K-k))!}{2^K k!(K-k)!} \\
        &= \frac{1}{4^K} \cdot \frac{(2k)!}{(k!)^2} \cdot \frac{(2(K-k))!}{((K-k)!)^2} \\
        &= \frac{1}{4^K} \binom{2k}{k} \binom{2(K-k)}{K-k}

    であるから、:prf:ref:`melzak_gen_hp` より、

    .. math::
        P(z) \prod_{k=0}^K \frac{1}{z+2k}
        &= \frac{1}{K!2^K} \sum_{k=0}^K (-1)^k \binom{K}{k} \frac{P(-2k)}{z+2k} \\
        &= \sum_{k=0}^K \frac{1}{4^K} \binom{2k}{k} \binom{2(K-k)}{K-k} \frac{1}{z+2k}

    となり、すなわち、

    .. math::
        \prod_{k=0}^{2K} (z+k)^{(-1)^{k+1}} = \frac{1}{4^K} \sum_{k=0}^K \binom{2k}{k} \binom{2(K-k)}{K-k} \frac{1}{z+2k}

    となる。

調和数列と不等式
~~~~~~~~~~~~~~~~~

.. prf:example::
    :label: mengoli_inequality

    :math:`x > 1` のとき、:math:`x+1 > x > x-1 > 0` ゆえ、

    .. math::
        \frac{1}{(x-1)x(x+1)} > 0

    である。ここで、:prf:ref:`hp_prod_pfd_example` より、

    .. math::
        \frac{1}{(x-1)x(x+1)} = \frac{1}{2} \qty( \frac{1}{x-1} - \frac{2}{x} + \frac{1}{x+1} )

    と部分分数分解できるから、

    .. math::
        \frac{1}{x-1} - \frac{2}{x} + \frac{1}{x+1} > 0

    が成り立ち、すなわち、

    .. math::
        \frac{1}{x-1} + \frac{1}{x} + \frac{1}{x+1} > \frac{3}{x}

    が成り立つ\ :footcite:ps:`Bell2018,AnalysisFact2023`。

.. footbibliography::
