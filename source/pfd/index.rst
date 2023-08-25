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
        \begin{align}
            &\phantom{{}={}} \dv[N_h-m]{z} (z-z_h)^{N_h} \sum_{k=0}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} \\
            &= \dv[N_h-m]{z} \qty[ (z-z_h)^{N_h} \sum_{k=0,k \neq h}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} + \sum_{n=1}^{N_h} a_h^{\langle n \rangle} (z-z_h)^{N_h-n} ] \\
            &= \dv[N_h-m]{z} \qty[ (z-z_h)^{N_h} \sum_{k=0,k \neq h}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} + \sum_{n=1,n \neq m}^{N_h} a_h^{\langle n \rangle} (z-z_h)^{N_h-n} + a_h^{\langle m \rangle} (z-z_h)^{N_h-m} ] \\
            &= a_h^{\langle m \rangle} \dv[N_h-m]{z} (z-z_h)^{N_h-m} + \dv[N_h-m]{z} \qty[ (z-z_h)^{N_h} \sum_{k=0,k \neq h}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} + \sum_{n=1}^{m-1} a_h^{\langle n \rangle} (z-z_h)^{N_h-n} ] \\
            &= a_h^{\langle m \rangle} (N_h-m)! + \dv[N_h-m]{z} \qty[ (z-z_h)^{N_h} \sum_{k=0,k \neq h}^K \sum_{n=1}^{N_k} \frac{ a_k^{\langle n \rangle} }{(z-z_k)^n} + \sum_{n=1}^{m-1} a_h^{\langle n \rangle} (z-z_h)^{N_h-n} ]
        \end{align}

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
