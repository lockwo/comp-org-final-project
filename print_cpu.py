from instruction import Instruction

def print_cpu(instructs, s, t):
    for i in instructs:
        print(i)
    
    for i in range(len(s)):
        print("$s" + str(i), "=", str(s[i]) + "\t", end='')
        if i == 3 or i == 7:
            print()

    for i in range(len(t)):
        print("$t" + str(i), "=", str(t[i]) + "\t", end='') 
        if i == 3 or i == 7:
            print()
    
