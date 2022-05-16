Running commands natively
=========================

Fabric uses the `paramiko <http://www.paramiko.org/>`_ library to transparently run commands via ``ssh``. This enables us to easily run any command on our node from our workstation:

.. code:: bash

    rln -- uname
    # Linux

    rln -- lncli --version
    # lncli version 0.13.0-beta commit=v0.13.0-beta

    rln -- bitcoin-cli --version
    # 10.4.3

    rln -- bos --version
    # Bitcoin Core RPC client version v0.21.0

    rln -- bos balance
    # 208456

    rln -- bos chain-deposit

    # deposit_address: bc1qn6djg22wzdtw339ssql6xwcg5da5ep8yk5dvsj
    # deposit_qr:
    #  """
    #   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    #   █ ▄▄▄▄▄ ██▀▀▄▄▀ ▄▄█▀██ ████ ▄▄▄▄▄ █
    #   █ █   █ █▀███ ▄█▄█▀█▀█ ▄▀▄█ █   █ █
    #   █ █▄▄▄█ █▄▄█▀▀███▀  ▄█ ▄▄▄█ █▄▄▄█ █
    #   █▄▄▄▄▄▄▄█▄█ ▀▄█ █ █▄█▄█ ▀ █▄▄▄▄▄▄▄█
    #   █ ▄▀▀▀ ▄▄▀ █▄▀▀█▀ ▄▄▀▄█▄▀▀██▀  ████
    #   █ ▄▄▄▀▄▄▀▀▀▄█▀ ▄▄▀███ ▄▀▀▀█  █ ▀ ▀█
    #   █▄ ▀▀▄▄▄▄█▄█▄▄▄█ ▀█▀  ▀█ ▀█  █▄█▄ █
    #   ███    ▄█▀██ ▄██ ██▀█▄▄ ▀█ █    ▄▀█
    #   █▀ █▄▄ ▄▀▄█ ▄▀▀▀▀▀▄�▀▄█▀▀█▀▀█▄▀█ ▀█
    #   █▀▄███▀▄▄ █▄▄▀▀█▄▀█▀▄███▄▄▄  ▀▄▀▀▄█
    #   █▀█▄ ▀█▄▀█ ▄█▄█  ▄▄█▀█▀▄▀█▀█  ▄██▄█
    #   █ █▄▄▄▀▄▄▄ ▀ ▄█▀  ▄▄█▀▄██▄█▀██▀▀▄▀█
    #   █▄▄▄▄▄█▄█▀▄██▀  ▀ ▀▀  █▀▄ ▄▄▄ ▄▀▄ █
    #   █ ▄▄▄▄▄ █  ▀█▀  ▄▄▄ █▄█▄  █▄█ ▀▀ ██
    #   █ █   █ ██▄▀█▄█▄▀▀ ▄▀▄█▄█▄ ▄  █▀▀ █
    #   █ █▄▄▄█ █▀ █▀▄▄ ▄███ ▀█  █▀█▀▄█▀▄▄█
    #   █▄▄▄▄▄▄▄█▄▄▄▄███▄█▄████▄▄▄▄▄▄█▄█▄██
    #  """

This is incredibly useful, as it also enables us to use unix pipes or redirects to manipulate ``stdin`` and ``stdout`` into the rest of the gnu toolchain, via our current terminal on our local workstation.

Examples
--------

Pipe channels into channels.json
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    rln -- lncli listchannels > channels.json

Extract peer pub_keys using jq
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    lncli listpeers | jq '.peers[].pub_key'

    # "0245f703677f3c4066ee684caa3cbec90aef082542009f000186f1e455017169cc"
    # "03ce61cb90aa08f4b19b28d8393fa39d107fefa3ff8d303808449ed0853487d150"
    # "0381de1709efbda38f9afd2d47399caa19a2630c0c795acd24755efa442685fc7d"
    # "0304ce547809e86aa0afd31b9b1c762142ca598b5fea05834a996a107434e2c693"
    # "0217890e3aad8d35bc054f43acc00084b25229ecff0ab68debd82883ad65ee8266"
    # "03abf6f44c355dec0d5aa155bdbdd6e0c8fefe318eff402de65c6eb2e1be55dc3e"
    # "0311e4ee7e18ebd68b4e1c425da78a5a8af4d5825ece596d9258d152bd962a7e2b"
    # "023af4cbff89bd4bf01a58d39743b80ef8e76dccc04a81dfcc869d38b0fad4f0ae"
    # "022ea68ac7588959a6a4829a5ff176c296329d614b90b3f5f4456b5d6130ea50f6"