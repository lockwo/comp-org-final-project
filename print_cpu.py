from instruction import Instruction

def print_cpu(instructs, s, t, cycle):
    print("----------------------------------------------------------------------------------")
    print("CPU Cycles ===>".ljust(20), end='')
    for i in range(15):
        print(str(i+1).ljust(4), end='')
    print(str(16))
    for i in instructs:
        if(i.counter>0):
            print(i.instruct.ljust(20), end='')
            for c in range(len(i.cycles)):
                if c == len(i.cycles)-1:
                    break
                print(i.cycles[c].ljust(4),end='')
            print(i.cycles[len(i.cycles)-1])
    print()
    # from https://stackoverflow.com/questions/8450472/how-to-print-a-string-in-fixed-width
    for i in range(len(s)):
        #print("I", i)
        st = "$s" + str(i) + " = " + str(s[i])
        if i == 3 or i == 7:
            print(st)
        else:
            print(st.ljust(20), end='')

    for i in range(len(t)-1):
        st = "$t" + str(i) + " = " + str(t[i])
        if i == 3 or i == 7:
            print(st)
        else:
            print(st.ljust(20), end='')
    st = "$t" + str(9) + " = " + str(t[9])
    print(st)
