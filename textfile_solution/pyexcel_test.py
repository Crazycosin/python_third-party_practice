# - * - coding: utf-8 - * -
import pyexcel
from textfile_solution import PROJECT_PATH

def load_and_export_csv_test():
    sheet = pyexcel.get_sheet(file_name=PROJECT_PATH+"//file_location//data.csv")
    print(sheet)

    with open('./file_location/tab_example.csv', 'w') as f:
        unused = f.write('I\tam\ttab\tseparated\tcsv\n')  # for passing doctest
        unused = f.write('You\tneed\tdelimiter\tparameter\n')  # unused is added
    sheet = pyexcel.get_sheet(file_name=PROJECT_PATH+"//file_location//tab_example.csv", delimiter='\t')
    print(sheet)


if __name__ == "__main__":
    load_and_export_csv_test()