package com.comp318_002_g5.voicetodo;

import java.util.ArrayList;


public class ToDoList {
    public String Name;
    public ArrayList<ToDoListItem> Tasks;
    public ToDoList(String name) {
        Name = name;
        Tasks = new ArrayList<>();
    }
    public void AddTask(String task){
        Tasks.add(new ToDoListItem(task));
    }

    public void AddTasks(ArrayList<String> tasks){
        for(String task: tasks){
            AddTask(task);
        }
    }
    public void ToggleComplete(int idx){
        // Setting this up with Index reference if the UI is easier
        // to interact with as a list of elements
        Tasks.get(idx).ToggleComplete();
    }

    public String PrintTasks(){
        StringBuilder out_msg = new StringBuilder();
        for(ToDoListItem task: Tasks){
            out_msg.append("- ").append(task.Task).append("/n");
        }
        return out_msg.toString();
    }
}