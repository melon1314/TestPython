from model.BaseInput import BaseInput


class Input1(BaseInput):

    aliance = 'Fizz'

    def __init__(self, raw_int):
        BaseInput.__init__(self, raw_int)

    # 包含关系输出
    def containerOut(self, number):
        if str(number).__contains__(str(self.raw_int)):
            return True


