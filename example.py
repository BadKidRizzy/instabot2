#!/usr/bin/env python
# -*- coding: utf-8 -*-

from instabot import InstaBot

bot = InstaBot(login="zeno_of_elea", password="Madskills101",
               like_per_day=10000,
               comments_per_day=0,
               tag_list=['follow4follow','like4like','rap' ,
                         'hiphop','indierap','shecute','trap','tracks',
                         'microphone','grind','dope','musicislife','phattygirl',
                         'prettybrown','latinadoitbetter','yellowbone'],
               max_like_for_one_tag=100000,
               follow_per_day=0,
               follow_time=5*60*60,
               unfollow_per_day=150,
               unfollow_break_min=15,
               unfollow_break_max=30,
               log_mod=0)

bot.new_auto_mod()
