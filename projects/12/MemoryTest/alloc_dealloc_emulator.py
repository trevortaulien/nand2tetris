print("I'm running :)")

heap = {}

for address in range(2048, 16383):
    heap[address] = 0

hBase = 2048

# Initial Conditions #
heap[hBase] = 0
heap[hBase + 1] = 14334
free = hBase

def malloc(size):
    global free
    startFree = free
    while(heap[free + 1] < (size + 2)):
        if(heap[free] == 0):
            print("MEMORY ERROR")
        prevNext = free
        free = heap[free]
    block = free + 2
    if(startFree == free):
        nextAddr = heap[free]
        segSize = heap[free + 1] - size - 2
        heap[free + 1] = size
        free = size + 2 + free
        heap[free] = nextAddr
        heap[free + 1] = segSize
    else:
        #print('Free: ' + str(free))
        #print('prevNext: ' + str(prevNext))
        postNext = heap[free]
        segSize = heap[free + 1] - size - 2
        heap[free + 1] = size
        newNext = size + 2 + free
        heap[prevNext] = newNext
        heap[newNext] = postNext
        heap[newNext + 1] = segSize
        free = startFree
    # print(block)
    return block


def dealloc(dBase):
    global free
    startFree = free
    oldPointer = heap[free]
    while(oldPointer != 0):
        free = oldPointer
        oldPointer = heap[free]
    # print('dealloc free: ' + str(free))
    heap[free] = dBase - 2
    heap[dBase - 2] = 0
    free = startFree

def printOutput():
    print("{:<8} {:<15}".format('Address','Value'))
    for addr, value in heap.items():
        print("{:<8} {:<15}".format(addr, value))


# malloc(3)
# malloc(5)
# malloc(2)
# dealloc(2055)
# malloc(8)
# dealloc(2062)
# dealloc(2066)
# dealloc(2050)
# malloc(66)
# malloc(6)

# malloc(20)
# malloc(20)
# malloc(45)
# dealloc(2072)
# malloc(10)
# dealloc(2050)
# malloc(6)

a = malloc(20)
print('a: ' + str(a))
print('Free: ' + str(free))
b = malloc(3)
print('b: ' + str(b))
print('Free: ' + str(free))
c = malloc(500)
print('c: ' + str(c))
print('Free: ' + str(free))
dealloc(a)
dealloc(b)
b = malloc(3)
print('b: ' + str(b))
print('Free: ' + str(free))
dealloc(c)
dealloc(b)
a = malloc(8000)
print('a: ' + str(a))
print('Free: ' + str(free))
dealloc(a)
a = malloc(7000)
dealloc(a)
print('a: ' + str(a))
print('Free: ' + str(free))
# printOutput()

print("I'm done :)")