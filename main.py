from heandlers import *


commands = {
    
    'hello': help_handler,
    'add' : add_handler,
    'change': change_handler,
    'phone' : phone_handler,
    'show': show_all_handler,
    'good': bye_handler,
    'close': bye_handler,
    'exit': bye_handler,
}


def get_handler(command):
    return commands[command]


def main():
    while True:
        get_command = input(">>").lower()
        sep_com = get_command.split(' ')
        if get_command.startswith('hello') or get_command.startswith('add') or \
            get_command.startswith('change') or get_command.startswith('phone') or \
            get_command.startswith('show all') or get_command.startswith('good bye') or \
            get_command.startswith('close') or get_command.startswith('exit'):
                handler = get_handler(sep_com[0])
                if sep_com[0] in ['add', 'change']:
                    print(handler(get_command))
                elif sep_com[0] == 'phone':
                    print(handler(get_command))
                elif sep_com[0] in ['hello', 'show']:
                    print(handler())
                elif sep_com[0] in ['good', 'close', 'exit']:
                    print(handler())
                    break
        else:
            print("Give me correct command")
        




if __name__ == '__main__':

    main()

    #print(contact_list)
