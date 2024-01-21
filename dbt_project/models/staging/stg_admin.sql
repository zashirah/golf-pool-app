select 
    tournament_name,
    tournament_id,
    par,
    pot,
    start_time,
    end_time,
    status,
    played,
    winner
    
from read_csv_auto({{ source("staging", "admin") }}, header=true)