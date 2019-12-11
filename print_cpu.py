from instruction import Instruction

def print_cpu(instructs, s, t, cycle):
    print("----------------------------------------------------------------------------------")
    print("CPU Cycles ===>".ljust(20), end='')
    for i in range(16):
        print(str(i+1).ljust(4), end='')
    print()
    for i in instructs:
        if(i.counter>0):
            print(i.instruct.ljust(20), end='')
            for c in i.cycles:
                print(c.ljust(4),end='')
            print()
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
