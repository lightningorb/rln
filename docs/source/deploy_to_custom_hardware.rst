Deploy to a linux host
======================

You can deploy a lightning node to any clean Ubuntu 20.04.2 host.

``rln`` currently assumes a few things about your host:

-  You have an external SSD mounted on ``/blockchain``, or the system's SSD has enough space to host bitcoin's blockchain.
-  The host is running ``Ubuntu 20.04.2``.

If these conditions are met, you can start by telling ``rln`` about
your node:

.. code:: bash

   $ mkdir ~/.rln/lightning/lightning_key.pem
   $ cp key.pem ~/.rln/lightning/lightning_key.pem

   $ ./rln -H ubuntu@10.10.10.10 \
      -i ~/.rln/lightning/lightning_key.pem \
      setup-node --name lightning

You can now test the waters with:

.. code:: bash

   $ ./rln -- uname -a

Output:

.. code:: bash

   Linux lightning #47-Ubuntu SMP Tue Apr 13 07:02:25 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux

You can now run the deployment:

.. code:: bash

   $ ./rln setup-node --name lightning --mainnet

When you’re prompted for a password, this is to create an encrypted zipfile
that contains your seed, and the entropy used to generate it. The wallet seed is saved in ``~/.rln/lightning/lightning_secrets.zip``. Keep it safe. If you ever need to re-create your wallet or your node, it will get used to restore your wallet.
