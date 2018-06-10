import argparse
import getpass
import hashlib, time
import json

import sys

from web3 import Web3, EthereumTesterProvider, HTTPProvider
from eth_account import Account
from eth_tester import EthereumTester
import ethereum.exceptions

class BlockchainEthereum:

    # methods called from main.py

    def __init__(self, cli_args, ini_args, logger):
        self.cli_args = cli_args
        self.ini_args = ini_args
        self.logger = logger

        provider = self.ini_args.get('ethereum','provider')
        if provider == 'test':
            self.w3 = Web3(EthereumTesterProvider())
        elif provider == 'local':
            self.w3 = Web3(Web3.IPCProvider())
        elif provider == 'network':
            self.w3 = Web3(HTTPProvider('https://rinkeby.infura.io'))
        else:
            self.w3 = Web3(HTTPProvider(provider))

    def handle_command(self, command):
        if command=='eth-create-address':
            tmp = getpass.getpass('Please enter a few random words: ')
            tmp = hashlib.sha256((tmp + str(time.time())).encode('utf-8')).hexdigest()
            account = Account.create(tmp)
            # account.address
            # account.privateKey
            self.__ask_decrypt_password()
            encrypted = Account.encrypt(account.privateKey, self.decrypt_password)

            try:
                with open(self.ini_args.get('ethereum', 'private_key_file'), 'x') as keyfile:
                    keyfile.write(json.dumps(encrypted))
            except OSError as e:
                sys.exit('Error storing private key: ' + str(e))

            self.__load_private_key()

    def add_to_blockchain(self, dataset_hashes):
        # FIXME: segmentation ; convert to binary
        self.logger.info('Sending transaction to blockchain')
        self.__send_data(dataset_hashes)
        
    # private methods
    def __ask_decrypt_password(self):
        if hasattr(self, 'decrypt_password'):
            return

        if 'password' in self.cli_args and self.cli_args.password != None:
            self.decrypt_password = self.cli_args.password
            sys.stderr.write('Using password from command line. THIS IS UNSAFE. ANYONE ON THE SAME MACHINE COULD SEE YOUR PASSWORD.\n')
        else:
            self.decrypt_password = getpass.getpass('Please enter password to decrypt the private key: ')

    def __load_private_key(self):
        if hasattr(self, 'private_key'):
            return

        self.__ask_decrypt_password()

        try:
            with open(self.ini_args.get('ethereum', 'private_key_file')) as keyfile:
                keyfile_json = keyfile.read()

            self.private_key = Account.decrypt(keyfile_json, self.decrypt_password)
        except (ValueError, OSError) as e:
            sys.exit('Error loading private key: ' + str(e))

        if self.ini_args.get('ethereum','provider') == 'test':
            # make sure the sending account is well funded 
            account = Account.privateKeyToAccount(self.private_key)

            if self.w3.eth.getBalance(account.address) == 0:
                self.w3.eth.sendTransaction({
                    'from': self.w3.eth.coinbase,
                    'to': account.address,
                    # 'gas': 21000,
                    'value': 10000000,
                    'nonce': self.w3.eth.getTransactionCount(self.w3.eth.coinbase),
                })

    def __send_data(self, data):

        self.__load_private_key()
        account = Account.privateKeyToAccount(self.private_key)

        signed_transaction = self.w3.eth.account.signTransaction({
            'nonce': self.w3.eth.getTransactionCount(account.address), # FIXME: add pending transactions
            'gasPrice': self.w3.eth.gasPrice,
            'gas': 900000, # should be auto-calculated

            'to': self.ini_args.get('ethereum', 'target_address'), 

            'value': 0,
            'data': data
        }, self.private_key)

        # FIXME: gasPrice? nonce?
        # FIXME: error checking?

        try:
            self.w3.eth.sendRawTransaction(signed_transaction.rawTransaction)
        except ethereum.exceptions.InsufficientBalance as e:
            self.logger.error('Error sending transaction to blockchain: ' + str(e))
            return False

        return True

    # class methods

    def add_cli_commands(subparsers):
        # eth-create-address
        sub_create_address = subparsers.add_parser('eth-create-address', help='Create a new Ethereum address for sending')


# vim: ai ts=4 sts=4 et sw=4 ft=python
