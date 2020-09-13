from typing import List
import os
import re

def save_asm(assembly_instructions: List[str], obj_file: str):
    """Saves assembly instructions to s file

    Parameters
    ----------
    assembly_instructions : List[str]
        assembly instructions to save to file
    obj_file : str
        path to obj file to use to name s file

    Raises
    ------
    ValueError
        raises ValueError if path to output file does not exist
    """
    output_file = re.sub("\.obj$", ".s", obj_file)

    if not os.path.exists(os.path.split(output_file)[0]):
        raise ValueError(f"Path to {output_file} does not exist, cannot save assembly instructions")

    with open(output_file, "w") as out_file:
        out_file.writelines(f"{line}\n" for line in assembly_instructions)
