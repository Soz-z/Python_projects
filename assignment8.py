'''The following are the program requirements for Assignment 9.1:

    /Prompt the user for the name of the directory in which they want to save a file. - 15%
    /Prompt the user for the name of the file they want to save to the directory in requirement 1. - 15%
    /If the directory from requirement 1 doesn't exist the program must create the specified directory. - 20%
    /The program will prompt the user for their name, address, and phone number and write that data
    /as a line of comma separated values to the file using the directory and filename from requirements
    /1 and 2. (example: John Smith, 123 Main St,402-555-1212) - 20%
    /After the data has been written to the file your program must open the file, read the contents,
    /and display the contents to the user as program output. - 20%
    /Create a GitHub Respository for Assignment 8.1 - 5%
    /Submit a link to the respository from requirement 6 as your assignment submission. - 5%
'''

import os

def check_exists(filename):
    os.path.exists(filename)
    return

def i_filename():
    filename = input("Name the file that you want to save in this diretory: ")
    return filename
def i_directory():
    directory_name = input("Name the directory where you want to save the file: ")
    return directory_name

def user_info():
    name = input("Please input your name: ")
    address = input("Please input your address: ")
    phone_num = input("Please input your phone number: ")
    return name, address, phone_num

def read_from(path):
    with open(path) as file_object:
        contents = file_object.read()
    print(contents)

def main():
    dir_name = i_directory()
    if os.path.exists(dir_name) == True:
        pass
    else:
        os.mkdir(dir_name)
    filename = i_filename()
    path = dir_name + '/' + filename
    name, address, phone = user_info()
    with open(path, 'w') as file_object:
        file_object.write(f'{name}, {address}, {phone}')
    read_from(path)
    

main()
