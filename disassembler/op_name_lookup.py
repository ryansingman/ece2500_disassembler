from .instruction_type import find_instruction_type, InstructionType

# dict that maps function codes to operation names (R-type)
r_op_names = {
    "20" : "add",
    "21" : "addu",
    "24" : "and",
    "27" : "nor",
    "25" : "or",
    "2A" : "slt",
    "2B" : "sltu",
    "00" : "sll",
    "02" : "srl",
    "22" : "sub",
    "23" : "subu",
}

# dict that maps op codes to operation names (I-type)
i_op_names = {
    "08" : "addi",
    "09" : "addiu",
    "0C" : "andi",
    "04" : "beq",
    "05" : "bne",
    "24" : "lbu",
    "25" : "lhu",
    "30" : "ll",
    "0F" : "lui",
    "23" : "lw",
    "0D" : "ori",
    "0A" : "slti",
    "0B" : "sltiu",
    "28" : "sb",
    "38" : "sc",
    "29" : "sh",
    "2B" : "sw",
}

def operation_to_str(opcode: str, funct: str = None) -> str:
    """Converts hex code for opcode (and funct for R-type) to operation name

    Parameters
    ----------
    opcode: str
        operation code in hex
    funct : str, optional
        function code in hex, default is None

    Returns
    -------
    str
        operation name as string 

    Raises
    ------
    ValueError
        Raises ValueError if opcode not in range
    """
    instruction_type = find_instruction_type(opcode)

    if instruction_type == InstructionType.R:
        if funct is None:
            raise ValueError("funct must be defined for R-type instructions")

        elif funct not in r_op_names:
            raise ValueError(f"function code {funct} is not in range for R-type instruction")

        op_name = r_op_names[funct]

    else:
        if opcode not in i_op_names:
            raise ValueError(f"opcode {opcode} is not in range for I-type instruction")

        op_name = i_op_names[opcode]

    return op_name
