#Author: Drew Rafferty

todos = []
completed = []

print("Welcome to your todo list")

while True:
    command = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").lower().strip()
    if command == "q":
        break
    elif command == "v":
        viewTorC = input("View (T)odos or (C)ompleted Items?").lower().strip()
        if viewTorC == "t":
            for todo in todos:
                print(f"- {todo}")
            if not todos:
                print("You have no todos")
        elif viewTorC == "c":
            for complete in completed:
                print(f"- {complete}")
            if not completed:
                print("You have no done items")
        else: 
            print("invalid command")
    elif command == "a":
        addTodo = input("Enter ToDo: ")
        todos.append(addTodo)
    elif command == "r":
        rTodo = input("Enter todo: ")
        if rTodo in todos:
            todos.remove(rTodo)
            completed.append(rTodo)
        else: 
            print(f"Sorry " + rTodo +" is not in your list")
    else:
        print("invalid command")
print("Goodbye")