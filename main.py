from heandlers import *

def main():
    while True:
    
        get_command = input(">>").lower()
        if get_command.startswith('hello'):
            help_handler()
        elif get_command.startswith('add'):
            add_handler(get_command)
        elif get_command.startswith('change'):
            change_handler(get_command)
        elif get_command.startswith('phone'):
            phone_handler(get_command)
        elif get_command.startswith('show all'):
            show_all_handler()
        elif get_command.startswith('good bye') or \
            get_command.startswith('close') or get_command.startswith('exit'):
            bye_handler()
            break
        else: 
            print("Please enter the correct request!")

if __name__ == '__main__':

    main()

    #print(contact_list)