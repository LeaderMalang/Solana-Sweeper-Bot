import asyncio
import time

import os

from solathon.core.instructions import transfer
from solathon import AsyncClient, Transaction, PublicKey, Keypair,Client
from transfer import do_transfer

SOL_MIN_SWEEP = os.environ['SOL_MIN_SWEEP'] # SOL MIN SWEEP (float)
WALLET_SWEEP_KEY = os.environ['WALLET_SWEEP_KEY']

def print_progress(progress):
    print(progress, end='\r', flush=True)

def sleep(seconds):
    time.sleep(seconds)


async def main():
    
    solana_client = AsyncClient(os.environ['SOLANA_CHAIN_URL'])
    WALLET_SWEEP = os.environ['WALLET_SWEEP']
    WALLET_DEST = os.environ['WALLET_DEST']
    SOL_GAS_LAMPORTS = int(105 * 1e9)  # 0.000000105 SOL in lamports
    SOL_MIN = int(float(SOL_MIN_SWEEP) * 1e9)  # SOL_MIN_SWEEP in lamports

    counter = 0
    done = 0
    errors = 0

    while True:
        await solana_client.refresh_http()
        counter += 1
        text = f'A: {done} / E: {errors} / Checked: {counter} / Balance: '
        try:
            balance = await solana_client.get_balance(PublicKey(WALLET_SWEEP))
        except Exception as e:
            await solana_client.refresh_http()
            balance = await solana_client.get_balance(PublicKey(WALLET_SWEEP))


        if balance['result']['value'] > SOL_MIN:
            try:
                await do_transfer()
                sleep(60)
            except Exception as e:
                sleep(10)
                print(e)
                errors += 1
        else:
            view = balance['result']['value'] / 1e9  # Convert back to SOL
            text += f'{view} SOL'

        print_progress(text)

if __name__ == "__main__":
    asyncio.run(main())
