from instruction import Instruction

# JUST A BASE CASE IMPLEMENTATION SO I CAN TEST THINGS USING THIS
def forward(instructs, total_cycles):
    for i in instructs:
        if (i.counter == 0 and i.order == total_cycles) or (i.counter != 0 and i.counter != 5):
            i.counter += 1
    return instructs
