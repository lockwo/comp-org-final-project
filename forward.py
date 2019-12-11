from instruction import Instruction
import math

# JUST A BASE CASE IMPLEMENTATION SO I CAN TEST THINGS USING THIS

#add more functions and funcionality

def forward(instructs, total_cycles):
    """
    Write one function
    and then

    instruction classes - makes it easier

    depending on which cycle and which pipeline

    if forwarding doesn't solve, insert a nop
    certain cases, use forwarding instead instead of nop

    branch

    Data Hazard? check for those in all the stages
    nop?

    hard to visualize
    """

    instr_len = len(instructs)
    i = 0
    found = False
    clock = total_cycles - 1

    #check for nops at some point

    while (i < instr_len):

        #if branching, print *

        if(instructs[i].counter == 0):
            instructs[i].cycles[clock] = 'IF'
            instructs[i].counter+=1
        elif(instructs[i].counter == 1):
            if(i>0 and instructs[i-1].cycles[clock]=='ID' ):
                instructs[i].cycles[clock]='IF'
            else:
                instructs[i].cycles[clock]='ID'
                instructs[i].counter+=1;
        elif(instructs[i].counter == 2):
            if(i>0 and instructs[i-1].cycles[clock]=='EX' ):
                instructs[i].cycles[clock]='ID'
            else:
                instructs[i].cycles[clock]='EX'
                instructs[i].counter+=1;

        #EX HAZARD

        elif(instructs[i].counter == 3):
            if(i>0 and instructs[i-1].cycles[clock]=='MEM' ):
                instructs[i].cycles[clock]='EX'
            else:
                instructs[i].cycles[clock]='MEM'
                instructs[i].counter+=1;

        #MEM HAZARD

        elif(instructs[i].counter == 4):
            if(i>0 and instructs[i-1].cycles[clock]=='WB' ):
                instructs[i].cycles[clock]='MEM'
            else:
                instructs[i].cycles[clock]='WB'
                instructs[i].counter+=1;
        i+=1;
    return instructs;

    """


    if the first argument is 'F'

    total cycles is the number of the cycle we are at ( 1 to 16)

    instructs is a list of the instances of the class
    list of instructuions in order of execution


    instruct
    oper
    r1
    r2
    r3
    counter

    don't need to worry about branching for now

    check branching and can happen anywhere

    bne and evaluate register
    
    #print("----------------------------------------------------------------------------------\n")
    #print("CPU Cycles ===>     1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16\n")

    end = 0
    next_line = 1

    for i in instructs:
        i.instruct
    return instructs
        #print("THIS IS: \n")
        #print(next_line)
        #print(i.instruct)
        #print(i.oper)
        #print(i.r1)
        #print(i.r2)
        #print(i.r3)
        #if (i.counter == 0 and i.order == total_cycles) or (i.counter != 0 and i.counter != 5):
        #   continue;
            #i.counter += 1
        #next_line = next_line + 1
    #return instructs
    """
