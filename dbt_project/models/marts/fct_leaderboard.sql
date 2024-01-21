select 
    l.pos, 
    l.player_name,
    l.total,
    l.thru,
    l.round,
    l.r1,
    l.r2,
    l.r3,
    l.r4,
    l.tournament_name,
    l.tournament_id,
    a.status, 
    a.par,
    f.player_id
    
from {{ ref('stg_leaderboard') }} l
inner join {{ ref('stg_admin') }} a
using (tournament_id)
left join {{ ref('fct_field') }} f
on l.player_name = f.player_name