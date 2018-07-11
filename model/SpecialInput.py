# -*- coding: UTF-8 -*-
class SpecialInput():

    def __init__(self, raw_int=0, aliance=None):
        self.raw_int = raw_int
        self.aliance = aliance

    def beishuOut(self, number):

        if self.raw_int!=0 and int(number)%int(self.raw_int) == 0:
            return True

    # 包含关系输出
    def containerOut(self, number):
        if str(number).__contains__(str(self.raw_int)):
            return True

    
