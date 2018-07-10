# -*- coding: UTF-8 -*-
class BaseInput():
    raw_int = 0
    aliance = None

    def __init__(self, raw_int):
        self.raw_int = raw_int

    def beishuOut(self, number):
        if int(number)%int(self.raw_int) == 0:
            return True

    def containerOut(self, number):
        return False

    
