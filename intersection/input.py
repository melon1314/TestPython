from model.SpecialInput import SpecialInput

model_list = []


def init_input_model_list():
    input1 = SpecialInput(aliance='Fizz')
    input2 = SpecialInput(aliance='Buzz')
    input3 = SpecialInput(aliance='Whizz')
    global model_list
    model_list.append(input1)
    model_list.append(input2)
    model_list.append(input3)
    return model_list


def clear_model_list():
    global model_list
    model_list = []


def update_model_by_input_list(input_list):
    global model_list
    for index in range(len(input_list)):
        model_list[index].raw_int = int(input_list[index])
    return model_list


def get_model_list():
    return model_list


def input_length_check(list):
    if len(list) == len(model_list):
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

