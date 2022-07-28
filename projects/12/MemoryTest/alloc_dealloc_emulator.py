print("I'm running :)")

heap = {}

for address in range(2048, 2148):
    heap[address] = 0

hBase = 2048

# Initial Conditions #
heap[hBase] = 0
heap[hBase + 1] = 98
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


malloc(3)
malloc(5)
malloc(2)
dealloc(2055)
malloc(8)
dealloc(2062)
dealloc(2066)
dealloc(2050)
malloc(66)
malloc(6)
print('Free: ' + str(free))
printOutput()

print("I'm done :)")