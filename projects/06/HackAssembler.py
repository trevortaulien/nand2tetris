from operator import truediv


print("I'm running :)")

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

def cInstruction(line):
    print(line)

with open("projects/06/add/Add.asm", "r") as asmFile:
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