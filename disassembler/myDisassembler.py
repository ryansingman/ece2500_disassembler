from disassembler import disassemble
from asm_io import read_obj, save_asm 

def main(obj_file: str):
    """Main function of myDisassembler

    Parameters
    ----------
    obj_file : str
        path to object file to disassemble
    """
    # load object file
    obj_instructions = read_obj(obj_file)

    # disassemble object file
    disassembled_instructions = disassemble(obj_instructions)

    # save disassembled instructions to file
    save_asm(disassembled_instructions, obj_file)
     

if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(description="Disassemble an object file")

    parser.add_argument("obj_file", help="path to object file to disassemble")

    args = parser.parse_args()

    main(args.obj_file)
