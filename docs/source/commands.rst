Commands
========

``rln generate-docs``
-----------

.. code:: bash

    Usage: rln [--core-opts] generate-docs [other tasks here ...]
    
    Docstring:
      Generate this task documentation
    
    Options:
      none
    
    

``rln reset-wallet``
-----------

.. code:: bash

    Usage: rln [--core-opts] reset-wallet [--options] [other tasks here ...]
    
    Docstring:
      Performs a start to finish reset of the wallet, this includes:
    
      - shutting down bitcoind softly
      - shutting down lnd
      - deleting the ~/.lnd folder
      - re-running the lnd setup task
      - re-creating the wallet using the password protected secrets.zip file
    
      This command is mostly useful for getting a clean lnd slate while maintaining wallet information
    
    Options:
      -n STRING, --name=STRING
    
    

``rln create-aws-node``
-----------

.. code:: bash

    Usage: rln [--core-opts] create-aws-node [--options] [other tasks here ...]
    
    Docstring:
      Creates an AWS lightning node, from start to finish (excluding the security group).
    
      This includes:
    
      - updating package information
      - creating the volume to hold the blockchain data
      - attaching the volume
      - formatting & mounting the volume
      - installing tor
      - building bitcoind from source
      - configuring bitcoind
      - installing go
      - building and install lnd
      - configuring lnd
      - installing balance of satoshis
      - install mosh
      - creating the wallet, and downloading the mnemonic and entropy to a password protected zipfile
      - saving the newly created node as the default (preferred node)
    
    Options:
      -a STRING, --availability-zone=STRING   Exact zone, e.g if you're using us-
                                              east-1 as your default zone, this has
                                              to be e.g us-east-1a
      -d STRING, --disk-size=STRING
      -i STRING, --instance-type=STRING       EC2 instance type, recommended:
                                              t3.medium
      -k STRING, --keypair-name=STRING
      -m, --[no-]mainnet                      Whether to use mainnet or testnet
      -n STRING, --name=STRING                EC2 instances have names, a good name
                                              would be mainnet
    
    

``rln setup-node``
-----------

.. code:: bash

    Usage: rln [--core-opts] setup-node [--options] [other tasks here ...]
    
    Docstring:
      Setup a lightning node on the given host, from scratch. It assumes
      a large enough disk is mounted on /blockchain. This includes:
    
      - allowing up to 512000 open files
      - configuring ufw and iptables against flooding
      - installing tor
      - building bitcoind from source
      - configuring bitcoind
      - installing go
      - building and install lnd
      - configuring lnd
      - installing balance of satoshis
      - install mosh
      - creating the wallet, and downloading the mnemonic and entropy to a password protected zipfile
      - saving the newly created node as the default (preferred node)
    
    Options:
      -m, --[no-]mainnet
      -n STRING, --name=STRING
    
    

``rln reset``
-----------

.. code:: bash

    Usage: rln [--core-opts] reset [other tasks here ...]
    
    Docstring:
      Perform a full reset and uninstall (experimental).
    
    Options:
      none
    
    

``rln soft-reboot``
-----------

.. code:: bash

    Usage: rln [--core-opts] soft-reboot [other tasks here ...]
    
    Docstring:
      Softly shut down bitcoind, and lnd, then reboot the system.
    
    Options:
      none
    
    

``rln soft-shutdown``
-----------

.. code:: bash

    Usage: rln [--core-opts] soft-shutdown [other tasks here ...]
    
    Docstring:
      Softly shut down bitcoind, and lnd.
    
    Options:
      none
    
    

``rln aws.save-credentials``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.save-credentials [--options] [other tasks here ...]
    
    Docstring:
      Saves your AWS credentials and default zone in your
      default AWS configuration files:
    
      ~/.aws/config
      ~/.aws/credentials
    
    Options:
      -a STRING, --access-key=STRING
      -k STRING, --key-id=STRING
      -r STRING, --region=STRING
    
    

``rln aws.show-ip``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.show-ip [--options] [other tasks here ...]
    
    Docstring:
      Print and return the public ip address for the given
      AWS instance name
    
    Options:
      -n STRING, --name=STRING   The EC2 instance name you chose during creation
    
    

``rln aws.create-keypair``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.create-keypair [--options] [other tasks here ...]
    
    Docstring:
      Create a key-pair called 'name' in default AWS region
    
    Options:
      -n STRING, --name=STRING   The EC2 key-pair to ssh into this node
    
    

``rln aws.delete-keypair``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.delete-keypair [--options] [other tasks here ...]
    
    Docstring:
      Delete a key-pair called 'name' in the default AWS region
    
    Options:
      -n STRING, --name=STRING   The EC2 key-pair to delete
    
    

``rln aws.describe-key-pairs``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.describe-key-pairs [other tasks here ...]
    
    Docstring:
      Print and retrieve all key-pairs for default AWS region
    
    Options:
      none
    
    

``rln aws.create-security-group``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.create-security-group [other tasks here ...]
    
    Docstring:
      Create the 'lightning' security group. This is the AWS EC2 level
      firewall protection that prevents the outside world from connecting
      to your node. Please note this is created in your default region.
    
    Options:
      none
    
    

``rln aws.create``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.create [--options] [other tasks here ...]
    
    Docstring:
      Create the AWS EC2 instance, and wait until it's running, has a public
      IP, and we're able to SSH into it.
    
    Options:
      -a STRING, --availability-zone=STRING   Exact zone, e.g if you're using us-
                                              east-1 as your default zone, this has
                                              to be e.g us-east-1a
      -i STRING, --instance-type=STRING       EC2 instance type, recommended:
                                              t3.medium
      -k STRING, --keypair-name=STRING
      -n STRING, --name=STRING                EC2 instances have names, a good name
                                              would be mainnet
    
    

``rln aws.create-blockchain-disk``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.create-blockchain-disk [--options] [other tasks here ...]
    
    Docstring:
      Create the blockchain disk of the given size, name, and in given availability zone.
    
    Options:
      -a STRING, --availability-zone=STRING   The exact zone in which to create the
                                              disk. This is usually your default
                                              zone adding with an a or b.
      -d STRING, --disk-size=STRING           The disk's size in GB
      -n STRING, --name=STRING                The name of the newly created disk
    
    

``rln aws.attach-blockchain-disk``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.attach-blockchain-disk [--options] [other tasks here ...]
    
    Docstring:
      Attach disk to the node.
    
    Options:
      -d STRING, --disk-name=STRING   The disk's name
      -n STRING, --node-name=STRING   The node's name
    
    

``rln aws.delete-blockchain-disk``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.delete-blockchain-disk [--options] [other tasks here ...]
    
    Docstring:
      Delete disk with the given name. User with care.
    
    Options:
      -d STRING, --disk-name=STRING   The disk's name
    
    

``rln aws.detach-blockchain-disk``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.detach-blockchain-disk [--options] [other tasks here ...]
    
    Docstring:
      Detach disk with the given name.
    
    Options:
      -d STRING, --disk-name=STRING   The disk's name
    
    

``rln aws.config-blockchain-disk``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.config-blockchain-disk [--options] [other tasks here ...]
    
    Docstring:
      Add the disk to fstab, mount it, format it (optional), and create the /blockchain fs path.
    
    Options:
      -d STRING, --disk-size=STRING   The disk's size in GB.
      -f, --format                    Whether to format the disk or not
    
    

``rln aws.kill``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.kill [--options] [other tasks here ...]
    
    Docstring:
      Delete the node.
    
    Options:
      -f, --force
      -n STRING, --node-name=STRING
    
    

``rln aws.show-running``
-----------

.. code:: bash

    Usage: rln [--core-opts] aws.show-running [other tasks here ...]
    
    Docstring:
      Print out a list of running instances, and their ip addresses
    
    Options:
      none
    
    

``rln btc.build``
-----------

.. code:: bash

    Usage: rln [--core-opts] btc.build [other tasks here ...]
    
    Docstring:
      Build bitcoind from source.
      Create the required /blockchain bitcoin (sub)directories.
    
    Options:
      none
    
    

``rln btc.reset``
-----------

.. code:: bash

    Usage: rln [--core-opts] btc.reset [--options] [other tasks here ...]
    
    Docstring:
      none
    
    Options:
      -u, --[no-]use-tor
    
    

``rln btc.setup``
-----------

.. code:: bash

    Usage: rln [--core-opts] btc.setup [--options] [other tasks here ...]
    
    Docstring:
      Set up bitcoin.
    
      This includes:
    
      - generating the rpcauth passwords
      - configuring ~/.bitcoin/bitcoin.conf
      - starting bitcoind
      - configuring bitcoind to start on reboot
      - setting up log rotation
      - creating log symbolic links
      - setting proper permissions on the /blockchain mount
    
    Options:
      -m, --[no-]mainnet   If true use mainnet, else use testnet
      -u, --[no-]use-tor   Connect with peers via the tor network
    
    

``rln btc.stop``
-----------

.. code:: bash

    Usage: rln [--core-opts] btc.stop [other tasks here ...]
    
    Docstring:
      Stop bitcoind softly. This task will not return until bitcoind
      has written all its data to disk. This is to prevent having to
      re-scan the entire blockchain in case the command is followed by
      a reboot.
    
    Options:
      none
    
    

``rln btc.start``
-----------

.. code:: bash

    Usage: rln [--core-opts] btc.start [other tasks here ...]
    
    Docstring:
      Start bitcoind. Block, and keep scanning the logs until bitcoind
      has indeed started successfully.
    
    Options:
      none
    
    

``rln btc.show-sync-progress``
-----------

.. code:: bash

    Usage: rln [--core-opts] btc.show-sync-progress [other tasks here ...]
    
    Docstring:
      Attempts to provide an estimated date in time for when the blockchain
      is synced (in local time). Probably highly inacurate.
    
    Options:
      none
    
    

``rln btc.logs``
-----------

.. code:: bash

    Usage: rln [--core-opts] btc.logs [other tasks here ...]
    
    Docstring:
      Tail bitcion's logs until cancelled.
    
    Options:
      none
    
    

``rln ssh.ssh``
-----------

.. code:: bash

    Usage: rln [--core-opts] ssh.ssh [other tasks here ...]
    
    Docstring:
      ssh into the current node. This might not work with windows yet.
    
    Options:
      none
    
    

``rln ssh.mosh``
-----------

.. code:: bash

    Usage: rln [--core-opts] ssh.mosh [other tasks here ...]
    
    Docstring:
      mosh into the current node. This might not work with windows yet.
    
    Options:
      none
    
    

``rln ssh.install-mosh``
-----------

.. code:: bash

    Usage: rln [--core-opts] ssh.install-mosh [other tasks here ...]
    
    Docstring:
      Install mosh, and configure ufw to allow connection on port 60k.
    
    Options:
      none
    
    

``rln ssh.get``
-----------

.. code:: bash

    Usage: rln [--core-opts] ssh.get [--options] [other tasks here ...]
    
    Docstring:
      none
    
    Options:
      -l STRING, --local=STRING
      -r STRING, --remote=STRING
    
    

``rln lnd.install-go``
-----------

.. code:: bash

    Usage: rln [--core-opts] lnd.install-go [other tasks here ...]
    
    Docstring:
      Install Go 1.16.5.
    
    Options:
      none
    
    

``rln lnd.logs``
-----------

.. code:: bash

    Usage: rln [--core-opts] lnd.logs [other tasks here ...]
    
    Docstring:
      Tail lnd logs until cancelled.
    
    Options:
      none
    
    

``rln lnd.install``
-----------

.. code:: bash

    Usage: rln [--core-opts] lnd.install [--options] [other tasks here ...]
    
    Docstring:
      Install lnd, and configure it with systemd.
    
    Options:
      -v STRING, --version=STRING
    
    

``rln lnd.reset``
-----------

.. code:: bash

    Usage: rln [--core-opts] lnd.reset [other tasks here ...]
    
    Docstring:
      Reset lnd configuration, and re-create .lnd folder.
    
    Options:
      none
    
    

``rln lnd.setup``
-----------

.. code:: bash

    Usage: rln [--core-opts] lnd.setup [other tasks here ...]
    
    Docstring:
      Set up lnd with lnd.conf, and bitcoind's rpc password.
    
    Options:
      none
    
    

``rln lnd.start``
-----------

.. code:: bash

    Usage: rln [--core-opts] lnd.start [other tasks here ...]
    
    Docstring:
      Start lnd.
    
    Options:
      none
    
    

``rln lnd.stop``
-----------

.. code:: bash

    Usage: rln [--core-opts] lnd.stop [other tasks here ...]
    
    Docstring:
      Stop lnd.
    
    Options:
      none
    
    

``rln lnd.restart``
-----------

.. code:: bash

    Usage: rln [--core-opts] lnd.restart [other tasks here ...]
    
    Docstring:
      Restart lnd.
    
    Options:
      none
    
    

``rln lnd.journal``
-----------

.. code:: bash

    Usage: rln [--core-opts] lnd.journal [other tasks here ...]
    
    Docstring:
      Display systemctl's journals for lnd.
    
    Options:
      none
    
    

``rln lnd.backup-channels``
-----------

.. code:: bash

    Usage: rln [--core-opts] lnd.backup-channels [--options] [other tasks here ...]
    
    Docstring:
      Create a backup file of the open channels, and download it to ~/.rln
    
    Options:
      -n STRING, --node-name=STRING
    
    

``rln lnd.get-graph``
-----------

.. code:: bash

    Usage: rln [--core-opts] lnd.get-graph [other tasks here ...]
    
    Docstring:
      Run a describe graph and download as ./graph.json
    
    Options:
      none
    
    

``rln bos.install``
-----------

.. code:: bash

    Usage: rln [--core-opts] bos.install [other tasks here ...]
    
    Docstring:
      Install Balance of Satohis. Includes first installing and configuring nodejs.
    
    Options:
      none
    
    

``rln bos.unlock``
-----------

.. code:: bash

    Usage: rln [--core-opts] bos.unlock [other tasks here ...]
    
    Docstring:
      Unlock lightning wallet using bos.
    
    Options:
      none
    
    

``rln bos.install-tg-bot``
-----------

.. code:: bash

    Usage: rln [--core-opts] bos.install-tg-bot [other tasks here ...]
    
    Docstring:
      Install, configure, enable and start bos telegram bot.
    
    Options:
      none
    
    

``rln bos.tunnel-gateway``
-----------

.. code:: bash

    Usage: rln [--core-opts] bos.tunnel-gateway [other tasks here ...]
    
    Docstring:
      Bos has some basic UI functionality, however it doesn't do much besides
      allowing to send and recieve lightning payments. To try it out, run:
    
      rln -- bos gateway
    
      in a second terminal run:
    
      rln bos.tunnel-gateway
    
      then head to: https://ln-operator.github.io/ and paste the connect code you were
      provided with in the first terminal
    
    Options:
      none
    
    

``rln tor.setup``
-----------

.. code:: bash

    Usage: rln [--core-opts] tor.setup [other tasks here ...]
    
    Docstring:
      Configure tor from start to finish.
    
    Options:
      none
    
    

``rln tor.uninstall``
-----------

.. code:: bash

    Usage: rln [--core-opts] tor.uninstall [other tasks here ...]
    
    Docstring:
      none
    
    Options:
      none
    
    

``rln tor.check``
-----------

.. code:: bash

    Usage: rln [--core-opts] tor.check [other tasks here ...]
    
    Docstring:
      Check whether tor is running
    
    Options:
      none
    
    

``rln prefs.save``
-----------

.. code:: bash

    Usage: rln [--core-opts] prefs.save [--options] [other tasks here ...]
    
    Docstring:
      Save the current connection into ~/.rln/prefs.toml.
      This becomes the default configuration for rln,
      so the host no longer needs to be explicitely
      detailed upon invocation.
    
      e.g
    
      $ rln -H ubuntu@10.10.10.10 -i ~/.rln/lightning/lightning_key.pem prefs.save lightning
      $ rln -H ubuntu@20.20.20.20 -i ~/.rln/testnet/testnet_key.pem prefs.save testnet
    
    Options:
      -n STRING, --name=STRING
    
    

``rln prefs.set-default``
-----------

.. code:: bash

    Usage: rln [--core-opts] prefs.set-default [--options] [other tasks here ...]
    
    Docstring:
      Set the default (preferred) node for future CLI commands.
      The name of the node needs to exist in your prefs file.
    
      e.g:
    
      $ rln prefs.set-default lightning
      $ rln -- uname -a
    
      output:
    
      Linux ip-x-x-x-x 5.8.0-1038-aws #40~20.04.1-Ubuntu SMP Thu Jun 17 13:25:28 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
    
      $ rln prefs.set-default testnet
      $ rln -- uname -a
    
      output:
    
      Linux testnet 5.8.0-55-generic #62-Ubuntu SMP Tue Jun 1 08:21:18 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
    
    Options:
      -n STRING, --name=STRING
    
    

``rln prefs.show-default``
-----------

.. code:: bash

    Usage: rln [--core-opts] prefs.show-default [other tasks here ...]
    
    Docstring:
      Show the default (preferred) node for future CLI commands.
    
    Options:
      none
    
    

``rln prefs.show``
-----------

.. code:: bash

    Usage: rln [--core-opts] prefs.show [other tasks here ...]
    
    Docstring:
      Show prefs file.
    
    Options:
      none
    
    

``rln prefs.remove``
-----------

.. code:: bash

    Usage: rln [--core-opts] prefs.remove [--options] [other tasks here ...]
    
    Docstring:
      Remove node from prefs file, and delete its .pem and secrets
    
    Options:
      -n STRING, --name=STRING
    
    

``rln prefs.reset-prefs-file``
-----------

.. code:: bash

    Usage: rln [--core-opts] prefs.reset-prefs-file [other tasks here ...]
    
    Docstring:
      Delete the prefs file.
    
    Options:
      none
    
    

``rln system.setup``
-----------

.. code:: bash

    Usage: rln [--core-opts] system.setup [--options] [other tasks here ...]
    
    Docstring:
      Basic host setup, i.e updating packages, install vim and nmon (for system monitoring),
      setup PATHS and aliases properly at the top of .bashrc for non-login shells
    
    Options:
      -m, --[no-]mainnet   If False, then an alias for lncli --testnet is created.
      -u, --[no-]upgrade   Whether to upgrade all the packages to their latest
                           version. This can be time-consuming.
    
    

``rln system.fd``
-----------

.. code:: bash

    Usage: rln [--core-opts] system.fd [other tasks here ...]
    
    Docstring:
      Up the maximum number of files open simultaniously to
      half a million (512000). Does not require a system reboot.
    
    Options:
      none
    
    

``rln system.ufw``
-----------

.. code:: bash

    Usage: rln [--core-opts] system.ufw [other tasks here ...]
    
    Docstring:
      Block all ports, apart from OpenSSH, 10009 (standard GRPC) and 9735 (standard P2P).
    
    Options:
      none
    
    

``rln system.flood-protection``
-----------

.. code:: bash

    Usage: rln [--core-opts] system.flood-protection [other tasks here ...]
    
    Docstring:
      Protect the network interface from being flooded with packets.
    
    Options:
      none
    
    

``rln system.shutdown``
-----------

.. code:: bash

    Usage: rln [--core-opts] system.shutdown [other tasks here ...]
    
    Docstring:
      Shut the system down. Make sure you first stop bitcoind, as it needs
      to write its dbcache to disk first.
    
    Options:
      none
    
    

``rln system.reboot``
-----------

.. code:: bash

    Usage: rln [--core-opts] system.reboot [other tasks here ...]
    
    Docstring:
      Reboot the system. Make sure you first stop bitcoind, as it needs
      to write its dbcache to disk first.
    
    Options:
      none
    
    

``rln utils.resources``
-----------

.. code:: bash

    Usage: rln [--core-opts] utils.resources [other tasks here ...]
    
    Docstring:
      List a bunch of very useful external resources, to improve your node's
      ranking.
    
    Options:
      none
    
    

``rln utils.suez``
-----------

.. code:: bash

    Usage: rln [--core-opts] utils.suez [other tasks here ...]
    
    Docstring:
      Run the suez app from src/suez
      to find out more: https://github.com/prusnak/suez
    
    Options:
      none
    
    

``rln utils.get``
-----------

.. code:: bash

    Usage: rln [--core-opts] utils.get [--options] [other tasks here ...]
    
    Docstring:
      Transfer a file from remote to local
    
    Options:
      -f STRING, --from-path=STRING   the source path, on remote host
      -t STRING, --to-path=STRING     the dest path, on local host
    
    

``rln utils.update-fees``
-----------

.. code:: bash

    Usage: rln [--core-opts] utils.update-fees [other tasks here ...]
    
    Docstring:
      Run a fee update with policy on every channel
    
    Options:
      none
    
    

``rln utils.channel-balance``
-----------

.. code:: bash

    Usage: rln [--core-opts] utils.channel-balance [other tasks here ...]
    
    Docstring:
      Report on whether node liquidity is balanced
    
    Options:
      none
    
    

``rln ui.balance``
-----------

.. code:: bash

    Usage: rln [--core-opts] ui.balance [other tasks here ...]
    
    Docstring:
      none
    
    Options:
      none
    
    

``rln ui.forwards``
-----------

.. code:: bash

    Usage: rln [--core-opts] ui.forwards [other tasks here ...]
    
    Docstring:
      none
    
    Options:
      none
    
    

``rln ui.connect``
-----------

.. code:: bash

    Usage: rln [--core-opts] ui.connect [other tasks here ...]
    
    Docstring:
      none
    
    Options:
      none
    
    

``rln ui.open-channel``
-----------

.. code:: bash

    Usage: rln [--core-opts] ui.open-channel [other tasks here ...]
    
    Docstring:
      Open a channel with another node, uses lncli
    
    Options:
      none
    
    

``rln ui.close-channel``
-----------

.. code:: bash

    Usage: rln [--core-opts] ui.close-channel [other tasks here ...]
    
    Docstring:
      Close a channel
    
    Options:
      none
    
    

``rln lit.install``
-----------

.. code:: bash

    Usage: rln [--core-opts] lit.install [other tasks here ...]
    
    Docstring:
      none
    
    Options:
      none
    
    

``rln lit.start``
-----------

.. code:: bash

    Usage: rln [--core-opts] lit.start [other tasks here ...]
    
    Docstring:
      none
    
    Options:
      none
    
    

``rln lit.stop``
-----------

.. code:: bash

    Usage: rln [--core-opts] lit.stop [other tasks here ...]
    
    Docstring:
      none
    
    Options:
      none
    
    

``rln lit.journal``
-----------

.. code:: bash

    Usage: rln [--core-opts] lit.journal [other tasks here ...]
    
    Docstring:
      none
    
    Options:
      none
    
    

