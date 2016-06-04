# template for "Stopwatch: The Game"

import simplegui

# define global variables
count = 0
successes = 0
total = 0
interval = 100


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):

    pass


# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    pass


def Stop():
    pass


def Reset():
    pass


# define event handler for timer with 0.1 sec interval
def tick():
    pass


# define draw handler
def draw(canvas):
    text = format(count)
    canvas.draw_text( text, (80, 125), 42, "white")
    canvas.draw_text(str(successes) + '/' + str(total), (190,30), 24, "pink")
    
# Create a frame 
frame = simplegui.create_frame("Stopwatch game", 250, 250)
frame.set_canvas_background('green')

# Register event handlers
frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# Start the frame animation
frame.start()
Reset()


# Please remember to review the grading rubric
