from instruction import Instruction


def update_regs(instructs, s, t):
    for i in range(len(instructs)):
        if instructs[i].counter != 5 or instructs[i].taken:
            continue
        if instructs[i].oper == "add":
            if instructs[i].r2[1] == "s":
                v1 = s[int(instructs[i].r2[2])]
            elif instructs[i].r2[1] == "t":
                v1 = t[int(instructs[i].r2[2])]
            else:
                v1 = 0
            if instructs[i].r3[1] == "s":
                v2 = s[int(instructs[i].r3[2])]
            elif instructs[i].r3[1] == "t":
                v2 = t[int(instructs[i].r3[2])]
            else:
                v2 = 0
            vale = v1 + v2
            if instructs[i].r1[1] == "s":
                s[int(instructs[i].r1[2])] = vale
            else:
                t[int(instructs[i].r1[2])] = vale
        elif instructs[i].oper == "addi":
            if instructs[i].r2[1] == "s":
                v1 = s[int(instructs[i].r2[2])]
            elif instructs[i].r2[1] == "t":
                v1 = t[int(instructs[i].r2[2])]
            else:
                v1 = 0
            vale = v1 + int(instructs[i].r3)
            if instructs[i].r1[1] == "s":
                s[int(instructs[i].r1[2])] = vale
            else:
                t[int(instructs[i].r1[2])] = vale
        elif instructs[i].oper == "and":
            if instructs[i].r2[1] == "s":
                v1 = s[int(instructs[i].r2[2])]
            elif instructs[i].r2[1] == "t":
                v1 = t[int(instructs[i].r2[2])]
            else:
                v1 = 0
            if instructs[i].r3[1] == "s":
                v2 = s[int(instructs[i].r3[2])]
            elif instructs[i].r3[1] == "t":
                v2 = t[int(instructs[i].r3[2])]
            else:
                v2 = 0
            vale = int(v1 & v2)
            if instructs[i].r1[1] == "s":
                s[int(instructs[i].r1[2])] = vale
            else:
                t[int(instructs[i].r1[2])] = vale
        elif instructs[i].oper == "andi":
            if instructs[i].r2[1] == "s":
                v1 = s[int(instructs[i].r2[2])]
            elif instructs[i].r2[1] == "t":
                v1 = t[int(instructs[i].r2[2])]
            else:
                v1 = 0
            vale = int(v1 & int(instructs[i].r3))
            if instructs[i].r1[1] == "s":
                s[int(instructs[i].r1[2])] = vale
            else:
                t[int(instructs[i].r1[2])] = vale
        elif instructs[i].oper == "or":
            if instructs[i].r2[1] == "s":
                v1 = s[int(instructs[i].r2[2])]
            elif instructs[i].r2[1] == "t":
                v1 = t[int(instructs[i].r2[2])]
            else:
                v1 = 0
            if instructs[i].r3[1] == "s":
                v2 = s[int(instructs[i].r3[2])]
            elif instructs[i].r3[1] == "t":
                v2 = t[int(instructs[i].r3[2])]
            else:
                v2 = 0
            vale = int(v1 | v2)
            if instructs[i].r1[1] == "s":
                s[int(instructs[i].r1[2])] = vale
            else:
                t[int(instructs[i].r1[2])] = vale
        elif instructs[i].oper == "ori":
            if instructs[i].r2[1] == "s":
                v1 = s[int(instructs[i].r2[2])]
            elif instructs[i].r2[1] == "t":
                v1 = t[int(instructs[i].r2[2])]
            else:
                v1 = 0
            vale = int(v1 | int(instructs[i].r3))
            if instructs[i].r1[1] == "s":
                s[int(instructs[i].r1[2])] = vale
            else:
                t[int(instructs[i].r1[2])] = vale
        elif instructs[i].oper == "slt":
            if instructs[i].r2[1] == "s":
                v1 = s[int(instructs[i].r2[2])]
            elif instructs[i].r2[1] == "t":
                v1 = t[int(instructs[i].r2[2])]
            else:
                v1 = 0
            if instructs[i].r3[1] == "s":
                v2 = s[int(instructs[i].r3[2])]
            elif instructs[i].r3[1] == "t":
                v2 = t[int(instructs[i].r3[2])]
            else:
                v2 = 0
            vale = int(v1 < v2)
            if instructs[i].r1[1] == "s":
                s[int(instructs[i].r1[2])] = vale
            else:
                t[int(instructs[i].r1[2])] = vale
        elif instructs[i].oper == "slti":
            if instructs[i].r2[1] == "s":
                v1 = s[int(instructs[i].r2[2])]
            elif instructs[i].r2[1] == "t":
                v1 = t[int(instructs[i].r2[2])]
            else:
                v1 = 0
            vale = int(v1 < int(instructs[i].r3))
            if instructs[i].r1[1] == "s":
                s[int(instructs[i].r1[2])] = vale
            else:
                t[int(instructs[i].r1[2])] = vale

    return s, t
