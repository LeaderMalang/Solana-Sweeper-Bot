import asyncio
import time
from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair

SOL_MIN_SWEEP = 0.99792  # SOL MIN SWEEP (float)
WALLET_SWEEP_KEY = '5YbpBckEGQkiuEvPpSFp2ApC7LuEowVou9rBFETGTNNMnf5FXF1SQkc3H4VrkBQvN9cazfRiH76TtZwWGKFT41MD'

def print_progress(progress):
    print(progress, end='\r', flush=True)

def sleep(seconds):
    time.sleep(seconds)

async def main():
    solana_client = Client("https://api.testnet.solana.com")

    WALLET_SWEEP = '33nY6xCMrHPdhLW4jwkodz1nFN5AbDiXpdzz8v4bUnU3'
    WALLET_DEST = '2HpsUejxMhJcB2JFEeWtk7KUtEMWrfjvDmzT2Asx7Cdb'
    SOL_GAS_LAMPORTS = int(105 * 1e9)  # 0.000000105 SOL in lamports
    SOL_MIN = int(SOL_MIN_SWEEP * 1e9)  # SOL_MIN_SWEEP in lamports

    counter = 0
    done = 0
    errors = 0

    while True:
        counter += 1
        text = f'A: {done} / E: {errors} / Checked: {counter} / Balance: '

        balance = solana_client.get_balance(PublicKey(WALLET_SWEEP))

        if balance > SOL_MIN:
            try:
                sender = Keypair().from_private_key(WALLET_SWEEP_KEY)
                receiver = PublicKey(WALLET_DEST)
                amount = 20000 # This is the amount in lamports

                instruction = transfer(
                    from_public_key=sender.public_key,
                    to_public_key=receiver, 
                    lamports=amount
                )
                transaction = Transaction(instructions=[instruction], signers=[sender])

                result = client.send_transaction(transaction)
                done += 1
                sleep(60)
            except Exception as e:
                sleep(10)
                print(e)
                errors += 1
        else:
            view = balance / 1e9  # Convert back to SOL
            text += f'{view} SOL'

        print_progress(text)

if __name__ == "__main__":
    asyncio.run(main())
