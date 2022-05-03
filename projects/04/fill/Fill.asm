// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

@ones
M=!D

@zeros

@KBD
D=A
@screenend
M=D

@POLL
0;JMP

(BLACKOUT)
@screenend
D=M		//get ending address
@screenpointer
D=D-M		//compute difference between current and end address
@POLL
D;JEQ		//if no difference then end of screen reached and exit to poll
@ones
D=M		//gather ones to write
@screenpointer
A=M		//get address to write
M=D		//write ones to address
@screenpointer
M=M+1		//increment pointer
@BLACKOUT	
0;JMP

(WHITEOUT)	//Same as blackout just writing zeros instead of ones
@screenend
D=M
@screenpointer
D=D-M
@POLL
D;JEQ	
@zeros
D=M
@screenpointer
A=M
M=D
@screenpointer
M=M+1
@WHITEOUT
0;JMP

(POLL)
@SCREEN
D=A		//Getting base address of screen
@screenpointer
M=D		//Storing screen base address
@KBD
D=M		//Getting value of keyboard
@BLACKOUT
D;JNE		//Blackout if key pressed
@WHITEOUT
D;JEQ		//Whiteout if no key pressed
@POLL
0;JMP
