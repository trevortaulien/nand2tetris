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


// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop that 0
@0
D=A
@THAT
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


// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1


// pop that 1
@1
D=A
@THAT
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


// pop argument 0
@0
D=A
@ARG
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


// label MAIN_LOOP_START
(Default$MAIN_LOOP_START)


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


// if-goto COMPUTE_ELEMENT
@SP
AM=M-1
D=M
@Default$COMPUTE_ELEMENT
D;JNE


// goto END_PROGRAM
@Default$END_PROGRAM
0;JMP


// label COMPUTE_ELEMENT
(Default$COMPUTE_ELEMENT)


// push that 0
@0
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1


// push that 1
@1
D=A
@THAT
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


// pop that 2
@2
D=A
@THAT
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


// push pointer 1
@3
D=A
@1
A=D+A
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


// pop argument 0
@0
D=A
@ARG
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


// goto MAIN_LOOP_START
@Default$MAIN_LOOP_START
0;JMP


// label END_PROGRAM
(Default$END_PROGRAM)


