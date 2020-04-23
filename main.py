import tkinter as tk
from enemy import *

#主角
class character(object):
    def __init__(self):
        self.lv = 1
        self.hp = 50
        self.mp = 50
        self.attack = 10
        self.defence = 0
        self.speed = 20
        
        self.equip1 = '无'
        self.equip2 = '无'
        self.equip3 = '无'
        self.equip4 = '无'
        self.equip5 = '无'
        self.equip6 = '无'
    #升级
    def lv_up(self):
        self.lv += 1
        self.hp += 10
        self.mp += 10
        self.attack += 1
        self.defence += 1
    #装备
    def equip_up(self, equip):
        pass

man = character()

def rush():
    #主界面
    window = tk.Tk()
    window.title('主界面')
    window.geometry('500x300')

    #角色按钮对应的函数
    def character():
        #角色界面
        character_win = tk.Tk()
        character_win.title('角色')
        character_win.geometry('500x300')
        #角色界面关闭函数和关闭按钮
        def close_character_win():
            character_win.destroy()
        close_bt = tk.Button(character_win, text = '关闭', width = 7,height = 2, command = close_character_win)
        close_bt.place(x = 30, y = 200, anchor = 'nw')
        #信息显示框
        info_listbox = tk.Listbox(character_win)
        info_listbox.place(x = 200, y = 30, anchor = 'nw')

        #显示属性函数和属性按钮
        def show_attr():
            info_listbox.delete(0, 'end')
            info_listbox.insert('end','等级: ' + str(man.lv))
            info_listbox.insert('end','血量: ' + str(man.hp))
            info_listbox.insert('end','魔法: ' + str(man.mp))
            info_listbox.insert('end','攻击: ' + str(man.attack))
            info_listbox.insert('end','防御: ' + str(man.defence))
            info_listbox.insert('end','速度: ' + str(man.speed))
        attr_bt = tk.Button(character_win, text = '属性', width = 7, height = 2, command = show_attr)
        attr_bt.place(x = 30, y = 30, anchor = 'nw')

        #显示装备函数和装备按钮
        def show_equip():
            info_listbox.delete(0, 'end')
            info_listbox.insert('end','武器: ' + man.equip1)
            info_listbox.insert('end','帽子: ' + man.equip2)
            info_listbox.insert('end','衣服: ' + man.equip3)
            info_listbox.insert('end','手套: ' + man.equip4)
            info_listbox.insert('end','靴子: ' + man.equip5)
            info_listbox.insert('end','戒指: ' + man.equip6)
        equip_bt = tk.Button(character_win, text = '装备', width = 7, height = 2, command = show_equip)
        equip_bt.place(x = 30, y = 90, anchor = 'nw')
    #角色按钮
    character_bt = tk.Button(window, text = '角色', width = 7, height = 2, command = character)
    character_bt.place(x = 30, y = 30, anchor = 'nw')

    #冒险函数
    def adventure():
        pass
    #冒险按钮
    adventure_bt = tk.Button(window, text = '冒险', width = 7, height = 2, command = adventure)
    adventure_bt.place(x = 30, y = 90, anchor = 'nw')


    window.mainloop()

rush()
