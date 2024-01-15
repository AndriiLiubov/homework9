contact_list = {}

def input_error(func):
    
    error_v = "Give me correct number"
    error_i = "Give me name and phone"
    error_k = "Give me name"
    
    def inner(*args):

        try:
            return func(*args)
        except ValueError:
            return error_v
        except IndexError:
            return error_i
        except KeyError:
            return error_k
    return inner


def help_handler():
    hello = "How can I help you?"
    return hello


@input_error
def add_handler(command):
    raw_command = command.removeprefix('add ')
    user_data = raw_command.split(' ')
    for key in contact_list:
        if key == user_data[0]:
            message = "Contact already exists"
            return message
    contact_list.update({user_data[0]:int(user_data[1])})
    message = "Contact has been added"
    return message



@input_error
def change_handler(command):
    raw_command = command.removeprefix('change ')
    user_data = raw_command.split(' ')
    for key in contact_list:
        if key == user_data[0]:
            contact_list[key] = int(user_data[1])
            message = "Contact has been changed"
            return message
    raise KeyError


@input_error
def phone_handler(command):
    raw_command = command.removeprefix('phone ')
    user_data = raw_command.split(' ')
    return contact_list.get(user_data[0])



def show_all_handler():
    return contact_list


def bye_handler():
    bye = "Good bye!"
    return bye
    

if __name__ == '__main__':

    help_handler()
    add_handler()
    change_handler()
    phone_handler()
    show_all_handler()
    bye_handler()