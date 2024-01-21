with unpivot_t as (
    UNPIVOT {{ ref('pickem_leaderboard') }}
    ON tier1_total, tier2_total, tier3_total, tier4_total
), 
row_num_t as (
    select 
    tournament_name, 
    tournament_id, 
    user_id, 
    value, 
    row_number() over (partition by tournament_id, tournament_name, user_id order by value) row_num

    from unpivot_t
)
select tournament_id, tournament_name, user_id, sum(value) as total
from row_num_t
where row_num in (1,2)
group by 1,2,3