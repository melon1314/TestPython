from model.BaseInput import BaseInput


class Input3(BaseInput):

    aliance = 'Whizz'

    def __init__(self, raw_int):
        BaseInput.__init__(self, raw_int)

