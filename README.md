# ckan2blockchain
`ckan2blockchain` is an app for pushing the CKAN dataset hashes to Ethereum blockchain. The motivation is to increase the perceived trustworthiness of the datasets by allowing to verify their integrity over time.

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

## Usage
TODO

## Contributing
This a free and open-source project. We welcome all kinds of contributions. If you would like to contribute, please send us a pull request.

## License
This project is licensed under the terms of [GNU GENERAL PUBLIC LICENSE, Version 3](LICENSE). Contact us if you suspect a breach of license terms.
