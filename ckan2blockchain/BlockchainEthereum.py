import argparse
from web3 import Web3, EthereumTesterProvider, HTTPProvider
from eth_account import Account

import sys

class BlockchainEthereum:
    def __init__(self, cli_args, ini_args):
        if cli_args['ethereum']['provider'] == 'test':
            self.w3 = Web3(EthereumTesterProvider())
        elif cli_args['ethereum']['provider'] == 'local':
            self.w3 = Web3(Web3.IPCProvider())
        elif cli_args['ethereum']['provider'] == 'network':
            self.w3 = Web3(HTTPProvider('https://rinkeby.infura.io'))
        else:
            self.w3 = Web3(HTTPProvider(cli_args['ethereum']['provider']))

    # class methods

    def add_cli_commands(subparsers):
        # eth-create-address
        sub_create_address = subparsers.add_parser('eth-create-address')

# vim: ai ts=4 sts=4 et sw=4 ft=python
