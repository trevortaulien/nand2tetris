// Bootstrap
@256
D=A
@SP
M=D
@Sys.init$ret.0
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
(Sys.init$ret.0)


// function Sys.init 0
(Sys.init)


// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1


// call Main.fibonacci 1
@Main.fibonacci$ret.1
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.1)


// label WHILE
(Sys.init$WHILE)


// goto WHILE
@Sys.init$WHILE
0;JMP


// function Main.fibonacci 0
(Main.fibonacci)


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


// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1


// lt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@SUCCESS_LT_0
D;JGT
@SP
A=M
M=0
@SP
M=M+1
@END_LT_0
0;JMP
(SUCCESS_LT_0)
@SP
A=M
M=-1
@SP
M=M+1
(END_LT_0)


// if-goto IF_TRUE
@SP
AM=M-1
D=M
@Main.fibonacci$IF_TRUE
D;JNE


// goto IF_FALSE
@Main.fibonacci$IF_FALSE
0;JMP


// label IF_TRUE
(Main.fibonacci$IF_TRUE)


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


// return
// frame = LCL
@LCL
D=M
@R13
M=D
// retAddr = *(frame - 5)
@5
D=A
@R13
A=M-D
D=M
@R14
M=D
// *ARG = pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// SP = ARG + 1
@ARG
D=M
@SP
M=D+1
// THAT = *(frame - 1)
@R13
AM=M-1
D=M
@THAT
M=D
// THIS = *(frame - 2)
@R13
AM=M-1
D=M
@THIS
M=D
// ARG = *(frame - 3)
@R13
AM=M-1
D=M
@ARG
M=D
// LCL = *(frame - 4)
@R13
AM=M-1
D=M
@LCL
M=D
// goto retAddr
@R14
A=M
0;JMP


// label IF_FALSE
(Main.fibonacci$IF_FALSE)


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


// push constant 2
@2
D=A
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


// call Main.fibonacci 1
@Main.fibonacci$ret.2
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.2)


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


// push constant 1
@1
D=A
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


// call Main.fibonacci 1
@Main.fibonacci$ret.3
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
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.3)


// add
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M+D
@SP
A=M
M=D
@SP
M=M+1


// return
// frame = LCL
@LCL
D=M
@R13
M=D
// retAddr = *(frame - 5)
@5
D=A
@R13
A=M-D
D=M
@R14
M=D
// *ARG = pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// SP = ARG + 1
@ARG
D=M
@SP
M=D+1
// THAT = *(frame - 1)
@R13
AM=M-1
D=M
@THAT
M=D
// THIS = *(frame - 2)
@R13
AM=M-1
D=M
@THIS
M=D
// ARG = *(frame - 3)
@R13
AM=M-1
D=M
@ARG
M=D
// LCL = *(frame - 4)
@R13
AM=M-1
D=M
@LCL
M=D
// goto retAddr
@R14
A=M
0;JMP


