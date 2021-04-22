#!/usr/local/bin/python3

# import re

# turn = "X"

# grid = {
#     "a": {
#         1: " ",
#         2: " ",
#         3: " "
#     },
#     "b": {
#         1: " ",
#         2: " ",
#         3: " "
#     },
#     "c": {
#         1: " ",
#         2: " ",
#         3: " "
#     }
#     }

# def banner():
#     print("Welcome to Tic Tac Toe")

# def header():
#     print("to win tictactoe you need a 3 in a row column or ")

# def printboard():
#     global grid
#     print("--1-2-3-")
#     print(f"A|{grid['a'][1]}|{grid['a'][2]}|{grid['a'][3]}|")
#     print("--------")

#     print(f"B|{grid['b'][1]}|{grid['b'][2]}|{grid['b'][3]}|")
#     print("--------")

#     print(f"C|{grid['c'][1]}|{grid['c'][2]}|{grid['c'][3]}|")
#     print("--------")


# def inputhandler():
#     global turn,grid 
#     printboard()
#     print(f"It is the turn of: {turn}")
#     row, column = validateinput()
#     columnint = int(column)

#     if grid[row][columnint] != " ":
#         inputhandler() 

#     print(f"You choose row: {row} column: {column}")
#     grid[row][columnint] = turn

#     if CheckVictory():   #see if user has won
#         print("CONGRATULATIONS, you win!. Another game?")
#     turn = switchturn(turn)
#     inputhandler()

# def validateinput():
#     global grid
#     choice = input()
#     if choice == "quit":
#         exit()    
#     choice = input()
#     match = re.search(r'^([a|b|c])([1|2|3])$', choice)
#     if match:
#         print(f"row is {match[1]} column is {match[2]}")
#         return (match[1], match[2])
#     else:
#         print("Input invalid. Please enter row and column i.e A1")
#         validateinput()

# def CheckVictory():
#     global grid

#     if grid["a"][1] == grid["a"][2] == grid["a"][3] != " ":
#         return True

#     if grid["b"][1] == grid["b"][2] == grid["b"][3] != " ":
#         return True

#     if grid["c"][1] == grid["c"][2] == grid["c"][3] != " ": 
#         return True 

#     if grid["a"][1] == grid["b"][1] == grid["c"][1] != " ":
#         return True 
 
#     if grid["a"][2] == grid["b"][2] == grid["c"][2] != " ":
#         return True
    
#     if grid["a"][3] == grid["b"][3] == grid["c"][3] != " ":
#         return True 
    
#     if grid["a"][3] == grid["b"][2] == grid["c"][1] != " ":
#         return True 
    
#     if grid["a"][1] == grid["b"][2] == grid["c"][3] != " ":
#         return True 

#     return False
    


# def switchturn(turn):
#     if turn == "X":
#       return "O"
#     else:
#       return "X"


# banner()
# header()
# inputhandler()




import os
 
class Person:
    def __init__(self, first, last, age, phone_number):
        self.first = first
        self.last = last
        self.age = age
        self.phone_number = phone_number
 
    def full_name(self):
        return f'{self.first} {self.last}'
 
    def __str__(self):
        return f"{self.first} {self.last} : {self.age} : {self.phone_number}"
 
contacts = list()
 
if os.path.isfile("contacts.csv"):
    with open("contacts.csv") as f:
        csv_list = f.readlines()
        for contact_line in csv_list:
            contact_data = contact_line.rstrip().split(",")
            contact = Person(contact_data[0],
                             contact_data[1], 
                             contact_data[2],
                             contact_data[3])
            contacts.append(contact)
        
users_input = ""
 
 
print("Welcome to the address book program")
 
while users_input != "q":
    print("Available options")
    print("1 - Enter a contact")
    print("2 - Display contacts")
    print("3 - Find contact")
    print("q - quit program")
    users_input = input("Select option: ")
    
    if users_input == "1":
        print("Enter your contact's information")
 
        first_name = input("First name = ")
        last_name = input("Last name = ")
        age = input("Age = ")
        phone_number = input("Phone number = ")
 
        our_contact = Person(first_name, last_name, age, phone_number)
        contacts.append(our_contact)
        print("Thank you we have received your contacts information")
    elif users_input == "2":
        for contact in contacts:
            print(contact)
        input("Contacts displayed. Hit enter to continue.")
    elif users_input == "3":
        to_lookup = input("Enter contact's name to lookup\n")
        for contact in contacts:
            if to_lookup in contact.full_name():
                print(contact)
    elif users_input.lower() == "q":
        break
 
with open("contacts.csv", "w") as f:
    for contact in contacts:
        f.write(f"{contact.first},{contact.last},{contact.age},{contact.phone_number}\n")
 
print("Thank you for using the address book")