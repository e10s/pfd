調和数列の積に関する部分分数分解
==================================

分母が等差数列の積である有理関数の部分分数分解を考える。これは Melzak の公式を用いて表せる。

公式
~~~~

.. prf:theorem:: Melzak の公式
    :label: melzak

    複素数 :math:`w,z` と非負整数 :math:`K` と高々 :math:`K` 次の多項式 :math:`P(z)` について、

    .. math::
        P(z+w) \prod_{k=0}^K \frac{1}{z+k} = \frac{1}{K!} \sum_{k=0}^K (-1)^k \binom{K}{k} \frac{P(w-k)}{z+k}

    が成り立つ\ :footcite:ps:`Boyadzhiev2017,Abel2019,Gould2010,Melzak1953`。ここで、:math:`\binom{K}{k}` は二項係数である。

.. prf:proof::
    左辺は、:math:`z` について分母が :math:`K+1` 次で分子が高々 :math:`K` 次であり、:prf:ref:`pfd_theorem` より、

    .. math::

        P(z+w) \prod_{k=0}^K \frac{1}{z+k} = \sum_{k=0}^K \frac{a_k}{z+k}

    と部分分数分解できる。

    :prf:ref:`Heaviside の方法 <heaviside_method>` より、 :math:`k=h` のときの :math:`1/(z+h)` の係数 :math:`a_h` は、

    .. math::
        :label: hp_prod_pfd_coef

        a_h
        &= \eval{ (z+h) P(z+w) \prod_{k=0}^K \frac{1}{z+k} }_{z=-h} \\
        &= \eval{ P(z+w) \qty[ \prod_{k=0}^{h-1} \frac{1}{z+k} ] \qty[ \prod_{k=h+1}^K \frac{1}{z+k} ] }_{z=-h} \\
        &= P(w-h) \qty[ \prod_{k=0}^{h-1} \frac{1}{-h+k} ] \qty[ \prod_{k=h+1}^K \frac{1}{-h+k} ] \\
        &= P(w-h) \qty[ (-1)^h \prod_{k=0}^{h-1} \frac{1}{h-k} ] \qty[ \prod_{k=1}^{K-h} \frac{1}{k} ] \\
        &= P(w-h) (-1)^h \frac{1}{h! (K-h)!} \\
        &= \frac{1}{K!} (-1)^h \binom{K}{h} P(w-h)

    であるがゆえ、示された。

.. note::
    どちらかというと、二項変換の閉じた式を与える公式としての応用のほうが強そうではあるが、ここでは部分分数分解の公式として捉える。

系
~~

.. prf:corollary:: Melzak の公式の系
    :label: melzak_cor

    とくに :math:`w \triangleq 0` としたとき、

    .. math::
        P(z) \prod_{k=0}^K \frac{1}{z+k} = \frac{1}{K!} \sum_{k=0}^K (-1)^k \binom{K}{k} \frac{P(-k)}{z+k}

    が成り立つ。

.. prf:corollary:: 調和数列の積の部分分数分解
    :label: hp_prod_pfd

    とくに :math:`P(z) \triangleq 1` としたとき、

    .. math::

        \prod_{k=0}^K \frac{1}{z+k} = \frac{1}{K!} \sum_{k=0}^K (-1)^k \binom{K}{k} \frac{1}{z+k}

    が成り立つ。

例
~~

.. prf:example:: 調和数列の積の部分分数分解
    :label: hp_prod_pfd_example

    .. math::
        \frac{1}{(2x-1)(2x-3)(2x-5)}

    の部分分数分解を考える。

    :math:`z \triangleq x-5/2` とおくと、

    .. math::
        \frac{1}{(2x-1)(2x-3)(2x-5)} = \frac{1}{8 (z+2)(z+1)z}

    となる。ゆえに、:prf:ref:`hp_prod_pfd` より、

    .. math::
        \frac{1}{(2x-1)(2x-3)(2x-5)}
        &= \frac{1}{8} \prod_{k=0}^2 \frac{1}{z+k} \\
        &= \frac{1}{8} \cdot \frac{1}{2!} \sum_{k=0}^2 (-1)^k \binom{2}{k} \frac{1}{z+k} \\
        &= \frac{1}{16} \qty[ \frac{1}{z+2} - \frac{2}{z+1} + \frac{1}{z} ] \\
        &= \frac{1}{16} \qty[ \frac{1}{x-\frac{5}{2}+2} - \frac{2}{x-\frac{5}{2}+1} + \frac{1}{x-\frac{5}{2}} ] \\
        &= \frac{1}{8} \qty[ \frac{1}{2x-1} - \frac{2}{2x-3} + \frac{1}{2x-5} ]

    となる。

.. prf:example:: 調和数列と多項式の積の部分分数分解
    :label: melzak_example

    .. math::
        \frac{(x-2)^2}{(2x-1)(2x-3)(2x-5)}

    の部分分数分解を考える。

    :math:`z \triangleq x-5/2` とおくと、

    .. math::
        \frac{(x-2)^2}{(2x-1)(2x-3)(2x-5)} = \frac{(z+\frac{1}{2})^2}{8 (z+2)(z+1)z}

    となる。さらに、:math:`P(z) \triangleq z^2` とおくと、:prf:ref:`melzak` より、

    .. math::
        \frac{(x-2)^2}{(2x-1)(2x-3)(2x-5)}
        &= \frac{P \qty( z+\frac{1}{2} )}{8} \prod_{k=0}^2 \frac{1}{z+k} \\
        &= \frac{1}{8} \cdot \frac{1}{2!} \sum_{k=0}^2 (-1)^k \binom{2}{k} \frac{P \qty( \frac{1}{2}-k )}{z+k} \\
        &= \frac{1}{16} \qty[ \frac{\qty( -\frac{3}{2} )^2}{z+2} - \frac{2 \qty( -\frac{1}{2} )^2}{z+1} + \frac{\qty( \frac{1}{2} )^2}{z} ] \\
        &= \frac{1}{64} \qty[ \frac{9}{x-\frac{5}{2}+2} - \frac{2}{x-\frac{5}{2}+1} + \frac{1}{x-\frac{5}{2}} ] \\
        &= \frac{1}{32} \qty[ \frac{9}{2x-1} - \frac{2}{2x-3} + \frac{1}{2x-5} ]

    となる。

.. prf:property:: 一般の調和数列の場合
    :label: melzak_gen_hp

    一般に、公差が :math:`d \neq 0` のとき、:prf:ref:`melzak`、:prf:ref:`melzak_cor` および :prf:ref:`hp_prod_pfd` に対応するものとして、

    .. math::
        :no-wrap:

        \begin{empheq}[left=\empheqlbrace]{align}
        P(z+w) \prod_{k=0}^K \frac{1}{z+kd} &= \frac{1}{K!d^K} \sum_{k=0}^K (-1)^k \binom{K}{k} \frac{P(w-kd)}{z+kd} \\
        P(z) \prod_{k=0}^K \frac{1}{z+kd} &= \frac{1}{K!d^K} \sum_{k=0}^K (-1)^k \binom{K}{k} \frac{P(-kd)}{z+kd} \\
        \prod_{k=0}^K \frac{1}{z+kd} &= \frac{1}{K!d^K} \sum_{k=0}^K (-1)^k \binom{K}{k} \frac{1}{z+kd}
        \end{empheq}

    が成り立つ。

.. prf:example:: 調和数列の部分列の積の部分分数分解
    :label: hp_subseq_prod_pfd_example

    .. math::
        \frac{1}{(z+1)(z+3)(z+4)}

    を部分分数分解を考える。少し遠回りして、

    .. math::
        \frac{1}{(z+1)(z+3)(z+4)} = z(z+2) \prod_{k=0}^4 \frac{1}{z+k}

    といったんみなす。ここで、

    .. math::
        P(z) \triangleq z(z+2)

    とおくと、

    .. math::
        P(0)=0,P(-1)=-1,P(-2)=0,P(-3)=3,P(-4)=8

    である。すると、:prf:ref:`melzak_cor` より、

    .. math::
        \frac{1}{(z+1)(z+3)(z+4)}
        &= P(z) \prod_{k=0}^4 \frac{1}{z+k} \\
        &= \frac{1}{4!} \sum_{k=0}^4 (-1)^k \binom{4}{k} \frac{P(-k)}{z+k} \\
        &= \frac{1}{4!} \qty[ \frac{1 \cdot 0}{z} - \frac{4 \cdot (-1)}{z+1} + \frac{6 \cdot 0}{z+2} - \frac{4 \cdot 3}{z+3} + \frac{1 \cdot 8}{z+4} ] \\
        &= \frac{1}{24} \qty[ - \frac{-4}{z+1} - \frac{12}{z+3} + \frac{8}{z+4} ] \\
        &= \frac{1}{6} \qty[ \frac{1}{z+1} - \frac{3}{z+3} + \frac{2}{z+4} ] \\

    となる。

.. tip::
    調和数列の部分列の積は、うまく選んだ多項式を分子とした有理関数が約分された結果であるとみなすことで Melzak の公式が使える。

.. footbibliography::
