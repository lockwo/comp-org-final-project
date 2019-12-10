from instruction import Instruction

def print_cpu(instructs, s, t, cycle):
    print("----------------------------------------------------------------------------------")
    print("CPU Cycles ===>\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16")
    for i in instructs:
        if (i.counter == 0) or (i.order > cycle):
            continue
        print(i.instruct, end='\t')
        for j in range(i.order-1):
            print(".", end='\t')
        for j in range(i.counter):
            print(i.pipe[j], end='\t')
        for j in range(16-i.counter-i.order):
            print(".", end='\t')
        print()
    
    for i in range(len(s)):
        print("$s" + str(i), "=", str(s[i]) + "\t", end='')
        if i == 3 or i == 7:
            print()

    for i in range(len(t)):
        print("$t" + str(i), "=", str(t[i]) + "\t", end='') 
        if i == 3 or i == 7:
            print()
    
    print()
    
