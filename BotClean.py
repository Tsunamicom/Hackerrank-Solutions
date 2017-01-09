# https://www.hackerrank.com/challenges/botclean

def findAllDirt(board):
    """Returns a list of all dirt locations, given a board"""
    dirt = list()
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 'd':
                dirt.append((y, x))
    return dirt

def greedyFindClosest(botloc, dirtloc):
    """Returns a tuple of the closest location of dirt to the bot"""
    mindist = 9999999999999999999999
    mindirt = None
    for dirt in dirtloc:
        distance = ((botloc[0]-dirt[0])**2+(botloc[1]-dirt[1])**2)**(1/2)
        if distance < mindist:
            mindist = distance
            mindirt = dirt
    return mindirt

def next_move(posr, posc, board):
    alldirt = findAllDirt(board)
    dirt = greedyFindClosest([posr, posc], alldirt)
    if dirt == (posr, posc):
        print("CLEAN")
    elif (posr == dirt[0]):
        if (posc < dirt[1]):
            print("RIGHT")
        else:
            print("LEFT")
    else:
        if posr < dirt[0]:
            print("DOWN")
        else:
            print("UP")

def runProgram():
    bot = list(map(int, input().split(' ')))
    board = [input() for row in range(5)]
    next_move(bot[0], bot[1], board)    
        
if __name__ == '__main__':
    runProgram()



'''  ALTERNATIVE FUNCTIONS TO FINISH THE PROBLEM
def cleanNextDirt(bot, nextDirt):
    """Prints all actions required for the bot move toward and clean the next dirt"""
    while bot != list(nextDirt):
        if (bot[0] == nextDirt[0]):
            if (bot[1] < nextDirt[1]):
                print("RIGHT")
                bot[1] += 1
            else:
                print("LEFT")
                bot[1] -= 1
        else:
            if bot[0] < nextDirt[0]:
                print("DOWN")
                bot[0] += 1
            else:
                print("UP")
                bot[0] -= 1
    print("CLEAN")
    
def runCleanProgram(bot, board):
    alldirt = findAllDirt(board)
    while alldirt != []:
        dirt = greedyFindClosest(bot, alldirt)
        cleanNextDirt(bot, dirt)
        alldirt.remove(dirt)
        
runCleanProgram(bot, board)
'''  
