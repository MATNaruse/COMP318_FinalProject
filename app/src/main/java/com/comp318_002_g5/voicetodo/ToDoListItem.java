package com.comp318_002_g5.voicetodo;

public class ToDoListItem {
    public String Task;
    public Boolean Completed;
    public ToDoListItem(String task){
        Task = task;
        Completed = false;
    }

    public void ToggleComplete(){
        Completed = !Completed;
    }
}
