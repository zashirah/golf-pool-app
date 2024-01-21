import pandas as pd
import requests
import json


class Schedule:
    def __init__(self, year):
        self.X_API_KEY = "da2-gsrx5bibzbb4njvhl7t37wqyl4"
        self.year = year


    def write_table(self, df):
        df.to_csv(f'schedule_{self.year}.csv', index=False)
    

    def write_raw(self, data):
        with open(f'schedule_{self.year}.json', 'w') as f:
            json.dump(data, f)


    def schedule(self, write_table=False, write_raw=False):
        payload = {
            "operationName":"Schedule",
            "variables": {
                "tourCode":"R",
                "year":self.year
            },
            "query":"query Schedule($tourCode: String!, $year: String, $filter: TournamentCategory) {\n  schedule(tourCode: $tourCode, year: $year, filter: $filter) {\n    completed {\n      month\n      year\n      monthSort\n      ...ScheduleTournament\n    }\n    filters {\n      type\n      name\n    }\n    seasonYear\n    tour\n    upcoming {\n      month\n      year\n      monthSort\n      ...ScheduleTournament\n    }\n  }\n}\n\nfragment ScheduleTournament on ScheduleMonth {\n  tournaments {\n    tournamentName\n    id\n    beautyImage\n    champion\n    champions {\n      displayName\n      playerId\n    }\n    championEarnings\n    championId\n    city\n    country\n    countryCode\n    courseName\n    date\n    dateAccessibilityText\n    purse\n    sortDate\n    startDate\n    state\n    stateCode\n    status {\n      roundDisplay\n      roundStatus\n      roundStatusColor\n      roundStatusDisplay\n    }\n    ticketsURL\n    tourStandingHeading\n    tourStandingValue\n    tournamentLogo\n    display\n    sequenceNumber\n    tournamentCategoryInfo {\n      type\n      logoLight\n      logoDark\n      label\n    }\n  }\n}"
        }

        page = requests.post("https://orchestrator.pgatour.com/graphql", json=payload, headers={"x-api-key": self.X_API_KEY})
        page.raise_for_status()
        data = page.json()["data"]

        tournament_details = {
            'tournament_name': [],
            'tournament_id': [],
            'date': [],
            'status': []
        }
        for schedule_type in ['completed', 'upcoming']:
            for month in data['schedule'][schedule_type]:
                for tournament in month['tournaments']:
                    tournament_details['tournament_name'].append(tournament['tournamentName'])
                    tournament_details['tournament_id'].append(tournament['id'])
                    tournament_details['date'].append(tournament['date'])
                    tournament_details['status'].append(schedule_type)

        df = pd.DataFrame(tournament_details)

        if write_table:
            self.write_table(df)
        if write_raw:
            self.write_raw(data)

        return data, df

