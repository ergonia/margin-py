from borsh_construct import CStruct, Bool, U8, U32, U128, I64
from anchorpy.borsh_extension import BorshPubkey


MDecimal = CStruct(
    "flags" / U32,
    "hi" / U32,
    "lo" / U32,
    "mid" / U32
)

UTPAccountConfig = CStruct(
    "address" / BorshPubkey,
    "authoritySeed" / BorshPubkey,
    "authorityBump" / U8,
    "utpAddressBook" / BorshPubkey[4],
    "reservedSpace" / U32[32]
)

Bank = CStruct(
    "scalingFactorC" / MDecimal,
    "fixedFee" / MDecimal,
    "interestFee" / MDecimal,
    "depositAccumulator" / MDecimal,
    "borrowAccumulator" / MDecimal,
    "lastUpdate" / I64,
    "nativeDepositBalance" / MDecimal,
    "nativeBorrowBalance" / MDecimal,
    "mint" / BorshPubkey,
    "vault" / BorshPubkey,
    "vaultAuthorityPdaBump" / U8,
    "insuranceVault" / BorshPubkey,
    "insuranceVaultAuthorityPdaBump" / U8,
    "insuranceVaultOutstandingTransfers" / MDecimal,
    "feeVault" / BorshPubkey,
    "feeVaultAuthorityPdaBump" / U8,
    "feeVaultOutstandingTransfers" / MDecimal,
    "initMarginRatio" / MDecimal,
    "maintMarginRatio" / MDecimal,
    "accountDepositLimit" / MDecimal,
    "lpDepositLimit" / MDecimal,
    "reservedSpace" / U128[31]
)

MarginfiAccount = CStruct(
    "authority" / BorshPubkey,
    "marginfiGroup" / BorshPubkey,
    "depositRecord" / MDecimal,
    "borrowRecord" / MDecimal,
    "activeUtps" / U8[32],
    "utpAccountConfig" / UTPAccountConfig[32],
    "reservedSpace" / U128[256]
)

MarginfiGroup = CStruct(
    "admin" / BorshPubkey,
    "bank" / Bank,
    "paused" / Bool,
    "reservedSpace" / U128[384]
)

State = CStruct(
    "totalCollateral" / U128,
    "freeCollateral" / U128,
    "marginRequirementInit" / U128,
    "marginRequirementMaint" / U128,
    "equity" / U128
)