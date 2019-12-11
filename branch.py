from instruction import Instruction

'''
instructions = LIST OF INSTRUCTIONS
all_instructions = LIST OF ALL INPUT, INSTRUCTIONS AND LOOP HEADERS
'''
def branch(instructions, all_instructions, cycle_count, tregs, sregs):
    for i in range(len(instructions)):
        #print(instructions[i].oper, (instructions[i].oper == 'beq' and instructions[i].be == False) or (instructions[i].oper == 'bne' and instructions[i].be == False))
        if (instructions[i].oper == 'beq' and instructions[i].be == False) or (instructions[i].oper == 'bne' and instructions[i].be == False):
            # The branch value isn't evaluated until MEM stage (4th stage in datapath)
            if instructions[i].counter < 4:
                continue
            elif instructions[i].counter == 4:
                r2, r3 = instructions[i].r2, instructions[i].r3
                # checking whether it's $zero, t, or s register
                if r2[1] == 'z':
                    r2 = 0
                elif r2[1] == 't':
                    r2 = tregs[int(r2[2])]
                elif r2[1] == 's':
                    r2 = sregs[int(r2[2])]
                if r3[1] == 'z':
                    r3 = 0
                elif r3[1] == 't':
                    r3 = tregs[int(r3[2])]
                elif r3[1] == 's':
                    r3 = sregs[int(r3[2])]
####################################################################################################
##DO DIFFERENT THINGS FOR BNE AND BEQ
####################################################################################################
                if (instructions[i].oper == 'beq' and r2 == r3) or (instructions[i].oper == 'bne' and r2 != r3):
                    # loop through instructions after the branch instruction and for all
                    # instructions that have started running, set taken to True to stop
                    count = 0

                    #DEBUGGING CODE
                    # for j in range(i+1, i+4):
                    #     instructions[j].counter += 1
                    # Count the number of instructions that have started pipelining after the branch instruction
                    for j in range(i + 1, len(instructions)):
                        if (instructions[j].counter > 0):
                            instructions[j].taken = True
                            count += 1

                    loop_title = instructions[i].r1 + ":"
                    # loop through instructions after the jump header, and add them to the list of instructions
                    for j in range(all_instructions.index(loop_title), len(all_instructions)):
                        if ':' in all_instructions[j]:
                            continue
                        else:
                            instructions.append(Instruction(all_instructions[j], len(instructions))) # THIS IS A TEMP FIX THAT NEEDS TO BE CHANGED
                    instructions[i].be = True
                    #print(instructions[15])
                    return instructions
            elif instructions[i].counter > 4:
                for j in range(len(instructions)):
                    if instructions[j].taken:
                        if (instructions[j].counter + instructions[j].taken_counter) == 5:
                            continue
                        else:
                            instructions[j].taken_counter += 1
                return instructions
    return instructions
'''
with open('p1-input03.txt', 'r') as input:
    a = input.readlines()
b = []
for i in range(len(a)):
    print(a[i], end='')
    if '$' in a[i]:
        b.append(Instruction(a[i]))
# print("here")
# for i in range(len(b)):
#     print(b[i], end='')
t = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s = [0, 0, 0, 0, 0, 0, 0, 0]
print('------------------------\nSTARTING BRANCH\n------------------------\n')
branch(b, a, 4, t, s)
'''
