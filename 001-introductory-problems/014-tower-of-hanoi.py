# We want to  move the pile of disks from sourceStack to destinationStack 
# The goal is to move the last disk to the destinationStack then we don't have to move it
# To move the last disk to destinationStack we first have to 
# Move all the (n - 1) disks to the auxiliaryStack using the destinationStack as auxiliaryStack(MiddleMan)
# Then we move the last disk to the destinationStack
# And now we have to move the (n - 1) disks from auxiliaryStack to destinationStack using sourceStack(MiddleMan)

def towerOfHanoi(diskNumber, moves, sourceStack, destinationStack, auxiliaryStack):
    # Base Case: If there is only one disk, move it directly from source to destination
    if diskNumber == 1:
        moves.append([sourceStack, destinationStack])
        # To stop the recursion
        return
    # Move (n - 1) disks from source to auxiliary using destination(tempStack)
    towerOfHanoi(diskNumber - 1, moves, sourceStack, auxiliaryStack, destinationStack)
    # Move the nth disk from source to destination
    moves.append([sourceStack, destinationStack])
    # Move (n - 1) disks from auxiliary to destination using source(tempStack)
    towerOfHanoi(diskNumber - 1, moves, auxiliaryStack, destinationStack, sourceStack)


n = int(input())
moves = []
towerOfHanoi(n, moves, 1, 3, 2)
print(len(moves))
for i in moves:
    print(*i)