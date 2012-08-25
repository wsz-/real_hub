# -*- coding: cp936 -*-
import random
st=['st','jz']
jz=['jz','bu']
bu=['bu','st']
mapp={
    'st':st,
    'jz':jz,
    'bu':bu}
user=str(raw_input("输入：st,jz,bu"))
computer=random.sample(['st','bu','jz'],1)[0]
print computer
print mapp[user][0]==mapp[computer][0] and 'equal' or mapp[user][1]==mapp[computer][1]
