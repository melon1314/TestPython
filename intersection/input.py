from data.InputData import input_data


def input_length_check(list):
    if len(list) == len(input_data.model_list):
        return True
    else:
        return False


def input_items_check(list):
    for index in list:
        if int(index) > 0 and int(index) < 10 and index.isalnum():
            continue
        else:
            return False
    return True


def input_info():
    print('please input three int numbers(1~100) with space seprated:')
    while True:
        input_str = input()
        input_list = input_str.split(' ')
        if input_length_check(input_list) and input_items_check(input_list):
            input_data.init_input_list(input_list)
            break
        else:
            print('input number or format is incorrect, please re-input again')

