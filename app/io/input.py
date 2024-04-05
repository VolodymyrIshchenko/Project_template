import pandas


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

    Example:
        >>> with open(path, 'r') as file:
        file content

    Returns:
         str: file content located at "path"
    """
    with open(path, 'r') as file:
        return file.read()


def file_csv_pandas(path):
    """This function reads CSV file with help of pandas library
    Pandas helps covers stings of data to data frame.

    Example:
        >>> file_csv_pandas(path)
        data frame

    Args:
        path (string): path to csv

    Returns:
        data frame: structured data from the file
    """
    return pandas.read_csv(path)




