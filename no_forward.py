from instruction import Instruction


def no_forward(instructs, total_cycles):
    #finds the first instruction that has

    #TODO DEAL WITH BEQ AND BNE DEPENDENCIES
    found=False
    clock=total_cycles-1
    i=0
    while i<len(instructs):
        #adds stars if the instruction has been flushed by a branch thing
        if(instructs[i].taken):
            if(instructs[i].counter<5):
                instructs[i].cycles[clock]='*'
                instructs[i].counter+=1
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
        #if it is on the IF STEP, check whether or not the ID stage is in use
        elif(instructs[i].counter==1):
            if(i>0 and instructs[i-1].cycles[clock]=='ID' ):
                #dont move if in use
                instructs[i].cycles[clock]='IF'
            else:
                #move to id stage if it is not in use
                instructs[i].cycles[clock]='ID'
                instructs[i].counter+=1;
        #on ID stage, determine wheter to insert stalls or move on to the EX stage
        elif instructs[i].counter==2:
            index2=i-2-instructs[i].nopCount-instructs[i-1].nopCount
            index=i-1-instructs[i].nopCount-instructs[i-1].nopCount
            #checks for dependencies on two instructions before itself
            if (i>=2) and ((instructs[index2].r1==instructs[i].r2 or instructs[index2].r1==instructs[i].r3) and instructs[index2].counter==5):
                #remain at ID stage
                instructs[i].cycles[clock]='ID'
                instructs[i].nopCount+=1
                #create a nop to insert
                temp=Instruction("nop")
                temp.cycles=instructs[i].cycles.copy()
                temp.cycles[clock]='*'
                temp.counter=3
                #insert the nop
                instructs.insert(i,temp)
                i+=1
            #checks for dependencies on previous instruction
            elif (i>0)and ((instructs[index].r1==instructs[i].r2 or instructs[index].r1==instructs[i].r3) and (instructs[index].counter==5 or instructs[index].counter==4)):
                #remain at ID stage
                instructs[i].cycles[clock]='ID'
                instructs[i].nopCount+=1
                #create a nop to insert
                temp=Instruction("nop")
                temp.cycles=instructs[i].cycles.copy()
                temp.cycles[clock]='*'
                temp.counter=3
                #insert the nop
                instructs.insert(i,temp)
                i+=1
            else:
                instructs[i].cycles[clock]='EX'
                instructs[i].counter+=1;
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

f=open("test.txt")
d=f.read()
d=d.split('\n')
d.remove('')
list=[]
for c in d:
    list.append(Instruction(c))
z=1;
while z<=16:
    list=no_forward(list,z)
    for x in list:
        print(x.instruct,"\t",end="")
        for y in x.cycles:
            if(len(y)==3):
                print(y,"",end="")
            elif(len(y)==2):
                print(y," ",end="")
            elif(len(y)==1):
                print(y,"  ",end="")
            print("  ",end="")
        print()
    print()
    z+=1

for x in list:
    print(x.instruct,"\t",end="")
    for y in x.cycles:
        if(len(y)==3):
            print(y,"",end="")
        elif(len(y)==2):
            print(y," ",end="")
        elif(len(y)==1):
            print(y,"  ",end="")
        print("  ",end="")
    print()
