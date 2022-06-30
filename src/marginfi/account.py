import os
import json
from pathlib import Path
from anchorpy import AccountsCoder, Idl
from marginfi.solana_rpc import query_solana_account


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
    return margin_account


def load_margin_group(address, path_to_idl=None, solana_rpc="https://api.mainnet-beta.solana.com"):
    margin_group = query_solana_account(address, solana_rpc)
    idl = load_idl(path_to_idl)
    idl = AccountsCoder(Idl.from_json(idl))
    margin_group = idl.parse(margin_group)
    return margin_group


if __name__ == "__main__":
    print(load_margin_account("HHS3XAt2UDSr2N6QWfEp5muML4VDggLwX5Tr8xqA6pf3"))
