from datetime import datetime
import requests
import pandas as pd

class Tournament:
    def __init__(self, year, tournament_name, tournament_id):
        self.X_API_KEY = "da2-gsrx5bibzbb4njvhl7t37wqyl4"
        self.year = year
        self.tournament_name = tournament_name
        self.tournament_id = tournament_id
        self.execution_time = datetime.now()


    def write_table(self, df, object_type):
        df.to_csv(f'{object_type}_{self.tournament_name}_{self.year}.csv', index=False)


    def write_raw(self, data):
        with open(f'{self.tournament_name}_{object_type}_{self.year}.json', 'w') as f:
            json.dump(data, f)


    def leaderboard(self, write_table=False):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.chrome.options import Options

        def set_chrome_options():
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_prefs = {}
            chrome_options.experimental_options["prefs"] = chrome_prefs
            chrome_prefs["profile.default_content_settings"] = {"images": 2}
            return chrome_options
        
        driver = webdriver.Chrome(options=set_chrome_options())

        # load page
        driver.get(f"https://www.pgatour.com/tournaments/{self.year}/{self.tournament_name.lower().replace(' ','-')}/{self.tournament_id}/leaderboard")

        # get table
        table = driver.find_element(By.CSS_SELECTOR, "table.chakra-table")
        assert table, "table not found"

        # remove empty rows
        driver.execute_script("""arguments[0].querySelectorAll("td.css-1au52ex").forEach((e) => e.parentElement.remove())""", table)

        # get html of the table
        table_html = table.get_attribute("outerHTML")

        # quit selenium
        driver.quit()

        df = pd.read_html(table_html)[0]
        df = df[df.columns[:11]]
        df['tournament_name'] = self.tournament_name
        df['tournament_id'] = self.tournament_id
        for col in df.columns:
            if col not in [
                'Pos','Unnamed: 1','Player','Total',
                'Thru','Round','R1','R2','R3','R4',
                'tournament_name','tournament_id'
                ]:
                df.drop(columns=col, inplace=True)

        cut_index = df[df['Pos'].str.contains('The following players failed to make the cut')].index
        df.drop(cut_index, inplace=True)

        df['Total'] = df['Total'].replace('E', 0)
        df['Total'] = df['Total'].replace('-', 0)
        df['Round'] = df['Round'].replace('E', 0)
        df['Round'] = df['Round'].replace('-', 0)
        df['R1'] = df['R1'].replace('E', 0)
        df['R1'] = df['R1'].replace('-', 0)
        df['R2'] = df['R2'].replace('E', 0)
        df['R2'] = df['R2'].replace('-', 0)
        df['R3'] = df['R3'].replace('E', 0)
        df['R3'] = df['R3'].replace('-', 0)
        df['R4'] = df['R4'].replace('E', 0)
        df['R4'] = df['R4'].replace('-', 0)

        if write_table:
            self.write_table(df, 'leaderboard')

        return df


    def field(self, write_raw=False, write_table=False):
        payload = {
            "operationName":"Field",
            "variables":{
                "fieldId": self.tournament_id
            },
            "query":"query Field($fieldId: ID!, $includeWithdrawn: Boolean, $changesOnly: Boolean) {\n  field(\n    id: $fieldId\n    includeWithdrawn: $includeWithdrawn\n    changesOnly: $changesOnly\n  ) {\n    tournamentName\n    id\n    lastUpdated\n    message\n    features {\n      name\n      new\n      tooltipText\n      tooltipTitle\n      fieldStatType\n      leaderboardFeatures\n    }\n    players {\n      ...FieldPlayer\n      teammate {\n        id\n        alphaSort\n        firstName\n        lastName\n        shortName\n        displayName\n        amateur\n        favorite\n        country\n        countryFlag\n        headshot\n        qualifier\n        alternate\n        withdrawn\n        status\n        owgr\n        rankingPoints\n      }\n    }\n    alternates {\n      ...FieldPlayer\n    }\n    standingsHeader\n  }\n}\n\nfragment FieldPlayer on PlayerField {\n  id\n  alphaSort\n  firstName\n  lastName\n  shortName\n  displayName\n  amateur\n  favorite\n  country\n  countryFlag\n  headshot\n  qualifier\n  alternate\n  withdrawn\n  status\n  owgr\n  rankingPoints\n  rankLogoLight\n  rankLogoDark\n}"
        }
        # post the request
        page = requests.post(
            "https://orchestrator.pgatour.com/graphql", 
            json=payload, 
            headers={"x-api-key": self.X_API_KEY}
        )
        
        # check for status code
        page.raise_for_status()

        # get the data
        data = page.json()["data"]["field"]["players"]

        out_data = {
            "year": [],
            "tournament_id": [],
            "tournament_name": [],
            "execution_time": [],
            "player_id": [],
            "first_name": [],
            "last_name": [],
            "display_name": [],
            "status": [],
            "owgr": []
        }

        for player in data:
            out_data['year'].append(self.year)
            out_data['tournament_id'].append(self.tournament_id)
            out_data['tournament_name'].append(self.tournament_name)
            out_data['execution_time'].append(self.execution_time)
            out_data['player_id'].append(player["id"])
            out_data['first_name'].append(player["firstName"])
            out_data['last_name'].append(player["lastName"])
            out_data['display_name'].append(player["displayName"])
            out_data['status'].append(player["status"])
            out_data['owgr'].append(player["owgr"])

        df = pd.DataFrame(out_data)

        if write_raw:
            self.write_raw(data, 'field')
        if write_table:
            self.write_table(df, 'field')

        return data
