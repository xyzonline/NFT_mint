from web3 import Web3
import config



def get_network(network, INFURA_SECRET_KEY):
    infura_url = f'https://{network}.infura.io/v3/{INFURA_SECRET_KEY}'
    w3 = Web3(Web3.HTTPProvider(infura_url))
    print(f'The {network} network is connected',w3.isConnected())
    return w3

def mint_nft(wallet_address, private_key, contract_address, contract_abi, number_of_tokens, network, 
             INFURA_SECRET_KEY, gas_price = 5, gas_limit = 1000):
    w3 = get_network(network, INFURA_SECRET_KEY)
    
    eth = f'https://{network}.infura.io/v3/{INFURA_SECRET_KEY}'
    buy_address = w3.toChecksumAddress(wallet_address)
    nft_address = w3.toChecksumAddress(contract_address)
    
    nft_mint = w3.eth.contract(nft_address, abi = contract_abi)
    name = nft_mint.functions.name().call()
    
    price = nft_mint.functions.MBAIPrice().call()
    print(price)    
    
    nonce = w3.eth.get_transaction_count(buy_address)
    
    mint = nft_mint.functions.giveAway(buy_address, number_of_tokens).buildTransaction({
        'from': buy_address,
        'gasPrice': w3.toWei(10, 'gwei'),
        'nonce': nonce,
        'value': price * number_of_tokens
    })
    
    signed_tx = w3.eth.account.sign_transaction(mint, private_key)
    tx_token = w3.eth.send_transaction(signed_tx.rawTransaction)
    print('NFT bought' + w3.toHex(tx_token))

def main():
    WALLET_ADDRESS = config.WALLET_ADDRESS
    PRIVATE_KEY = config.PRIVATE_KEY
    CONTRACT_ADDRESS = config.NFT_CONTRACT_ADDRESS
    CONTRACT_ABI = config.nft_abi
    number_of_tokens = 3
    network = 'mainnet'
    INFURA_SECRET_KEY = config.INFURA_SECRET_KEY
    
    mint_nft(WALLET_ADDRESS, PRIVATE_KEY, CONTRACT_ADDRESS, CONTRACT_ABI, number_of_tokens, 
             network, INFURA_SECRET_KEY)

if __name__ == '__main__':
    main()
    