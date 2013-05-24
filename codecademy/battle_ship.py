# -*- coding: utf-8 -*-

from random import randint

def board(x):  # 生成边长为x的正方形游戏棋盘
    board = []
    for i in range(x):
        board.append(["O"] * x)
    return board

def print_board(board):  # 打印棋盘
    for row in board:
        print " ".join(row)  # 优化打印格式
    
def random(board):  # 生成随机行数、列数
    return randint(0, len(board) - 1), randint(0, len(board[0]) - 1)

def play(times):  # times为机会次数
    map_size = int(raw_input("please confirm the map size: "))
    game = board(map_size)
    ship_row, ship_col = random(game)

    for turn in range(times):
        guess_row = input("Guess Row:")
        guess_col = input("Guess Col:")  # 输入猜测行列数

        if guess_row == ship_row and guess_col == ship_col:  # 如果猜对游戏结束
            print "Congratulations! You sunk my battleship!"
            break
        else:
            if (guess_row < 0 or guess_row > (map_size - 1)) or (guess_col < 0 or guess_col > (map_size - 1)):  # 猜测超出范围
                print "Oops, that's not even in the ocean."
            elif(game[guess_row][guess_col] == "X"):  # 位置已猜过
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                game[guess_row][guess_col] = "X"  # 已猜的位置标记为X
            print_board(game)
            print "You have %d times left!" % (times - turn - 1)

play(2)
