class intcode_computer:

    def __init__(self, intcode=[]):
        self.intcode = intcode

    def alarm1202(self, noun = 12, verb = 2):
        self.intcode[1] = noun
        self.intcode[2] = verb

    def intcode_parser(self):
        pc = 0
        while self.intcode[pc] != 99:
            if self.intcode[pc] == 1:
                self.intcode[self.intcode[pc + 3]] = self.intcode[self.intcode[pc + 1]] + self.intcode[self.intcode[pc + 2]]
                pc += 4
            elif self.intcode[pc] == 2:
                self.intcode[self.intcode[pc + 3]] = self.intcode[self.intcode[pc + 1]] * self.intcode[self.intcode[pc + 2]]
                pc += 4

    def set_intcode(self, intcode):
        self.intcode = intcode

    def get_intcode(self):
        return self.intcode
