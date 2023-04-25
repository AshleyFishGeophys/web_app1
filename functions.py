FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of
    todo items
    :param filepath: default
    :return: todo txt file
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    open a text file and
    then write arg lines to todo file
    :param todos_arg: todo txt file
    :param filepath: default
    :return: None
    """
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arg)


"""
Used to check if the current file is 
being run as the main program or if it 
is being imported as a module into another program.

By checking if __name__ is equal to '__main__', 
we can write code that will only be executed 
when the file is run directly as a script, 
but not when it is imported as a module.

This can be useful for testing and debugging 
code within a module without running it every 
time it is imported into another program.
"""
if __name__ == "__main__":
    print("Print something.")
