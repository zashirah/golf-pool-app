with field as (
    select *
    from {{ ref('stg_field') }}
),
tier_levels as (
    select 
        tournament_name, tournament_id,
        quantile_cont(owgr, .05) tier1_max, 
        quantile_cont(owgr, .25) tier2_max, 
        quantile_cont(owgr, .5) tier3_max

    from field

    group by all
)

select 
    f.tournament_name,
    f.execution_time,
    f.player_id,
    f.first_name,
    f.last_name,
    f.display_name,
    f.first_name || ' ' || f.last_name as player_name,
    f.status,
    f.owgr,
    tl.tier1_max,
    tl.tier2_max,
    tl.tier3_max,
    case 
        when f.owgr <= tl.tier1_max then 'tier 1'
        when f.owgr <= tl.tier2_max then 'tier 2'
        when f.owgr <= tl.tier3_max then 'tier 3'
    else 'tier 4' end as pickem_tier
    
from field f
inner join tier_levels tl
using (tournament_name)
