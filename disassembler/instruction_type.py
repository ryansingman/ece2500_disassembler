from enum import Enum
from typing import NewType
from collections import namedtuple


class InstructionType(Enum):
    """Instruction type enumeration"""
    R = 0
    I = 1


# R and I instruction structures
RInstruction = namedtuple("RInstruction", ["opcode", "rs", "rt", "rd", "shamt", "funct"])
IInstruction = namedtuple("IInstruction", ["opcode", "rs", "rt", "imm"])


def find_instruction_type(opcode: str) -> InstructionType:
    """Finds instruction type for object instruction

    Parameters
    ----------
    opcode : str
        opcode of instruction in hex

    Returns
    -------
    InstructionType
        type of instruction using InstructionType enum
    """
    # R type instructions always have opcode = 00
    if opcode == "00":
        i_type = InstructionType.R

    # I type instructions have opcode > 03
    elif opcode > "03":
        i_type = InstructionType.I

    return i_type
