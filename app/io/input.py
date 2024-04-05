

def input_string(text):
    """This function implements the feature of
    input data from console

    Args:
        text (str): argument which takes a string from console

    Returns:
        str: argument which is taken from console
        """
    text = input("Enter a string")
    return text


def read_file(path):
    """This function reads a file content located at "path"
    with help of Python functions

    Returns:
         str: file content located at "path"
    """
    with open(path, 'r') as file:
        return file.read()


import pandas as pd
def read_file_csv(path):
    return pandas.read_csv(path)

