from instruction import Instruction


def no_forward(instructs, total_cycles):
    def no_forward(instructs, total_cycles):
    #finds the first instruction that has
    found=False;
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
            index2=i-2-instructs[i].nopCount-instructs[i-1].nopCount
            index=i-1-instructs[i].nopCount-instructs[i-1].nopCount
            if (i>=2) and ((instructs[index2].r1==instructs[i].r2 or instructs[index2].r1==instructs[i].r3) and instructs[index2].counter==5):
                instructs[i].cycles[clock]='ID'
                instructs[i].nopCount+=1
                temp=Instruction("nop")
                temp.cycles=instructs[i].cycles.copy()
                temp.cycles[clock]='*'
                temp.counter=3
                instructs.insert(i,temp)
                i+=1
            elif (i>0)and ((instructs[index].r1==instructs[i].r2 or instructs[index].r1==instructs[i].r3) and (instructs[index].counter==5 or instructs[index].counter==4)):
                instructs[i].cycles[clock]='ID'
                instructs[i].nopCount+=1
                temp=Instruction("nop")
                temp.cycles=instructs[i].cycles.copy()
                temp.cycles[clock]='*'
                temp.counter=3
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
