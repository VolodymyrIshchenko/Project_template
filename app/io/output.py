def print_text(text):
    """This function print a text to console

    Example:
        >>> def print_text(text):
        text

    Args:
        text(str): text to be printed
    """
    return print(text)


def import_to_file(path, data):
    """This function imports a data to file

    Args:
        path(str): path to file
        data(str): data to be imported
    """
    with open(path, 'w') as file:
        file.write(data)