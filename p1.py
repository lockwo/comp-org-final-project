import sys
from file_read import file_read
from branch import branch
from forward import forward
from no_forward import no_forward
from update_regs import update_regs
from print_cpu import print_cpu
from instruction import Instruction


if __name__=='__main__':
    f = sys.argv[1]

    try:
        input_file = open(sys.argv[2], 'r')
    except:
        print('Failed to open file\n')
        sys.exit()

    s = [0 for i in range(8)]
    t = [0 for i in range(10)]
    # all_instructs is just list of strings of the file per line, mainly just for Randy/Branching, feel free to modify it how you see fit
    instructs, all_instructs = file_read(input_file)
    '''
    print(instructs, all_instructs)
    for i in instructs:
        print(i)
    '''
    done = False
    total_cycles = 1
    toprint=0
    if f == "F":
        print("START OF SIMULATION (forwarding)")
    else:
        print("START OF SIMULATION (no forwarding)")
    while ((not done) and (total_cycles <= 16)):
        instructs = branch(instructs, all_instructs, total_cycles, t, s)
        #for j in instructs:
        #    print(j.instruct,j.taken,j.counter,j.taken_counter)
        if f == "F":
            instructs = forward(instructs, total_cycles)
        else:
            instructs = no_forward(instructs, total_cycles)
        s, t = update_regs(instructs, s, t)
        print_cpu(instructs, s, t, total_cycles)
        done = True
        for i in instructs:
            if i.counter != 6:
                done = False
        if(done==False and instructs[len(instructs)-1].counter==5):
            done=True
        total_cycles += 1

    print("----------------------------------------------------------------------------------")
    print("END OF SIMULATION")
