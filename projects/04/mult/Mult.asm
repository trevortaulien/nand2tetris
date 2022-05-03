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

@term1
M=D	//Write value at R0 to term1 Address

@R1
D=M

@term2
M=D	//Write value at R1 to term2 Address

@R2
M=0	//Write result to zero

@term1
D=M
@END
D;JLE	//Jump to end if term1 = zero

@term2
D=M
@END
D;JLE	//Jump to end if term2 = zero

@term1
D=M
(LOOP)
@term2
M=M-1	//Decrement term2
D=M	//Put value of term2 into D for jump comparison	
@WRITE
D;JLT	//Jump straight to write if term is less than zero
@result
D=M	//Get current value of result
@term1
D=D+M	//Add term1 to result
@result
M=D	//Store result
@LOOP
0;JMP

(WRITE)
@result
D=M
@R2
M=D	//Store result
@result
M=0	//Clear Result

(END)
@END
0;JMP
