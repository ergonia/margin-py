from marginfi.schema import MarginfiAccount, MarginfiGroup
from marginfi.solana_rpc import query_solana_account


ACCOUNT_DISCRIMINATOR_SIZE = 8


def load_margin_account(address, solana_rpc="https://api.mainnet-beta.solana.com"):
    margin_account = query_solana_account(address, solana_rpc)
    margin_account = MarginfiAccount.parse(margin_account[ACCOUNT_DISCRIMINATOR_SIZE:])
    return margin_account


def load_margin_group(address, solana_rpc="https://api.mainnet-beta.solana.com"):
    margin_account = load_margin_account(address, solana_rpc)
    margin_group = query_solana_account(margin_account.marginfiGroup, solana_rpc)
    margin_group = MarginfiGroup.parse(margin_group[ACCOUNT_DISCRIMINATOR_SIZE:])
    return margin_group


if __name__ == "__main__":
    print(load_margin_group("HHS3XAt2UDSr2N6QWfEp5muML4VDggLwX5Tr8xqA6pf3"))
