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

def documentInstructionNumber(lines):
    l = 0
    numbered_lines = []
    for line in lines:
        if(line[0] == ('(')):
            numbered_lines.append(line)
        else:
            numbered_lines.append([l,line])
            l = l + 1

    return numbered_lines

def documentLabelSymbols(lines, symbolTable):
    for location, line in enumerate(lines):
        if(line[0] == ('(')):
            symbol = line.strip('()')
            symbolTable[symbol] = str(lines[location + 1][0])
               
    return symbolTable

def popLabelDeclarations(lines):
    survivors = []
    for line in lines:
        if(line[0] != '('):
            survivors.append(line)
            
    return survivors

def stripInstructionNumber(lines):
    strippedLines = []
    for line in lines:
        strippedLines.append(line[1])

    return strippedLines

def swapLabelSymbols4address(lines, symbolTable):
    swappedLines = []
    for line in lines:
        if((line[0] == '@') & (symbolTable.get(line.strip('@')) != None)):
            value = symbolTable[line.strip('@')]
            swappedLines.append('@' + str(value))
        else:
            swappedLines.append(line)

    return swappedLines

def documentVariableSymbols(lines,symbolTable):
    
    def numCheck(unit):
        try: 
            unit.strip('@')
            int(unit)
            return True
        except:
            return False
    
    offset = 0
    for line in lines:
        if(line[0] == '@'):
            address = line.strip('@')
            if((numCheck(address) == False) & ((symbolTable.get(address)) == None)):
                symbolTable[address] = 16 + offset
                offset = offset + 1

    return symbolTable

def swapVariableSymbols4address(lines, symbolTable):
    instructions = []
    for line in lines:
        if(line[0] == '@'):
            address = line.strip('@')
            if(symbolTable.get(address) != None):
                instructions.append('@'+ str(symbolTable[address]))
            else:
                instructions.append(line)
        else:
            instructions.append(line)
    
    return instructions

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

with open("projects/06/pong/Pong.asm", "r") as asmFile:
    lines = asmFile.readlines()

lines = list(filter(emptyLine,lines))
lines = list(filter(commentLine,lines))

lines = [line.replace(' ','') for line in lines]
lines = [line.strip('\n') for line in lines]
lines = [inlineComment(line) for line in lines]

symbolTable = {'R0' : '0', 'R1' : '1', 'R2' : '2', 'R3' : '3', 'R4' : '4', 'R5' : '5', 'R6' : '6', 'R7' : '7',
               'R8' : '8', 'R9' : '9', 'R10' : '10', 'R11' : '11', 'R12' : '12', 'R13' : '13', 'R14' : '14', 'R15' : '15',
               'SCREEN' : '16384', 'KBD' : '24576', 'SP' : '0', 'LCL' : '1', 'ARG' : '2', 'THIS' : '3', 'THAT' : '4'}

lines = documentInstructionNumber(lines)
symbolTable = documentLabelSymbols(lines, symbolTable)
lines = popLabelDeclarations(lines)
lines = stripInstructionNumber(lines)
lines = swapLabelSymbols4address(lines, symbolTable)
symbolTable = documentVariableSymbols(lines,symbolTable)
lines = swapVariableSymbols4address(lines, symbolTable)

machineCode = []
for line in lines:
    if(line[0] == '@'):
        instruction = aInstruction(line)
        #print(instruction)
        machineCode.append(instruction)
    else:
        instruction = cInstruction(line)
        #print(line)
        machineCode.append(instruction)

# print(machineCode)

with open("projects/06/pong/Pong.hack", "w") as macFile:
    macFile.write('\n'.join(machineCode))

print("I'm done :)")