from model.Input1 import Input1
from model.Input2 import Input2
from model.Input3 import Input3


def input_length_check(list):
    if len(list) == 3:
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
            return input_list
        else:
            print('input number or format is incorrect, please input again')


def get_input_model(input_list):
    input_model_list = []
    input1 = Input1(int(input_list[0]))
    input_model_list.append(input1)
    input2 = Input2(int(input_list[1]))
    input_model_list.append(input2)
    input3 = Input3(int(input_list[2]))
    input_model_list.append(input3)
    return input_model_list