import os
from datetime import datetime
import webbrowser


def command_line():
    running = True
    math_mode = False

    # Messages
    message = 'Type "help" for a list of all commands.'
    help_message = '''mkdir - Makes a Directory
    rmdir - Removes/Deletes a Directory
    rm = Removes/Deletes a file
    cd - Changes Directory
    ls, dir - shows items directories and files in current directory
    read - shows contents text in a file (txt, ini, etc;)a
    open - Opens a webpage
    change - Changes The Password needed to login
    exit, close, bye - Exits Terminal
    help - Displays This Help Message
    math - Enables Math Mode
    Math Mode Commands - add, subtract, multiply and divide'''
    no_name_warning = 'Command Not Found'
    dir_not_empty_warning = 'The directory is not empty'
    math_with_letter_warning = 'noooo you cant do math with letter'
    no_command_warning = 'Command Not Found'

    print(message)

    # Paths
    home = os.environ.get('USERPROFILE')
    desktop = os.path.join(home, 'Desktop')
    documents = os.path.join(home, 'Documents')

    # Functions

    def add(number1, number2):
        return int(number1) + int(number2)

    def subtract(number1, number2):
        return int(number1) - int(number2)

    def divide(number1, number2):
        return round(float(number1)) / round(float(number2))

    def multiply(number1, number2):
        return int(number1) * int(number2)

    # Main Loop
    while running:
        global second_word, last_word, no_dir_warning, dir_exists_warning, joined_path

        try:
            if math_mode:
                inp = input('>>>> ')
            else:
                inp = input('$ ')
                split_inp = inp.split()
                first_word = split_inp[0]

            if ' ' in inp:
                last_word = split_inp[-1]
                second_word = split_inp[1]
                if len(split_inp) >= 3:
                    third_word = split_inp[2]

                no_dir_warning = f'Folder "{second_word}" Not Found'
                no_file_warning = f'File "{second_word}" Not Found'
                no_file_or_dir_warning = f"Folder or File {second_word} Not Found"
                dir_exists_warning = f'Folder "{second_word}" Already Exists'
            else:
                pass

            if not math_mode:

                if first_word == 'change':
                    with open('C:/Users/User/PycharmProjects/Command Line Interface/secretpassword.txt', 'w') as password_file:
                        if 'third_word' in locals():
                            password_file.truncate(0)
                            password_file.write(second_word + ' ' + third_word)
                            print(f"Successfully Changed Password To '{second_word, third_word}'")
                        else:
                            password_file.truncate(0)
                            password_file.write(second_word)
                            print(f"Successfully Changed Password To '{second_word}'")

                elif first_word == 'mkdir':
                    directory = second_word
                    if not os.path.isdir(directory):
                        if last_word == 'desktop' or last_word == 'Desktop' or last_word == 'desk':
                            os.makedirs(os.path.join(desktop, directory))
                            print(f'Made Folder "{directory}" in Desktop')
                        elif last_word == 'documents' or last_word == 'Documents' or last_word == 'docs':
                            os.makedirs(os.path.join(documents, directory))
                            print(f'Made Folder "{directory}" in Documents')
                        elif last_word == 'home' or last_word == 'Home' or last_word == '~':
                            os.makedirs(os.path.join(home, directory))
                            print(f'Made Folder "{directory}" in the Home Directory')
                        else:
                            os.makedirs(second_word)
                            print(f'Made Folder "{directory}"')
                    else:
                        print(dir_exists_warning)

                elif first_word == 'rmdir':
                    if os.path.isdir(second_word):
                        if last_word == "desktop" or last_word == 'Desktop' or last_word == 'desk':
                            os.rmdir(os.path.join(desktop, second_word))
                            print(f'Removed Folder "{second_word}" in Desktop')
                        elif last_word == "documents" or last_word == 'Documents' or last_word == 'docs':
                            os.rmdir(os.path.join(documents, second_word))
                            print(f'Removed Folder "{second_word}" in Documents')
                        elif last_word == 'home' or last_word == 'Home' or last_word == '~':
                            os.rmdir(os.path.join(home, second_word))
                            print(f'Deleted Folder "{second_word}" in the Home Directory')
                        else:
                            os.rmdir(second_word)
                            print(f'Removed Folder "{second_word}"')
                    else:
                        print(no_dir_warning)

                elif first_word == 'rm' or first_word == 'remove':
                    if os.path.isfile(second_word):
                        if last_word == "desktop" or last_word == 'Desktop' or last_word == 'desk':
                            os.remove(os.path.join(desktop, second_word))
                            print(f'Removed "{second_word}" in Desktop')
                        elif last_word == "documents" or last_word == 'Documents' or last_word == 'docs':
                            os.remove(os.path.join(documents, second_word))
                            print(f'Removed "{second_word}" in Documents')
                        elif last_word == 'home' or last_word == 'Home' or last_word == '~':
                            os.remove(os.path.join(home, second_word))
                            print(f'Removed "{second_word}" in the Home Directory')
                        else:
                            os.remove(second_word)
                            print(f'Removed "{second_word}"')
                    else:
                        print(no_file_warning)

                elif first_word == 'info' or first_word == '?':
                    if os.path.exists(joined_path):
                        if third_word == 'size' or third_word == '?size' or third_word == 'size?':
                            if last_word == "desktop" or last_word == 'Desktop' or last_word == 'desk':
                                joined_path = os.path.join(desktop, second_word)
                                size = os.path.getsize(joined_path)
                                print(str(size) + ' bytes')
                            elif last_word == "documents" or last_word == 'Documents' or last_word == 'docs':
                                joined_path = os.path.join(documents, second_word)
                                size = os.path.getsize(joined_path)
                                print(str(size) + ' bytes')
                            elif last_word == 'home' or last_word == 'Home' or last_word == '~':
                                joined_path = os.path.join(home, second_word)
                                size = os.path.getsize(joined_path)
                                print(str(size) + ' bytes')
                            else:
                                size = os.path.getsize(second_word)
                                print(str(size) + ' bytes')
                        elif third_word == 'modtime' or third_word == 'mtime':
                            if last_word == "desktop" or last_word == 'Desktop' or last_word == 'desk':
                                joined_path = os.path.join(desktop, second_word)
                                mtime = os.path.getmtime(joined_path)
                                print('Last Modified: ' + datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M'))
                            elif last_word == "documents" or last_word == 'Documents' or last_word == 'docs':
                                joined_path = os.path.join(documents, second_word)
                                mtime = os.path.getmtime(joined_path)
                                print('Last Modified: ' + datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M'))
                            elif last_word == 'home' or last_word == 'Home' or last_word == '~':
                                joined_path = os.path.join(home, second_word)
                                mtime = os.path.getmtime(joined_path)
                                print('Last Modified: ' + datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M'))
                            else:
                                mtime = os.path.getmtime(second_word)
                                print('Last Modified: ' + datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M'))
                    else:
                        print(no_file_or_dir_warning)

                elif first_word == 'read':
                    if os.path.isfile(joined_path):
                        if last_word == "desktop" or last_word == 'Desktop' or last_word == 'desk':
                            joined_path = os.path.join(desktop, second_word)
                            with open(joined_path, 'r') as file:
                                for line in file:
                                    print(line, end='')
                                print()
                        elif last_word == "documents" or last_word == 'Documents' or last_word == 'docs':
                            joined_path = os.path.join(documents, second_word)
                            with open(joined_path, 'r') as file:
                                for line in file:
                                    print(line, end='')
                                print()
                        elif last_word == 'home' or last_word == 'Home' or last_word == '~':
                            joined_path = os.path.join(home, second_word)
                            with open(joined_path, 'r') as file:
                                for line in file:
                                    print(line, end='')
                                print()
                        else:
                            with open(second_word, 'r') as file:
                                for line in file:
                                    print(line, end='')
                                print()
                    else:
                        print(no_file_warning)

                elif first_word == 'rename':
                    os.rename(second_word, last_word)
                    print(f"Renamed {second_word} to {last_word}.")

                elif first_word == 'cd' or first_word == 'changedir':
                    os.chdir(second_word)
                    print('Current Directory: ' + os.getcwd())

                elif first_word == 'dir' or first_word == 'ls':
                    print('Directory of', os.getcwd(), '\n')
                    dir_contents = os.listdir()
                    for item in dir_contents:
                        if os.path.isdir(item):
                            dir_or_file = 'dir'
                        else:
                            dir_or_file = 'file'
                        print(item, str(os.stat(item).st_size), 'bytes', '-', dir_or_file)

                elif first_word == 'open':
                    if '.' in second_word:
                        split_url = second_word.split('.')
                        tld = split_url[1]
                        if tld == 'com' or tld == 'net' or tld == 'kz' or tld == 'org' or tld == 'ru':
                            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                            webbrowser.get(chrome_path).open_new_tab(second_word)
                            print(f"Opened '{second_word}'")
                    elif '.' not in second_word:
                        search_url = f'https://www.google.com/search?q={second_word}&oq={second_word}&aqs=chrome.0.69i59j0l3j0i457j0l2j0i10j0j46.1085j0j7&sourceid=chrome&ie=UTF-8'
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                        webbrowser.get(chrome_path).open_new_tab(search_url)
                        print(f"Searched '{second_word}'")

                elif inp == 'exit' or inp == 'close' or inp == 'bye':
                    running = False

                elif inp == 'help':
                    print(help_message)

                elif exit_math:
                    math_mode = False
                    continue

                elif first_word == 'math':
                    math_mode = True
                else:
                    print(no_command_warning)
            else:
                if inp == 'add' or inp == 'Add':
                    number_1 = int(input('Number 1: '))
                    number_2 = int(input('Number 2: '))
                    print('Answer:', add(number_1, number_2))
                    print('')
                elif inp == 'subtract' or inp == 'minus':
                    number_1 = int(input('Number 1: '))
                    number_2 = int(input('Number 2: '))
                    print('Answer:', subtract(number_1, number_2))
                    print('')
                elif inp == 'multiply':
                    number_1 = int(input('Number 1: '))
                    number_2 = int(input('Number 2: '))
                    print('Answer:', multiply(number_1, number_2))
                    print('')
                elif inp == 'divide':
                    number_1 = int(input('Number 1: '))
                    number_2 = int(input('Number 2: '))
                    if number_1 == 0:
                        print('Cannot Divide By Zero')
                        continue
                    else:
                        print('Answer:', divide(number_1, number_2))
                        print('')
                elif inp == 'exit math':
                    exit_math = True
                else:
                    print(no_command_warning)
        except OSError:
            print(dir_not_empty_warning)
        # except NameError:
        #     print(no_name_warning)
        except ValueError:
            print(math_with_letter_warning)
        except IndexError:
            pass
        except FileNotFoundError:
            print(f"The Folder or File '{second_word} was not found'")
