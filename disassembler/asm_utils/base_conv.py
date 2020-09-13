def hex_to_bin(hex_str: str, width: int = 32) -> str:
    """Converts hex string to binary string

    Parameters
    ----------
    hex_str : str
        hexadecimal string to convert

    width : int, optional
        width of binary output (used for zero padding), default=32

    Returns
    -------
    str
        binary array as string

    Raises
    ------
    ValueError
        raises ValueError if supplied width is not wide enough for binary string
    """
    if len(hex_str)*4 > width:
        raise ValueError(
            f"Hex string of length {len(hex_str)} too large for binary array of width {width}"
        )

    format_str = f"{{0:0{width}b}}"

    return format_str.format(int(hex_str, 16))


def bin_to_hex(bin_str: str, width: int = 8) -> str:
    """Converts binary string to hex string

    Parameters
    ----------
    bin_str : str
        binary string to convert

    width : int, optional
        width of hex output (used for zero padding), default=8

    Returns
    -------
    str
        hexadecimal array as string

    Raises
    ------
    ValueError
        raises ValueError if supplied width is not wide enough for hex string
    """
    if len(bin_str)/4.0 > width:
        raise ValueError(
            f"Binary string of length {len(bin_str)} too large for hex array of width {width}"
        )

    format_str = f"{{0:0{width}X}}"

    return format_str.format(int(bin_str, 2))


def bin_to_int(bin_str: str, signed: bool = True) -> str:
    """Converts binary string to int string

    Parameters
    ----------
    bin_str : str
        binary string to convert
    signed : bool, optional
        if the binary string should be interpreted as signed or not, default True

    Returns
    -------
    str
        integer as string

    """
    if signed:
        # if negative two's complemented #
        if bin_str[0] == "1":
            int_str = f"{int(bin_str,2) - 2**(len(bin_str))}"

        # if pos
        else:
            int_str = f"{int(bin_str,2)}"

    else:
        int_str = f"{int(bin_str,2)}"

    return int_str

def int_to_hex(integer: int, width: int = 8) -> str:
    """Converts integer to hex string

    Parameters
    ----------
    integer : int
        integer to convert

    width : int, optional
        width of hex output (used for zero padding), default=8

    Returns
    -------
    str
        hexadecimal array as string

    Raises
    ------
    ValueError
        raises ValueError if supplied width is not wide enough for hex string
    """
    if integer > 16**width - 1:
        raise ValueError(
            f"Integer {integer} too large for hex array of width {width}"
        )

    format_str = f"{{0:0{width}X}}"

    return format_str.format(integer)
