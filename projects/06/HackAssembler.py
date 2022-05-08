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
    match field:
        case '0':
            bin = '0' + '101010'
        case '1':
            bin = '0' + '111111'
        case '-1':
            bin = '0' + '111010'
        case 'D':
            bin = '0' + '001100'
        case 'A':
            bin = '0' + '110000'
        case '!D':
            bin = '0' + '001101'
        case '!A':
            bin = '0' + '110001'
        case '-D':
            bin = '0' + '001111'
        case '-A':
            bin = '0' + '110011'
        case 'D+1':
            bin = '0' + '011111'
        case 'A+1':
            bin = '0' + '110111'
        case 'D-1':
            bin = '0' + '001110'
        case 'A-1':
            bin = '0' + '110010'
        case 'D+A':
            bin = '0' + '000010'
        case 'D-A':
            bin = '0' + '010011'
        case 'A-D':
            bin = '0' + '000111'
        case 'D&A':
            bin = '0' + '000000'
        case 'D|A':
            bin = '0' + '010101'

        case 'M':
            bin = '1' + '110000'
        case '!M':
            bin = '1' + '110001'
        case '-M':
            bin = '1' + '110011'
        case 'M+1':
            bin = '1' + '110111'
        case 'M-1':
            bin = '1' + '110010'
        case 'D+M':
            bin = '1' + '000010'
        case 'D-M':
            bin = '1' + '010011'
        case 'M-D':
            bin = '1' + '000111'
        case 'D&M':
            bin = '1' + '000000'
        case 'D|M':
            bin = '1' + '010101'

def dMatch2Bin(field):
    pass

def jMatch2Bin(field):
    pass

def cInstruction(line):
    if(line.find('=') == True):
        d_cFields = line.split('=')
        dBin = dMatch2Bin(d_cFields[0])
        cBin = cMatch2Bin(d_cFields[1])

    elif(line.find(';') == True):
        c_jFields = line.split(';')
        cBin = cMatch2Bin(c_jFields[0])
        jBin = jMatch2Bin(c_jFields[1])
        
    # instruction = '111' + dest + aComp + jump
    # return(instruction)

with open("projects/06/max/MaxL.asm", "r") as asmFile:
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


print("I'm done :)")