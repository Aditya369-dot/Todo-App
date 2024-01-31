# from Function import get_todos, write_todos(either use this or)
import Function
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("it is", now)
while True:
    user_action = input("Type add, show, edit, complete, or exit:") #using while loop to iterate on the given commnd.
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = Function.get_todos()

        todos.append(todo + '\n')

        Function.write_todos(todos, filepath='todos.txt')

    elif user_action.startswith("show"):

        todos = Function.get_todos()




        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:

            number = int(user_action[5:])

            print(number)

            number = number - 1

            todos = Function.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            Function.write_todos(todos, filepath='todos.txt')
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            removable = int(user_action[9:])

            todos = Function.get_todos()

            index = removable - 1

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            Function.write_todos(todos, filepath='todos.txt')

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is No item with that Number.")
        except ValueError:
            print("Please Specify a Number")

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("Bye")




