#! /usr/bin/env python3

import argparse

class Ckan2Blockchain:
    def set_blockchain(self, blockchain, testnet=False):
        pass

    def create_account(self, force=False):
        pass

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--create-account', action='store_true', help='create a new crypto account from which the transactions will be commited')
        parser.add_argument('-f', '--force', action='store_true', help='force the action (use with care)')
        args = parser.parse_args()

        if args.create_account:
            self.create_account(args.force)

if __name__ == '__main__':
    app = Ckan2Blockchain()
    app.main()

# vim: ai ts=4 sts=4 et sw=4 ft=python
