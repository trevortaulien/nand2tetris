// Bootstrap
@256
D=A
@SP
M=D
@Sys.Sys.init$ret.0
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
@Sys.Sys.init
0;JMP
(Sys.Sys.init$ret.0)


// function Sys.init 0
(Sys.Sys.init)


// push constant 4000
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop pointer 0
@0
D=A
@3
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D


// push constant 5000
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop pointer 1
@1
D=A
@3
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D


// call Sys.main 0
@Sys.Sys.main$ret.0
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
@Sys.Sys.main
0;JMP
(Sys.Sys.main$ret.0)


// pop temp 1
@5
D=A
@1
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


// label LOOP
(Sys.Sys.init$LOOP)


// goto LOOP
@Sys.Sys.init$LOOP
0;JMP


// function Sys.main 5
(Sys.Sys.main)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1


// push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop pointer 0
@0
D=A
@3
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D


// push constant 5001
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop pointer 1
@1
D=A
@3
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D


// push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop local 1
@1
D=A
@LCL
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D


// push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop local 2
@2
D=A
@LCL
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D


// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop local 3
@3
D=A
@LCL
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D


// push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1


// call Sys.add12 1
@Sys.Sys.add12$ret.0
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
@Sys.Sys.add12
0;JMP
(Sys.Sys.add12$ret.0)


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


// push local 0
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1


// push local 1
@1
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1


// push local 2
@2
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1


// push local 3
@3
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1


// push local 4
@4
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1


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


// function Sys.add12 0
(Sys.Sys.add12)


// push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop pointer 0
@0
D=A
@3
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D


// push constant 5002
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop pointer 1
@1
D=A
@3
D=D+A
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D


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


// push constant 12
@12
D=A
@SP
A=M
M=D
@SP
M=M+1


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


