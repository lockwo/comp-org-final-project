from instruction import Instruction

'''
instructions = LIST OF INSTRUCTIONS
all_instructions = LIST OF ALL INPUT, INSTRUCTIONS AND LOOP HEADERS
'''
def branch(instructions, all_instructions, cycle_count, tregs, sregs):
    for i in range(len(instructions)):
        if instructions[i].oper == 'beq' or instructions[i].oper == 'bne':
            #instructions[i].counter = 4
            # The branch value isn't evaluated until MEM stage (4th stage in datapath)
            if instructions[i].counter < 4:
                continue
            else:
                r1, r2 = instructions[i].r1, instructions[i].r2
                # print(r1, r2)
                # checking whether it's $zero, t, or s register 
                if r1[1] == 'z':
                    r1 = 0
                elif r1[1] == 't':
                    r1 = tregs[int(r1[2])]
                elif r1[1] == 's':
                    r1 = sregs[int(r1[2])]
                if r2[1] == 'z':
                    r2 = 0
                elif r2[1] == 't':
                    r2 = tregs[int(r2[2])]
                elif r2[1] == 's':
                    r2 = sregs[int(r2[2])]
                # print(f'r1: {r1}, r2: {r2}')

                if r1 == r2:
                    # loop through instructions after the branch instruction and for all
                    # instructions that have started running, set taken to True to stop
                    count = 0

                    #DEBUGGING CODE
                    for j in range(i+1, i+4):
                        instructions[j].counter += 1
                    
                    # Count the number of instructions that have started pipelining after the branch instruction
                    for j in range(i + 1, len(instructions)):
                        if (instructions[j].counter > 0):
                            instructions[j].taken = True
                            count += 1
                    
                    # print(count)
                    instructions = instructions[0:i+1+count]
                    
                    loop_title = instructions[i].r3 + ":"
                    # print(str(all_instructions))
                    # for j in range(i+1, len(instructions)):
                    #     if instructions[j].counter > 0:
                    #         instructions.append(instructions[j])
                    # print('=======================================')
                    # for j in range(len(instructions)):
                    #     print(instructions[j])
                    # print('=======================================')
                    for j in range(all_instructions.index(loop_title), len(all_instructions)):
                        if ':' in all_instructions[j]:
                            continue
                        else:
                            instructions.append(Instruction(all_instructions[j], len(instructions))) # THIS IS A TEMP FIX THAT NEEDS TO BE CHANGED
                    # print("here bitch")
                    # for j in range(len(instructions)):
                    #     print(instructions[j])
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
