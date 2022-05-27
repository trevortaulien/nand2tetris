##################################################

### Segments ###

# argument          
# local
# static
# constant
# this
# that
# pointer
# temp

# Segment Note - 
# The segments are separated memory locations that make the creation of high level language compiler easier. There are no
# symbolic variables. Variables are represented as entries into virtual memory segments.

### Arithmetric and Logic Commands ###

# add
# sub
# neg
# eq
# gt
# lt
# and
# or
# not

# A&L Fundamental Operation - 
# 1. pop neccessary memory off stack
# 2. perform A&L operation
# 3. push result back onto stack

# Note -
# For given command eg 'add', takes in the variables x + y. y is the top of the stack and x is second from top.
# Similarly command 'not' takes in arguments y. 

### Memory Access Commands ###

# pop segment i         pseudo: SP-- --> x = RAM[SP]    
# push segment i        pseudo: RAM[SP] = x --> SP++    

# Access Note - 
# VM commands access ALL virtual memory segments in the same way, using the 'segment name' followed by the 'nonnegative index' where
# index is the index from the segments base address

### Stack Machine ###

# Stack pointer stored at RAM[0]
# Stack base address is 256

##################################################

