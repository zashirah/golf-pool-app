with unpivot_total as (
    UNPIVOT {{ ref('pickem_leaderboard') }}
    ON tier1_total, tier2_total, tier3_total, tier4_total
), 
unpivot_cut as (
    UNPIVOT {{ ref('pickem_leaderboard') }}
    ON tier1_cut, tier2_cut, tier3_cut, tier4_cut
),
total_score as (
    select 
        tournament_name, 
        tournament_id, 
        user_id, 
        value as total,
        row_number() over (partition by tournament_id, tournament_name, user_id order by value) row_num

    from unpivot_total
),
total_top2 as (
    select 
        tournament_id,
        tournament_name,
        user_id,
        sum(total) as score_total

    from total_score
    where row_num in (1,2)
    group by all
),
cut_score as (
    select 
        tournament_id,
        tournament_name,
        user_id,
        sum(value)::TINYINT as cut_total
    from unpivot_cut
    group by all
)
select *

from total_top2
inner join cut_score 
using (tournament_id, tournament_name, user_id)
