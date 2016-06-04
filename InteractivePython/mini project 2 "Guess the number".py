# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
secret_num = 0
guesses_left = 0


# helper function to start and restart the game
def new_game():  

    pass


# define event handlers for control panel
def range100():

    pass


def range1000():

    pass

    
def input_guess(guess):    
    # main game logic goes here	
    pass
            
    
# create frame
f = simplegui.create_frame("Game: Guess the number!", 250, 250)
f.set_canvas_background('Green')

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 100)
f.add_button("Range is [0, 1000)", range1000, 100)	
f.add_input("Enter your guess", input_guess, 100)

# call new_game and start frame
new_game()
f.start()



# always remember to check your completed program against the grading rubric
