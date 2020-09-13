register_codes = {
    "00": "$zero",
    "01": "$at",
    "02": "$v0",
    "03": "$v1",
    "04": "$a0",
    "05": "$a1",
    "06": "$a2",
    "07": "$a3",
    "08": "$t0",
    "09": "$t1",
    "0A": "$t2",
    "0B": "$t3",
    "0C": "$t4",
    "0D": "$t5",
    "0E": "$t6",
    "0F": "$t7",
    "10": "$s0",
    "11": "$s1",
    "12": "$s2",
    "13": "$s3",
    "14": "$s4",
    "15": "$s5",
    "16": "$s6",
    "17": "$s7",
    "18": "$t8",
    "19": "$t9",
    "1A": "$k0",
    "1B": "$k1",
    "1C": "$gp",
    "1D": "$sp",
    "1E": "$fp",
    "1F": "$ra"
}

def register_hex_to_str(hex_reg: str) -> str:
    """Converts hex code for register to register name

    Parameters
    ----------
    hex_reg : str
        register code as hex

    Returns
    -------
    str
        register name as string 

    Raises
    ------
    ValueError
        Raises ValueError if hex code not in range
    """
    if not hex_reg in register_codes:
        raise ValueError("Hex register code {hex_reg} not defined")

    return register_codes[hex_reg]
