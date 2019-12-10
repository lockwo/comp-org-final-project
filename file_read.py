from instruction import Instruction

def file_read(f):
    full = []
    instruct = []
    i = 0
    for line in f:
        full.append(line.strip())
        if ':' not in line:
            instruct.append(Instruction(line.strip()), i)
            i += 1

    return instruct, full
