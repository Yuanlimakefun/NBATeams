# -*- encoding:utf-8 -*-

import re
from models.team_model import TeamModel
from models.player_model import PlayerModel


class Analyzer():
    def __init__(self):
        pass

    # 解析每只球队对应的id和队名
    def analyze_teams_data(self, index_data):
        teams_data = re.findall(r'<h1\s+class="b">\s*<a\s+href="/team/(\d+)/teaminfo.html".*?>(.*?)</a>\s*</h1>', index_data)
        return teams_data

    def analyze_teams_ranking(self, teams_ranking_data):
        ranking_data = re.findall(r'<td><span.*?>(\d+)</span></td>.*?<td><a.*?>(.*?)</a></td>.*?<td>(\d+)</td>.*?<td>(\d+)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>', teams_ranking_data, re.DOTALL)
        return ranking_data

    def analyze_team_info(self, team_info_data):
        team = TeamModel()
        team_name = re.findall(r'<span\s+class="b\s+f14\s+fl">(.*?)</span>', team_info_data, re.DOTALL)
        team.name = team_name[0]
        
        team_data = re.findall(r'<div\s+class="fl\s+w560\s+g3">(.*?)</div>', team_info_data, re.DOTALL)
        team_introduction = re.findall(r'<td.*?>(.*?)</td>', team_data[0])
        team.introduction = team_introduction

        data_box = re.findall(r'<div\s+class="g3\s+databox">(.*?)</div>', team_info_data, re.DOTALL)
        players_info = re.findall(r'<td.*?>(.*?)</td>', data_box[0])
        team.players = []
        for i in range(len(players_info) // 9 - 1):
            player = PlayerModel()
            player_index = 9 * i
            player.number = players_info[player_index+9]

            player_data = re.findall(r'<a\s+href="/player/(\d+)/playerinfo.html".*?>(.*?)</a>', players_info[player_index+10], re.DOTALL)
            player.id = player_data[0][0]
            player.name = player_data[0][1]

            player.position = players_info[player_index+11]
            player.height = players_info[player_index+12]
            player.weight = players_info[player_index+13]
            player.age = players_info[player_index+14]
            player.birthday = players_info[player_index+15]
            player.salary = players_info[player_index+16]
            player.time_enter = players_info[player_index+17]
            team.players.append(player)

        return team

    def analyze_team_data_leader(self, team_info_data):
        team_average = re.findall(r'<span\s+class="b">(.*?)</span>(.*?)</p>\s*<div\s+class="redbox\s+tc">(.*?)</div>', team_info_data, re.DOTALL)
        team_leader = re.findall(r'<div\s+class="fl\s+head".*?>\s*<a.*?>\s*<img\s+src="(.*?)".*?>\s*</a>.*?<h1\s+class="b">(.*?)</h1>.*?<a.*?>(.*?)</a>.*?<p\s+class="mt5">(.*?)</p>', team_info_data, re.DOTALL)
        return (team_average, team_leader)
        
