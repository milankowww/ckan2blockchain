#! /usr/bin/env python3

import configparser
import argparse
import sys
import logging, logging.handlers

from BlockchainEthereum import BlockchainEthereum

class Ckan2Blockchain:

    def __init__(self):
        self.logger = logging.getLogger('Ckan2Blockchain')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.handlers.SysLogHandler())
        self.logger.info('started')

    def add_cli_commmands(self,subparsers):
        # dataset-store
        sub_dataset_store = subparsers.add_parser('dataset-store', help='retrieve hash of selected dataset from CKAN and store it to the block chain')
        sub_dataset_store.add_argument('-d', '--dataset', action='append', help='dataset identificator')

        # dataset-verify
        sub_dataset_verify = subparsers.add_parser('dataset-verify', help='retrieve hash of the dataset from the block chain and verify against CKAN')
        sub_dataset_verify.add_argument('-d', '--dataset', action='append', help='dataset identificator')

        # dataset-store-all
        sub_dataset_store_all = subparsers.add_parser('dataset-store-all', help='store all hashes from CKAN to the blockchain')

        # dataset-verify-all
        sub_dataset_verify_all = subparsers.add_parser('dataset-verify-all', help='verify hashes presently on the blockchain against CKAN')

    def handle_command(self, command):
        if command=='dataset-store':
            # data = ...TODO...
            # self.chain.add_to_blockchain(data)
            self.chain.add_to_blockchain('a00aa00a')
            pass

    def main(self):

        # command line argument parser
        parser = argparse.ArgumentParser()
        # 1. add options and flags
        parser.add_argument('-f', '--force', action='store_true', help='force the action (use with care)')
        parser.add_argument('-c', '--config-file', action='store', default='/etc/ckan2blockchain.ini', help='path to the configuration file')
        parser.add_argument('-p', '--password', action='store', help='specify password to decrypt keychain on command line. THIS IS UNSAFE in a multi-user environment. Other users may see your password plainly. Enter the password through console instead.')
        # 2. add ckan and blockchain related commands
        command_subparsers = parser.add_subparsers(dest='command')
        command_subparsers.required = True
        self.add_cli_commmands(command_subparsers)
        BlockchainEthereum.add_cli_commands(command_subparsers)
        # 3. finally, parse the command line arguments
        self.cli_args = parser.parse_args()

        # ini file settings
        ini_defaults = {
            'general': {
                'blockchain': 'ethereum'
            }
        }
        self.ini_args = configparser.ConfigParser(defaults=ini_defaults)

        try:
            found = self.ini_args.read(self.cli_args.config_file)
            if len(found) == 0:
                raise(ValueError('Cannot open the file '+self.cli_args.config_file))

            tmp = self.ini_args.get('general','blockchain')
            if tmp == 'ethereum':
                self.chain = BlockchainEthereum(self.cli_args, self.ini_args, self.logger)
            else:
                raise(ValueError('Unsupported type of blockchain: '+tmp))

        except (ValueError,configparser.Error) as e:
            sys.exit("Configuration file error: "+str(e))

        self.handle_command(self.cli_args.command)
        self.chain.handle_command(self.cli_args.command)

#        if args.blockchain == '--ethereum':
#            self.chain = BlockchainEthereum(self.cli_args)
#
#        if cli_args.create_account:
#            self.create_account(cli_args.force)

if __name__ == '__main__':
    app = Ckan2Blockchain()
    app.main()

# vim: ai ts=4 sts=4 et sw=4 ft=python
