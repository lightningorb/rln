RLN Overview
================

The idea behind `rln` is to provide the ability to securely, swiftly, and easily deploy a fully-configured lightning node to AWS or custom hardware in a handful of minutes, with zero manual configuration.


Intended audience
-----------------

The target audience is technical users, developers, organisations in need of deploying lightning nodes programmatically at scale, or non-technical users willing to learn how to manage their lightning node via the CLI.

Secure
------

Security is tantamount to `rln`, and the setup is robust, giving you the confidence to allocate funds without the fear of losing them. The firewall settings are optimal, and nodes can only be accessed via a `.pem` protected `ssh` connection, and nothing else.

Open Source
-----------

The stack is minimalistic, built from source, and 100% open-source. It currently uses:

- bitcoind
- lnd
- tor
- bos

Built on
--------

`rln` uses `Fabric <http://www.fabfile.org/>`_, a python library for remote host configuration and administration. Fabric makes `rln` highly and easily extensible, and gives you the ability to write your own scripts easily (docs coming soon for extending functionality).

Fabric allows creating `DLSs <https://en.wikipedia.org/wiki/Domain-specific_language>`_, that turn complex administration tasks into simple and flexible one-liners.

Convenience
-----------

ssh-ing is done transparently in the background via the `paramiko <http://www.paramiko.org/>`_ library. This means with simple aliases `bicoin-cli`, `lncli` and `bos` commands can be run directly from your workstation, as if they were running on your local host.


Indices and tables
==================

.. toctree::
   :maxdepth: 2
   :includehidden:

   self
   installation
   deploy_to_aws
   deploy_to_custom_hardware
   invoking_nodes
   prefs
   running_commands_natively
   setting_up_aliases
   controlling_an_existing_node
   security

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
   :maxdepth: 2
   :includehidden:

   commands
