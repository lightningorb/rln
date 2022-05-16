#!/bin/bash

alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'
alias b='bos balance'
alias pk="lncli getinfo | jq '.identity_pubkey'"
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias get='bos chain-deposit'
alias grep='grep --color=auto'
alias lct='lncli listchaintxns | jq '\''.transactions[0]'\'''
alias nct='lncli listchaintxns | jq '\''.transactions | length'\'''
alias lct="lncli listchaintxns | jq '.transactions[0]'"
alias nct="lncli listchaintxns | jq '.transactions | length'"
alias get="bos chain-deposit"
alias b="bos balance"
alias lnactive='lncli listchannels | jq '\''[ .channels | .[] | select(.active==true) ] | length '\'''
alias send='bos send'
alias towers='lncli wtclient towers'