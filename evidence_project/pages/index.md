```sql field
    select *
    from golf.field
    where tournament_name  = '${inputs.tournament_name_filter}'
```
```sql field_t1
    select *
    from golf.field
    where tournament_name  = '${inputs.tournament_name_filter}'
    and pickem_tier = 'tier 1' 
    order by owgr
```
```sql field_t2
    select *
    from golf.field
    where tournament_name  = '${inputs.tournament_name_filter}'
    and pickem_tier = 'tier 2' 
    order by owgr
```
```sql field_t3
    select *
    from golf.field
    where tournament_name  = '${inputs.tournament_name_filter}'
    and pickem_tier = 'tier 3' 
    order by owgr
```
```sql field_t4
    select *
    from golf.field
    where tournament_name  = '${inputs.tournament_name_filter}'
    and pickem_tier = 'tier 4' 
    order by owgr
```
```sql tournament_list
    select *
    from golf.tournaments
```
```sql tournament_details
    select status, pot, par
    from golf.tournaments
    where tournament_name = '${inputs.tournament_name_filter}'
```
```sql leaderboard
    select distinct *
    from golf.leaderboard
    where tournament_name = '${inputs.tournament_name_filter}'
    order by total
```
```sql pickem_leaderboard
    select 
        l.*,
        case when cut_total <= 2 then lt.score_total else 'CUT' end as total

    from golf.pickem_leaderboard l
    inner join golf.pickem_leaderboard_total lt
    using (tournament_id, user_id)
    where l.tournament_name = '${inputs.tournament_name_filter}'
    order by total
```
```sql picks
    select *
    from golf.picks
    where tournament_name = '${inputs.tournament_name_filter}'
```
```sql picks_contextualized
    select *
    from golf.picks_contextualized
    where tournament_name = '${inputs.tournament_name_filter}'
```

<Dropdown
    data={tournament_list} 
    defaultValue='WM Phoenix Open'
    name=tournament_name_filter
    value=tournament_name
    title='Tournament:'
/>

# {inputs.tournament_name_filter}

### Tournament Status: <Value data={tournament_details} column=status/>
### Tournament Pot: <Value data={tournament_details} column=pot/>
### Tournament Par: <Value data={tournament_details} column=par/>


<Tabs>
    <Tab label="Pickem Leaderboard">

        <DataTable data={pickem_leaderboard}>
            <Column id='user_id'/>
            <Column id='total'/>
            <Column id='tier1_pick'/>
            <Column id='tier1_total'/>
            <Column id='tier2_pick'/>
            <Column id='tier2_total'/>
            <Column id='tier3_pick'/>
            <Column id='tier3_total'/>
            <Column id='tier4_pick'/>
            <Column id='tier4_total'/>
        </DataTable>
        <Alert status="info">
            If there is no data in this table, that is because the tournament hasn't started or started recently
        </Alert>
        
    </Tab>
    <Tab label="Picks">

        <DataTable data={picks_contextualized}>
            <Column id='user_id'/>
            <Column id='tier1_pick'/>
            <Column id='tier2_pick'/>
            <Column id='tier3_pick'/>
            <Column id='tier4_pick'/>
        </DataTable>
    </Tab>

    <Tab label="Field / Tiers">
        <Tabs>
            <Tab label="Tier 1">

                <DataTable data={field_t1} search=true>
                    <Column id="player_id"/>
                    <Column id="first_name"/>
                    <Column id="last_name"/>
                    <Column id="owgr" title="Official World Golf Ranking"/>
                    <Column id="status"/>
                </DataTable>
            </Tab>
            <Tab label="Tier 2">

                <DataTable data={field_t2} search=true>
                    <Column id="player_id"/>
                    <Column id="first_name"/>
                    <Column id="last_name"/>
                    <Column id="owgr" title="Official World Golf Ranking"/>
                    <Column id="status"/>
                </DataTable>
            </Tab>

            <Tab label="Tier 3">

                <DataTable data={field_t3} search=true>
                    <Column id="player_id"/>
                    <Column id="first_name"/>
                    <Column id="last_name"/>
                    <Column id="owgr" title="Official World Golf Ranking"/>
                    <Column id="status"/>
                </DataTable>
            </Tab>

            <Tab label="Tier 4">

                <DataTable data={field_t4} search=true>
                    <Column id="player_id"/>
                    <Column id="first_name"/>
                    <Column id="last_name"/>
                    <Column id="owgr" title="Official World Golf Ranking"/>
                    <Column id="status"/>
                </DataTable>
            </Tab>
        </Tabs>
    </Tab>

    <Tab label="Tournament Leaderboard">

        <DataTable data={leaderboard} search=true>
            <Column id="Pos"/>
            <Column id="player_name"/>
            <Column id="Thru"/>
            <Column id="R1"/>
            <Column id="R2"/>
            <Column id="R3"/>
            <Column id="R4"/>
            <Column id="Total"/>
        </DataTable>
        <Alert status="info">
            If there is no data in this table, that is because the tournament hasn't started or started recently
        </Alert>
    </Tab>
</Tabs>
