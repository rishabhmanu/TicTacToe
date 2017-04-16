# A command based Tic-Tac-toe game
theBoard = {'top-l':' ', 'top-m':' ', 'top-r':' ',
            'mid-l':' ', 'mid-m':' ', 'mid-r':' ',
            'low-l':' ', 'low-m':' ', 'low-r':' '}
def printBoard(board):
    print board['top-l'] + '|' + board['top-m'] + '|' + board['top-r']
    print '-+-+-'
    print board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r']
    print '-+-+-'
    print board['low-l'] + '|' + board['low-m'] + '|' + board['low-r']
print """Instructions :
        - A two player game (command based)
        - use keywords 'top-l': for top left position
                       'top-m': for top middle position
                       'top-r': for top right position
                       'mid-l': for mid left position
                       'mid-m': for mid middle position
                       'mid-r': for mid right position
                       'low-l': for lower left position
                       'low-m': for lower middle position
                       'low-r': for lower right position"""
print "Enjoy!"
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print "Turn for " + turn + ". Move on which space ?"
    move = raw_input()
    theBoard[move] = turn
    if theBoard['top-l'] == theBoard['top-m'] == theBoard['top-r'] != ' ':
        print "Congrats! " + turn + " has won the match!"
        break
    elif theBoard['mid-l'] == theBoard['mid-m'] == theBoard['mid-r'] != ' ':
        print "Congrats! " + turn + " has won the match!"
        break
    elif theBoard['low-l'] == theBoard['low-m'] == theBoard['low-r'] != ' ':
        print "Congrats! " + turn + " has won the match!"
        break
    elif theBoard['top-l'] == theBoard['mid-l'] == theBoard['low-l'] != ' ':
        print "Congrats! " + turn + " has won the match!"
        break
    elif theBoard['top-m'] == theBoard['mid-m'] == theBoard['low-m'] != ' ':
        print "Congrats! " + turn + " has won the match!"
        break
    elif theBoard['top-r'] == theBoard['mid-r'] == theBoard['low-r'] != ' ':
        print "Congrats! " + turn + " has won the match!"
        break
    elif theBoard['top-l'] == theBoard['mid-m'] == theBoard['low-r'] != ' ':
        print "Congrats! " + turn + " has won the match!"
        break
    elif theBoard['low-l'] == theBoard['mid-m'] == theBoard['top-r'] != ' ':
        print "Congrats! " + turn + " has won the match!"
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
