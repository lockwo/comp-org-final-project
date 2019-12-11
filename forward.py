from instruction import Instruction
import math

# JUST A BASE CASE IMPLEMENTATION SO I CAN TEST THINGS USING THIS

#add more functions and funcionality

def forward(instructs, total_cycles):
    found=False
    clock=total_cycles-1
    i=0
    while i<len(instructs):
        #if nop then increment and add stars
        if(instructs[i].instruct=="nop"):
            if(instructs[i].counter<5):
                instructs[i].cycles[clock]='*'
                instructs[i].counter+=1
        #starts an instruction with IF each cycle
        elif(not found and instructs[i].counter==0):
            instructs[i].cycles[clock]='IF'
            found=True
            instructs[i].counter+=1;
        #if it is on the IF STEP
        elif(instructs[i].counter==1):
            if(i>0 and instructs[i-1].cycles[clock]=='ID' ):
                instructs[i].cycles[clock]='IF'
            else:
                instructs[i].cycles[clock]='ID'
                instructs[i].counter+=1;
        elif instructs[i].counter==2:
            index=i-1-instructs[i].nopCount-instructs[i-1].nopCount
            if (i>=1) and ((instructs[index].r1==instructs[i].r2 or instructs[index].r1==instructs[i].r3) and instructs[index].counter < 5):
                instructs[i].cycles[clock]='ID'
                instructs[i].counter+=1;
                instructs[i].nopCount+=1
                temp=Instruction("nop", i)
                temp.cycles=instructs[i].cycles.copy()
                temp.cycles[clock]='*'
                temp.counter=instructs[i].counter
                instructs.insert(i,temp)
                i+=1
            else:
                print(i)
                print(instructs[index])
                print(instructs[i])
                print(instructs[index].counter)
                print("Nop count" + str(instructs[index].nopCount))
                print("Nop count" + str(instructs[i].nopCount))
                print(instructs[index].instruct)
                while (instructs[index].instruct == "nop"):
                    index -= 1
                print(instructs[index].instruct)
                print(instructs[index])
                #two apart instead of one apart
                if (i>=1) and ((instructs[index].r1==instructs[i].r2 or instructs[index].r1==instructs[i].r3) and instructs[index].counter < 5):
                    print("dependency")
                #if dependency has not been written back yet, acess depdency and not incriment
                #cant incriment

                else:
                    instructs[i].cycles[clock]='EX'
                    instructs[i].counter+=1;
            """
            elif (i>0) and ((instructs[index].r1==instructs[i].r2 or instructs[index].r1==instructs[i].r3) and (instructs[index].counter==5 or instructs[index].counter==4)):
                instructs[i].cycles[clock]='ID'
                instructs[i].nopCount+=1
                temp=Instruction("nop", i)
                temp.cycles=instructs[i].cycles.copy()
                temp.cycles[clock]='*'
                temp.counter=3
                instructs.insert(i,temp)
                i+=1
            """
        elif instructs[i].counter==3:
            instructs[i].cycles[clock]='MEM'
            instructs[i].counter+=1;
        elif instructs[i].counter==4:
            instructs[i].cycles[clock]='WB'
            instructs[i].counter+=1;
        elif instructs[i].counter==5:
            instructs[i].counter+=1;
        i+=1;
    return instructs
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

    only need to do arthmetic stuff
    think about it as perfect knowledge of the system
    
    go to next or previous index to see if they rely on each other

    look at cases for when you need it

    make sure your code runs with other code



    """

    """

    instr_len = len(instructs)
    i = 0
    found = False
    clock = total_cycles - 1

    #check for nops at some point

    while (i < instr_len):
        if(self.taken == True):
            continue;
        prev_instruction = instructs[i-1].cycles[clock]

        #if branching, print *

        if(instructs[i].counter == 0):
            instructs[i].cycles[clock] = 'IF'
            instructs[i].counter+=1
        elif(instructs[i].counter == 1):
            if(i>0 and instructs[i-1].cycles[clock]=='ID'):
                instructs[i].cycles[clock]='IF'
            else:
                instructs[i].cycles[clock]='ID'
                instructs[i].counter+=1;
        elif(instructs[i].counter == 2):
            if(i>0 and instructs[i-1].cycles[clock]=='EX'):
                instructs[i].cycles[clock]='ID'
            else:
                instructs[i].cycles[clock]='EX'
                instructs[i].counter+=1;

        #EX HAZARD

        elif(instructs[i].counter == 3):
            if(i>0 and instructs[i-1].cycles[clock]=='MEM'):
                instructs[i].cycles[clock]='EX'
            else:
                instructs[i].cycles[clock]='MEM'
                instructs[i].counter+=1;

        #MEM HAZARD

        elif(instructs[i].counter == 4):
            if(i>0 and instructs[i-1].cycles[clock]=='WB'):
                instructs[i].cycles[clock]='MEM'
            else:
                instructs[i].cycles[clock]='WB'
                instructs[i].counter+=1;
        i+=1;
    return instructs;

    """
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
