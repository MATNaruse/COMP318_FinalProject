package com.comp318_002_g5.voicetodo;

public class SeedData {
    public static ToDoList MainList = new ToDoList("Main");
    public static void PrimeMainList(){
        MainList.AddTask("Buy Milk");
        MainList.AddTask("Go to Gym");
        MainList.AddTask("Write Email");
        MainList.AddTask("Call Mechanic");
        MainList.AddTask("Read reviews");
        System.out.println(MainList.PrintTasks());
    }
}
