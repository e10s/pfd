応用
====

n 倍角の公式
~~~~~~~~~~~~

.. prf:theorem:: 余接関数の n 倍角の公式
    :label: cot_multiple_angle

    整数 :math:`n \neq 0` について、

    .. math::
        \cot nt = \frac{1}{n} \sum_{k=0}^{\abs{n}-1} \cot ( t \pm \frac{k}{n} \pi )

    が成り立つ。

.. prf:proof::
    Euler の公式より、

    .. math::
        \cot t
        &= \frac{\cos t}{\sin t} \\
        &= \frac{e^{it} + e^{-it}}{2} \frac{2i}{e^{it} - e^{-it}} \\
        &= i \frac{e^{i 2t} + 1}{e^{i 2t} - 1} \\
        &= i \qty[ 1 + \frac{2}{e^{i 2t} - 1} ]

    と表せる。このとき、正の整数 :math:`K` について、

    .. math::
        \cot Kt = i \qty[ 1 + \frac{2}{e^{i 2Kt} - 1} ]

    となり、:prf:ref:`1 の冪根と部分分数分解の公式 <roots_of_unity_pfd>` より、

    .. math::
        \cot Kt
        &= i \qty[ 1 + \frac{2}{(e^{i 2t})^K - 1} ] \\
        &= i \qty[ 1 + \frac{1}{K} \sum_{k=0}^{K-1} \frac{2 \zeta_K^k}{e^{i 2t} - \zeta_K^k} ] \\
        &= \frac{i}{K} \qty[ K + \sum_{k=0}^{K-1} \frac{2}{e^{i 2t} \zeta_K^{-k} - 1} ] \\
        &= \frac{1}{K} \sum_{k=0}^{K-1} i \qty[ 1 + \frac{2}{e^{i 2t} \zeta_K^{-k} - 1} ] \\
        &= \frac{1}{K} \sum_{k=0}^{K-1} i \qty[ 1 + \frac{2}{e^{i 2(t - k \pi/K)} - 1} ] \\
        &= \frac{1}{K} \sum_{k=0}^{K-1} \cot (t - \frac{k}{K} \pi)

    が成り立つ。さらに :math:`t` を :math:`-t` に置き換え、両辺に :math:`-1` を掛けると、

    .. math::
        -\cot (-Kt) = -\frac{1}{K} \sum_{k=0}^{K-1} \cot (-t - \frac{k}{K} \pi)

    となり、:math:`\cot` が奇関数であることに注意すると、

    .. math::
        \cot Kt = \frac{1}{K} \sum_{k=0}^{K-1} \cot (t + \frac{k}{K} \pi)

    となる。以上の議論より、

    .. math::
        :label: cot_n_temp_pos

        \cot Kt = \frac{1}{K} \sum_{k=0}^{K-1} \cot (t \pm \frac{k}{K} \pi)

    が成り立つ。

    さらに、負の整数 :math:`n` について、:eq:`cot_n_temp_pos` において :math:`K \triangleq -n` とすることにより、:math:`\cot` が奇関数であることにふたたび注意すると、

    .. math::
        :label: cot_n_temp_neg

        \cot nt
        &= -\cot Kt \\
        &= -\frac{1}{K} \sum_{k=0}^{K-1} \cot (t \pm \frac{k}{K} \pi) \\
        &= \frac{1}{n} \sum_{k=0}^{-n-1} \cot (t \mp \frac{k}{n} \pi)

    が成り立つ。

    :eq:`cot_n_temp_pos` および :eq:`cot_n_temp_neg` により示された。

蛇足ながら、さらに発展させることで正弦関数の n 倍角の公式が導かれる。

.. prf:theorem:: 正弦関数の n 倍角の公式
    :label: sin_multiple_angle

    正の整数 :math:`n` について、

    .. math::
        \sin nt = 2^{n-1} \prod_{k=0}^{n-1} \sin ( t + \frac{k}{n} \pi )

    が成り立つ。

.. prf:proof::
    :prf:ref:`cot_multiple_angle` より、正の整数 :math:`n` について、

    .. math::
        \cot nt = \frac{1}{n} \sum_{k=0}^{n-1} \cot ( t + \frac{k}{n} \pi )

    が成り立つから、この両辺の不定積分をとると、:math:`C` を定数として、

    .. math::
        \frac{1}{n} \log( C \sin nt)
        &= \frac{1}{n} \sum_{k=0}^{n-1} \log \qty[ \sin ( t + \frac{k}{n} \pi ) ] \\
        &= \frac{1}{n} \log \prod_{k=0}^{n-1} \sin ( t + \frac{k}{n} \pi )

    と表せる。ゆえに、真数を比較することにより、

    .. math::
        :label: sin_n_temp

        C \sin nt = \prod_{k=0}^{n-1} \sin ( t + \frac{k}{n} \pi )


    と表されることがわかり、これを満たす :math:`C` を求めればよい。

    :eq:`sin_n_temp` の両辺を微分すると、

    .. math::
        Cn \cos nt
        &= \dv{t} \sin t \prod_{k=1}^{n-1} \sin ( t + \frac{k}{n} \pi ) \\
        &= \cos t \prod_{k=1}^{n-1} \sin ( t + \frac{k}{n} \pi ) + \sin t \dv{t} \prod_{k=1}^{n-1} \sin ( t + \frac{k}{n} \pi )

    であるから、:eq:`sin_n_temp` の両辺について :math:`t = 0` における微分係数は、

    .. math::
        Cn
        &= \prod_{k=1}^{n-1} \sin \frac{k}{n} \pi \\
        &= \prod_{k=1}^{n-1} \frac{ e^{i k \pi/ n} - e^{-i k \pi/ n} }{2i} \\
        &= \prod_{k=1}^{n-1} \frac{i}{2} ( e^{-i k \pi/ n} - e^{i k \pi/ n} ) \\
        &= \frac{i^{n-1}}{2^{n-1}} \prod_{k=1}^{n-1} e^{-i k \pi/ n} (1-e^{i 2 \pi k/n}) \\
        &= \frac{(e^{i \pi/ 2})^{n-1}}{2^{n-1}} (e^{-i \pi/ n})^{n(n-1)/2} \prod_{k=1}^{n-1} (1-e^{i 2 \pi k/n}) \\
        &= \frac{1}{2^{n-1}} \prod_{k=1}^{n-1} (1-e^{i 2 \pi k/n})

    である。ここで、:prf:ref:`1 の冪根に関する積の性質 <roots_of_unity_prop_prod>` より、

    .. math::
        C = \frac{1}{2^{n-1}}

    となるから、:eq:`sin_n_temp` より、示された。
