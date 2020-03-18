import random

board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos]==' '

def printBoard(board):
    print('    |    |')
    print(' '+board[1]+'  | '+board[2]+'  | '+board[3])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' '+board[4]+'  | '+board[5]+'  | '+board[6])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' '+board[7]+'  | '+board[8]+'  | '+board[9])
    print('    |    |')


def isWinner(bo, a):
    return ((bo[1]==a and bo[2]==a and bo[3]==a) or
    (bo[4]==a and bo[5]==a and bo[6]==a) or
    (bo[7]==a and bo[8]==a and bo[9]==a) or
    (bo[1]==a and bo[4]==a and bo[7]==a) or
    (bo[2]==a and bo[5]==a and bo[8]==a) or
    (bo[3]==a and bo[6]==a and bo[9]==a) or
    (bo[1]==a and bo[5]==a and bo[9]==a) or
    (bo[3]==a and bo[5]==a and bo[7]==a))

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place \'X\' (1-9): ')
        
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')

        except:
            print('Please type a number!')


def compMove():
    possMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move=0

    for let in ['O', 'X']:
        for i in possMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move=i
                return move
    corners=[]
    for i in possMoves:
        if i in [1,3,7,9]:
            corners.append(i)

    if len(corners)>0:
        move = selectRandom(corners)
        return move
    
    if 5 in possMoves:
        move = 5
        return move
    
    edges=[]
    for i in possMoves:
        if i in [2,4,6,8]:
            edges.append(i)
    if len(edges)>0:
        move = selectRandom(edges)
    return move

def selectRandom(li):
    l = len(li)
    x = random.randrange(0,l)
    return li[x]

def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic-Tac-Toe')
    printBoard(board)
    tie = False
    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, Computer won this time!")
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move==0:
                print("This game is a Tie!")
                tie  =  True
            else:
                insertLetter('O', move)
                print("Computer placed an \'O\' at position ", move,":")
                printBoard(board)
        else:
            print("Congratulations! You won!")
            break

    if isBoardFull(board) and not(tie):
        print('This game is a Tie!')
main()
while True:
    ans = input("Do you want to play again? (Y/N):")
    if ans.lower()=='y' or ans.lower()=='yes':
        board=[' ' for x in range(10)]
        print('---------------------------------')
        main()

    else:
        break
