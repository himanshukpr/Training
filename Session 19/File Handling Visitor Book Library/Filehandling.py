# utility clas, where we will have file IO operations
# IO -> input (reading data from  file into program)
        # output (writing data from program to file)

import os

class FileHandling:
    def __init__(self):
        if not os.path.exists('VisitorBookLibrary.csv'):
            with open('VisitorBookLibrary.csv', 'a+') as file:
                file.write("Sr No, Date Time, Name, Roll No, Branch, Purpose\n")
                print('File created successfully')
        else:
            print('File already exists')

    def write_to_file(self, content):
        with open('VisitorBookLibrary.csv', 'a+') as file:
            file.write(str(content) + '\n')
            print("Data written to file successfully.")


    def read_file(self):
        with open('VisitorBookLibrary.csv','r') as file:
            lines = file.readlines()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('Total lines are : ', len(lines))
            for line in lines:
                print(line)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


    def line_in_file(self):
        with open('VisitorBookLibrary.csv', 'r') as file:
            lines = file.readlines()
            return len(lines) 