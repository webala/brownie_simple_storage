from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[
        -1
    ]  # get latest deployed contract from SimpleStorage list

    # brownie already knows the contract Address and the ABI
    print(simple_storage.retrieve())


def main():
    read_contract()
