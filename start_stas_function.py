import pandas as pd
from bs4 import BeautifulSoup


def generate_season_for_str(start_year):
    """
    生成赛季的字符串
    :param start_year: 赛季开始的年份
    """
    r = '20'
    if start_year < 10:
        r += '0'
    r += str(start_year)
    r += '-'
    if start_year + 1 < 10:
        r += '0'
    r += str(start_year + 1)
    return r


def for_first_deal(season):
    """

    :param season:
    :return:
    """
    soup = BeautifulSoup(open('./stats/{}/Teams Box Scores _ Stats _ NBA.com.html'.format(season),
                              encoding='utf-8'), features='lxml')
    return soup.tbody.find_all(attrs={"data-ng-repeat": "(i, row) in page track by row.$hash"})


def for_game_stat(games_stats_total):
    """

    :param games_stats_total:
    :return:
    """
    r = []
    for game in games_stats_total:
        game_stat = {"team": game.contents[1].text,
                     "opponent": game.contents[3].text[-4:],
                     "date": game.contents[5].text,
                     "min": game.contents[11].text,
                     "win_or_lose": game.contents[9].text,
                     "score": game.contents[13].text,
                     "FGM": game.contents[15].text,
                     "FGA": game.contents[17].text,
                     "FG%": game.contents[19].text,
                     "FG3M": game.contents[21].text,
                     "FG3A": game.contents[23].text,
                     "3P%": game.contents[25].text,
                     "FTM": game.contents[27].text,
                     "FTA": game.contents[29].text,
                     "FT%": game.contents[31].text,
                     "OREB": game.contents[33].text,
                     "DREB": game.contents[35].text,
                     "REB": game.contents[37].text,
                     "AST": game.contents[39].text,
                     "STL": game.contents[41].text,
                     "BLK": game.contents[43].text,
                     "TOV": game.contents[45].text,
                     "PF": game.contents[47].text,
                     "+/-": game.contents[49].text
                     }
        for stat in game_stat:
            game_stat[stat] = game_stat[stat].strip()
        r.append(game_stat)
    return r


def sava_season_stats(score_stats, season):
    """

    :param season:
    :param score_stats:
    """
    print(score_stats)
    season_data = pd.DataFrame(score_stats)
    season_data.to_csv("./stats/{}/{}.csv".format(season, season), mode='w+')