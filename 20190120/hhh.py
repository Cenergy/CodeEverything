# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '21/1/2019 4:01 PM'

import random

class WinningPrize:
    def __init__(self,chance,playTime,N):
        self.chance=chance
        self.playTime=playTime
        self.N=N
        self.wins=0

    def run(self):
        for i in range(self.N):
            if self.play():
                self.wins=self.wins+1
        return ("rate",str(float(self.wins/self.N)))
    def play(self):
        for i in range(self.playTime):
            x=random.random()
            if x<self.chance:
                return True
        return False




if __name__ == '__main__':
    exp=WinningPrize(0.2,10,1000000)
    print(':'.join(list(exp.run())))