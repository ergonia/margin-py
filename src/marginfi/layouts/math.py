from construct import BitsInteger, BitsSwapped, BitStruct, Const, Flag


FLAGS_LAYOUT = BitStruct(
    "scale" / BitsInteger(16),
    Const(0, BitsInteger(15)),
    "sign" / Flag
)