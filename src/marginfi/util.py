from marginfi.layouts.math import FLAGS_LAYOUT
from collections import OrderedDict

class Position(OrderedDict):
    pass

def mdecimal_to_float(mdecimal):
    # this is written from the spec of rust-decimal but im pretty sure its wrong
    byteorder = "big"
    length = 4
    number = b""
    for decimal in [
        mdecimal.hi,
        mdecimal.mid,
        mdecimal.lo
    ]:
        number += decimal.to_bytes(length=length, byteorder=byteorder)
    flags = FLAGS_LAYOUT.parse(mdecimal.flags.to_bytes(length=length, byteorder=byteorder))
    number = int.from_bytes(number, byteorder=byteorder) / 10**flags.scale
    if flags.sign:
        number *= -1
    return number
