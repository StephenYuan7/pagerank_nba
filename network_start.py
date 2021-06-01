
from networkx import in_degree_centrality

from start_stas_function import generate_season_for_str
import networkx as nx
from matplotlib import pyplot as plt
import csv


def season_csv_read(season='2020-21'):
    """

    :param season: 具体哪个赛季
    :return:
    """
    file = csv.reader(open('./csv_stat_by_season/{}.csv'.format(season), 'r'))
    r = []
    for stat in file:
        r.append(stat)
    return r


def get_teams_name(stats):
    """

    :param stats:
    """
    teams_name = set()
    for stat in stats:
        teams_name.add(stat[1])
        if len(teams_name) == 31:
            break
    teams_name.discard('team')
    return list(teams_name)


def get_start_network(stats, roll_self):
    """

    :param roll_self:
    :param stats:
    """
    r = nx.DiGraph()
    for stat in stats:
        if stat[1] != 'team':
            r.add_edge(stat[2], stat[1], weight=0)
            r.add_edge(stat[1], stat[1], weight=roll_self)
    return r


def get_win_network(stats, roll_self):
    """

    :param stats: 读取的数据
    """
    r = get_start_network(stats, roll_self)
    stats_len = len(stats)
    now = 0
    for stat in stats:
        now += 1
        if stat[1] != 'team':
            r[stat[2]][stat[1]]['weight'] += get_weight(now, stat, stats_len)
    for stat in stats:
        if stat[1] != 'team':
            if r.has_edge(stat[2], stat[1]) and r[stat[2]][stat[1]]['weight'] < 0:
                r.remove_edge(stat[2], stat[1])
    return r


def get_weight(now, stat, stats_len):
    """

    :param now:
    :param stat:
    :param stats_len:
    :return: 计算边的权值的函数
    """
    # r = max(int(stat[-1]), 10) * (now / stats_len)
    r = int(stat[-1])
    return r


def pagerank_initail():
    champion = ['LAL', 'SAS', 'DET', 'SAS', 'MIA', 'SAS', 'BOS', 'LAL', 'LAL', 'DAL',
                'MIA', 'MIA', 'SAS', 'GSW', 'CLE', 'GSW', 'GSW', 'TOR', 'LAL']
    best_roll = [0, 500]
    for self_roll in range(950, 951):
        loss = 0
        for i in range(1, 20):
            season_str = generate_season_for_str(i)
            print(season_str)
            season_stat = season_csv_read(season_str)
            g = get_win_network(season_stat, self_roll)
            pr = nx.pagerank(g)
            sort_pr = sorted(zip(pr.values(), pr.keys()), reverse=True)
            sort_pr = [s[1] for s in sort_pr]
            loss += sort_pr.index(champion[i-1])
            node_size_by_pr = []
            for node, pageRankValue in pr.items():
                g.nodes[node]['pr'] = pageRankValue
                node_size_by_pr.append(pageRankValue*5000)

            print(sorted(zip(pr.values(), pr.keys()), reverse=True))
            nx.draw(g, with_labels=True, node_size=node_size_by_pr)
            plt.savefig('./image_by_pr/{}.jpg'.format(season_str))
            plt.show()
            node = get_teams_name(season_stat)
            g.add_nodes_from(node)
        if loss < best_roll[1]:
            best_roll[0] = self_roll
            best_roll[1] = loss
        print(best_roll, [self_roll, loss])


def centrality():
    """
        计算简单的中心性
    """
    for i in range(1, 20):
        season_str = generate_season_for_str(i)
        print(season_str)
        season_stat = season_csv_read(season_str)
        g = get_win_network(season_stat, -1)
        nx.draw(g, with_labels=True)
        plt.savefig('./image_start/{}.jpg'.format(season_str))
        plt.show()

        in_degree = in_degree_centrality(g)
        node_size_by_in_degree = []
        for node, in_degree_num in in_degree.items():
            g.nodes[node]['in_degree'] = in_degree_num
            node_size_by_in_degree.append(in_degree_num * 500)

        print("in_degree:")
        print(sorted(zip(in_degree.values(), in_degree.keys()), reverse=True))
        nx.draw(g, with_labels=True, node_size=node_size_by_in_degree)
        plt.savefig('./image_by_in_degree/{}.jpg'.format(season_str))
        plt.show()

        katz_centrality = nx.katz_centrality_numpy(g)
        node_size_by_katz_centrality = []
        for node, katz_centrality_num in katz_centrality.items():
            g.nodes[node]['katz_centrality'] = katz_centrality_num
            node_size_by_katz_centrality.append(katz_centrality_num * 1000)

        print("katz_centrality:")
        print(sorted(zip(katz_centrality.values(), katz_centrality.keys()), reverse=True))
        nx.draw(g, with_labels=True, node_size=node_size_by_katz_centrality)
        plt.savefig('./image_by_katz_centrality/{}.jpg'.format(season_str))
        plt.show()




def goal_diff(stats):
    """
    构建初始网络
    首先计算净胜分
    :param stats:
    """
    r = get_start_network(stats, 0)
    teams_name = get_teams_name(stats)
    stats_len = len(stats)
    games_num = get_games_num(stats)
    now = 0
    for stat in stats:
        now += 1
        if stat[1] != 'team':
            r[stat[2]][stat[1]]['weight'] += get_weight(now, stat, stats_len)
    for team_a in teams_name:
        r.nodes[team_a]['srs'] = 0
        r.nodes[team_a]['srs_next'] = 0
        for team_b in teams_name:
            if r.has_edge(team_b, team_a):
                r.nodes[team_a]['srs'] += r[team_b][team_a]['weight']
        r.nodes[team_a]['srs'] /= games_num
    return r


def get_games_num(stats):
    """
    获取比赛数目
    :param stats:
    :return:
    """
    return len(stats) / len(get_teams_name(stats))


def min_max_norm(stats):
    """
    归一化
    :param stats:
    """
    s_min = min(stats)
    s_max = max(stats)
    max_min = s_max - s_min
    r = []
    for i in stats:
        r.append((i-s_min)/max_min)
    return r


def srs():
    """
    计算SRS值
    """
    for i in range(1, 20):
        season_str = generate_season_for_str(i)
        print(season_str)
        season_stat = season_csv_read(season_str)
        g = goal_diff(season_stat)
        for j in range(10000):
            diff = []
            for team in g.nodes:
                diff.append(abs(g.nodes[team]['srs'] - g.nodes[team]['srs_next']))
            if sum(diff) < 1e-6:
                break
            games_num = get_games_num(season_stat)
            for team_a in g.nodes:
                g.nodes[team_a]['srs'] = g.nodes[team_a]['srs_next']
                g.nodes[team_a]['srs_next'] = 0
            for team_a in g.nodes:
                for team_b in g.nodes:
                    if g.has_edge(team_b, team_a):
                        g.nodes[team_a]['srs_next'] += g[team_b][team_a]['weight']+g.nodes[team_b]['srs']
                g.nodes[team_a]['srs_next'] /= games_num
        srs_num = {}
        node_side_by_srs = []
        for team in g.nodes:
            srs_num[team] = g.nodes[team]['srs']
            node_side_by_srs.append(g.nodes[team]['srs'])
        node_side_by_srs = min_max_norm(node_side_by_srs)
        for node in range(len(node_side_by_srs)):
            node_side_by_srs[node] = (node_side_by_srs[node]+0.01)*500
        print(sorted(zip(srs_num.values(), srs_num.keys()), reverse=True))
        for team_a in g.nodes:
            for team_b in g.nodes:
                if g.has_edge(team_b, team_a) and g[team_b][team_a]['weight'] <= 10:
                    g.remove_edge(team_b, team_a)
        nx.draw_spring(g, with_labels=True, node_size=node_side_by_srs)
        plt.savefig('./image_by_srs/{}.jpg'.format(season_str))
        plt.show()


centrality()
