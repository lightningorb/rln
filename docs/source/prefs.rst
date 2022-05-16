Prefs
=====

You'll generally only want to work with one host at a time. After creating an ``AWS`` node, the node because your default.

However you can add any number of nodes to your prefs file, located in ``~/.rln/prefs.toml``.

.. code:: bash

    rln -H ubuntu@10.10.10.10 -i ~/.rln/lightning/lightning_key.pem prefs.save --name lightning

.. code:: bash

    rln -H ubuntu@20.20.20.20 -i ~/.rln/testnet/testnet_key.pem prefs.save --name testnet

We now have two nodes in our prefs:

- lightning
- testnet

We can easily set ``lightning`` as our preferred node:

.. code:: bash

    rln prefs.set-default --name lightning
    
    rln -- uname -a
    # Linux 5.8.0-1038-aws #40~20.04.1-Ubuntu SMP Thu Jun 17 13:25:28 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux


Or ``testnet`` as our preferred node:

.. code:: bash

    rln prefs.set-default --name testnet
    
    rln -- uname -a
    # Linux testnet 5.8.0-55-generic #62-Ubuntu SMP Tue Jun 1 08:21:18 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
