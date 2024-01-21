select 
    pos, 
    player[:position('(' in player)-1] as player_name,
    total,
    thru,
    round,
    r1,
    r2,
    r3,
    r4,
    tournament_name,
    tournament_id

from read_csv_auto({{ source("staging", "leaderboard") }}, header=true)