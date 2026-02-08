部分分数分解の基本
==================

原理
~~~~

.. prf:theorem:: 有理関数の部分分数分解
    :label: pfd_theorem

    複素数係数の多項式 :math:`P(z),Q(z)` があり、それぞれの次数は :math:`\deg P < \deg Q` を満たし、:math:`Q(z)` は相異なる :math:`z_0,\dots,z_K` のもと、

    .. math::
        Q(z) \triangleq \prod_{k=0}^K (z-z_k)^{N_k}

    と因数分解できるものとする。ただし、次数 :math:`N_k` は正の整数である。

    このとき、有理関数 :math:`P(z)/Q(z)` について、

    .. math::
        :label: pfd

        \frac{P(z)}{Q(z)} = \sum_{k=0}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n}

    となる複素数 :math:`a_k^{\langle n \rangle}` が存在する\ :footcite:ps:`stevecheng2013,Hairer2016`。

.. prf:proof::
    多項式 :math:`q_0(z)` を、

    .. math::
        q_0(z) \triangleq \prod_{k=1}^K (z-z_k)^{N_k}

    と定義すると :math:`Q(z) = (z-z_0)^{N_0} q_0(z)` と表せる。このとき、

    .. math::
        a_0^{\langle N_0 \rangle} \triangleq \frac{P(z_0)}{q_0(z_0)}

    と定めれば、これを変形して :math:`P(z_0) - a_0^{\langle N_0 \rangle} q_0(z_0) = 0` となることから、因数定理より、

    .. math::
        p_0^{\langle N_0 \rangle}(z) \triangleq \frac{P(z) - a_0^{\langle N_0 \rangle} q_0(z) }{z-z_0}

    を多項式として定義できる。さらに、:math:`\deg p_0^{\langle N_0 \rangle} < \deg Q - 1` を満たす。すると、

    .. math::
        \frac{P(z)}{(z-z_0)^{N_0} q_0(z)} = \frac{p_0^{\langle N_0 \rangle}(z)}{(z-z_0)^{N_0-1} q_0(z)} + \frac{a_0^{\langle N_0 \rangle}}{(z-z_0)^{N_0}}

    と部分分数分解できることが右辺を通分することで確かめられる。

    また、同様にして、

    .. math::
        \frac{p_0^{\langle N_0 \rangle}(z)}{(z-z_0)^{N_0-1} q_0(z)} = \frac{p_0^{\langle N_0-1 \rangle}(z)}{(z-z_0)^{N_0-2} q_0(z)} + \frac{a_0^{\langle N_0-1\rangle}}{(z-z_0)^{N_0-1}}

    となる複素数 :math:`a_0^{\langle N_0-1 \rangle}` と多項式 :math:`p_0^{\langle N_0-1 \rangle}(z)` が得られるから、この操作を繰り返すことで :math:`z-z_0` の負冪の項をすべて取り出して、

    .. math::
        \frac{P(z)}{Q(z)} = \frac{p_0^{\langle 1 \rangle}(z)}{q_0(z)} + \sum_{n=1}^{N_0} \frac{ a_0^{\langle n \rangle} }{(z-z_0)^n}

    と部分分数分解できる。

    さらに :math:`q_0(z)` の各因子について :math:`p_0^{\langle 1 \rangle}(z) / q_0(z)` に同様の操作を繰り返すことで、最終的に :eq:`pfd` が得られる。

.. prf:theorem:: 一般の有理関数の部分分数分解
    :label: pfd_theorem_general

    有理関数 :math:`R(z)` が複素数係数の多項式 :math:`P(z),Q(z)` により :math:`P(z)/Q(z)` と表され、:math:`Q(z)` は相異なる :math:`z_0,\dots,z_K` のもと、

    .. math::
        Q(z) \triangleq \prod_{k=0}^K (z-z_k)^{N_k}

    と因数分解できるものとする。ただし、次数 :math:`N_k` は正の整数である。

    また、:math:`P(z)` を :math:`Q(z)` で割った商を :math:`S(z)` とすると、

    .. math::
        :label: pfd_general

        R(z) = S(z) + \sum_{k=0}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n}

    となる複素数 :math:`a_k^{\langle n \rangle}` が存在する\ :footcite:ps:`stevecheng2013,Hairer2016`。

.. prf:proof::

    :math:`P(z)` を :math:`Q(z)` で割った余りを :math:`\hat{P}(z)` とすると、

    .. math::
        :label: polynomial_division

        R(z) = S(z) + \frac{\hat{P}(z)}{Q(z)}

    と表せる。ここで :math:`\deg \hat{P} < \deg Q` であるから、:prf:ref:`pfd_theorem` より、

    .. math::
        \frac{\hat{P}(z)}{Q(z)} = \sum_{k=0}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n}

    と部分分数分解できる。これを :eq:`polynomial_division` に代入することで :eq:`pfd_general` が得られる。

公式
~~~~

.. prf:theorem:: Heaviside の方法
    :label: heaviside_method

    :eq:`pfd_general` における :math:`a_k^{\langle n \rangle}` は、

    .. math::
        :label: heaviside_coeff

        a_k^{\langle n \rangle} = \frac{1}{(N_k-n)!} \eval{ \dv[N_k-n]{z} (z-z_k)^{N_k} R(z) }_{z=z_k}

    と表される\ :footcite:ps:`Hairer2016`。

.. note::
    Heaviside の目隠し法 (cover-up method) などとも呼ばれる。

.. prf:proof::
    :math:`k=h,n=m` であるときの :math:`1/(z-z_h)^m` の係数 :math:`a_h^{\langle m \rangle}` を求める。

    :eq:`pfd_general` の両辺に :math:`(z-z_h)^{N_h}` を掛け、さらに :math:`z=z_h` における :math:`N_h-m` 階微分係数を求めても等式は成り立つ。すなわち、

    .. math::
        :label: heaviside_proof_temp

        \eval{ \dv[N_h-m]{z} (z-z_h)^{N_h} R(z) }_{z=z_h} =
        \eval{ \dv[N_h-m]{z} (z-z_h)^{N_h} \qty[ S(z) + \sum_{k=0}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} ] }_{z=z_h}

    となる。

    :eq:`heaviside_proof_temp` の右辺について考える。

    まず、

    .. math::
        \dv[N_h-m]{z} (z-z_h)^{N_h} S(z)

    は :math:`S(z)` が多項式であることから被微分関数は :math:`(z-z_h)^{N_h}` を因数に持ち、:prf:ref:`一般の Leibniz 則 <leibniz_rule_general>` より :math:`N_h-m` 階微分によって :math:`z-z_h` が因数として残るから、

    .. math::
        :label: heaviside_proof_rhs1

        \eval{ \dv[N_h-m]{z} (z-z_h)^{N_h} S(z) }_{z=z_h} = 0

    である。また、

    .. math::
        &\phantom{{}={}} \dv[N_h-m]{z} (z-z_h)^{N_h} \sum_{k=0}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} \\
        &= \dv[N_h-m]{z} \qty[ (z-z_h)^{N_h} \sum_{k=0,k \neq h}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} + \sum_{n=1}^{N_h} a_h^{\langle n \rangle} (z-z_h)^{N_h-n} ] \\
        &= \dv[N_h-m]{z} \qty[ (z-z_h)^{N_h} \sum_{k=0,k \neq h}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} + \sum_{n=1,n \neq m}^{N_h} a_h^{\langle n \rangle} (z-z_h)^{N_h-n} + a_h^{\langle m \rangle} (z-z_h)^{N_h-m} ] \\
        &= a_h^{\langle m \rangle} \dv[N_h-m]{z} (z-z_h)^{N_h-m} + \dv[N_h-m]{z} \qty[ (z-z_h)^{N_h} \sum_{k=0,k \neq h}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} + \sum_{n=1}^{m-1} a_h^{\langle n \rangle} (z-z_h)^{N_h-n} ] \\
        &= a_h^{\langle m \rangle} (N_h-m)! + \dv[N_h-m]{z} \qty[ (z-z_h)^{N_h} \sum_{k=0,k \neq h}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} + \sum_{n=1}^{m-1} a_h^{\langle n \rangle} (z-z_h)^{N_h-n} ]

    であるが、この被微分関数は :math:`(z-z_h)^{N_h-m+1}` を因数に持ち、:prf:ref:`一般の Leibniz 則 <leibniz_rule_general>` より :math:`N_h-m` 階微分によって分子に :math:`z-z_h` が因数として残るから、

    .. math::
        :label: heaviside_proof_rhs2

        \eval{ \dv[N_h-m]{z} (z-z_h)^{N_h} \sum_{k=0}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} }_{z=z_h} = a_h^{\langle m \rangle} (N_h-m)!

    となる。ゆえに :eq:`heaviside_proof_rhs1` および :eq:`heaviside_proof_rhs2` を :eq:`heaviside_proof_temp` を代入すれば、

    .. math::
        \eval{ \dv[N_h-m]{z} (z-z_h)^{N_h} R(z) }_{z=z_h} = a_h^{\langle m \rangle} (N_h-m)!

    であるから、

    .. math::
        a_h^{\langle m \rangle} = \frac{1}{(N_h-m)!} \eval{ \dv[N_h-m]{z} (z-z_h)^{N_h} R(z) }_{z=z_h}

    となり、示された。

.. prf:theorem:: Laurent 級数の主要部の和による表現
    :label: laurent_principal_part

    :prf:ref:`pfd_theorem_general` の状況において有理関数 :math:`R(z)` のすべての極について、その極のまわりの Laurent 級数を考える。このとき、:math:`R(z) - S(z)` はそれらの主要部の総和として表せる\ :footcite:ps:`Jimbo2024,Horiguchi2000`。

.. prf:proof::
    :prf:ref:`pfd_theorem_general` より、

    .. math::
        :label: laurent_principal_part_proof

        R(z) - S(z) = \sum_{k=0}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n}

    と書ける。ここで :math:`z=z_k` は :math:`Q(z)` の根であるとする。:math:`R(z)` の :math:`z=z_k` のまわりの Laurent 級数における :math:`1/(z-z_k)^n` の係数は :eq:`heaviside_coeff` で表せるから、:prf:ref:`heaviside_method` より、:eq:`laurent_principal_part_proof` の右辺の内側の総和はそのような Laurent 級数の主要部にほかならない。

    :math:`z=z_k` は :math:`R(z)` の高々 :math:`N_k` 位の極である。しかしながらこれが除去可能特異点であるならば主要部は :math:`0` であることに注意すると、:eq:`laurent_principal_part_proof` の右辺の外側の総和は :math:`z_k` が極であるようなすべての :math:`k` たちをわたれば十分であり、示された。

例
~~

.. prf:example::
    :label: pfd_example_division

    有理関数

    .. math::
        \frac{x^2-3}{(x-1)(x+3)^2}

    の部分分数分解を :prf:ref:`pfd_theorem` の証明で用いた方法、すなわち多項式の除算を繰り返すことで行う。

    :math:`P(x) \triangleq x^2-3, Q(x) \triangleq (x-1)(x+3)^2, x_0 \triangleq 1, x_1 \triangleq -3` とおく。

    多項式 :math:`q_0(x) \triangleq (x-x_1)^2` のもと :math:`Q(x) = (x-x_0) q_0(x)` と表せて、

    .. math::
        :no-wrap:

        \begin{empheq}[left=\empheqlbrace]{align}
        a_0^{\langle 1 \rangle}
        &\triangleq \frac{P(x_0)}{q_0(x_0)} \\
        &= -\frac{1}{8} \\
        p_0^{\langle 1 \rangle}(x)
        &\triangleq \frac{P(x) - a_0^{\langle 1 \rangle} q_0(x)}{x-x_0} \\
        &= \frac{(x^2-3) + \frac{1}{8} (x+3)^2}{x-1} \\
        &= \frac{3}{8} (3x+5)
        \end{empheq}

    とおくと、

    .. math::
        \frac{P(x)}{(x-x_0) q_0(x)}
        &=\frac{p_0^{\langle 1 \rangle}(x)}{q_0(x)} + \frac{a_0^{\langle 1 \rangle}}{(x-x_0)} \\
        &= \frac{\frac{3}{8} (3x+5)}{(x+3)^2} - \frac{1}{8(x-1)}

    となる。

    次に、多項式 :math:`q_1(x) \triangleq 1` のもと :math:`q_0(x) = (x-x_1)^2 q_1(x)` と表せて、

    .. math::
        :no-wrap:

        \begin{empheq}[left=\empheqlbrace]{align}
        a_1^{\langle 2 \rangle}
        &\triangleq \frac{p_0^{\langle 1 \rangle}(x_1)}{q_1(x_1)} \\
        &= -\frac{3}{2} \\
        p_1^{\langle 2 \rangle}(x)
        &\triangleq \frac{p_0^{\langle 1 \rangle}(x) - a_1^{\langle 2 \rangle} q_1(x)}{x-x_1} \\
        &= \frac{\frac{3}{8} (3x+5) + \frac{3}{2}}{x+3} \\
        &= \frac{9}{8}
        \end{empheq}

    とおくと、

    .. math::
        \frac{p_0^{\langle 1 \rangle}(x)}{(x-x_1)^2 q_1(x)}
        &=\frac{p_1^{\langle 2 \rangle}(x)}{(x-x_1) q_1(x)} + \frac{a_1^{\langle 2 \rangle}}{(x-x_1)^2} \\
        &= \frac{9}{8(x+3)} - \frac{3}{2 (x+3)^2}

    となる。

    以上から、

    .. math::
        \frac{x^2-3}{(x-1)(x+3)^2}
        &= \frac{P(x)}{Q(x)} \\
        &= \frac{P(x)}{(x-x_0) q_0(x)} \\
        &= \frac{p_0^{\langle 1 \rangle}(x)}{q_0(x)} + \frac{a_0^{\langle 1 \rangle}}{(x-x_0)} \\
        &= \frac{p_0^{\langle 1 \rangle}(x)}{(x-x_1)^2 q_1(x)} + \frac{a_0^{\langle 1 \rangle}}{(x-x_0)} \\
        &= \qty[ \frac{9}{8(x+3)} - \frac{3}{2 (x+3)^2} ] - \frac{1}{8(x-1)} \\
        &= -\frac{1}{8(x-1)} - \frac{3}{2 (x+3)^2} + \frac{9}{8(x+3)}

    と部分分数分解できる。

.. prf:example::
    :label: pfd_example_heaviside

    :prf:ref:`pfd_example_division` と同じ有理関数

    .. math::
        \frac{x^2-3}{(x-1)(x+3)^2}

    の部分分数分解を :prf:ref:`Heaviside の方法 <heaviside_method>` を用いて行う。

    .. math::
        \frac{x^2-3}{(x-1)(x+3)^2} = \frac{A}{x-1} + \frac{B}{(x+3)^2} + \frac{C}{x+3}

    と部分分数分解でき、係数 :math:`A,B,C` は、

    .. math::
        :no-wrap:

        \begin{empheq}[left=\empheqlbrace]{alignat=2}
        A &= &\eval{ \frac{x^2-3}{(x+3)^2} }_{x=1} &= -\frac{1}{8} \\
        B &= &\eval{ \frac{x^2-3}{x-1} }_{x=-3} &= -\frac{3}{2}\\
        C &= &\eval{ \dv{x} \frac{x^2-3}{x-1} }_{x=-3} &= \frac{9}{8}
        \end{empheq}

    と求められる。ゆえに、

    .. math::
        \frac{x^2-3}{(x-1)(x+3)^2} = -\frac{1}{8(x-1)} - \frac{3}{2 (x+3)^2} + \frac{9}{8(x+3)}

    となる。

.. footbibliography::
