微分法則
========

積の微分法則
~~~~~~~~~~~~

.. prf:theorem:: Leibniz 則
    :label: leibniz_rule

    関数 :math:`f(z),g(z)` の積の導関数は、

    .. math::
        (f(z) g(z))' = f'(z) g(z) + f(z) g'(z)

    と表される\ :footcite:ps:`weissteinProductRule,mathcam2013`。


.. prf:theorem:: 多因子の場合の Leibniz 則
    :label: leibniz_rule_multifactor

    関数列 :math:`\qty{ f_n(z) }` について、それらの積の導関数は、:prf:ref:`Leibniz 則 <leibniz_rule>` より、

    .. math::
        \qty( \prod_n f_n(z) )' = \sum_n \qty( f_n'(z) \prod_{k \ne n} f_k(z) )

    と表される\ :footcite:ps:`mathcam2013`。

.. prf:theorem:: 一般の Leibniz 則
    :label: leibniz_rule_general

    関数 :math:`f(z),g(z)` の積の :math:`n` 階導関数は、:prf:ref:`Leibniz 則 <leibniz_rule>` より、

    .. math::
        (f(z) g(z))^{(n)} = \sum_{k=0}^n \binom{n}{k} f^{(n-k)}(z) g^{(k)}(z)

    と表される\ :footcite:ps:`weissteinLeibnizIdentity`。ここで、:math:`\binom{n}{k}` は二項係数である。

合成関数の高階微分
~~~~~~~~~~~~~~~~~~

Bell 多項式
-----------

.. prf:definition:: Bell 多項式
    :label: bell_polynomial

    非負整数 :math:`n,k\,(\leq n)` について、Bell 多項式 :math:`B_{n,k}` を、

    .. math::
        B_{n,k}(x_1,x_2,\dots,x_{n-k+1}) \triangleq \sum \frac{n!}{\prod_{i=1}^{n-k+1} j_i!}
        \prod_{i=1}^{n-k+1} \qty( \frac{x_i}{i!} )^{j_i}

    と定義する。ただし、

    .. math::
        :no-wrap:

        \begin{empheq}[left=\empheqlbrace]{align}
            &\sum_{i=1}^{n-k+1} j_i = k \\
            &\sum_{i=1}^{n-k+1} i j_i = n
        \end{empheq}

    の非負整数の解 :math:`(j_1,j_2,\dots,j_{n-k+1})` 全体にわたって和をとる。

.. prf:definition:: 完全 Bell 多項式
    :label: complete_bell_polynomial

    非負整数 :math:`n` について、:math:`n` 次完全 Bell 多項式 :math:`B_n` を、

    .. math::
        B_n(x_1,x_2\dots,x_n) \triangleq \sum_{k=0}^n B_{n,k}(x_1,x_2,\dots,x_{n-k+1})

    と定義する。

.. prf:property::
    :label: bell_polynomial_gp

    Bell 多項式の引数が等比数列との積になっているとき、:prf:ref:`bell_polynomial` より、

    .. math::
        B_{n,k}(ab x_1,ab^2 x_2,\dots,ab^{n-k+1} x_{n-k+1})
        = a^k b^n B_{n,k}(x_1,x_2,\dots,x_{n-k+1})

    が成り立つ。

.. prf:property::
    :label: complete_bell_polynomial_gp

    完全 Bell 多項式の引数が等比数列との積になっているとき、:prf:ref:`bell_polynomial_gp` より、

    .. math::
        B_n(b x_1,b^2 x_2,\dots,b^n x_n) = b^n B_n(x_1,x_2\dots,x_n)

    が成り立つ。

Faà di Bruno の公式
------------------------

.. prf:theorem:: Faà di Bruno の公式
    :label: faa_di_bruno

    適当な複数回微分可能な関数 :math:`f(z),g(z)` について、:math:`f(g(z))` の :math:`n` 階導関数は :prf:ref:`Bell 多項式 <bell_polynomial>` を用いて、

    .. math::
        \dv[n]{z} f(g(z)) = \sum_{k=0}^n f^{(k)}(g(z))
        B_{n,k}( g'(z),g''(z),\dots,g^{(n-k+1)}(z) )

    と表せる\ :footcite:ps:`weissteinFaadiBrunosFormula`。

.. prf:corollary::
    :label: faa_di_bruno_cor

    とくに :math:`f(z) \triangleq e^z` のとき、:math:`f(g(z)) = e^{g(z)}` の :math:`n` 階導関数は :prf:ref:`完全 Bell 多項式 <complete_bell_polynomial>` を用いて、

    .. math::
        \dv[n]{z} e^{g(z)}
        &= \sum_{k=0}^n e^{g(z)} B_{n,k}( g'(z),g''(z),\dots,g^{(n-k+1)}(z) ) \\
        &= e^{g(z)} B_n( g'(z),g''(z),\dots,g^{(n)}(z) )

    と表せる。

.. footbibliography::

