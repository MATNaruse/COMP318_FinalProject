def GetTestList():
    from lib.classes.ToDoList import ToDoList
    MainList = ToDoList()
    MainList.add_task("Buy Milk")
    MainList.add_task("Wash Car")
    MainList.add_task("Run Errands")
    MainList.add_task("Cook Dinner")
    MainList.tasks[1].toggle_complete()
    return MainList
