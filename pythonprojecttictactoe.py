#!/usr/local/bin/python3

import re

game_is_on = True
turn = "X"
winner = None

def init_board():
	return {
    "a": {
        1: " ",
        2: " ",
        3: " "
    },
    "b": {
        1: " ",
        2: " ",
        3: " "
    },
    "c": {
        1: " ",
        2: " ",
        3: " "
    }
    }

grid = init_board()

def banner():
    print("Welcome to Tic Tac Toe")

def header():
    print("to win tictactoe you need a 3 in a row column or ")



def printboard():
    global grid
    print("--1-2-3-")
    print(f"A|{grid['a'][1]}|{grid['a'][2]}|{grid['a'][3]}|")
    print("--------")

    print(f"B|{grid['b'][1]}|{grid['b'][2]}|{grid['b'][3]}|")
    print("--------")

    print(f"C|{grid['c'][1]}|{grid['c'][2]}|{grid['c'][3]}|")
    print("--------")


def inputhandler():
    global turn,grid 
    printboard()
    print(f"It is the turn of: {turn}")
    row, column = validateinput()
    columnint = int(column)

    if grid[row][columnint] != " ":
        inputhandler() 

    print(f"You choose row: {row} column: {column}")
    grid[row][columnint] = turn

    if CheckVictory():   #see if user has won
        print("CONGRATULATIONS, you win!")
        play_game()
    turn = switchturn(turn)
    inputhandler()

def validateinput():
    global grid
    choice = input()
    match = re.search(r'^([a|b|c])([1|2|3])$', choice)
    if match:
        print(f"row is {match[1]} column is {match[2]}")
        return (match[1], match[2])
    else:
        print("Input invalid. Please enter row and column i.e A1")
        validateinput()

def CheckVictory():
    global grid

    if grid["a"][1] == grid["a"][2] == grid["a"][3] != " ":
        return True

    if grid["b"][1] == grid["b"][2] == grid["b"][3] != " ":
        return True

    if grid["c"][1] == grid["c"][2] == grid["c"][3] != " ":
        return True 

    if grid["a"][1] == grid["b"][1] == grid["c"][1] != " ":
        return True 
 
    if grid["a"][2] == grid["b"][2] == grid["c"][2] != " ":
        return True
    
    if grid["a"][3] == grid["b"][3] == grid["c"][3] != " ":
        return True 
    
    if grid["a"][3] == grid["b"][2] == grid["c"][1] != " ":
        return True 
    
    if grid["a"][1] == grid["b"][2] == grid["c"][3] != " ":
        return True 

    return False

def check_if_game_over():
        check_for_winner()
        check_if_tie()


    

def switchturn(turn):
    if turn == "X":
      return "O"
    else:
      return "X"


def play_game():
    global grid
    run_again = input("another game (yes/no):")
    if run_again=='yes'.lower():
      grid = init_board()
      start()
    elif run_again=='no'.lower():
        print("player don't want to play")
        exit()
    else:
        print("Invalid")
        play_game()


def start():
  print("welcome back")
  banner()
  header()
  inputhandler()


start()