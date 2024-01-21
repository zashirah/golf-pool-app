select distinct
    p.tournament_id, 
    p.tournament_name,
    p.user_id,
    l1.player_name as tier1_pick,
    l1.total as tier1_total,
    l2.player_name as tier2_pick,
    l2.total as tier2_total,
    l3.player_name as tier3_pick,
    l3.total as tier3_total,
    l4.player_name as tier4_pick,
    l4.total as tier4_total

from {{ ref('fct_picks') }} p
inner join {{ ref('fct_leaderboard') }} l1 
on p.tier1 = l1.player_id
and p.tournament_id = l1.tournament_id
inner join {{ ref('fct_leaderboard') }} l2
on p.tier2 = l2.player_id
and p.tournament_id = l2.tournament_id
inner join {{ ref('fct_leaderboard') }} l3
on p.tier3 = l3.player_id
and p.tournament_id = l3.tournament_id
inner join {{ ref('fct_leaderboard') }} l4
on p.tier4 = l4.player_id
and p.tournament_id = l4.tournament_id