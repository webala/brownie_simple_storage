from brownie import accounts, config, SimpleStorage, network
import os


def get_account():
    if network.show_active() == 'development': #natively check the network chain being used
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def deploy_simple_storage():
    account = get_account() #get account generated by brownie(ganache)
    #account = accounts.load('whiterose') #get account added from the command line
    #account = accounts.add(os.getenv('PRIVATE_KEY')) #get account from environment variable
    #account = accounts.add(config['wallets']['from_key']) #loading account from config file
    simple_storage = SimpleStorage.deploy({'from': account})

    stored_value = simple_storage.retrieve() 
    print(stored_value)
    transaction = simple_storage.store(15, {'from': account})
    transaction.wait(1) # wait for one block

    updated_stored_val = simple_storage.retrieve()
    
    print(updated_stored_val)





def main():  # will be called when script is run
    deploy_simple_storage()
 