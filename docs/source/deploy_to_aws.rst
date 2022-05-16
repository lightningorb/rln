Deploy to AWS
=============

If you don’t have any hardware readily available to run lightning, a
quick way of getting up & running is on AWS. Note you’ll be looking at a
roughly ``$80`` monthly bill (this can be recouped on routing fees).

-  `create an account on AWS <https://aws.amazon.com/account/sign-up>`__

-  `retrieve your access
   keys <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey>`__

-  Save your access keys and nearest region:

.. code:: bash

   ./rln aws.save-credentials \
      --key-id=JD7LEI6EKA4BQLS3UFHA \
      --access-key=dp20o8asdgp98723498yhuihs098u0s9uef08oh2 \
      --region=us-east-1
                
Create your AWS key-pair certificate
------------------------------------

You’ll want to be the only person able to ``ssh`` into your node.

For this to happen, let’s create a key-pair. This process tells AWS to
generate an X. 509 certificate, CSR, and cryptographic key:

.. code:: bash

   ./rln aws.create-keypair --name=lightning

Note the pem file gets created in ``~/.rln/lightning/lightning_key.pem``,
without this key, you cannot ssh into your server, so keep it safe.

Create your AWS Security Group (firewall)
-----------------------------------------

Create the security group:

.. code:: bash

   ./rln aws.create-security-group

This is your node’s firewall, with only the required ports open.

Wonderful, you are now ready!

Create your lightning node
--------------------------

This command creates & configures your AWS node, from start to finish.

.. code:: bash

   ./rln create-aws-node \
      --instance-type=t3.medium \
      --availability-zone=us-east-1a \
      --name=lightning \
      --disk-size=800 \
      --mainnet

When you’re prompted for a password, this is to create an encrypted zipfile
that contains your seed, and the entropy used to generate it. The wallet seed is saved in ``~/.rln/lightning/lightning_secrets.zip``. Keep it safe. If you ever need to re-create your wallet or your node, it will get used to restore your wallet.

Syncing the blockchain will take several days. To view sync progress, simply scan the logs for the ``progress`` entry:

.. code:: bash

   ./rln btc.logs

