import os
import json
from pathlib import Path
from anchorpy import AccountsCoder, Idl
from marginfi.solana_rpc import query_solana_account
from marginfi.util import mdecimal_to_float, Position


def load_idl(path=None):
    if not path:
        path = os.path.join(os.environ["CURRENT_DIR"], "idls/marginfi.json")
    with Path(path).open() as f:
        return json.load(f)
    

def load_margin_account(address, path_to_idl=None, solana_rpc="https://api.mainnet-beta.solana.com"):
    margin_account = query_solana_account(address, solana_rpc)
    idl = load_idl(path_to_idl)
    idl = AccountsCoder(Idl.from_json(idl))
    margin_account = idl.parse(margin_account)
    return margin_account.data


def load_margin_group(address, path_to_idl=None, solana_rpc="https://api.mainnet-beta.solana.com"):
    margin_group = query_solana_account(address, solana_rpc)
    idl = load_idl(path_to_idl)
    idl = AccountsCoder(Idl.from_json(idl))
    margin_group = idl.parse(margin_group)
    return margin_group.data


def load_account_summary(address, path_to_idl=None, solana_rpc="https://api.mainnet-beta.solana.com"):
    margin_account = load_margin_account(address, path_to_idl, solana_rpc)
    margin_group = load_margin_account(margin_account.marginfi_group, path_to_idl, solana_rpc)

    # there must be a way to do this type conversation at the time the idl is being parsed but requires a better understanding of anchor-py
    deposit_record = mdecimal_to_float(margin_account.deposit_record)
    borrow_record = mdecimal_to_float(margin_account.borrow_record)
    deposit_accumulator = mdecimal_to_float(margin_group.bank.deposit_accumulator)
    borrow_accumulator = mdecimal_to_float(margin_group.bank.borrow_accumulator)

    position = Position()
    position["amount_deposited"] = deposit_record*deposit_accumulator
    position["amount_borrowed"] = borrow_record*borrow_accumulator
    return position


if __name__ == "__main__":
    print(load_account_summary("HHS3XAt2UDSr2N6QWfEp5muML4VDggLwX5Tr8xqA6pf3"))
