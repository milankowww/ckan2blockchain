# ckan2blockchain
`ckan2blockchain` is an app for pushing the CKAN dataset hashes to Ethereum blockchain. The motivation is to increase the perceived trustworthiness of datasets by maintaining their integrity over time in the blockchain.

## Installation
Installation is very simple. You could either install the project files using Ansible or manaully by following the provided instructions.

### Install from pip
Installation from pip will be available soon.

### Manual installation
Install all the OS level and Python level prerequisites. On Debian or Ubuntu based systems, this means running the following commands:
```sh
apt-get install install python3 python3-pip
pip3 install click web3 eth-testrpc
```

### Install through Ansible
When installing the server, add the role from [ansible_roles/ckan2blockchain](ansible_roles/ckan2blockchain) to the list of roles. It will install the prerequisites automatically.

## Configuration

Create or edit the configuration file `/etc/ckan2blockchain.ini` and configure the required fields. Example ini file may look like this:

	[general]
	blockchain = ethereum

	[ckan]
	url = https://www.data.gov.sk/

	[ethereum]
	# provider - how to connect to Ethereum network. Valid values:
	#  test - use fake connection for testing
	#  local - use a locally running geth node. Safer, but more resource heavy.
	#  network - use a network node to connect to Ethereum (infura.io)
	#  https://x.x.x.x/ - use a network node running on given address
	provider = network

	# how to obtain the private key. This may be a path to local geth keystore
	private_key_file = /home/myuser/.ethereum/keystore/KEYFILENAME

## Usage

Enter `ckan2blockchain --help` to see the general help. Use `ckan2blockchain <COMMAND> --help` to see the help for particular command.

<!--
### Examples

TODO
-->

## Contributing
This a free and open-source project. We welcome all kinds of contributions. If you would like to contribute, please send us a pull request.

## License
This project is licensed under the terms of [GNU GENERAL PUBLIC LICENSE, Version 3](LICENSE). Contact us if you suspect a breach of license terms.
