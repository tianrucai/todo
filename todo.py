import os

# stored file
todo_file = "todo.txt"

# if file exists, load the file, else return empty list
def load_file():
    if not os.path.exists(todo_file):
        return []
    with open(todo_file, "r") as file:
        return file.readlines()

# save the file
def save_file(todos):
    with open(todo_file, "w") as file:
        file.writelines(todos)

# add a todo
def add_todo(todo):
    todos = load_file()
    todos.append(todo + "\n")
    save_file(todos)

# remove a todo
def remove_todo(index):
    todos = load_file()
    if 0 <= index < len(todos):
        todos.pop(index)
        save_file(todos)
    else:
        print("Invalid index")

# show all todos
def show_todos():
    todos = load_file()
    for index, todo in enumerate(todos, 1):
        print(f"{index}. {todo.strip()}")

# main function
def main():
    while True:
        print("\nTodo List")
        print("1. Add Todo")
        print("2. Remove Todo")
        print("3. Show Todos")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            todo = input("Enter a todo: ")
            add_todo(todo)
        elif choice == '2':
            index = int(input("Enter the index of the todo to remove: ")) - 1
            remove_todo(index)
        elif choice == '3':
            show_todos()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()