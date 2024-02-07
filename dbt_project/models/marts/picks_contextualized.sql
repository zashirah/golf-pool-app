select distinct
    p.tournament_id, 
    p.tournament_name,
    p.user_id,
    l1.player_name as tier1_pick,
    l2.player_name as tier2_pick,
    l3.player_name as tier3_pick,
    l4.player_name as tier4_pick,

from {{ ref('fct_picks') }} p
left join {{ ref('fct_field') }} l1 
on p.tier1 = l1.player_id
and p.tournament_id = l1.tournament_id
left join {{ ref('fct_field') }} l2
on p.tier2 = l2.player_id
and p.tournament_id = l2.tournament_id
left join {{ ref('fct_field') }} l3
on p.tier3 = l3.player_id
and p.tournament_id = l3.tournament_id
left join {{ ref('fct_field') }} l4
on p.tier4 = l4.player_id
and p.tournament_id = l4.tournament_id