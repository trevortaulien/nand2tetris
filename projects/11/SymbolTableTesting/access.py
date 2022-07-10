class SymbolTable():

    fieldOrArg = []
    staticOrVar = []

    def __init__(self):
        pass      

    def reset(self):
        self.fieldOrArg = []
        self.staticOrVar = []

    def define(self, name, type, kind):
        if(kind == 'FIELD' or kind == 'ARG'):
            self.fieldOrArg.append([name,type,kind])
        else:
            self.staticOrVar.append([name,type,kind])

    def varCount(self, kind):
        if(kind == 'FIELD' or kind == 'ARG'):
            return len(self.fieldOrArg)
        elif(kind == 'STATIC' or kind == 'VAR'):
            return len(self.staticOrVar)

    def kindOf(self, name):
        for entry in self.fieldOrArg:
            if(entry[0] == name):
                return entry[2]
        for entry in self.staticOrVar:
            if(entry[0] == name):
                return entry[2]

    def typeOf(self, name):
        for entry in self.fieldOrArg:
            if(entry[0] == name):
                return entry[1]
        for entry in self.staticOrVar:
            if(entry[0] == name):
                return entry[1]

    def indexOf(self, name):
        for index, entry in enumerate(self.fieldOrArg):
            if(entry[0] == name):
                return index
        for index, entry in enumerate(self.staticOrVar):
            if(entry[0] == name):
                return index


classST = SymbolTable()

classST.define('x', 'INT', 'FIELD')
classST.define('y', 'INT', 'FIELD')

classST.define('vars', 'BOOLEAN', 'STATIC')
classST.define('bars', 'CHAR', 'STATIC')

print(classST.fieldOrArg)
print(classST.staticOrVar)

print(classST.reset())

print(classST.fieldOrArg)
print(classST.staticOrVar)