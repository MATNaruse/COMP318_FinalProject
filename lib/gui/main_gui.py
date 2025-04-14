import random

from nicegui import ui

from lib.static_data import static_data

ui.label('Hello NiceGUI!')

img = ui.image('https://picsum.photos/640/360').classes('w-64')

def random_circle():
    directions = list(static_data.options.keys())
    chosen_direction= random.choice(directions)
    img.source = static_data.options.get(chosen_direction)
    img.force_reload()

ui.button('New Direction', on_click=random_circle)


ui.run()
