Installation
============

.. code-block:: bash
    
    git clone https://github.com/bc31164b-cfd5-4a63-8144-875100622b2d/rln.git
    cd rln

    # run from git dir
    ./rln --list

Listing commands
----------------

Listing commands can be achieved via the ``--list`` flag.

.. code:: bash
    
    ./rln --list
    
    # Available tasks:
    # 
    #   create-aws-node              Creates an AWS lightning node, from start to
    #                                finish (excluding the security group).
    #   generate-docs                Generate this task documentation
    #   reset                        Perform a full reset and uninstall
    #                                (experimental).
    #   reset-wallet                 Performs a start to finish reset of the
    #                                wallet, this includes:
    #   setup-node                   Setup a lightning node on the given host, from
    #                                scratch. It assumes
    # ...


Listing command collections
---------------------------

Commands are grouped in collections. e.g to list all `aws` commands:

.. code:: bash
    
    ./rln --list aws
    
    # Available 'aws' tasks:
    #
    #  .attach-blockchain-disk   Attach disk to the node.
    #  .config-blockchain-disk   Add the disk to fstab, mount it, format it (optional), and create the
    #                            /blockchain fs path.
    #  .create                   Create the AWS EC2 instance, and wait until it's running, has a public
    #  .create-blockchain-disk   Create the blockchain disk of the given size, name, and in given availability
    #                            zone.
    #  .create-keypair           Create a key-pair called 'name' in default AWS region
    #  .create-security-group    Create the 'lightning' security group. This is the AWS EC2 level
    # ...

Getting help on specific commands
---------------------------------

Getting help for specific commands can be achieved via the ``--help`` flag, placed before the desired command:

.. code:: bash

    ./rln --help create-aws-node

    # Usage: rln [--core-opts] create-aws-node [--options] [other tasks here ...]
    #
    # Docstring:
    #   Creates an AWS lightning node, from start to finish (excluding the security group).
    # 
    #   This includes:
    # 
    #   - updating package information
    #   - creating the volume to hold the blockchain data
    #   - attaching the volume
    #   - formatting & mounting the volume
    #   - installing tor
    #   - building bitcoind from source
    #   - configuring bitcoind
    #   - installing go
    #   - building and install lnd
    #   - configuring lnd
    #   - installing balance of satoshis
    #   - install mosh
    #   - creating the wallet, and downloading the mnemonic and entropy to a password protected zipfile
    #   - saving the newly created node as the default (preferred node)
    # 
    # Options:
    #   -a STRING, --availability-zone=STRING   Exact zone, e.g if you're using us-east-1 as your default zone,
    #                                           this has to be e.g us-east-1a
    #   -d STRING, --disk-size=STRING
    #   -i STRING, --instance-type=STRING       EC2 instance type, recommended: t3.medium
    #   -k STRING, --keypair-name=STRING
    #   -m, --[no-]mainnet                      Whether to use mainnet or testnet
    #   -n STRING, --name=STRING                EC2 instances have names, a good name would be mainnet
    # ...


