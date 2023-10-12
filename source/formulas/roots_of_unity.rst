1 の冪根に関する性質
=====================

とくに、:math:`1-e^{i 2 \pi /K}` に関する諸性質を並べる。

積の性質
~~~~~~~~

.. prf:theorem:: 積の性質
    :label: roots_of_unity_prop_prod

    正の整数 :math:`K` について、

    .. math::
        \prod_{k=1}^{K-1} (1-\zeta_K^k) = K

    が成り立つ。ここで、:math:`\zeta_K \triangleq e^{i 2 \pi /K}` である。

.. prf:proof::
    :math:`z^K-1` を複素数の範囲で因数分解すると、

    .. math::
        \begin{align}
        z^K-1
        &= \prod_{k=0}^{K-1} (z-\zeta_K^k) \\
        &= (z-1) \prod_{k=1}^{K-1} (z-\zeta_K^k)
        \end{align}

    となる。ここで、両辺の :math:`z=1` における微分係数を考えると、左辺について、

    .. math::
        \begin{align}
        \eval{ \dv{z} (z^K-1) }_{z=1}
        &= \eval{ K z^{K-1} }_{z=1} \\
        &= K
        \end{align}

    であり、右辺について、

    .. math::
        \begin{align}
        \eval{ \dv{z} (z-1) \prod_{k=1}^{K-1} (z-\zeta_K^k) }_{z=1}
        &= \eval{ \qty[ \prod_{k=1}^{K-1} (z-\zeta_K^k) + (z-1) \dv{z} \prod_{k=1}^{K-1} (z-\zeta_K^k) ] }_{z=1} \\
        &= \prod_{k=1}^{K-1} (1-\zeta_K^k)
        \end{align}

    となる。したがって、

    .. math::
        \prod_{k=1}^{K-1} (1-\zeta_K^k) = K

    となり、示された。

蛇足ながら、幾何的な性質を見いだせる。

.. prf:theorem:: 正多角形の対角線の長さの積
    :label: regular_polygon_prod

    半径 :math:`1` の円に内接する正 :math:`K` 角形について、ある頂点とそれ以外の頂点を結んだ :math:`K-1` 本の線分の長さの積は :math:`K` に等しい。

.. prf:proof::
    複素数平面上の :math:`z^K-1` の根を頂点とする正 :math:`K` 角形について、点 :math:`1` を共通の端点とする線分たちを考えても一般性を失わない。

    このとき、それらの線分の長さの積は、

    .. math::
        \prod_{k=1}^{K-1} \abs{1-\zeta_K^k} = \abs{\prod_{k=1}^{K-1} (1-\zeta_K^k)}

    と表せるから、:prf:ref:`roots_of_unity_prop_prod` により示された。

和の性質
~~~~~~~~

.. prf:theorem:: 逆数の冪和の性質
    :label: gessel

    正の整数 :math:`K,n` について、

    .. math::
        \sum_{k=1}^{K-1} \frac{1}{(1-\zeta_K^k)^n} =
        \frac{1}{(n-1)!} \sum_{r=1}^n \stirI{n}{r} \frac{B^-_r}{r} (1-K^r)

    が成り立つ\ :footcite:ps:`Duran1991,Gessel1996`。ここで、:math:`\zeta_K \triangleq e^{i 2 \pi /K}` である。また、:math:`\stirI{n}{r}` は符号なし第 1 種 Stirling 数であり、:math:`B^-_n` は Bernoulli 数で :math:`B^-_1=-1/2` となるほうである。

Gessel の技巧的な証明を概ねなぞることにする。

.. prf:proof::

    左辺について、:math:`S_{K,n}` を、

    .. math::
        S_{K,n} \triangleq \sum_{k=1}^{K-1} \frac{1}{(1-\zeta_K^k)^n}

    と定義し、:math:`S_{K,n}/n` の母関数 :math:`f(z)` を、

    .. math::
        :label: gessel_temp_1

        \begin{align}
        f(z)
        &\triangleq \sum_{n=1}^\infty \frac{S_{K,n}}{n} z^n \\
        &= \sum_{n=1}^\infty \frac{1}{n} \sum_{k=1}^{K-1} \frac{1}{(1-\zeta_K^k)^n} z^n \\
        &= \sum_{k=1}^{K-1} \sum_{n=1}^\infty \frac{1}{n} \qty( \frac{z}{1-\zeta_K^k} )^n
        \end{align}

    とおく。ここで、

    .. math::
        :label: log_expansion

        \frac{[\log(1-x)]^r}{r!} = (-1)^r \sum_{n=r}^\infty \stirI{n}{r} \frac{x^n}{n!}

    と Maclaurin 展開できることから、とくに :math:`r \triangleq 1` のとき、:math:`\stirI{n}{1} = (n-1)!` であることに注意すると、

    .. math::
        :label: log_expansion_1

        \log(1-x) = -\sum_{n=1}^\infty \frac{x^n}{n}

    であり、:eq:`log_expansion_1` に :math:`x \triangleq z/(1-\zeta_K^k)` を代入すると、:eq:`gessel_temp_1` は、

    .. math::
        :label: gessel_temp_2

        \begin{align}
        f(z)
        &= -\sum_{k=1}^{K-1} \log \qty( 1 - \frac{z}{1-\zeta_K^k} ) \\
        &= -\sum_{k=1}^{K-1} \log \frac{(1-z)-\zeta_K^k}{1-\zeta_K^k}
        \end{align}

    とできる。ここで、:math:`w \triangleq \log(1-z)` とおく。:math:`1-z = e^w` であることから、:eq:`gessel_temp_2` は、

    .. math::
        :label: gessel_temp_3

        \begin{align}
        f(z)
        &= -\sum_{k=1}^{K-1} \log \frac{e^w-\zeta_K^k}{1-\zeta_K^k} \\
        &= \sum_{k=1}^{K-1} \log (1-\zeta_K^k) - \sum_{k=1}^{K-1} \log ( e^w-\zeta_K^k ) \\
        &= \log \prod_{k=1}^{K-1} (1-\zeta_K^k) - \log \prod_{k=1}^{K-1} ( e^w-\zeta_K^k )
        \end{align}

    となり、:prf:ref:`1 の冪根に関する積の性質 <roots_of_unity_prop_prod>` より、:eq:`gessel_temp_3` は、

    .. math::
        :label: gessel_temp_4

        \begin{align}
        f(z)
        &= \log K - \log \prod_{k=1}^{K-1} ( e^w-\zeta_K^k ) \\
        &= \log K - \log \frac{e^{Kw} - 1}{e^w - 1} \\
        &= \log K - \log (e^{Kw}-1) + \log (e^w-1) \\
        &= \qty[ \log K + \log w - \log (e^{Kw}-1) ] - \qty[ \log w - \log (e^w-1) ] \\
        &= \log \frac{Kw}{e^{Kw}-1} - \log \frac{w}{e^w-1} \\
        &= \int_w^{Kw} \dv{x} \log \frac{x}{e^x-1} \dd{x} \\
        &= \int_w^{Kw} \qty[ \dv{x} \log x - \dv{x} \log(e^x-1) ] \dd{x} \\
        &= \int_w^{Kw} \qty[ \frac{1}{x} - \frac{e^x}{e^x-1} ] \dd{x} \\
        &= \int_w^{Kw} \qty[ \frac{1}{x} \qty( 1 - \frac{x e^x}{e^x-1} ) ] \dd{x}
        \end{align}

    となる。ここで、Bernoulli 数 :math:`B^-_r` の母関数が、

    .. math::
        \frac{x}{e^x-1} = \sum_{r=0}^\infty \frac{B^-_r}{r!} x^r

    と表されるから、:math:`x` を :math:`-x` と置き換えることで、

    .. math::
        \frac{x e^x}{e^x-1} = \sum_{r=0}^\infty \frac{(-1)^r B^-_r}{r!} x^r

    となり、:eq:`gessel_temp_4` は、

    .. math::
        :label: gessel_temp_5

        \begin{align}
        f(z)
        &= \int_w^{Kw} \qty[ \frac{1}{x} \qty( 1 - \sum_{r=0}^\infty \frac{(-1)^r B^-_r}{r!} x^r ) ] \dd{x} \\
        &= \int_w^{Kw} \qty[ \frac{1}{x} \qty( 1 - \frac{B^-_0}{0!} - \sum_{r=1}^\infty \frac{(-1)^r B^-_r}{r!} x^r) ] \dd{x} \\
        &= - \sum_{r=1}^\infty \frac{(-1)^r B^-_r}{r!} \int_w^{Kw} x^{r-1} \dd{x} \\
        &= - \sum_{r=1}^\infty \frac{(-1)^r B^-_r}{r!} \frac{K^r-1}{r} w^r \\
        &= \sum_{r=1}^\infty \frac{B^-_r}{r} (1-K^r) (-1)^r \frac{[\log(1-z)]^r}{r!}
        \end{align}

    となる。ここで、対数関数に関する Maclaurin 展開 :eq:`log_expansion` より、:eq:`gessel_temp_5` は、

    .. math::
        :label: gessel_temp_6

        f(z) = \sum_{r=1}^\infty \frac{B^-_r}{r} (1-K^r)
        \sum_{n=r}^\infty \stirI{n}{r} \frac{z^n}{n!}

    となる。二重総和部について、各 :math:`n \geq 1` について :math:`r` は :math:`1 \leq r \leq n` を動くことに注意して :eq:`gessel_temp_6` の総和記号を入れ替えると、

    .. math::
        \begin{align}
        f(z)
        &= \sum_{n=1}^\infty \sum_{r=1}^n \stirI{n}{r} \frac{B^-_r}{r} (1-K^r) \frac{z^n}{n!} \\
        &= \sum_{n=1}^\infty \qty[ \frac{1}{(n-1)!} \sum_{r=1}^n \stirI{n}{r} \frac{B^-_r}{r} (1-K^r) ] \frac{z^n}{n}
        \end{align}

    となり、示された。

蛇足ながら、これにも幾何的な性質を見いだせる。

.. prf:theorem:: 正多角形の対角線の長さの逆数の偶数冪和
    :label: regular_polygon_recip_sq_sum

    半径 :math:`1` の円に内接する正 :math:`K` 角形について、ある頂点とそれ以外の頂点を結んだ :math:`K-1` 本の線分の長さの :math:`2M` 乗の逆数和は、

    .. math::
        \sum_{m=0}^M \frac{(-1)^m}{(M+m-1)!} \binom{M}{m} \sum_{r=1}^{M+m} \stirI{M+m}{r} \frac{B^-_r}{r} (1-K^r)

    である。ただし、:math:`M` は正の整数である。

.. prf:proof::
    複素数平面上の :math:`z^K-1` の根を頂点とする正 :math:`K` 角形について、点 :math:`1` を共通の端点とする線分たちを考えても一般性を失わない。

    このとき、それらの線分の長さの :math:`2M` 乗の逆数和は、

    .. math::
        \begin{align}
        \sum_{k=1}^{K-1} \frac{1}{\abs{1-\zeta_K^k}^{2M}}
        &= \sum_{k=1}^{K-1} \qty[ \frac{1}{(1-\zeta_K^k)(1-\zeta_K^{-k})} ]^M \\
        &= \sum_{k=1}^{K-1} \qty[ \frac{-\zeta_K^k}{(1-\zeta_K^k)^2} ]^M \\
        &= \sum_{k=1}^{K-1} \qty[ \frac{1}{1-\zeta_K^k} - \frac{1}{(1-\zeta_K^k)^2} ]^M \\
        &= \sum_{k=1}^{K-1} \frac{1}{(1-\zeta_K^k)^M} \qty(1 - \frac{1}{1-\zeta_K^k} )^M \\
        &= \sum_{k=1}^{K-1} \frac{1}{(1-\zeta_K^k)^M} \sum_{m=0}^M (-1)^m \binom{M}{m} \frac{1}{(1-\zeta_K^k)^m} \\
        &= \sum_{k=1}^{K-1} \sum_{m=0}^M (-1)^m \binom{M}{m} \frac{1}{(1-\zeta_K^k)^{M+m}} \\
        &= \sum_{m=0}^M (-1)^m \binom{M}{m} \sum_{k=1}^{K-1} \frac{1}{(1-\zeta_K^k)^{M+m}}
        \end{align}

    と表せるから、:prf:ref:`gessel` より、

    .. math::
        \sum_{k=1}^{K-1} \frac{1}{\abs{1-\zeta_K^k}^{2M}} = \sum_{m=0}^M \frac{(-1)^m}{(M+m-1)!} \binom{M}{m} \sum_{r=1}^{M+m} \stirI{M+m}{r} \frac{B^-_r}{r} (1-K^r)

    となり、示された。

.. footbibliography::
