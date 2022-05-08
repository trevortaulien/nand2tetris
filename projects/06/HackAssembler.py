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

def aInstruction(line):
    address = line.strip('@')
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
    elif field == 'A':
        bin = '100'
    elif field == 'AM':
        bin = '101'
    elif field == 'AD':
        bin = '110'
    elif field == 'ADM':
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

with open("projects/06/rect/RectL.asm", "r") as asmFile:
    lines = asmFile.readlines()

lines = list(filter(emptyLine,lines))
lines = list(filter(commentLine,lines))

lines = [line.strip('\n') for line in lines]

machineCode = []
for line in lines:
    if(line[0] == '@'):
        instruction = aInstruction(line)
        machineCode.append(instruction)
    else:
        instruction = cInstruction(line)
        machineCode.append(instruction)

print(machineCode)

with open("projects/06/rect/RectL.hack", "w") as macFile:
    macFile.write('\n'.join(machineCode))

print("I'm done :)")