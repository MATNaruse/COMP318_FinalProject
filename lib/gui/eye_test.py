# File to hold Eye Test portion of GUI
import asyncio
import random
from time import sleep
from nicegui import ui

from lib.static_data import static_data as stcd


# Creating the Image Object
img = ui.interactive_image().classes('w-64')

# Setting event for when button is clicked
def random_circle():
    directions = list(stcd.options.keys()) # Getting the direction options from static_data.py
    chosen_direction= random.choice(directions) # Choosing a random option
    img.source = stcd.options.get(chosen_direction) # Setting chosen option image
    img.force_reload() # Reloading the Display Image object

testlist = stcd.preset_test1

#random_circle() # Running the code for the first load
async def preset_test():
    answers = []
    correct_count = 0
    sleep_len = 1

    for prompt in testlist:
        print(f"Prompt = {prompt}")
        img.source = stcd.options.get(str(prompt).capitalize())
        img.force_reload()
        img.update()
        await asyncio.sleep(sleep_len)
        print(f"Slept for {sleep_len}")
    print("End of test\n")

def step_thru():
    img.source = stcd.options.get(testlist[0].capitalize())
    img.force_reload()
    used = testlist.pop(0)
    testlist.append(used)

# Setting the Button as a variable so it can be called in main_gui.py
# TODO: Replace this button with the Voice Recognition later
# debug_reroll_btn = ui.button('New Direction', on_click=random_circle)
debug_reroll_btn = ui.button('Start Cycle', on_click=preset_test)