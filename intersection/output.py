from intersection.input import *


def process_number(number, input_model_list):
    output = ''
    for input_model in input_model_list:
        if input_model.containerOut(number):
            output = input_model.aliance
            break
        elif input_model.beishuOut(number):
            output += input_model.aliance
    if not output:
        output = number

    return output


def out_print():
    input_list = input_info()
    input_model_list = get_input_model(input_list)
    print('output:')
    for index in range(1,101):
        result = process_number(index, input_model_list)
        print(result)


out_print()