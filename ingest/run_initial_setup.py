from admin import Admin
from tournament import Tournament

a = Admin()

admin_tbl = a.admin(write_table=True)

current = admin_tbl[admin_tbl['status'] == 'current'].reset_index()

tournament_id = current['tournament_id'][0]
tournament_name = current['tournament_name'][0]

t = Tournament('2024', tournament_name, tournament_id)

field = t.field(write_table=True)
