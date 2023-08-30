from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
w3 = Web3(Web3.HTTPProvider(infura_url))

contract_address = "0xYourContractAddress"
contract_abi = [{"constant":True,"inputs":[],"name":"getSomeValue","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"newValue","type":"uint256"}],"name":"setSomeValue","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"}]
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def read_contract():
    result = contract.functions.getSomeValue().call()
    print("Value from contract:", result)

def send_transaction():
    sender_address = "0xYourSenderAddress"
    private_key = "YourPrivateKey"

    nonce = w3.eth.getTransactionCount(sender_address)
    tx = contract.functions.setSomeValue(42).buildTransaction({
        'chainId': 1,
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'nonce': nonce,
    })

    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    print("Transaction Hash:", tx_hash.hex())

if w3.isConnected():
    read_contract()
    send_transaction()
else:
    print("Failed to connect to Ethereum node")
