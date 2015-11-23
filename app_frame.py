# -*- encoding:utf-8 -*-

from tkinter import *
from tkinter.ttk import *
from spider import Spider
from analyzer import Analyzer
import utils
from team_info_frame import TeamInfoFrame


class AppFrame:
    def __init__(self, master):
        self.master = master
        
        east_group = LabelFrame(master, text='东部')
        east_group.grid(row=0, column=0, padx=5, pady=5)
        west_group = LabelFrame(master, text='西部')
        west_group.grid(row=1, column=0, padx=5, pady=5)
        
        # 东部排名
        east_ranking = LabelFrame(master, text='东部排名')
        east_ranking.grid(row=0, column=1, rowspan=2, padx=5, pady=5, sticky=N)
        self.east_ranking_list = self.creat_teams_ranking_list(east_ranking)

        # 西部排名
        west_ranking = LabelFrame(master, text='西部排名')
        west_ranking.grid(row=0, column=2, rowspan=2, padx=5, pady=5, sticky=N)
        self.west_ranking_list = self.creat_teams_ranking_list(west_ranking)

        # 东部
        atlantic_group = LabelFrame(east_group, text='大西洋区')
        atlantic_group.grid(row=0, column=0, padx=5, pady=5)
        central_group = LabelFrame(east_group, text='中部区')
        central_group.grid(row=0, column=1, padx=5, pady=5)
        southeast_group = LabelFrame(east_group, text='东南区')
        southeast_group.grid(row=0, column=2, padx=5, pady=5)

        # 西部
        pacific_group = LabelFrame(west_group, text='太平洋区')
        pacific_group.grid(row=1, column=0, padx=5, pady=5)
        southwest_group = LabelFrame(west_group, text='西南区')
        southwest_group.grid(row=1, column=1, padx=5, pady=5)
        northwest_group = LabelFrame(west_group, text='西北区')
        northwest_group.grid(row=1, column=2, padx=5, pady=5)


        spider = Spider()
        index_data = spider.load_teams_index()
        teams_ranking_data = spider.load_teams_ranking()

        analyzer = Analyzer()
        teams_data = analyzer.analyze_teams_data(index_data)
        self.teams_ranking = analyzer.analyze_teams_ranking(teams_ranking_data)

        self.load_teams_ranking()

        self.teams_logo = utils.load_teams_logos()
        self.load_group(atlantic_group, teams_data[0:5])
        self.load_group(pacific_group, teams_data[5:10])
        self.load_group(central_group, teams_data[10:15])
        self.load_group(southwest_group, teams_data[15:20])
        self.load_group(southeast_group, teams_data[20:25])
        self.load_group(northwest_group, teams_data[25:30])

    def creat_teams_ranking_list(self, parent_frame):
        ranking_list = Treeview(parent_frame, columns=('0', '1', '2', '3', '4', '5'), show='headings', height=15)
        ranking_list.grid(row=0, column=0, padx=5, pady=14)
        ranking_list.column('0', width=35, anchor='center')
        ranking_list.column('1', width=70, anchor='center')
        ranking_list.column('2', width=35, anchor='center')
        ranking_list.column('3', width=35, anchor='center')
        ranking_list.column('4', width=45, anchor='center')
        ranking_list.column('5', width=40, anchor='center')
        ranking_list.heading('0', text='排名')
        ranking_list.heading('1', text='球队')
        ranking_list.heading('2', text='胜')
        ranking_list.heading('3', text='负')
        ranking_list.heading('4', text='胜率')
        ranking_list.heading('5', text='胜差')

        return ranking_list

    def load_group(self, parent_frame, teams_data):
        row_index = 0
        for team in teams_data:
            team_logo = Label(parent_frame, image=self.teams_logo[team[0]])
            team_logo.grid(row=row_index, column=0, rowspan=2, padx=5, pady=2)
            team_logo.image = self.teams_logo[team[0]]
            
            team_name_label = Label(parent_frame, text=team[1], cursor='hand2')
            team_name_label.grid(row=row_index, column=1, columnspan=5, sticky=W)
            team_name_label.bind('<Button-1>', self.handler_adaptor(self.view_team_info, team_id=team[0]))
            
            statistics_label = Label(parent_frame, text='统计', cursor='hand2')
            statistics_label.grid(row=row_index+1, column=1)
            statistics_label.bind('<Button-1>', self.handler_adaptor(self.view_team_info, team_id=team[0]))
            
            Label(parent_frame, text='|').grid(row=row_index+1, column=2)
            
            Label(parent_frame, text='赛程', cursor='hand2').grid(row=row_index+1, column=3)
            

            Label(parent_frame, text='|').grid(row=row_index+1, column=4)
            
            players_label = Label(parent_frame, text='阵容', cursor='hand2')
            players_label.grid(row=row_index+1, column=5)
            players_label.bind('<Button-1>', self.handler_adaptor(self.view_team_info, team_id=team[0]))

            Label(parent_frame, text='|').grid(row=row_index+1, column=6)
            Label(parent_frame, text='转会', cursor='hand2').grid(row=row_index+1, column=7)
            Label(parent_frame, text='|').grid(row=row_index+1, column=8)
            Label(parent_frame, text='伤病', cursor='hand2').grid(row=row_index+1, column=9)

            row_index += 2

    def load_teams_ranking(self):
        for ranking in self.teams_ranking[0:15]:
            self.east_ranking_list.insert('', 'end', value=ranking)

        for ranking in self.teams_ranking[15:30]:
            self.west_ranking_list.insert('', 'end', value=ranking)

    def handler_adaptor(self, fun, **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

    def view_team_info(self, event, team_id):
        TeamInfoFrame(self.master, team_id)
        
