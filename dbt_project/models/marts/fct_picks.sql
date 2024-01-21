select 
    user_id, 
    tier1,
    tier2,
    tier3,
    tier4,
    tournament_name,
    tournament_id,
    year,

from {{ ref('stg_picks') }}