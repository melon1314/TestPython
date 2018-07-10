from model.BaseInput import BaseInput


class Input2(BaseInput):
    aliance = 'Buzz'

    def __init__(self, raw_int):
        BaseInput.__init__(self, raw_int)



