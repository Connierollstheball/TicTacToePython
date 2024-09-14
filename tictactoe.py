# -------------------------------------------------
# Tic-Tac-Toe by Connie - initially coded while tipsy at a party, a bit touched upon on the day after said party.
# September 13th 2024 and September 14th 2024.
# -------------------------------------------------

import os
import random
from tkinter import messagebox

# Clear the console so we can draw the first board and not have anything get in our way.
os.system('cls')

# Initiate the grid. It should only have 9 spots.
gridvals = [0] * 9

# The value of the winner - 0 for no winner, 1 or 2 for either 1 or 2 being the winner.
winner = 0

# Assign the gridsfilled value. This will be useful for detecting ties.
gridsfilled = 0

# This function checks if there are any winners or not. If there are, return the value of the winnter.
def checkforwin(tocheckfor):
    # Should return the winner as the value - 1 or 2, depending on what player is being checked (indicated by tocheckfor)
    # There's probably such a better way to do this...

    # Vertical Checks
    if gridvals[0] == tocheckfor and gridvals[3] == tocheckfor and gridvals[6] == tocheckfor:
        reportWin(tocheckfor)
    if gridvals[1] == tocheckfor and gridvals[4] == tocheckfor and gridvals[7] == tocheckfor:
        reportWin(tocheckfor)
    if gridvals[2] == tocheckfor and gridvals[5] == tocheckfor and gridvals[8] == tocheckfor:
        reportWin(tocheckfor)
        
    # Horizontal Checks
    if gridvals[0] == tocheckfor and gridvals[1] == tocheckfor and gridvals[2] == tocheckfor:
        reportWin(tocheckfor)
    if gridvals[3] == tocheckfor and gridvals[4] == tocheckfor and gridvals[5] == tocheckfor:
        reportWin(tocheckfor)
    if gridvals[6] == tocheckfor and gridvals[7] == tocheckfor and gridvals[8] == tocheckfor:
        reportWin(tocheckfor)
        
    # Diagonal Checks
    if gridvals[0] == tocheckfor and gridvals[4] == tocheckfor and gridvals[8] == tocheckfor:
        reportWin(tocheckfor)
    if gridvals[6] == tocheckfor and gridvals[4] == tocheckfor and gridvals[2] == tocheckfor:
        reportWin(tocheckfor)

    # Tie Checks - If there are no wins, and all spaces are filled, declare a Tie.
    if gridsfilled == 9:
        reportWin(0)

# Interpret 0 as a blank space, 1 as X and 2 as 0 (the players).
def interpretTicTacNumber(numb):
    match numb:
        case 0:
            return " "
        case 1:
            return "X"
        case 2:
            return "0"
        case _:
            return None

# Function used by checkforWin to report a win (or a tie).
def reportWin(winnerval):
    drawBoard()

    # If the reported value was 0, declare it a Tie.
    if winnerval == 0:
        print('Tie! No one wins.')
        messagebox.showinfo('Game Over', 'Tie! No one wins.')
        exit()

    # If we got here and there's no tie, announce the winner.
    print(str(interpretTicTacNumber(winnerval)) + ' wins!')
    messagebox.showinfo('Game Over', str(interpretTicTacNumber(winnerval)) + ' wins!')
    exit()

# Function used to draw the board.
def drawBoard():
    print('-------------        -------------')
    print('    Board           Reference Grids')
    print('-------------        -------------')
    print('| ' + interpretTicTacNumber(gridvals[0]) + ' | ' + interpretTicTacNumber(gridvals[1]) + ' | ' + interpretTicTacNumber(gridvals[2]) + ' |        | 0 | 1 | 2 |')
    print('-------------        -------------')
    print('| ' + interpretTicTacNumber(gridvals[3]) + ' | ' + interpretTicTacNumber(gridvals[4]) + ' | ' + interpretTicTacNumber(gridvals[5]) + ' |        | 3 | 4 | 5 |')
    print('-------------        -------------')
    print('| ' + interpretTicTacNumber(gridvals[6]) + ' | ' + interpretTicTacNumber(gridvals[7]) + ' | ' + interpretTicTacNumber(gridvals[8]) + ' |        | 6 | 7 | 8 |')
    print('-------------        -------------')

# Function used to announce stuff above the board
def announce(message):
    print('----------------------------------')
    print(str(message))
    print('----------------------------------')
    print('')

while True:
    # Draw the board and the reference grid
    drawBoard()

    # Get the player's input
    gridtodo = input('You are X. Choose where you place your tick (reference grid to the right) > ')

    # If you haven't inserted a number, bring them back to the start.
    if gridtodo.isnumeric():
        # If the number does not correspond to a value on the grid, bring them back to the start.
        if int(gridtodo) > len(gridvals) or int(gridtodo) == len(gridvals) or int(gridtodo) < 0:
            os.system('cls')
            announce('You have chosen a number which does not correspond to a proper grid placement! (0-8)')
            continue
        else: 
            os.system('cls')
            announce('You have chosen ' + gridtodo)
    else:
        os.system('cls')
        announce('You did not insert a numeric value!')
        continue

    # Turn what they inputed into an integer so we can do stuff with it.
    gridtodoint = int(gridtodo)

    # Don't let them override other values in the grid
    if gridvals[gridtodoint] != 0:
        os.system('cls')
        announce('There is already a value there! Please try again!')
        continue

    # If all checks have been passed, insert their value into the grid and clear out the board to draw the next board with the updated values.
    os.system('cls')
    gridvals[gridtodoint] = 1
    gridsfilled += 1

    # Do one initial check for the winner - 1 goes first.
    checkforwin(1)

    # Let the bot place a tick
    botgridbool = True
    botgridchosen = random.randint(0, 8)
    botgridtodo = botgridchosen + 1

    while botgridbool == True:
        # Got to a value above the length of the list, bring it back to 0 and continue the checking.
        if botgridtodo > len(gridvals) or botgridtodo == len(gridvals):
            botgridtodo = 0

        if gridvals[botgridtodo] != 0:
            botgridtodo += 1

            # If this has done a full loop back, just break it.
            if botgridtodo == botgridchosen:
                break

        else:
            # A space for the bot was found, place its check there.
            gridvals[botgridtodo] = 2
            gridsfilled += 1
            break

    # New check for winner, then do loop back to the start to redraw the board - 2 goes second.
    checkforwin(2)