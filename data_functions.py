FILEPATH = "todos"

def read_lines_file(file = FILEPATH):
    """ Reads a local file to pull each line.
     Returns a list wih each item being a line. """
    with open(file) as opened_file:
        file_content = opened_file.readlines()
    return file_content

def write_to_file(content_to_write, file = FILEPATH):
    """ Writes the input content to local text file. """
    with open(file, "w") as opened_file:
        opened_file.writelines(content_to_write)