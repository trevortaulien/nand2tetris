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

@ONES
M=!D

@ZEROS

@KBD
D=A
@SCREENEND
M=D

@POLL
0;JMP

(BLACKOUT)
@SCREENEND
D=M		//get ending address
@SCREENPOINTER
D=D-M		//compute difference between current and end address
@POLL
D;JEQ		//if no difference then end of screen reached and exit to poll
@ONES
D=M		//gather ones to write
@SCREENPOINTER
A=M		//get address to write
M=D		//write ones to address
@SCREENPOINTER
M=M+1		//increment pointer
@BLACKOUT	
0;JMP

(WHITEOUT)	//Same as blackout just writing zeros instead of ones
@SCREENEND
D=M
@SCREENPOINTER
D=D-M
@POLL
D;JEQ	
@ZEROS
D=M
@SCREENPOINTER
A=M
M=D
@SCREENPOINTER
M=M+1
@WHITEOUT
0;JMP

(POLL)
@SCREEN
D=A		//Getting base address of screen
@SCREENPOINTER
M=D		//Storing screen base address
@KBD
D=M		//Getting value of keyboard
@BLACKOUT
D;JNE		//Blackout if key pressed
@WHITEOUT
D;JEQ		//Whiteout if no key pressed
@POLL
0;JMP
