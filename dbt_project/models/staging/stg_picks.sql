select 
    "User ID" as user_id, 
    "Tier 1" as tier1,
    "Tier 2" as tier2,
    "Tier 3" as tier3,
    "Tier 4" as tier4,
    tournament_name,
    tournament_id,
    year

from read_csv_auto({{ source("staging", "picks") }}, header=true)