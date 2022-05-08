print("I'm running :)")

import re

def emptyLine(line):
    if(line == '\n'):
        return False
    else:
        return True

def commentLine(line):
    if((line[0] == '/') & (line[1] == '/')):
        return False
    else:
        return True

def inlineComment(line):
    if(line.find('/') != -1):
        instr_and_comment = line.split('/')
        return instr_and_comment[0]
    else:
        return line

def memoryManage(address):

    def checkPredefined(address):
        if address == 'R0':
            return '0'
        elif address == 'R1':
            return '1'
        elif address == 'R2':
            return '2'
        elif address == 'R3':
            return '3'
        elif address == 'R4':
            return '4'
        elif address == 'R5':
            return '5'
        elif address == 'R6':
            return '6'
        elif address == 'R7':
            return '7'
        elif address == 'R8':
            return '8'
        elif address == 'R9':
            return '9'
        elif address == 'R10':
            return '10'
        elif address == 'R11':
            return '11'
        elif address == 'R12':
            return '12'
        elif address == 'R13':
            return '13'
        elif address == 'R14':
            return '14'
        elif address == 'R15':
            return '15'
        elif address == 'SCREEN':
            return '16384'
        elif address == 'KBD':
            return '24575'
        elif address == 'SP':
            return '0'
        elif address == 'LCL':
            return '1'
        elif address == 'ARG':
            return '2'
        elif address == 'THIS':
            return '3'
        elif address == 'THAT':
            return '4'
        else:
            return -1

    if(checkPredefined(address) != -1):
        address = checkPredefined(address)
        return address

def aInstruction(line):
    address = line.strip('@')
    address = memoryManage(address)
    instruction = f'{int(address):016b}'
    return instruction

def cMatch2Bin(field):
    if field == '0':
        bin = '0' + '101010'
    elif field == '1':
        bin = '0' + '111111'
    elif field == '-1':
        bin = '0' + '111010'
    elif field == 'D':
        bin = '0' + '001100'
    elif field == 'A':
        bin = '0' + '110000'
    elif field == '!D':
        bin = '0' + '001101'
    elif field == '!A':
        bin = '0' + '110001'
    elif field == '-D':
        bin = '0' + '001111'
    elif field == '-A':
        bin = '0' + '110011'
    elif field == 'D+1':
        bin = '0' + '011111'
    elif field == 'A+1':
        bin = '0' + '110111'
    elif field == 'D-1':
        bin = '0' + '001110'
    elif field == 'A-1':
        bin = '0' + '110010'
    elif field == 'D+A':
        bin = '0' + '000010'
    elif field == 'D-A':
        bin = '0' + '010011'
    elif field == 'A-D':
        bin = '0' + '000111'
    elif field == 'D&A':
        bin = '0' + '000000'
    elif field == 'D|A':
        bin = '0' + '010101'

    elif field == 'M':
        bin = '1' + '110000'
    elif field == '!M':
        bin = '1' + '110001'
    elif field == '-M':
        bin = '1' + '110011'
    elif field == 'M+1':
        bin = '1' + '110111'
    elif field == 'M-1':
        bin = '1' + '110010'
    elif field == 'D+M':
        bin = '1' + '000010'
    elif field == 'D-M':
        bin = '1' + '010011'
    elif field == 'M-D':
        bin = '1' + '000111'
    elif field == 'D&M':
        bin = '1' + '000000'
    elif field == 'D|M':
        bin = '1' + '010101'
    else:
        print("No c match found. Given field:" + field)
        quit()

    return bin

def dMatch2Bin(field):
    if field == 'None':
        bin = '000'
    elif field == 'M':
        bin = '001'
    elif field == 'D':
        bin = '010'

    elif field == 'DM':
        bin = '011'
    elif field == 'MD':
        bin = '011'

    elif field == 'A':
        bin = '100'

    elif field == 'AM':
        bin = '101'
    elif field == 'MA':
        bin = '101'

    elif field == 'AD':
        bin = '110'
    elif field == 'DA':
        bin = '110'

    elif field == 'ADM':
        bin = '111'
    elif field == 'MAD':
        bin = '111'
    elif field == 'DMA':
        bin = '111'
    elif field == 'DAM':
        bin = '111'
    elif field == 'AMD':
        bin = '111'
    elif field == 'MDA':
        bin = '111'

    else:
        print("No d match found. Given field:" + field)
        quit()

    return bin

def jMatch2Bin(field):
    if field == 'None':
        bin = '000'
    elif field == 'JGT':
        bin = '001'
    elif field == 'JEQ':
        bin = '010'
    elif field == 'JGE':
        bin = '011'
    elif field == 'JLT':
        bin = '100'
    elif field == 'JNE':
        bin = '101'
    elif field == 'JLE':
        bin = '110'
    elif field == 'JMP':
        bin = '111'
    else:
        print("No j match found. Given field:" + field)
        quit()

    return bin

def cInstruction(line):
    if(line.find('=') != -1):
        d_cFields = line.split('=')
        dBin = dMatch2Bin(d_cFields[0])
        cBin = cMatch2Bin(d_cFields[1])
        jBin = '000'

    elif(line.find(';') != -1):
        c_jFields = line.split(';')
        dBin = '000'
        cBin = cMatch2Bin(c_jFields[0])
        jBin = jMatch2Bin(c_jFields[1])

    else:
        print("cInstruction formatting no good. Line is: " + line)
        quit()
   
    instruction = '111' + cBin + dBin + jBin
    return(instruction)

with open("projects/06/max/Max.asm", "r") as asmFile:
    lines = asmFile.readlines()

lines = list(filter(emptyLine,lines))
lines = list(filter(commentLine,lines))

lines = [line.replace(' ','') for line in lines]
lines = [line.strip('\n') for line in lines]

lines = [inlineComment(line) for line in lines]

print(lines)

machineCode = []
for line in lines:
    if(line[0] == '@'):
        instruction = aInstruction(line)
        print(instruction)
        machineCode.append(instruction)
    else:
        instruction = cInstruction(line)
        print(instruction)
        machineCode.append(instruction)

print(machineCode)

with open("projects/06/pong/PongL.hack", "w") as macFile:
    macFile.write('\n'.join(machineCode))

print("I'm done :)")