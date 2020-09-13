import os
from typing import List

from asm_utils import hex_to_bin

def read_obj(obj_file: str) -> List[str]:
    """Reads object file and returns list of instructions

    Parameters
    ----------
    obj_file : str
        path to object file

    Returns
    -------
    List[str]
        list of instructions in the form of binary arrays
    
    Raises
    ------
    FileNotFoundError
        raises FileNotFoundError if object file does not exist at supplied path
    """
    # ensure that file exists
    if not os.path.isfile(obj_file):
        raise FileNotFoundError(f"No object file found at {obj_file}, ensure that your path is correct")

    # load hex instructions into memory
    with open(obj_file, "r") as obj_input:
        hex_instructions = obj_input.readlines()

    # convert hex instructions into binary and return result
    return [
        hex_to_bin(hex_instruction[:-1]) 
        for hex_instruction in hex_instructions
    ]
