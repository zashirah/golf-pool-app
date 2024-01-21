select 
    s.tournament_name,
    s.tournament_id,
    s.date_range,
    case when upper(a.status) = 'CURRENT' then 'current' else s.status end as status,
    a.pot, 
    a.par


from {{ ref('stg_schedule') }} s
left join {{ ref('stg_admin') }} a
using (tournament_id)

