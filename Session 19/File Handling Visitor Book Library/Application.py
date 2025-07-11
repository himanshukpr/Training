from VisitorBookLibrary import Visitor
from Filehandling import FileHandling



class VisitorApp:
    def __init__(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Welcome to the Visitor App')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        self.file_helper = FileHandling()


    def show_menu(self):
        while True:
            print('~~~~~~~~~~~~~~Select Option~~~~~~~~~~~~~~~~~')
            print('1. Log a visit')
            print('2. View Visits')
            print('3. Quit')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            choice = input('Enter your choice: ')

            if choice == "1":
                self.add_visitor()
            elif choice == "2":
                self.view_visitors()
            elif choice == "3":
                break
            else:
                print('Invalid choice, please try again.') 


    def add_visitor(self):
        visitor = Visitor()
        visitor.add_visitor()
        visitor.srno = self.file_helper.line_in_file()  # Assuming srno is the next line number
        self.file_helper.write_to_file(content=str(visitor))
        

    def view_visitors(self):
        password = input('Enter the pass to access')
        if password == '123':
            self.file_helper.read_file()
        else:
            print('Invalid pass, access denied.')
