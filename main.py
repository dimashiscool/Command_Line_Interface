from termcolor import colored
import os

print('Type "help" for a list of all commands.')

running = True

while running:
    global second_word, last_word, desktop, nodir_warning, dir_exists_warning, documents

    inp = input('$ ')
    split_inp = inp.split()
    first_word = split_inp[0]

    if ' ' in inp:
        second_word = split_inp[1]
        last_word = split_inp[-1]
        desktop = "C:/Users/User/Desktop/"
        documents = "C:/Users/User/Documents/"
        nodir_warning = f'File "{last_word}" Not Found'
        dir_exists_warning = f'File "{last_word}" Already Exists'

    help_message = '''
mkdir - Makes a Directory
rmdir - Removes/Deletes a Directory
exit, close, bye - Exits Terminal
help - Displays This Help Message
                                    '''
    try:
        if first_word == 'mkdir':
            if last_word == 'desktop' or last_word == 'Desktop' or last_word == 'desk':
                os.mkdir(f"{desktop}{second_word}")
                print(f'Made Folder "{second_word}" in Desktop')
            elif last_word == 'documents' or last_word == 'Documents' or last_word == 'docs':
                os.mkdir(f"{documents}{second_word}")
                print(f'Made Folder "{second_word}" in Documents')
            else:
                os.mkdir(second_word)
                print(f'Made Folder "{second_word}"')
        elif first_word == 'rmdir':
            if last_word == "desktop" or last_word == 'Desktop' or last_word == 'desk':
                os.rmdir(f"{desktop}{second_word}")
                print(f'Removed Folder "{second_word}" in Desktop')
            elif last_word == "documents" or last_word == 'Documents' or last_word == 'docs':
                os.rmdir(f"{documents}{second_word}")
                print(f'Removed Folder "{second_word}" in Documents')
            else:
                os.rmdir(second_word)
                print(f'Removed Folder "{second_word}"')
        elif first_word == 'rm' or first_word == 'remove':
            if last_word == "desktop" or last_word == 'Desktop' or last_word == 'desk':
                os.remove(f"{desktop}{second_word}")
                print(f'Removed "{second_word}" in Desktop')
            elif last_word == "documents" or last_word == 'Documents' or last_word == 'docs':
                os.remove(f"{documents}{second_word}")
                print(f'Removed "{second_word}" in Documents')
            else:
                os.remove(second_word)
                print(f'Removed "{second_word}"')
        elif first_word == 'cd' or first_word == 'changedir':
            os.chdir(second_word)
            print('Current Directory: ' + os.getcwd())
        elif first_word == 'dir' or first_word == 'ls':
            print(os.listdir())
        elif inp == 'exit' or inp == 'close' or inp == 'bye':
            running = False
        elif inp == 'help':
            print(help_message)
        else:
            print(colored('Command Not Found', 'red'))
    except FileNotFoundError:
        print(colored(nodir_warning, 'red'))
    except FileExistsError:
        print(colored(dir_exists_warning, 'red'))
    except OSError:
        print(colored('The directory is not empty', 'red'))
