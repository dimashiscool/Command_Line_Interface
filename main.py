import command

with open('C:/Users/User/PycharmProjects/Command Line Interface/secretpassword.txt', 'r') as password_file:
    password = password_file.read()
    userinput = input('Enter Password: ')
    if userinput == password:
        command.command_line()
    else:
        print(f"Password: '{userinput}' incorrect\t")
    password_file.close()
