1 の冪根に関する部分分数分解
============================

分母が :math:`z^K-1` である有理関数の部分分数分解を考える。

公式
~~~~

.. prf:theorem:: 1 の冪根に関する部分分数分解
    :label: roots_of_unity_pfd

    複素数 :math:`z` と正の整数 :math:`K` と高々 :math:`K-1` 次の多項式 :math:`P(z)` について、

    .. math::
        \frac{P(z)}{z^K-1} = \frac{1}{K} \sum_{k=0}^{K-1} \frac{P(\zeta_K^k) \zeta_K^k}{z-\zeta_K^k}

    が成り立つ\ :footcite:ps:`Gould2010`。ここで、:math:`\zeta_K \triangleq e^{i 2 \pi /K}` である。

.. prf:proof::
    左辺は、:math:`z` について分母が :math:`K` 次で分子が高々 :math:`K-1` 次であり、:prf:ref:`pfd_theorem` より、

    .. math::

        \frac{P(z)}{z^K-1} = \sum_{k=0}^{K-1} \frac{a_k}{z-\zeta_K^k}

    と部分分数分解できる。

    :prf:ref:`Heaviside の方法 <heaviside_method>` より、:math:`k=h` のときの :math:`1/(z-\zeta_K^h)` の係数 :math:`a_h` は、

    .. math::
        \begin{align}
        a_h
        &= \eval{ (z-\zeta_K^h) P(z) \frac{1}{z^K-1} }_{z=\zeta_K^h} \\
        &= \eval{ (z-\zeta_K^h) P(z) \prod_{k=0}^{K-1} \frac{1}{z-\zeta_K^k} }_{z=\zeta_K^h} \\
        &= \eval{ (z-\zeta_K^h) P(z) \prod_{k=0}^{K-1} \frac{1}{z-\zeta_K^{k+h}} }_{z=\zeta_K^h} \\
        &= \eval{ P(z) \prod_{k=1}^{K-1} \frac{1}{z-\zeta_K^{k+h}} }_{z=\zeta_K^h} \\
        &= P(\zeta_K^h) \prod_{k=1}^{K-1} \frac{1}{\zeta_K^h-\zeta_K^{k+h}} \\
        &= P(\zeta_K^h) (\zeta_K^{-h})^{K-1} \prod_{k=1}^{K-1} \frac{1}{1-\zeta_K^k} \\
        &= P(\zeta_K^h) \zeta_K^h \prod_{k=1}^{K-1} \frac{1}{1-\zeta_K^k}
        \end{align}

    となり、:prf:ref:`1 の冪根に関する積の性質 <roots_of_unity_prop_prod>` より、

    .. math::
        :label: roots_of_unity_pfd_coef

        a_h = \frac{P(\zeta_K^h) \zeta_K^h}{K}

    であるがゆえ、示された。

系
~~

.. prf:corollary:: 1 の冪根に関する部分分数分解の系
    :label: roots_of_unity_pfd_cor

    とくに :math:`P(z) \triangleq 1` としたとき、

    .. math::
        \frac{1}{z^K-1} = \frac{1}{K} \sum_{k=0}^{K-1} \frac{\zeta_K^k}{z-\zeta_K^k}

    が成り立つ。

.. footbibliography::
