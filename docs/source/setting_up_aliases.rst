Setting up bash aliases
=======================

By setting up aliases in your local ``.bashrc`` or ``.profile`` file, you can invoke lightning commands directly from your local host.

.. code:: bash

    alias rlnd='rln ${*}'
    alias lncli='rln -- lncli ${*}'
    alias bitcoin-cli='rln -- bitcoin-cli ${*}'
    alias bos='rln -- bos ${*}'

Then a terminal:

.. code:: bash

    hash -r

    lncli --version
    # lncli version 0.13.0-beta commit=v0.13.0-beta

    bos --version
    # 10.4.3
    
    bitcoin-cli --version
    # Bitcoin Core RPC client version v0.21.0

    bos chart-chain-fees

    #                            Payments received
    #
    # 1000000.00 ┼                                                       ╭─╮
    #  933333.33 ┤                                                       │ │
    #  866666.67 ┤                                                       │ │
    #  800000.00 ┤                                                       │ │
    #  733333.33 ┤                                                       │ │
    #  666666.67 ┤                                                       │ │
    #  600000.00 ┤                                                       │ │
    #  533333.33 ┤                                                       │ │
    #  466666.67 ┤                                                       │ │
    #  400000.00 ┤                                                       │ │
    #  333333.33 ┤                                                       │ │
    #  266666.67 ┤                                                       │ │
    #  200000.00 ┤                                                       │ │
    #  133333.33 ┤                                                       │ │
    #   66666.67 ┤                                                       │ │
    #       0.00 ┼───────────────────────────────────────────────────────╯ ╰─
    #              Received in 60 days since 05/09/2021. Total: 0.02000000