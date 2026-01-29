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

.. tip::
    一般に、:math:`\deg P \geq \deg Q` の場合も、多項式の除算により、

    .. math::
        P(z) = q(z) Q(z) + r(z), \quad \deg r < \deg Q

    を満たす多項式 :math:`q(z),r(z)` が一意に存在することから、

    .. math::
        \frac{P(z)}{Q(z)} = q(z) + \frac{r(z)}{Q(z)}

    と表すことにより、:prf:ref:`pfd_theorem` で扱うことのできる :math:`r(z)/Q(z)` の部分分数分解に還元できる。

公式
~~~~

.. prf:theorem:: Heaviside の方法
    :label: heaviside_method

    :eq:`pfd` における :math:`a_k^{\langle n \rangle}` は、

    .. math::
        :label: heaviside_coeff

        a_k^{\langle n \rangle} = \frac{1}{(N_k-n)!} \eval{ \dv[N_k-n]{z} (z-z_k)^{N_k} \frac{P(z)}{Q(z)} }_{z=z_k}

    と表される\ :footcite:ps:`Hairer2016`。

.. note::
    Heaviside の目隠し法 (cover-up method) などとも呼ばれる。

.. prf:proof::
    :math:`k=h,n=m` であるときの :math:`1/(z-z_h)^m` の係数 :math:`a_h^{\langle m \rangle}` を求める。

    :eq:`pfd` の両辺に :math:`(z-z_h)^{N_h}` を掛け、さらに :math:`z=z_h` における :math:`N_h-m` 階微分係数を求めても等式は成り立つ。すなわち、

    .. math::
        :label: heaviside_proof_temp

        \eval{ \dv[N_h-m]{z} (z-z_h)^{N_h} \frac{P(z)}{Q(z)} }_{z=z_h} =
        \eval{ \dv[N_h-m]{z} (z-z_h)^{N_h} \sum_{k=0}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} }_{z=z_h}

    となる。

    :eq:`heaviside_proof_temp` の右辺について、

    .. math::
        &\phantom{{}={}} \dv[N_h-m]{z} (z-z_h)^{N_h} \sum_{k=0}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} \\
        &= \dv[N_h-m]{z} \qty[ (z-z_h)^{N_h} \sum_{k=0,k \neq h}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} + \sum_{n=1}^{N_h} a_h^{\langle n \rangle} (z-z_h)^{N_h-n} ] \\
        &= \dv[N_h-m]{z} \qty[ (z-z_h)^{N_h} \sum_{k=0,k \neq h}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} + \sum_{n=1,n \neq m}^{N_h} a_h^{\langle n \rangle} (z-z_h)^{N_h-n} + a_h^{\langle m \rangle} (z-z_h)^{N_h-m} ] \\
        &= a_h^{\langle m \rangle} \dv[N_h-m]{z} (z-z_h)^{N_h-m} + \dv[N_h-m]{z} \qty[ (z-z_h)^{N_h} \sum_{k=0,k \neq h}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} + \sum_{n=1}^{m-1} a_h^{\langle n \rangle} (z-z_h)^{N_h-n} ] \\
        &= a_h^{\langle m \rangle} (N_h-m)! + \dv[N_h-m]{z} \qty[ (z-z_h)^{N_h} \sum_{k=0,k \neq h}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} + \sum_{n=1}^{m-1} a_h^{\langle n \rangle} (z-z_h)^{N_h-n} ]

    であるが、この被微分関数は :math:`(z-z_h)^{N_h-m+1}` を因数に持ち、:prf:ref:`一般の Leibniz 則 <leibniz_rule_general>` より :math:`N_h-m` 階微分によって分子に :math:`z-z_h` が因数として残るから、

    .. math::
        \eval{ \dv[N_h-m]{z} (z-z_h)^{N_h} \sum_{k=0}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} }_{z=z_h} = a_h^{\langle m \rangle} (N_h-m)!

    となる。ゆえに :eq:`heaviside_proof_temp` より、

    .. math::
        \eval{ \dv[N_h-m]{z} (z-z_h)^{N_h} \frac{P(z)}{Q(z)} }_{z=z_h} = a_h^{\langle m \rangle} (N_h-m)!

    であるから、

    .. math::
        a_h^{\langle m \rangle} = \frac{1}{(N_h-m)!} \eval{ \dv[N_h-m]{z} (z-z_h)^{N_h} \frac{P(z)}{Q(z)} }_{z=z_h}

    となり、示された。

.. prf:theorem:: Laurent 級数の主要部の和による表現
    :label: laurent_principal_part

    :prf:ref:`pfd_theorem` の状況において :math:`P(z)/Q(z)` のすべての極について、その極のまわりの Laurent 級数を考える。このとき、:eq:`pfd` はそれらの主要部の総和として表せる\ :footcite:ps:`Jimbo2024,Horiguchi2000`。

.. prf:proof::
    :math:`z=z_k` は :math:`Q(z)` の根であるとする。:math:`P(z)/Q(z)` の :math:`z=z_k` のまわりの Laurent 級数における :math:`1/(z-z_k)^n` の係数は :eq:`heaviside_coeff` で表せるから、:prf:ref:`heaviside_method` より、:eq:`pfd` の右辺の内側の総和はそのような Laurent 級数の主要部にほかならない。

    :math:`z=z_k` は :math:`P(z)/Q(z)` の高々 :math:`N_k` 位の極である。しかしながらこれが除去可能特異点であるならば主要部は :math:`0` であることに注意すると、:eq:`pfd` の右辺の外側の総和はすべての極をわたれば十分であり、示された。

例
~~

.. prf:example::
    :label: pfd_example

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
