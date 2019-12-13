class intcode_computer:

    def __init__(self, intcode=[], input=[1,1]):
        self.intcode = intcode
        self.input = input
        self.inputcounter = 0
        self.pc = 0
        self.output = ''
        self.rel_base = 0

    def set_alarm1202(self, noun=12, verb=2):
        self.intcode[1] = noun
        self.intcode[2] = verb

    def intcode_parse_until_output(self):
        break_after_execution = False
        while self.intcode[self.pc] != 99:
            if self.intcode[self.pc] == 4:
                break_after_execution = True
            [opcode, mode1, mode2, mode3] = self.__decipher_instruction()
            self.__execute_instruction(opcode, mode1, mode2, mode3)
            if break_after_execution:
                break

    def intcode_parser(self):
        while self.intcode[self.pc] != 99:
            [opcode, mode1, mode2, mode3] = self.__decipher_instruction()
            self.__execute_instruction(opcode, mode1, mode2, mode3)

    def __execute_instruction(self, opcode, mode1, mode2, mode3):
        if opcode == 1:
            param1 = self.__get_parameter(self.pc + 1, mode1)
            param2 = self.__get_parameter(self.pc + 2, mode2)
            self.__set_parameter(self.pc + 3, mode3, param1 + param2)
            self.pc += 4
        elif opcode == 2:
            param1 = self.__get_parameter(self.pc + 1, mode1)
            param2 = self.__get_parameter(self.pc + 2, mode2)
            self.__set_parameter(self.pc + 3, mode3, param1 * param2)
            self.pc += 4
        elif opcode == 3:
            self.__set_parameter(self.pc + 1, mode1, self.input[self.inputcounter])
            self.inputcounter += 1
            self.pc += 2
        elif opcode == 4:
            param1 = self.__get_parameter(self.pc + 1, mode1)
            self.output = self.output + str(param1) + " "
            self.pc += 2
        elif opcode == 5:
            param1 = self.__get_parameter(self.pc + 1, mode1)
            param2 = self.__get_parameter(self.pc + 2, mode2)
            self.pc = param2 if param1 else self.pc + 3
        elif opcode == 6:
            param1 = self.__get_parameter(self.pc + 1, mode1)
            param2 = self.__get_parameter(self.pc + 2, mode2)
            self.pc = param2 if not param1 else self.pc + 3
        elif opcode == 7:
            param1 = self.__get_parameter(self.pc + 1, mode1)
            param2 = self.__get_parameter(self.pc + 2, mode2)
            if param1 < param2:
                self.__set_parameter(self.pc + 3, mode3, 1)
            else:
                self.__set_parameter(self.pc + 3, mode3, 0)
            self.pc += 4
        elif opcode == 8:
            param1 = self.__get_parameter(self.pc + 1, mode1)
            param2 = self.__get_parameter(self.pc + 2, mode2)
            param3 = self.__get_parameter(self.pc + 3, mode3)
            if param1 == param2:
                self.__set_parameter(self.pc + 3, mode3, 1)
            else:
                self.__set_parameter(self.pc + 3, mode3, 0)
            self.pc += 4
        elif opcode == 9:
            param1 = self.__get_parameter(self.pc + 1, mode1)
            self.rel_base += param1
            self.pc += 2

    def set_intcode(self, intcode):
        self.intcode = intcode

    def set_input(self, input):
        self.input = input
        self.inputcounter = 0

    def extend_input(self, input):
        self.input.extend(input)

    def get_intcode(self):
        return self.intcode

    def __get_parameter(self, pos, mode):
        if mode == 0:          # position mode
            if self.intcode[pos] > len(self.intcode) - 1:       # if memory location is out the initial program req
                    return 0
            return self.intcode[self.intcode[pos]]
        elif mode == 1:        # immediate mode
            if pos > len(self.intcode) - 1:
                    return 0
            return self.intcode[pos]
        elif mode == 2:        # relative mode
            if self.rel_base + self.intcode[pos] > len(self.intcode) - 1:
                    return 0
            return self.intcode[self.rel_base + self.intcode[pos]]


    def __set_parameter(self, pos, mode, result):
        # only position mode is valid
        if mode == 0:
            if self.intcode[pos] > len(self.intcode) - 1: # requires allocating more memory
                self.intcode = self.intcode + [0 for _ in range(self.intcode[pos] - len(self.intcode) + 1)]
                self.intcode[self.intcode[pos]] = result
            else:
                self.intcode[self.intcode[pos]] = result
        if mode == 2:
            if self.rel_base  + self.intcode[pos] > len(self.intcode) - 1: # requires allocating more memory
                self.intcode = self.intcode + [0 for _ in range(self.rel_base + self.intcode[pos] - len(self.intcode) + 1)]
                self.intcode[self.rel_base  + self.intcode[pos]] = result
            else:
                self.intcode[self.rel_base  + self.intcode[pos]] = result

    def __decipher_instruction(self):
        code = self.intcode[self.pc]
        opcode = code % 100
        code = code // 100
        mode1 = code % 10
        code = code // 10
        mode2 = code % 10
        code = code // 10
        mode3 = code % 10

        return [opcode, mode1, mode2, mode3]

    def reset(self):
        self.inputcounter = 0
        self.pc = 0
        self.output = ''

    def get_output(self):
        return self.output

    def clear_output(self):
        self.output = ''

    def has_halted(self):
        if self.intcode[self.pc] == 99:
            return 1
        return 0
