Invoking nodes
==============

Working with specific nodes is really easy, since we can simply list their connection settings via the command line:

.. code:: bash

    ./rln -H ubuntu@10.10.10.10 -i ~/.rln/lightning/lightning_key.pem -- uname

The ``-H`` flag
---------------

The ``-H`` flag allows us to specify the ``user@host`` string. The understanding is that the ``user`` account is ``ssh`` enabled, on the given ``host``.

The ``-i`` flag
---------------

The ``-i`` flag allows us to specify the ``<node_name>_key.pem`` file used to authenticate securely. Please note it is best practice to save it in ``~/.rln/<node_name>/<node_name>.pem`` so it ties in nicely with the prefs functionality.


Invoking multiple nodes
-----------------------

You can even run commands on multiple nodes at once.

.. code:: bash

    ./rln -H ubuntu@10.10.10.10,ubuntu@20.20.20.20 -i ~/.rln/lightning/lightning_key.pem -i ~/.rln/testnet/testnet_key.pem -- uname

