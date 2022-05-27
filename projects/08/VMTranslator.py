print("I'm running :)")

import sys
from commandTypes import *

class VMTranslator:

    lineIndex = 0
    vmMaster = []       # List of lists with each list at given index containing [commandType, arg1, arg2, rawLine]
    asmLines = []

    def __init__(self):
        with open(sys.argv[1], 'r') as fileIn:
            self.rawVM = fileIn.readlines()

        self.vmFileName = self._getVMFileName()

    def parse(self):
        self.parser = Parser()
        self.necessaryVM = self.parser.stripUnnecessary(self.rawVM)
        for vmLine in self.necessaryVM:
            subList = [None, None, None, None]
            subList[0] = self.parser.commandType(vmLine)
            
            if(subList[0] == C_ARITHMETIC):
                subList[1] = vmLine
            elif(subList[0] == C_RETURN):
                subList[1] = False
            else:
                subList[1] = self.parser.arg1(vmLine)
                
            if((subList[0] == C_PUSH) or (subList[0] == C_POP) or (subList[0] == C_FUNCTION) or (subList[0] == C_CALL)):
                subList[2] = self.parser.arg2(vmLine)
            else:
                subList[2] = False    
            subList[3] = vmLine            
            self.vmMaster.append(subList)
            self.incrementIndex()

    def codeWrite(self):
        self.writer = CodeWriter(self.vmFileName)
        for subList in self.vmMaster:
            if(subList[0] == C_ARITHMETIC):
                asm = self.writer.writeArithmetic(subList)
                self.asmLines.append('// ' + subList[3])
                self._flattenAndAppend(asm,self.asmLines)
                self.asmLines.append('\n')
            elif((subList[0] == C_PUSH) or (subList[0] == C_POP)):
                asm = self.writer.writePushPop(subList)
                self.asmLines.append('// ' + subList[3])
                self._flattenAndAppend(asm,self.asmLines)
                self.asmLines.append('\n')

    def outputAsm(self):
        outputPath = sys.argv[1].replace('.vm', '.asm')
        with open(outputPath, 'w') as fileOut:
            for line in self.asmLines:
                fileOut.write(line)
                fileOut.write('\n')

    def hasMoreCommands(self):
        try:
            if (self.rawVM[self.lineIndex]):
                return True
        except:
            return False

    def incrementIndex(self):
        self.lineIndex = self.lineIndex + 1

    def _flattenAndAppend(self, items, appendee):
        for item in items:
            appendee.append(item)

    def _getVMFileName(self):
        vmFileName = str(sys.argv[1])
        vmFileName = vmFileName.strip('.vm')
        vmFileName = vmFileName.split('/')
        vmFileName = vmFileName[-1]
        return vmFileName

class Parser(VMTranslator):
    
    def __init__(self):
        pass

    def commandType(self, vmLine):
        command = vmLine.split(' ')[0]
        if((command == 'add') or (command == 'sub') or (command == 'neg') or (command == 'eq') or (command == 'gt') or (command == 'lt') or (command == 'and') or (command == 'or') or (command == 'not')):
            return C_ARITHMETIC
        elif(command == 'pop'):
            return C_POP
        elif(command == 'push'):
            return C_PUSH
        else:
            print("ERROR COMMAND TYPE CANNONT BE DETERMNIED!!!")
            print("METHOD: commandType")
            print("vmLine: " + vmLine)
            print("command: " + command)
            quit()

    def arg1(self, vmLine):
        argOne = vmLine.split(' ')[1]
        return argOne

    def arg2(self, vmLine):
        argTwo = vmLine.split(' ')[2]
        return int(argTwo)

    def stripUnnecessary(self, rawVM):
        necessaryVM = self._removeComments(rawVM)
        necessaryVM = self._removeWhitespace(necessaryVM)
        necessaryVM = self._removeInlineComments(necessaryVM)
        necessaryVM = self._removeEOL(necessaryVM)
        return necessaryVM

    def _removeComments(self, lines):
        noCommentsVM = []
        for line in lines:
            if((line[0] == '/') & (line[1] == '/')):
                pass
            else:
                noCommentsVM.append(line)
        return noCommentsVM

    def _removeWhitespace(self, lines):
        noWhitespaceVM = []
        for line in lines:
            if((line == '\n') or (line == '\r') or (line == '\r\n')):
                pass
            else:
                noWhitespaceVM.append(line)
        return noWhitespaceVM

    def _removeInlineComments(self, lines):
        noInlineCommentsVM = []
        for line in lines:
            if(line.find('/') != -1):
                instr_and_comment = line.split('/')
                noInlineCommentsVM.append(instr_and_comment[0])
            else:
                noInlineCommentsVM.append(line)
        return noInlineCommentsVM

    def _removeEOL(self, lines):
        noEOL = []
        for line in lines:
            line = line.replace('\r\n', '')
            noEOL.append(line)

        return noEOL

class CodeWriter(VMTranslator):

    def __init__(self, vmFileName):
        self.vmFileName = vmFileName
        self.eqCount = 0
        self.gtCount = 0
        self.ltCount = 0

    def writeArithmetic(self, subList):
        operation = subList[1]
        if(operation == 'add'):
            return self._writeAdd()
        elif(operation == 'sub'):
            return self._writeSub()
        elif(operation == 'neg'):
            return self._writeNeg()
        elif(operation == 'eq'):
            return self._writeEq()
        elif(operation == 'gt'):
            return self._writeGt()
        elif(operation == 'lt'):
            return self._writeLt()
        elif(operation == 'and'):
            return self._writeAnd()
        elif(operation == 'or'):
            return self._writeOr()
        elif(operation == 'not'):
            return self._writeNot()

    def _writeAdd(self):
        asm = [
            '@SP',
            'AM=M-1',
            'D=M',
            '@SP',
            'AM=M-1',
            'D=M+D',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1'
        ]
        return asm

    def _writeSub(self):
        asm = [
            '@SP',
            'AM=M-1',
            'D=M',
            '@SP',
            'AM=M-1',
            'D=M-D',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1'
        ]
        return asm

    def _writeNeg(self):
        asm = [
            '@SP',
            'AM=M-1',
            'D=-M',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1'
        ]
        return asm

    def _writeEq(self):
        asm = [
            '@SP',
            'AM=M-1',
            'D=M',
            '@SP',
            'AM=M-1',
            'D=D-M',
            '@SUCCESS_EQ_' + str(self.eqCount),
            'D;JEQ',
            '@SP',
            'A=M',
            'M=0',
            '@SP',
            'M=M+1',
            '@END_EQ_' + str(self.eqCount),
            '0;JMP',
            '(SUCCESS_EQ_' + str(self.eqCount) + ')',
            '@SP',
            'A=M',
            'M=-1',
            '@SP',
            'M=M+1',
            '(END_EQ_' + str(self.eqCount) + ')'
        ]
        self.eqCount += 1
        return asm

    def _writeGt(self):
        asm = [
            '@SP',
            'AM=M-1',
            'D=M',
            '@SP',
            'AM=M-1',
            'D=D-M',
            '@SUCCESS_GT_' + str(self.gtCount),
            'D;JLT',
            '@SP',
            'A=M',
            'M=0',
            '@SP',
            'M=M+1',
            '@END_GT_' + str(self.gtCount),
            '0;JMP',
            '(SUCCESS_GT_' + str(self.gtCount) + ')',
            '@SP',
            'A=M',
            'M=-1',
            '@SP',
            'M=M+1',
            '(END_GT_' + str(self.gtCount) + ')'
        ]
        self.gtCount += 1
        return asm

    def _writeLt(self):
        asm = [
            '@SP',
            'AM=M-1',
            'D=M',
            '@SP',
            'AM=M-1',
            'D=D-M',
            '@SUCCESS_LT_' + str(self.ltCount),
            'D;JGT',
            '@SP',
            'A=M',
            'M=0',
            '@SP',
            'M=M+1',
            '@END_LT_' + str(self.ltCount),
            '0;JMP',
            '(SUCCESS_LT_' + str(self.ltCount) + ')',
            '@SP',
            'A=M',
            'M=-1',
            '@SP',
            'M=M+1',
            '(END_LT_' + str(self.ltCount) + ')'
        ]
        self.ltCount += 1
        return asm

    def _writeAnd(self):
        asm = [
            '@SP',
            'AM=M-1',
            'D=M',
            '@SP',
            'AM=M-1',
            'D=M&D',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1'
        ]
        return asm

    def _writeOr(self):
        asm = [
            '@SP',
            'AM=M-1',
            'D=M',
            '@SP',
            'AM=M-1',
            'D=M|D',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1'
        ]
        return asm

    def _writeNot(self):
        asm = [
            '@SP',
            'AM=M-1',
            'D=!M',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1'
        ]
        return asm

    def writePushPop(self, subList):
        segment = subList[1]
        if((segment == 'local') or (segment == 'argument') or (segment == 'this') or (segment == 'that')):
            return self._lattPushPop(subList)
        elif(segment == 'constant'):
            return self._constPush(subList)
        elif(segment == 'static'):
            return self._staticPushPop(subList)
        elif(segment == 'temp'):
            return self._tempPushPop(subList)
        elif(segment == 'pointer'):
            return self._pointPushPop(subList)

    def _lattPushPop(self, subList):
        if(subList[1] == 'local'):
            segment = 'LCL'
        elif(subList[1] == 'argument'):
            segment = 'ARG'
        elif(subList[1] == 'this'):
            segment = 'THIS'
        elif(subList[1] == 'that'):
            segment = 'THAT'

        i = subList[2]
        if(subList[0] == C_PUSH):
            asm = [
                '@' + str(i),
                'D=A',
                '@' + segment,
                'A=D+M',
                'D=M',
                '@SP',
                'A=M',
                'M=D',
                '@SP',
                'M=M+1'
            ]
            return asm

        elif(subList[0] == C_POP):
            asm = [
                '@' + str(i),
                'D=A',
                '@' + segment,
                'D=D+M',
                '@R13',
                'M=D',
                '@SP',
                'M=M-1',
                'A=M',
                'D=M',
                '@R13',
                'A=M',
                'M=D'
            ]
            return asm

    def _constPush(self, subList):
        asm = [
            '@' + str(subList[2]),
            'D=A',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1'
        ]
        return asm

    def _staticPushPop(self, subList):
        variableName = self.vmFileName
        if(subList[0] == C_PUSH):
            asm = [
                '@' + variableName + '.' + str(subList[2]),
                'D=M',
                '@SP',
                'A=M',
                'M=D',
                '@SP',
                'M=M+1'
            ]
        elif(subList[0] == C_POP):
            asm = [
                '@SP',
                'M=M-1',
                'A=M',
                'D=M',
                '@' + variableName + '.' + str(subList[2]),
                'M=D'
            ]

        return asm

    def _tempPushPop(self, subList):
        i = subList[2]
        if(subList[0] == C_PUSH):
            asm = [
                '@5',
                'D=A',
                '@' + str(i),
                'A=D+A',
                'D=M',
                '@SP',
                'A=M',
                'M=D',
                '@SP',
                'M=M+1'
            ]
            return asm
        elif(subList[0] == C_POP):
            asm = [
                '@5',
                'D=A',
                '@' + str(i),
                'D=D+A',
                '@R13',
                'M=D',
                '@SP',
                'M=M-1',
                'A=M',
                'D=M',
                '@R13',
                'A=M',
                'M=D'
            ]
            return asm

    def _pointPushPop(self, subList):
        i = subList[2]
        if(subList[0] == C_PUSH):
            asm = [
                '@3',
                'D=A',
                '@' + str(i),
                'A=D+A',
                'D=M',
                '@SP',
                'A=M',
                'M=D',
                '@SP',
                'M=M+1'
            ]
            return asm
        elif(subList[0] == C_POP):
            asm = [
                '@' + str(i),
                'D=A',
                '@3',
                'D=D+A',
                '@R13',
                'M=D',
                '@SP',
                'AM=M-1',
                'D=M',
                '@R13',
                'A=M',
                'M=D'
            ]
            return asm

    def _emptyLine(self):
        return ('')

    def _VMlineAsComment(self,subList):
        return ('//' + subList[3])

translator = VMTranslator()
translator.parse()
translator.codeWrite()
translator.outputAsm()

print("I'm done :)")