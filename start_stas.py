
from start_stas_function import generate_season_for_str, for_first_deal, for_game_stat, sava_season_stats

for i in range(1, 21):
    season_str = generate_season_for_str(i)
    games = for_first_deal(season_str)
    box_score_stats = for_game_stat(games)
    sava_season_stats(box_score_stats, season_str)
pass
