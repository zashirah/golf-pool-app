select 
    tournament_id,
    tournament_name,
    execution_time,
    player_id,
    first_name,
    last_name,
    display_name,
    status,
    owgr
    
from read_csv_auto({{ source('staging', 'field') }}, header=true)