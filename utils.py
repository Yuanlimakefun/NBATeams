# -*- encoding:utf-8 -*-

from PIL import Image, ImageTk

teams_id_logos = {
            '1': './res/Hawks-1.png',
            '2': './res/Celtics-1.png',
            '3': './res/pelicans-1.png',
            '4': './res/Bulls-1.png',
            '5': './res/Cavaliers-1.png',
            '6': './res/Mavericks-1.png',
            '7': './res/Nuggets-1.png',
            '8': './res/Pistons-1.png',
            '9': './res/Warriors-1.png',
            '10': './res/Rockets-1.png',
            '11': './res/Pacers-1.png',
            '12': './res/Clippers-1.png',
            '13': './res/Lakers-1.png',
            '14': './res/Heat-1.png',
            '15': './res/Bucks-1.png',
            '16': './res/Timberwolves-1.png',
            '17': './res/sBrooklynNets.png',
            '18': './res/Knicks-1.png',
            '19': './res/Magic-1.png',
            '20': './res/76ers-1.png',
            '21': './res/Suns-1.png',
            '22': './res/TrailBlazers-1.png',
            '23': './res/Kings-1.png',
            '24': './res/Spurs-1.png',
            '25': './res/sThunder.png',
            '26': './res/Jazz-1.png',
            '27': './res/Wizards-1.png',
            '28': './res/Raptors-1.png',
            '29': './res/Grizzlies-1.png',
            '5312': './res/Bobcats-1.png'
        }

def load_teams_logos():
    teams_logo = {}
    for team_id in teams_id_logos:
        image = Image.open(teams_id_logos[team_id])
        tk_image = ImageTk.PhotoImage(image)
        teams_logo.setdefault(team_id, tk_image)

    return teams_logo

def load_team_logo(team_id):
    image = Image.open(teams_id_logos[team_id])
    tk_image = ImageTk.PhotoImage(image)
    return tk_image
