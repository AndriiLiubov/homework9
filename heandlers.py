import sys

contact_list = {}

def input_error(func):
    def inner(*args):
        try:
            func(*args)
        except ValueError:
            print("Give me the correct phone number")
        except IndexError:
            print("Give me name and phone please")
        except KeyError:
            print("Give me the name from the contact list")
    return inner

def help_handler():
    sys.stdout.write("How can I help you?\n")

@input_error
def add_handler(command):
    raw_command = command.removeprefix('add ')
    user_data = raw_command.split(' ')
    contact_list.update({user_data[0]:int(user_data[1])})

@input_error
def change_handler(command):
    raw_command = command.removeprefix('change ')
    user_data = raw_command.split(' ')
    contact_list.update({user_data[0]:int(user_data[1])})

@input_error
def phone_handler(command):
    raw_command = command.removeprefix('phone ')
    print(contact_list.get(raw_command), get_error())

def show_all_handler():
    print(contact_list)

def bye_handler():
    sys.stdout.write("Good bye!\n")

def get_error():
    raise KeyError
    

if __name__ == '__main__':

    help_handler()
    add_handler()
    change_handler()
    phone_handler()
    show_all_handler()
    bye_handler()