1 の冪根に関する冪の部分分数分解
================================

分母が :math:`z^K-1` の冪である有理関数の部分分数分解を考える。

公式
~~~~

.. prf:theorem:: 1 の冪根と冪の部分分数分解
    :label: roots_of_unity_pow_pfd

    複素数 :math:`z` と正の整数 :math:`K,N` について、

    .. math::
        \frac{1}{(z^K-1)^N} = \sum_{k=0}^{K-1} \sum_{n=1}^N \frac{ a_k^{\langle n \rangle} }{(z-\zeta_K^k)^n}

    が成り立つ。ここで、:math:`\zeta_K \triangleq e^{i 2 \pi /K}` であり、

    .. math::
        a_k^{\langle n \rangle} \triangleq \frac{(-1)^{N-n}}{(N-n)!} \frac{\zeta_K^{nk}}{K^N} B_{N-n} (0! N S_{K,1},1! N S_{K,2},\dots,(N-n-1)! N S_{K,N-n})

    である。また、:math:`B_{N-n}` は :math:`N-n` 次 :prf:ref:`完全 Bell 多項式 <complete_bell_polynomial>` であり、

    .. math::
        S_{K,\nu} \triangleq \sum_{k=1}^{K-1} \frac{1}{(1-\zeta_K^k)^\nu}

    である。

.. tip::
    :prf:ref:`1 の冪根に関する逆数の冪和の性質 <gessel>` より、

    .. math::
        S_{K,\nu} = \frac{1}{(\nu-1)!} \sum_{r=1}^\nu \stirI{\nu}{r} \frac{B^-_r}{r} (1-K^r)

    と表せる。ただし、 :math:`\stirI{\nu}{r}` は符号なし第 1 種 Stirling 数であり、:math:`B^-_\nu` は Bernoulli 数で :math:`B^-_1=-1/2` となるほうであるとする。

.. prf:proof::
    左辺は、:math:`z` について分母が :math:`NK` 次で分子が :math:`0` 次であり、:prf:ref:`pfd_theorem` より、

    .. math::
        \frac{1}{(z^K-1)^N} = \sum_{k=0}^{K-1} \sum_{n=1}^N \frac{ a_k^{\langle n \rangle} }{(z-\zeta_K^k)^n}

    と部分分数分解できる。

    :prf:ref:`Heaviside の方法 <heaviside_method>` より、:math:`k=h,n=m` のときの :math:`1/(z-\zeta_K^h)^m` の係数 :math:`a_h^{\langle m \rangle}` は、

    .. math::
        :label: roots_of_unity_pow_pfd_temp_1

        a_h^{\langle m \rangle}
        &= \frac{1}{(N-m)!} \eval{ \dv[N-m]{z} \qty[ (z-\zeta_K^h) \frac{1}{z^K-1} ]^N }_{z=\zeta_K^h} \\
        &= \frac{1}{(N-m)!} \eval{ \dv[N-m]{z} \qty[ \prod_{k=1}^{K-1} \frac{1}{z-\zeta_K^{k+h}} ]^N }_{z=\zeta_K^h}

    と表せることがわかる。

    ここで、

    .. math::
        :no-wrap:

        \begin{empheq}[left=\empheqlbrace]{align}
        f(z) &\triangleq \prod_{k=1}^{K-1} \frac{1}{z-\zeta_K^{k+h}} \\
        g(z) &\triangleq N \log f(z)
        \end{empheq}

    と定義すると、

    .. math::
        e^{g(z)}
        &= e^{N \log f(z)} \\
        &= (f(z))^N

    であり、:prf:ref:`Faà di Bruno の公式の系 <faa_di_bruno_cor>` より、

    .. math::
        [(f(z))^N]^{(N-m)} = (f(z))^N B_{N-m} \qty(g'(z),g''(z),\dots,g^{(N-m)}(z))

    が成り立つから、:eq:`roots_of_unity_pow_pfd_temp_1` は、

    .. math::
        :label: roots_of_unity_pow_pfd_temp_2

        a_h^{\langle m \rangle}
        = \frac{(f(\zeta_K^h))^N}{(N-m)!} B_{N-m} \qty(g' (\zeta_K^h),g'' (\zeta_K^h),\dots,g^{(N-m)} (\zeta_K^h))

    となる。


    さらに、1 の冪根と部分分数分解の場合 :eq:`roots_of_unity_pfd_coef` と同様に、

    .. math::
        f(\zeta_K^h)
        &= \eval{ \prod_{k=1}^{K-1} \frac{1}{z-\zeta_K^{k+h}} }_{z=\zeta_K^h} \\
        &= \frac{\zeta_K^h}{K}

    であるから、:eq:`roots_of_unity_pow_pfd_temp_2` は、

    .. math::
        :label: roots_of_unity_pow_pfd_temp_3

        a_h^{\langle m \rangle}
        = \frac{1}{(N-m)!} \frac{\zeta_K^{Nh}}{K^N} B_{N-m} \qty(g' (\zeta_K^h),g'' (\zeta_K^h),\dots,g^{(N-m)} (\zeta_K^h))

    となる。

    また、:math:`\nu>0` について、:math:`\log f(z)` の :math:`\nu` 階導関数は、

    .. math::
        \dv[\nu]{z} \log f(z)
        &= \dv[\nu]{z} \log \prod_{k=1}^{K-1} \frac{1}{z-\zeta_K^{k+h}} \\
        &= \dv[\nu]{z} \sum_{k=1}^{K-1} \log \frac{1}{z-\zeta_K^{k+h}} \\
        &= (-1)^\nu (\nu-1)! \sum_{k=1}^{K-1} \frac{1}{(z-\zeta_K^{k+h})^\nu}

    となるから、:math:`\log f(z)` の :math:`z=\zeta_K^h` における :math:`\nu` 階微分係数は、

    .. math::
        \dv[\nu]{\log f}{z} (\zeta_K^h)
        &= (-1)^\nu (\nu-1)! \sum_{k=1}^{K-1} \frac{1}{(\zeta_K^h-\zeta_K^{k+h})^\nu} \\
        &= (-\zeta_K^{-h})^\nu (\nu-1)! \sum_{k=1}^{K-1} \frac{1}{(1-\zeta_K^k)^\nu} \\
        &= (-\zeta_K^{-h})^\nu (\nu-1)! S_{K,\nu}

    となり、

    .. math::
        g^{(\nu)} (\zeta_K^{-h}) = (-\zeta_K^{-h})^\nu (\nu-1)! N S_{K,\nu}

    であるから、:eq:`roots_of_unity_pow_pfd_temp_3` は、

    .. math::
        :label: roots_of_unity_pow_pfd_temp_4

        a_h^{\langle m \rangle}
        = \frac{1}{(N-m)!} \frac{\zeta_K^{Nh}}{K^N} B_{N-m} \qty(0!(-\zeta_K^{-h}) N S_{K,1},1!(-\zeta_K^{-h})^2 N S_{K,2},\dots,(N-m-1)!(-\zeta_K^{-h})^{N-m} N S_{K,N-m})

    となる。:prf:ref:`完全 Bell 多項式の引数が等比数列との積になっているときの性質 <complete_bell_polynomial_gp>` より、:eq:`roots_of_unity_pow_pfd_temp_4` は、

    .. math::
        a_h^{\langle m \rangle}
        &= \frac{1}{(N-m)!} \frac{\zeta_K^{Nh}}{K^N} (-\zeta_K^{-h})^{N-m} B_{N-m} (0! N S_{K,1},1! N S_{K,2},\dots,(N-m-1)! N S_{K,N-m}) \\
        &= \frac{(-1)^{N-m}}{(N-m)!} \frac{\zeta_K^{mh}}{K^N} B_{N-m} (0! N S_{K,1},1! N S_{K,2},\dots,(N-m-1)! N S_{K,N-m}) \\

    となるがゆえ、示された。

例
~~

.. prf:example:: 1 の冪根に関する部分分数分解の系
    :label: roots_of_unity_pfd_cor_rev

    :prf:ref:`roots_of_unity_pow_pfd` において :math:`N \triangleq 1` としたとき、:math:`B_0 = 1` であることを考慮すると、

    .. math::
        a_k^{\langle 1 \rangle} = \frac{\zeta_K^k}{K}

    となるから、

    .. math::
        \frac{1}{z^K-1} = \frac{1}{K} \sum_{k=0}^{K-1} \frac{\zeta_K^k}{z-\zeta_K^k}


    となり、:prf:ref:`1 の冪根に関する部分分数分解の公式の系 <roots_of_unity_pfd_cor>` となる。

.. prf:example:: 1 の冪根に関する 2 乗の部分分数分解
    :label: roots_of_unity_sq_pfd

    :prf:ref:`roots_of_unity_pow_pfd` において :math:`N \triangleq 2` としたとき、:math:`B_1(x_1) = x_1` であることを考慮すると、

    .. math::
        B_1(2 S_{K,1})
        &= 2 S_{K,1} \\
        &= K-1

    であり、:math:`B_0 = 1` であったから、

    .. math::
        :no-wrap:

        \begin{empheq}[left=\empheqlbrace]{align}
        a_k^{\langle 2 \rangle} &= \frac{\zeta_K^{2k}}{K^2} \\
        a_k^{\langle 1 \rangle} &= - \frac{(K-1) \zeta_K^{k}}{K^2}
        \end{empheq}

    となるがゆえ、

    .. math::
        \frac{1}{(z^K-1)^2} = \frac{1}{K^2} \sum_{k=0}^{K-1} \qty[ \frac{\zeta_K^{2k}}{(z-\zeta_K^k)^2} - \frac{(K-1) \zeta_K^k}{z-\zeta_K^k} ]

    となる。
