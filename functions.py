def get_todos(path=r'todos.txt'):
    with open(path, 'r') as file:
        todos = file.readlines()

    return todos


def write_todos(todos, path=r'todos.txt'):
    with open(path, 'w') as file:
        file.writelines(todos)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())