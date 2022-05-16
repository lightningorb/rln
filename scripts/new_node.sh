#!/bin/bash

./rln aws.create-keypair --name=lightning
./rln create-aws-node --instance-type=t3.medium --availability-zone=us-east-1a --name=lightning --disk-size=800 --mainnet --keypair-name lightning
