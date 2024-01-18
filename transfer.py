from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair
import os
# client = Client("https://api.testnet.solana.com")
# public_key = PublicKey("33nY6xCMrHPdhLW4jwkodz1nFN5AbDiXpdzz8v4bUnU3")
# balance = client.get_balance(public_key)

# print(balance)



# sender = Keypair().from_private_key("5YbpBckEGQkiuEvPpSFp2ApC7LuEowVou9rBFETGTNNMnf5FXF1SQkc3H4VrkBQvN9cazfRiH76TtZwWGKFT41MD")
# receiver = PublicKey("2HpsUejxMhJcB2JFEeWtk7KUtEMWrfjvDmzT2Asx7Cdb")
# amount = 20000 # This is the amount in lamports

# instruction = transfer(
#     from_public_key=sender.public_key,
#     to_public_key=receiver, 
#     lamports=amount
# )
# transaction = Transaction(instructions=[instruction], signers=[sender])

# result = client.send_transaction(transaction)

# print(result)

async def do_transfer():
    client = Client(os.environ['SOLANA_CHAIN_URL'])
    public_key = PublicKey(os.environ['WALLET_SWEEP'])
    balance = client.get_balance(public_key)
    print(balance)

    fee=client.get_fees()
    lamport_fee=fee['value']['feeCalculator']['lamportsPerSignature']
    receiver = PublicKey(os.environ['WALLET_DEST'])
    sender = Keypair().from_private_key(os.environ['WALLET_SWEEP_KEY'])
    amount = balance -lamport_fee # This is the amount in lamports
    
    instruction = transfer(
        from_public_key=sender.public_key,
        to_public_key=receiver, 
        lamports=amount
    )
    transaction = Transaction(instructions=[instruction], signers=[sender])

    result = client.send_transaction(transaction)

    print(result)