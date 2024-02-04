import pandas as pd
import json
from urllib import parse

class Picks:
    def __init__(self, year, tournament_name, tournament_id):
        self.sheet_id = '1_RYlJyHSRGYDIggI9TJ9fKJILz2I9wWmIOe2ra5exQY'
        self.year = year
        self.tournament_name = tournament_name
        self.tournament_id = tournament_id
        self.sheet_name = parse.quote(self.tournament_name)
        print(self.sheet_name)
        self.url = f"https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={self.sheet_name}"

    def write_table(self, df):
        df.to_csv(f'picks_{self.tournament_name}_{self.year}.csv', index=False)

    def picks(self, write_table=False):
        df = pd.read_csv(self.url)

        df['tournament_name'] = self.tournament_name
        df['tournament_id'] = self.tournament_id
        df['year'] = self.year

        if write_table:
            self.write_table(df)

        return df
        