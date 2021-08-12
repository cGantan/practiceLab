#source: codesignal.com, SpaceX company challenges
##Task:
#CPU with 43 32-bit unsigned integer registers, named R00..R32, all initialized to 0
#supports the following instructions:
# mov: move values from register to register and constant to register
# add: register to another register, stores contents in the first register
# dec/inc: incrementing or decrementing a register by 1, taking overflows into consideration
# inv: bitwise inversion of a register
# jmp: unconditionally jumps to instruction number d (1-based). d is guaranteed to be a valid instruction number
# jz: jumps to instruction d (1-based) only if register 0 contains 0
# nop: does nothing
# returns: value of register 42

def cpuEmulator(subroutine):
    reg = []
    for i in range(43):
        reg.append(0)
    count = 0
    while count < len(subroutine):
        inst = subroutine[count]
        spaces = inst.split(" ")
        inst_type = spaces[0]
        registers = ""
        #if the instruction is a NOP there are no registers
        if inst_type != "NOP":
            registers = spaces[1]
        if inst_type == "MOV":
            registers = registers.split(",")
            if registers[0][0] == "R":
                reg_1 = int(registers[0][1:])
                reg_2 = int(registers[1][1:])
                reg[reg_2] = reg[reg_1]
            else:
                reg_2 = int(registers[1][1:])
                val = int(registers[0])
                reg[reg_2] = val
            count = count + 1
        elif inst_type == "ADD":
            registers = registers.split(",")
            reg_1 = int(registers[0][1:])
            reg_2 = int(registers[1][1:])
            reg[reg_1] = (reg[reg_2]+reg[reg_1]) % (2**32)
            count = count + 1
        elif inst_type == "DEC":
            reg_1 = int(registers[1:])
            if reg[reg_1]==0:
                reg[reg_1] = 2**32 - 1
            else:
                reg[reg_1] = reg[reg_1]-1
            count = count + 1
        elif inst_type == "INC":
            reg_1 = int(registers[1:])
            if reg[reg_1]==2**32 - 1:
                reg[reg_1] = 0
            else:
                reg[reg_1] = reg[reg_1]+1
            count = count + 1
        elif inst_type == "INV":
            reg_1 = int(registers[1:])
            reg[reg_1] = ~reg[reg_1] & 0xFFFFFFFF
            count = count + 1
        elif inst_type == "JMP":
            val = int(registers)
            count = val - 1
        elif inst_type == "JZ":
            val = int(registers)
            if reg[0]==0:
                count = val - 1
            else:
                count = count + 1
        elif inst_type == "NOP":
            count = count + 1
    return str(reg[-1])
