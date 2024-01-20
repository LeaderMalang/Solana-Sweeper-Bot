from solana.rpc.api import Client
from spl.token.client import Token
from solders.pubkey import Pubkey
from solders.keypair import Keypair
import os
async def do_token_transfer(balance):

  mint = Pubkey.from_string(os.environ['TOKEN_ADDRESS']) #eg: https://solscan.io/token/FpekncBMe3Vsi1LMkh6zbNq8pdM6xEbNiFsJBRcPbMDQ**
  program_id = Pubkey.from_string(os.environ['TOKEN_PROGRAM_ID']) #eg: https://solscan.io/account/**TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA**

  privkey=os.environ['WALLET_SWEEP_KEY']
  key_pair = Keypair.from_base58_string(privkey)

  solana_client = Client(os.environ['SOLANA_CHAIN_URL'])
  spl_client = Token(conn=solana_client, pubkey=mint, program_id=program_id, payer=key_pair)

  source = Pubkey.from_string(os.environ['WALLET_SWEEP'])
  dest = Pubkey.from_string(os.environ['WALLET_DEST'])

  try:
      source_token_account = spl_client.get_accounts_by_owner(owner=source, commitment=None, encoding='base64').value[0].pubkey
  except:
      source_token_account = spl_client.create_associated_token_account(owner=source, skip_confirmation=False, recent_blockhash=None)
  try:
      dest_token_account = spl_client.get_accounts_by_owner(owner=dest, commitment=None, encoding='base64').value[0].pubkey
  except:
      dest_token_account = spl_client.create_associated_token_account(owner=dest, skip_confirmation=False, recent_blockhash=None)

  #amount = <actual_amount_in_float>

  transaction = spl_client.transfer(source=source_token_account, dest=dest_token_account, owner=key_pair, amount=int(balance), multi_signers=None, opts=None, recent_blockhash=None)
  print(transaction)