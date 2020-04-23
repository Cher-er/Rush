#敌人类
class enemy(object):
    def __init__(self):
        self.name = ''
        self.lv = 0
        self.hp = 0
        self.mp = 0
        self.attack = 0
        self.defence = 0
        self.speed = 0
    def set(self, lv, hp, mp, attack, defence, speed):
        self.lv = lv
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defence = defence
        self.speed = speed

enemy000 = enemy()
enemy000.set(1,10,0,5,0,10)
enemy000.name = '水滴史莱姆'
