// Bootstrap
@256
D=A
@SP
M=D
@None.Sys.init$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL //
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push LCL //
// push ARG //
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push ARG //
// push THIS //
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push THIS //
// push THAT //
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push THAT //
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(None.Sys.init$ret.0)


// function Sys.init 0
(Sys.Sys.init)


// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1


// call Class1.set 2
@Sys.Class1.set$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL //
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push LCL //
// push ARG //
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push ARG //
// push THIS //
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push THIS //
// push THAT //
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push THAT //
@SP
D=M
@5
D=D-A
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.set
0;JMP
(Sys.Class1.set$ret.0)


// pop temp 0
@5
D=A
@0
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D


// push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1


// call Class2.set 2
@Sys.Class2.set$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL //
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push LCL //
// push ARG //
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push ARG //
// push THIS //
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push THIS //
// push THAT //
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push THAT //
@SP
D=M
@5
D=D-A
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.set
0;JMP
(Sys.Class2.set$ret.1)


// pop temp 0
@5
D=A
@0
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D


// call Class1.get 0
@Sys.Class1.get$ret.2
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL //
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push LCL //
// push ARG //
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push ARG //
// push THIS //
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push THIS //
// push THAT //
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push THAT //
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class1.get
0;JMP
(Sys.Class1.get$ret.2)


// call Class2.get 0
@Sys.Class2.get$ret.3
D=A
@SP
A=M
M=D
@SP
M=M+1
// push LCL //
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push LCL //
// push ARG //
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push ARG //
// push THIS //
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push THIS //
// push THAT //
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// end push THAT //
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Class2.get
0;JMP
(Sys.Class2.get$ret.3)


// label WHILE
(Sys.Sys.init$WHILE)


// goto WHILE
@Sys.Sys.init$WHILE
0;JMP


// function Class2.set 0
(Class2.Class2.set)


// push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1


// pop static 0
@SP
M=M-1
A=M
D=M
@Class2.0
M=D


// push argument 1
@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1


// pop static 1
@SP
M=M-1
A=M
D=M
@Class2.1
M=D


// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1


// return
@LCL
D=M
@R13
M=D
@5
D=A
@R13
D=M-D
@R14
M=D
@0
D=A
@ARG
D=D+M
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP


// function Class2.get 0
(Class2.Class2.get)


// push static 0
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1


// push static 1
@Class2.1
D=M
@SP
A=M
M=D
@SP
M=M+1


// sub
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@SP
A=M
M=D
@SP
M=M+1


// return
@LCL
D=M
@R13
M=D
@5
D=A
@R13
D=M-D
@R14
M=D
@0
D=A
@ARG
D=D+M
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP


// function Class1.set 0
(Class1.Class1.set)


// push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1


// pop static 0
@SP
M=M-1
A=M
D=M
@Class1.0
M=D


// push argument 1
@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1


// pop static 1
@SP
M=M-1
A=M
D=M
@Class1.1
M=D


// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1


// return
@LCL
D=M
@R13
M=D
@5
D=A
@R13
D=M-D
@R14
M=D
@0
D=A
@ARG
D=D+M
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP


// function Class1.get 0
(Class1.Class1.get)


// push static 0
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1


// push static 1
@Class1.1
D=M
@SP
A=M
M=D
@SP
M=M+1


// sub
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@SP
A=M
M=D
@SP
M=M+1


// return
@LCL
D=M
@R13
M=D
@5
D=A
@R13
D=M-D
@R14
M=D
@0
D=A
@ARG
D=D+M
@R15
M=D
@SP
M=M-1
A=M
D=M
@R15
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
AM=M-1
D=M
@THAT
M=D
@R13
AM=M-1
D=M
@THIS
M=D
@R13
AM=M-1
D=M
@ARG
M=D
@R13
AM=M-1
D=M
@LCL
M=D
@R14
A=M
0;JMP


