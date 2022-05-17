print("I'm running :)")

from pickle import FALSE
import sys
import commandTypes as cmdTyp

class VMTranslator:

    lineIndex = 0
    vmMaster = []       # List of lists with each list at given index containing [commandType, arg1, arg2]

    def __init__(self):
        with open(sys.argv[1], 'r') as fileIn:
            self.rawVM = fileIn.readlines()

        self.fileInName = sys.argv[0].strip('.py')

    def parse(self):
        self.parser = Parser()
        self.necessaryVM = self.parser.stripUnnecessary(self.rawVM)
        for vmLine in self.necessaryVM:
            subList = []
            subList[0] = self.parser.commandType(vmLine)
            
            if(subList[0] != cmdTyp.C_RETURN):
                subList[1] = self.parser.arg1(vmLine)
            else:
                return FALSE
            if((subList[0] == cmdTyp.C_PUSH) or (subList[0] == cmdTyp.C_POP) or (subList[0] == cmdTyp.C_FUNCTION) or (subList[0] == cmdTyp.C_CALL)):
                subList[2] = FALSE
            else:
                subList[2] = self.parser.arg2(vmLine)
            
            self.vmMaster.append(subList)
            self.incrementIndex()

    def codeWrite(self):
        pass

    def outputAsm(self):
        pass

    def hasMoreCommands(self):
        try:
            if (self.rawVM[self.lineIndex]):
                return True
        except:
            return False

    def incrementIndex(self):
        self.lineIndex = self.lineIndex + 1

class Parser(VMTranslator):
    
    def __init__(self):
        pass

    def commandType(self, vmLine):
        pass

    def arg1(self, vmLine):
        pass

    def arg2(self, vmLine):
        pass

    def splitVMcommand(self):
        pass

    def stripUnnecessary(self, rawVM):
        necessaryVM = self._removeComments(rawVM)
        necessaryVM = self._removeWhitespace(necessaryVM)
        necessaryVM = self._removeInlineComments(necessaryVM)
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


class CodeWriter(VMTranslator):
    pass

translation0 = VMTranslator()
p = Parser()
print(len(translation0.rawVM))
necessaryVM = p.stripUnnecessary(translation0.rawVM)
print(len(necessaryVM))

print("I'm done :)")