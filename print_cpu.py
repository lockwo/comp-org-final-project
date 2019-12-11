from instruction import Instruction

def print_cpu(instructs, s, t, cycle):
    print("----------------------------------------------------------------------------------")
    print("CPU Cycles ===>\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16")
    for i in instructs:
        if(i.counter>0):
            print(i.instruct, end='\t')
            for c in i.cycles:
                print(c,end='\t')
            print()

    # from https://stackoverflow.com/questions/8450472/how-to-print-a-string-in-fixed-width
    for i in range(len(s)):
        #print("I", i)
        st = "$s" + str(i) + " = " + str(s[i])
        print(st.ljust(20), end='')
        if i == 3 or i == 7:
            print()

    for i in range(len(t)):
        st = "$t" + str(i) + " = " + str(t[i])
        print(st.ljust(20), end='')
        if i == 3 or i == 7:
            print()

    print()
