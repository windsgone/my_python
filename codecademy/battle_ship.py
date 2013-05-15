# -*- coding: utf-8 -*-

from random import randint

class BattleShip(object):

    def __init__(self, start):
        self.start = start

    def start_game(self):
        print "Are you ready to play the game?"
        check = raw_input("yes or no: ")
        if check == "yes":
            print_board(board)
        else:
            exit(0)


    start_game(print_board(board))


    def print_board(board):                     # 生成游戏棋盘                        
        board = []
        for x in range(5):
            board.append(["O"] * 5)
        for row in board:
            print " ".join(row)

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)
    print ship_row
    print ship_col

    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    for turn in range(4):
        guess_row = input("Guess Row:")
        guess_col = input("Guess Col:")
        
        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!"
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            # Print (turn + 1) here!
            print turn + 1
            print_board(board)
