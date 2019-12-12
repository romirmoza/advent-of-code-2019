class intcode_computer:

    def __init__(self, intcode=[], input=1):
        self.intcode = intcode
        self.input = input
        self.output = ""

    def set_alarm1202(self, noun=12, verb=2):
        self.intcode[1] = noun
        self.intcode[2] = verb

    def intcode_parser(self):
        pc = 0
        while self.intcode[pc] != 99:
            [opcode, mode1, mode2, mode3] = self.__decipher_instruction(pc)
            pc = self.__execute_instruction(pc, opcode, mode1, mode2, mode3)

    def __execute_instruction(self, pc, opcode, mode1, mode2, mode3):
        if opcode == 1:
            param1 = self.__get_parameter(pc + 1, mode1)
            param2 = self.__get_parameter(pc + 2, mode2)
            self.__set_parameter(pc + 3, param1 + param2)
            pc += 4
        elif opcode == 2:
            param1 = self.__get_parameter(pc + 1, mode1)
            param2 = self.__get_parameter(pc + 2, mode2)
            self.__set_parameter(pc + 3, param1 * param2)
            pc += 4
        elif opcode == 3:
            self.__set_parameter(pc + 1, self.input)
            pc += 2
        elif opcode == 4:
            param1 = self.__get_parameter(pc + 1, mode1)
            self.output = self.output + str(param1) + " "
            pc += 2
        elif opcode == 5:
            param1 = self.__get_parameter(pc + 1, mode1)
            param2 = self.__get_parameter(pc + 2, mode2)
            pc = param2 if param1 else pc + 3
        elif opcode == 6:
            param1 = self.__get_parameter(pc + 1, mode1)
            param2 = self.__get_parameter(pc + 2, mode2)
            pc = param2 if not param1 else pc + 3
        elif opcode == 7:
            param1 = self.__get_parameter(pc + 1, mode1)
            param2 = self.__get_parameter(pc + 2, mode2)
            if param1 < param2:
                self.__set_parameter(pc + 3, 1)
            else:
                self.__set_parameter(pc + 3, 0)
            pc += 4
        elif opcode == 8:
            param1 = self.__get_parameter(pc + 1, mode1)
            param2 = self.__get_parameter(pc + 2, mode2)
            param3 = self.__get_parameter(pc + 3, mode3)
            if param1 == param2:
                self.__set_parameter(pc + 3, 1)
            else:
                self.__set_parameter(pc + 3, 0)
            pc += 4
        return pc

    def set_intcode(self, intcode):
        self.intcode = intcode

    def get_intcode(self):
        return self.intcode

    def __get_parameter(self, pos, mode):
        if mode:        # immediate mode
            return self.intcode[pos]
        return self.intcode[self.intcode[pos]]       # position mode

    def __set_parameter(self, pos, result):
        self.intcode[self.intcode[pos]] = result     # only position mode is valid

    def __decipher_instruction(self, pc):
        code = self.intcode[pc]
        opcode = code % 100
        code = code // 100
        mode1 = code % 10
        code = code / 10
        mode2 = code % 10
        code = code / 10
        mode3 = code % 10

        return [opcode, mode1, mode2, mode3]

    def get_output(self):
        return self.output
