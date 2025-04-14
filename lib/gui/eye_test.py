# File to hold Eye Test portion of GUI
import random

from nicegui import ui

from lib.static_data import static_data

# Creating the Image Object
img = ui.image().classes('w-64')

# Setting event for when button is clicked
def random_circle():
    directions = list(static_data.options.keys()) # Getting the direction options from static_data.py
    chosen_direction= random.choice(directions) # Choosing a random option
    img.source = static_data.options.get(chosen_direction) # Setting chosen option image
    img.force_reload() # Reloading the Display Image object

random_circle() # Running the code for the first load

# Setting the Button as a variable so it can be called in main_gui.py
# TODO: Replace this button with the Voice Recognition later
debug_reroll_btn = ui.button('New Direction', on_click=random_circle)