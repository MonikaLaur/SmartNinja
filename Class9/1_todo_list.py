# todo list with dictionionary
# --> is blue because pycharm reconizes todo

import json

filename = "todo.json"

with open(filename, "r") as f:
    my_todo_list = json.load(f)

while True:
    print "(n) Exit program"
    print "(a) Add task to list"
    print "(s) Show list"
    print "(t) Show only not done entries"

    user_input = raw_input("Choose an option: ")
    if user_input.lower()== "n":
        with open(filename, "w", ) as f:
            json.dump(my_todo_list, f)
        break
    elif user_input.lower()=="a":
        task = raw_input("Enter the new task: ")
        done_str = raw_input("Is it done? (y,n): ")
        done = done_str.lower() == "y"

        my_todo_list[task] = done

    elif user_input.lower()=="s":
        for task, done in my_todo_list.items():
            if done:
                print task, "done"
            else:
                print task, "not done"
    elif user_input.lower()=="t":
        for task, done in my_todo_list.items():
            if done == False : # can also be written as " if not done: "
                print task, "not done" # can aslo just write print task

