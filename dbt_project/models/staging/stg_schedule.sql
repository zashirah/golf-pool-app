select 
    tournament_name,
    tournament_id,
    date as date_range,
    status

from read_csv_auto({{ source('staging', 'schedule') }}, header=true)