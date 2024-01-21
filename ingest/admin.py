import pandas as pd
import json

class Admin:
    def __init__(self):
        self.sheet_id = '1_RYlJyHSRGYDIggI9TJ9fKJILz2I9wWmIOe2ra5exQY'
        self.sheet_name = 'Admin'
        self.url = f"https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={self.sheet_name}"


    def write_table(self, df):
        df.to_csv('admin.csv', index=False)

    def admin(self, write_table=False):
        df = pd.read_csv(self.url, header=0)

        if write_table:
            self.write_table(df)

        return df
        