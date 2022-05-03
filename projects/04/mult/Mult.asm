// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

@R0
D=M

@TERM1
M=D	//Write value at R0 to TERM1 Address

@R1
D=M

@TERM2
M=D	//Write value at R1 to TERM2 Address

@R2
M=0	//Write result to zero

@TERM1
D=M
@END
D;JLE	//Jump to end if term1 = zero

@TERM2
D=M
@END
D;JLE	//Jump to end if term2 = zero

@TERM1
D=M
(LOOP)
@RESULT
D=M	//Get current value of result
@TERM1
D=D+M	//Add term1 to result
@RESULT
M=D	//Store result
@TERM2
M=M-1	//Decrement term2
D=M	//Put value of term2 into D for jump comparison	
@LOOP
D;JGE	//Loop again if term2 is greater than/equal to zero

@RESULT
D=M
@R2
M=D	//Store result

(END)
@END
0;JMP
