## 🧹 Solana Sweeper Bot
**How Script Works?**
THis script listen incoming transactions by solana address. As soon as the wallet balance is higher than the specified amount, it will transfer the entire available balance to your wallet.
>  **Attention**
> Of course, you must have a private key to the wallet you are going to listen to

## 💠 Variables

- `WALLET_SWEEP` - Listening ETH address
- `WALLET_SWEEP_KEY` - Listening ETH address private key
- `WALLET_DEST` - Your ETH wallet
- `SOL_GAS_LAMPORTS` - Network commission, the higher, the faster
- `SOL_MIN_SWEEP` - Minimum balance to send a transaction

>  **What is the purpose of this tool?**

>  Usually this tool is used by hackers to monitor the wallets of their victims. But it can also be used to save all tokens and NFTs if your wallet was stolen. Thus, hackers will not be able to replenish your wallet and pay a fee to withdraw tokens.

>  **Settings Up/Installation**

>  Please install python 3.10 or 3.9 version from Official website.After installing run following commands

> Create a virtual environment

`python -m venv env`

> Activate the virtual environment

`source /env/bin/activate`
> Install required packages

`pip install -r requirements.txt`

> Run Main.py 
`python main.py`
