from intersection.input import *


def process_number(number, input_model_list):
    output = ''
    for index in range(len(input_model_list)):
        if index == 0 and input_model_list[index].containerOut(number):
            # 区分处理第一个元素
            output = input_model_list[index].aliance
            break
        else:
            if input_model_list[index].beishuOut(number):
                output += input_model_list[index].aliance

    if not output:
        output = number

    return output


def out_print():
    # 初始化
    init_input_model_list()
    # 输入
    input_list = input_info()
    # 更新
    update_model_by_input_list(input_list)
    print('output:')
    for index in range(1,101):
        result = process_number(index, get_model_list())
        print(result)


# out_print()