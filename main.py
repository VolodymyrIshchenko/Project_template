 #noinspection PyUnresolvedReferences
from app.io.input import input_string, read_file, file_csv_pandas
 # noinspection PyUnresolvedReferences
from app.io.output import print_text, import_to_file

def main():
    name = input_string("Enter a number:")
    content = read_file(name)
    print_text(content)
    import_to_file('data/putput.txt', content)

    pandas_content = file_csv_pandas(name)
    pandas_content_to_str = pandas_content.to_string()
    print_text(pandas_content_to_str)
    import_to_file('data/output.txt', pandas_content_to_str)


if __name__ == "main":
     main()