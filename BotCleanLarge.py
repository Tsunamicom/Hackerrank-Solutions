# https://www.hackerrank.com/challenges/botcleanlarge

def findDirt(board):
    dirtlocations = []
    for row in range(len(board)):
        if 'd' in board[row]:
            position = 0
            subrow = board[row][position:]
            while ('d' in subrow) and (position < len(board[row])):
                dirtx = subrow.index('d') + position
                dirtlocations.append([row, dirtx])
                position = subrow.index('d')+1
                subrow = subrow[position:]
    return dirtlocations

def calcDistance(bot, dirtloc):
    return (((bot[0]-dirtloc[0])**2+(bot[1]-dirtloc[1])**2)**(1/2))
    
def findClosestDirt(bot, board):
    alldirt = findDirt(board)
    mindirtloc = bot
    mindist = float('inf')
    for currentdirt in range(len(alldirt)):
        dirtdist = calcDistance(bot, alldirt[currentdirt])
        if dirtdist < mindist:
            mindist = dirtdist
            mindirtloc = alldirt[currentdirt]
    return mindirtloc


def next_move(posx, posy, dimx, dimy, board):
    bot = [posx, posy]
    dirtloc = findClosestDirt(bot, board)
    if bot != dirtloc:
        if bot[0] == dirtloc[0]:
            if bot[1] < dirtloc[1]:
                print('RIGHT')
            else:
                print('LEFT')
        else:
            if bot[0] < dirtloc[0]:
                print('DOWN')
            else:
                print('UP')
    else:
        print('CLEAN')
    
    
"""GIVEN CODE"""
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
"""END GIVEN CODE"""
