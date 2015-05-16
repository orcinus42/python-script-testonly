#coding=utf-8
#!/usr/lib/python2.7
from sys import exit

class dead():
    def __init__(self,why):
        print(why + "愿你在天堂愉快！！！再见~")
    exit(0)
    


class gold_room(dead): 
    '黄金屋'

    def __init__(self):
        print('这个房间里到处都是黄金，你想拿走多少？')
        next = input('> ')
        if '0' in next or '1' in next:
            how_much = int(next)
        else:
            super(gold_room,self).__init__("连个数字都不会，去死吧！")
            # dead("连个数字都不会，去死吧！")

        if how_much < 50:
            print('算你不贪，你走吧！')
        else:
            super(gold_room,self).__init__('算你不贪，你走吧！')
            # dead('贪心不足蛇吞象，去死吧！')



class bear_room():
    '熊屋'
    print('''欢迎进入熊屋！
屋子里有一只熊。
熊的旁边有一罐蜂蜜.
屋子深入有一扇门店，不过门前有一只大胖熊.
此时此刻，你打打算怎么办？[1-拿走蜂蜜],[2-嘲笑大熊],[3-嘲笑小熊],[4-开门]''')
    def __init__(self):
        self.bear_moved = False
        self.dead = dead()

        while True:
            next = input('> ')
            if next == '1':
                self.dead.dead('你被熊一把掌扇死了！')
            elif next == '2' and not self.bear_moved:
                print('大胖熊从门边走开，你现在可以通过此门.')
                self.bear_moved = True
            elif next == '3' and self.bear_moved:
                self.dead.dead('小熊发怒把你的头一口吞下！')
            elif next == '4' and self.bear_moved:
                # 进入黄金屋
                in_gold_room = gold_room()
                gold_room.__init__()
            else:
                print('小熊把蜂蜜吃完了！')



class cthulhu_room():
    '火神克苏鲁屋'
    print('''在这里你遇到了邪恶的火神克鲁苏！！！
不管是人是鬼，谁见到他非死即伤~
你是[1-逃命]还是[2-自杀]？''')

    def __init__(self):
        self.dead = dead()
        next = input('> ')
        if next == '1':
            # 开始游戏
            start()
        elif next == '2':
            self.dead.dead('自杀身亡！')
        else:
            # '火神克苏鲁屋'
            self.__init__()




def start():
    print('''
你现在身处一个漆黑的房间.
你的左右边各有一扇门.
你选择打开哪一扇门？[1-左],[2-右]
''')
    next = input('> ')
    if next == '1':
        # 熊屋
        in_bear_room = bear_room()
        in_bear_room.__init__()
    elif next == '2':
        # 火神克苏鲁屋
        in_cthulhu_room = cthulhu_room()
        in_cthulhu_room.__init__()
    else:
        # dead('你被困在屋子里最后饿死.')
        is_dead = dead()
        dead.__init__('你被困在屋子里最后饿死.')



start()


        
