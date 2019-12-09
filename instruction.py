class Instruction:

    def __init__(self, instruct):
        self.counter = 0
        self.instruct = instruct
        self.taken = False
        if len(instruct) > 3:
            instruction = instruct.split(' ')
            self.oper = instruction[0]
            self.r1 = instruction[1].split(',')[0]
            self.r2 = instruction[1].split(',')[1]
            self.r3 = instruction[1].split(',')[2]
        else:
            self.oper = 'nop'
            self.r1 = 0
            self.r2 = 0
            self.r3 = 0

    def __str__(self):
        return f'{self.instruct}\n{self.oper}\n{self.r1}\n{self.r2}\n{self.r3}\n{self.counter}\n'
    
