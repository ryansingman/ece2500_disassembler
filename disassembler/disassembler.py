from typing import List, Tuple

from asm_utils import bin_to_hex, bin_to_int, int_to_hex

from .instruction_type import (
    InstructionType,
    find_instruction_type,
    RInstruction,
    IInstruction,
)
from .op_name_lookup import operation_to_str 
from .register_lookup import register_hex_to_str

def find_opcode(obj_instruction: str) -> str:
    """Finds opcode of object instruction

    Parameters
    ----------
    obj_instruction : str
        object instruction as binary string

    Returns
    -------
    str:
        opcode of instruction (in hex)
    """
    return bin_to_hex(obj_instruction[0:6], width=2)


def find_hex_address(address: int) -> str:
    """Finds hex address of instruction from int address

    Parameters
    ----------
    address : int
        integer address of object instruction

    Returns
    -------
    str:
        address of instruction (in hex)
    """
    return f"Addr_{int_to_hex(address*4, width=4)}"


def disassemble_R_instruction(obj_instruction: str) -> str:
    """Disassembles R instruction into str

    Parameters
    ----------
    obj_instruction : str
        object instruction as binary string

    Returns
    -------
    str
        str of disassembled MIPS instruction
    """
    # extract fields from object
    instruction = RInstruction(
        opcode = find_opcode(obj_instruction),
        rs = bin_to_hex(obj_instruction[6:11], width=2),
        rt = bin_to_hex(obj_instruction[11:16], width=2),
        rd = bin_to_hex(obj_instruction[16:21], width=2),
        shamt = bin_to_int(obj_instruction[21:26]),
        funct = bin_to_hex(obj_instruction[26:], width=2),
    )

    # determine output format and build instruction
    op_str = operation_to_str(instruction.opcode, funct=instruction.funct)
    if op_str in ["sll", "srl"]:
        output_str = (
            f"\t{op_str} "
            f"{register_hex_to_str(instruction.rd)}, "
            f"{register_hex_to_str(instruction.rt)}, "
            f"{instruction.shamt}"
        )
    else:
        output_str = (
            f"\t{op_str} "
            f"{register_hex_to_str(instruction.rd)}, "
            f"{register_hex_to_str(instruction.rs)}, "
            f"{register_hex_to_str(instruction.rt)}"
        )

    return output_str

def disassemble_I_instruction(obj_instruction: str, address: int) -> Tuple[str, int]:
    """Disassembles I instruction into str

    Parameters
    ----------
    obj_instruction : str
        object instruction as binary string
    address : int
        address of current instruction

    Returns
    -------
    Tuple(str, int)
        tuple of disassembled MIPS instruction and branch target
    """
    # extract fields from object
    instruction = IInstruction(
        opcode = find_opcode(obj_instruction),
        rs = bin_to_hex(obj_instruction[6:11], width=2),
        rt = bin_to_hex(obj_instruction[11:16], width=2),
        imm = bin_to_int(obj_instruction[16:]),
    )

    # init branch target to None
    branch_abs_address = None

    # determine what format instruction is in (load/store vs other)
    load_store_ops = ["lbu", "lhu", "ll", "lui", "lw", "sb", "sc", "sh", "sw"]
    op_str = operation_to_str(instruction.opcode)
    if op_str in load_store_ops:
        if op_str != "lui":
            output_str = (
                f"\t{operation_to_str(instruction.opcode)} "
                f"{register_hex_to_str(instruction.rt)}, "
                f"{instruction.imm}({register_hex_to_str(instruction.rs)})"
            )
        else:
            output_str = (
                f"\t{operation_to_str(instruction.opcode)} "
                f"{register_hex_to_str(instruction.rt)}, "
                f"{instruction.imm}"
            )
    else:
        if op_str in ["beq", "bne"]:
            # find absolute address of branch address
            branch_abs_address = (address+1) + int(instruction.imm)
            output_str = (
                f"\t{op_str} "
                f"{register_hex_to_str(instruction.rs)}, "
                f"{register_hex_to_str(instruction.rt)}, "
                f"{find_hex_address(branch_abs_address)}"
            )

        else:
            output_str = (
                f"\t{op_str} "
                f"{register_hex_to_str(instruction.rt)}, "
                f"{register_hex_to_str(instruction.rs)}, "
                f"{instruction.imm}"
            )

    # build and return instruction, branch point if exists
    return (output_str, branch_abs_address)


def disassemble(obj_instructions : List[str]) -> List[str]:
    """Disassembles binary object instructions into MIPS instructions

    Parameters
    ----------
    obj_instructions : List[str]
        list of binary object instructions

    Returns
    -------
    List[str]
        list of disassembled instructions
    """
    assembly_instructions = [None] * len(obj_instructions)
    branch_points = []
    # iterate over instructions and generate text instructions
    for ii, obj_instruction in enumerate(obj_instructions):
        # find instruction type (R or I) and disassemble for that type
        if find_instruction_type(find_opcode(obj_instruction)) == InstructionType.R:
            try:
                assembly_instructions[ii] = disassemble_R_instruction(
                    obj_instruction
                )
            except Exception as e:
                raise type(e)(
                    f"Cannot disassemble {bin_to_hex(obj_instruction, width=8)}"
                    f" at line number {ii+1}"
                ) from e

        elif find_instruction_type(find_opcode(obj_instruction)) == InstructionType.I:
            try:
                assembly_instructions[ii], branch_point = disassemble_I_instruction(
                    obj_instruction, ii
                )
            except Exception as e:
                raise type(e)(
                    f"Cannot disassemble {bin_to_hex(obj_instruction, width=8)}"
                    f" at line number {ii+1}"
                ) from e

            if branch_point is not None and branch_point not in branch_points:
                branch_points.append(branch_point)

    # final pass to add in addresses where needed
    for branch_point in sorted(branch_points, reverse=True):
        assembly_instructions.insert(branch_point, f"{find_hex_address(branch_point)}:")

    return assembly_instructions
