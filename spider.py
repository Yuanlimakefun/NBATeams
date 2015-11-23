# -*- encoding:utf-8 -*-

import urllib.request
import http.cookiejar
import random
from PIL import Image, ImageTk
import io

class Spider():
    def __init__(self):
        
        # 定义请求头的user_agents列表，模拟浏览器
        user_agents = ['Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
            'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0',
            'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'
        ]

        # 定义一个cookie
        cookie = http.cookiejar.CookieJar()
        # 创建一个opener
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        # 为opener添加请求头，并随机挑选一个user_agent
        self.opener.addheaders = [('User-Agent', random.choice(user_agents))]

    # 请求球队信息首页
    def load_teams_index(self):
        index_response = self.opener.open('http://nbadata.sports.qq.com/team/teams.html', timeout=5)
        index_data = index_response.read().decode('utf-8')
        return index_data

    # 请求球队排名
    def load_teams_ranking(self):
        teams_ranking_response = self.opener.open('http://nbadata.sports.qq.com/rank/teamconference.html', timeout=5)
        teams_ranking_data = teams_ranking_response.read().decode('utf-8')
        return teams_ranking_data

    # 根据team_id请求球队信息
    def load_team_info(self, team_id):
        team_info_response = self.opener.open('http://nbadata.sports.qq.com/team/' + team_id + '/teaminfo.html', timeout=5)
        team_info_data = team_info_response.read().decode('utf-8')
        return team_info_data

    # 加载网络图片
    # 加载失败的话，转为加载一张本地图片
    # Tkinter只支持gif格式，用ImageTk代替
    def load_internet_image(self, url):
        try:
            image_bytes = self.opener.open(url, timeout=5).read()
            data_stream = io.BytesIO(image_bytes)
            image = Image.open(data_stream)
            tk_image = ImageTk.PhotoImage(image)
        except urllib.error.URLError as e:
            image = Image.open('./res/x.png')
            tk_image = ImageTk.PhotoImage(image)

        return tk_image
