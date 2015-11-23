# -*- encoding:utf-8 -*-

from tkinter import *
from tkinter.ttk import *
from spider import Spider
from analyzer import Analyzer
import utils

class TeamInfoFrame():
    def __init__(self, master, team_id):
        self.team_info_win = Toplevel(master)
        self.team_info_win.resizable(False, False)
        self.team_id = team_id

        self.spider = Spider()
        team_info_data = self.spider.load_team_info(team_id)

        analyzer = Analyzer()
        self.team_info = analyzer.analyze_team_info(team_info_data)
        (self.team_average, self.team_leader) = analyzer.analyze_team_data_leader(team_info_data)

        self.team_info_win.title(self.team_info.name)

        self.load_team_introduction()
        self.load_team_data()
        self.load_players()

    def load_team_introduction(self):
        team_frame = LabelFrame(self.team_info_win, text=self.team_info.name)
        team_frame.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        team_logo_image = utils.load_team_logo(self.team_id)
        team_logo = Label(team_frame, image=team_logo_image)
        team_logo.grid(row=0, column=0, rowspan=2, padx=5, pady=5)
        team_logo.image = team_logo_image

        Label(team_frame, text=self.team_info.introduction[0], width=30).grid(row=0, column=1, sticky=W, padx=5, pady=5)
        Label(team_frame, text=self.team_info.introduction[1], width=30).grid(row=0, column=2, sticky=W, padx=5, pady=5)
        Label(team_frame, text=self.team_info.introduction[2], width=30).grid(row=0, column=3, sticky=W, padx=5, pady=5)
        Label(team_frame, text=self.team_info.introduction[3], width=30).grid(row=1, column=1, sticky=W, padx=5, pady=5)
        Label(team_frame, text=self.team_info.introduction[4], width=30).grid(row=1, column=2, sticky=W, padx=5, pady=5)
        Label(team_frame, text=self.team_info.introduction[5], width=30).grid(row=1, column=3, sticky=W, padx=5, pady=5)

    def load_team_data(self):
        self.load_points_frame()
        self.load_assists_frame()
        self.load_rebounds_frame()
        self.load_steal_frame()
        self.load_block_frame()
        
        '''team_average_frame = LabelFrame(self.team_info_win)
        team_average_frame.grid(row=1, column=0, padx=5, pady=5)
        Label(team_average_frame, text=self.team_average[0][0] + self.team_average[0][1] + '\n' + self.team_average[0][2]).grid(row=0, column=0)
        Label(team_average_frame, text=self.team_average[1][0] + self.team_average[1][1] + '\n' + self.team_average[1][2]).grid(row=0, column=1)
        Label(team_average_frame, text=self.team_average[2][0] + self.team_average[2][1] + '\n' + self.team_average[2][2]).grid(row=0, column=2)
        Label(team_average_frame, text=self.team_average[3][0] + self.team_average[3][1] + '\n' + self.team_average[3][2]).grid(row=0, column=3)
        Label(team_average_frame, text=self.team_average[4][0] + self.team_average[4][1] + '\n' + self.team_average[4][2]).grid(row=0, column=4)

        team_leader_frame = LabelFrame(self.team_info_win)
        team_leader_frame.grid(row=2, column=0, padx=5, pady=5)
        Label(team_leader_frame, text=self.team_leader[0][0] + '\n' + self.team_leader[0][1] + '\n' + self.team_leader[0][2]).grid(row=1, column=0)
        Label(team_leader_frame, text=self.team_leader[1][0] + '\n' + self.team_leader[1][1] + '\n' + self.team_leader[1][2]).grid(row=1, column=1)
        Label(team_leader_frame, text=self.team_leader[2][0] + '\n' + self.team_leader[2][1] + '\n' + self.team_leader[2][2]).grid(row=1, column=2)
        Label(team_leader_frame, text=self.team_leader[3][0] + '\n' + self.team_leader[3][1] + '\n' + self.team_leader[3][2]).grid(row=1, column=3)
        Label(team_leader_frame, text=self.team_leader[4][0] + '\n' + self.team_leader[4][1] + '\n' + self.team_leader[4][2]).grid(row=1, column=4)'''

    def load_points_frame(self):
        points_frame = LabelFrame(self.team_info_win, text='得分')
        points_frame.grid(row=1, column=0, padx=5, pady=5)

        # 球队得分
        Label(points_frame, text=self.team_average[0][0] + self.team_average[0][1] + '\n' + self.team_average[0][2]).grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # 个人得分
        image = self.spider.load_internet_image(self.team_leader[0][0])
        image_label = Label(points_frame, image=image)
        image_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        image_label.image = image
        Label(points_frame, text=self.team_leader[0][1] + '\n' + self.team_leader[0][2] + '\n' + self.team_leader[0][3]).grid(row=1, column=1, sticky=W, padx=5, pady=5)

    def load_assists_frame(self):
        assists_frame = LabelFrame(self.team_info_win, text='助攻')
        assists_frame.grid(row=1, column=1, padx=5, pady=5)

        Label(assists_frame, text=self.team_average[1][0] + self.team_average[1][1] + '\n' + self.team_average[1][2]).grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        image = self.spider.load_internet_image(self.team_leader[1][0])
        image_label = Label(assists_frame, image=image)
        image_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        image_label.image = image
        Label(assists_frame, text=self.team_leader[1][1] + '\n' + self.team_leader[1][2] + '\n' + self.team_leader[1][3]).grid(row=1, column=1, sticky=W, padx=5, pady=5)

    def load_rebounds_frame(self):
        rebounds_frame = LabelFrame(self.team_info_win, text='篮板')
        rebounds_frame.grid(row=1, column=2, padx=5, pady=5)

        Label(rebounds_frame, text=self.team_average[2][0] + self.team_average[2][1] + '\n' + self.team_average[2][2]).grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        image = self.spider.load_internet_image(self.team_leader[2][0])
        image_label = Label(rebounds_frame, image=image)
        image_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        image_label.image = image
        Label(rebounds_frame, text=self.team_leader[2][1] + '\n' + self.team_leader[2][2] + '\n' + self.team_leader[2][3]).grid(row=1, column=1, sticky=W, padx=5, pady=5)
        
    def load_steal_frame(self):
        steal_frame = LabelFrame(self.team_info_win, text='抢断')
        steal_frame.grid(row=1, column=3, padx=5, pady=5)

        Label(steal_frame, text=self.team_average[3][0] + self.team_average[3][1] + '\n' + self.team_average[3][2]).grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        image = self.spider.load_internet_image(self.team_leader[3][0])
        image_label = Label(steal_frame, image=image)
        image_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        image_label.image = image
        Label(steal_frame, text=self.team_leader[3][1] + '\n' + self.team_leader[3][2] + '\n' + self.team_leader[3][3]).grid(row=1, column=1, sticky=W, padx=5, pady=5)
        
    def load_block_frame(self):
        block_frame = LabelFrame(self.team_info_win, text='盖帽')
        block_frame.grid(row=1, column=4, padx=5, pady=5)

        Label(block_frame, text=self.team_average[4][0] + self.team_average[4][1] + '\n' + self.team_average[4][2]).grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        image = self.spider.load_internet_image(self.team_leader[4][0])
        image_label = Label(block_frame, image=image)
        image_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        image_label.image = image
        Label(block_frame, text=self.team_leader[4][1] + '\n' + self.team_leader[4][2] + '\n' + self.team_leader[4][3]).grid(row=1, column=1, sticky=W, padx=5, pady=5)

    def load_players(self):
        players_frame = LabelFrame(self.team_info_win, text='球员阵容')
        players_frame.grid(row=3, column=0, columnspan=5, padx=5, pady=5)

        players_list = Treeview(players_frame, columns=('0', '1', '2', '3', '4', '5', '6', '7', '8'), show='headings', height=len(self.team_info.players))
        players_list.grid(row=0, column=0)
        players_list.column('0', width=50, anchor='center')
        players_list.column('1', width=150, anchor='center')
        players_list.column('2', width=100, anchor='center')
        players_list.column('3', width=70, anchor='center')
        players_list.column('4', width=70, anchor='center')
        players_list.column('5', width=50, anchor='center')
        players_list.column('6', width=100, anchor='center')
        players_list.column('7', width=100, anchor='center')
        players_list.column('8', width=100, anchor='center')
        players_list.heading('0', text='号码')
        players_list.heading('1', text='球员')
        players_list.heading('2', text='位置')
        players_list.heading('3', text='身高')
        players_list.heading('4', text='体重')
        players_list.heading('5', text='年龄')
        players_list.heading('6', text='生日')
        players_list.heading('7', text='工资(美元)')
        players_list.heading('8', text='进入NBA')

        for player in self.team_info.players:
            players_list.insert('', 'end', value=(player.number, player.name, player.position, player.height,
                                                  player.weight, player.age, player.birthday, player.salary, player.time_enter))
