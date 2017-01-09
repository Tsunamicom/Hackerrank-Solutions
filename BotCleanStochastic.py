# https://www.hackerrank.com/challenges/botcleanr

def findDirt(board):
    for row in range(len(board)):
        if 'd' in board[row]:
            return [row, board[row].index('d')]

def nextMove(posr, posc, board):
    bot = [posr, posc]
    dirt = findDirt(board)
    if bot == dirt:
        print("CLEAN")
    elif bot[0] == dirt[0]:
        if bot[1] < dirt[1]:
            print("RIGHT")
        else:
            print("LEFT")
    else:
        if bot[0] < dirt[0]:
            print("DOWN")
        else:
            print("UP")
    
    
    
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
