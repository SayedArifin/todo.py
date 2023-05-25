print('Welcome to my Todo App!')
todo_list = []


def show():
    print("You have the following Todos:")
    n = 1
    for i in todo_list:
        print(f"{n}. {i}")
        n += 1


file = open('todo.txt', 'r')
saved_list = file.readlines()
for item in saved_list:
    todo_list.append(item.replace("\n", ""))
file.close()
while True:

    user_choice = input(
        "\nWhat would you like to do?\n 1. Add a Todo\n 2. See all Todos\n 3. Edit a Todo\n 4. Delete a Todo\n 5. Exit "
        "the app\n\nReply (Enter a number between 1 and 5): ")

    match user_choice:
        case "1":
            new_todo = input("Enter a new Todo: ") + "\n"
            file = open('todo.txt', 'r')
            todo_List = file.readlines()
            file.close()
            todo_List.append(new_todo)
            todo_list.append(new_todo.replace("\n", ""))
            file = open('todo.txt', 'w')
            file.writelines(todo_List)
            file.close()
            print("Todo added successfully!")

        case "2":
            if len(todo_list) == 0:
                print("You have no Todos.")
            else:
                show()
                input("Press 'ENTER' to continue.")

        case "3":
            if len(todo_list) == 0:
                print("You have no Todos to edit.")
            else:
                show()
                print('Which Todo do you want to edit?')
                num = int(input("Reply (Enter the corresponding number): "))

                match 1 <= num <= len(todo_list):
                    case True:
                        edited_text = input(f"What would you like to change '{todo_list[num - 1]}' to?\n: ")
                        todo_list[num - 1] = edited_text
                        print("Todo updated successfully!")
                    case _:
                        print("Invalid Todo number. Please try again.")

        case "4":
            if len(todo_list) == 0:
                print("You have no Todos to delete.")
            else:
                show()
                print('Which Todo do you want to delete?')
                num = int(input("Reply (Enter the corresponding number): "))

                match 1 <= num <= len(todo_list):
                    case True:
                        deleted_text = input(f"Are you sure you want to delete '{todo_list[num - 1]}'? (Y/N): ").lower()

                        match deleted_text:
                            case "y":
                                todo_list.pop(num - 1)
                                file = open('todo.txt', 'w')
                                for dt in todo_list:
                                    data = []
                                    data.append(dt + '\n')
                                    file.writelines(data)
                                file.close()

                                print("Todo deleted successfully!")
                            case _:
                                print('Deleting the Todo has been canceled.')
                    case _:
                        print("Invalid Todo number. Please try again.")

        case "5":
            break

        case _:
            print("Invalid input. Please enter a number between 1 and 5.")

print("\nThank you for using my app! Goodbye!")
