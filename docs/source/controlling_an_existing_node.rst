Controlling an existing node
============================

If you have an existing node you'd like to manage using ``rln`` you simply need to make sure the binaries you are interested in are in your ``$PATH`` for non-login shells.

An easy way to achieve this is to place them at the top of your ``.bashrc`` on the host. e.g

.. code:: bash

    GOPATH="$HOME/go"
    PATH="$HOME/.npm-global/bin:$PATH"
    PATH="$HOME/bin:$GOPATH/bin:$HOME/.local/bin:/usr/local/go/bin:$PATH"


You should then be able to run your commands transparently:

.. code:: bash
    
    lncli --version
    # lncli version 0.13.0-beta commit=v0.13.0-beta
