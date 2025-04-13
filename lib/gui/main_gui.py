from nicegui import ui

from lib.static_data.TestingData import GetTestList

ui.label('Hello NiceGUI!')
testlist = GetTestList()
print(testlist)
for task in testlist.tasks:
    with ui.row():
        ui.checkbox(task.desc, value=task.completed)
ui.run()
