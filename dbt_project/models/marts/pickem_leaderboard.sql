select distinct
    p.tournament_id, 
    p.tournament_name,
    p.user_id,
    l1.player_name as tier1_pick,
    l1.total::TINYINT as tier1_total,
    case when upper(l1.pos) in ('WD', 'CUT') then 1 else 0 end as tier1_cut,
    l2.player_name as tier2_pick,
    l2.total::TINYINT as tier2_total,
    case when upper(l2.pos) in ('WD', 'CUT') then 1 else 0 end as tier2_cut,
    l3.player_name as tier3_pick,
    l3.total::TINYINT as tier3_total,
    case when upper(l3.pos) in ('WD', 'CUT') then 1 else 0 end as tier3_cut,
    l4.player_name as tier4_pick,
    l4.total::TINYINT as tier4_total,
    case when upper(l4.pos) in ('WD', 'CUT') then 1 else 0 end as tier4_cut

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