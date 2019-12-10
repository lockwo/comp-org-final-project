from instruction import Instruction

def file_read(f):
    full = []
    instruct = []
    for line in f:
        full.append(line.strip())
        if ':' not in line:
            instruct.append(Instruction(line.strip()))

    return instruct, full