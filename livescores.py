import requests
import json

url = "https://api.sofascore.com/api/v1/sport/cricket/events/live"

payload = ""
headers = {
    "authority": "api.sofascore.com",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "origin": "https://www.sofascore.com",
    "referer": "https://www.sofascore.com/",
    "sec-ch-ua": "^\^Chromium^^;v=^\^118^^, ^\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

response = requests.request("GET", url, data=payload, headers=headers)

jsondata = json.loads(response.text)

def get_scores():
    finaly = ''
    for i in jsondata['events']:
        league = i['tournament']['name']
        home_team = i['homeTeam']['name']
        away_team = i['awayTeam']['name']
        home_score = i['homeScore']['current']
        away_score = i['awayScore']['current']
        if 'innings' in i['homeScore']:
            home_over =i['homeScore']['innings']['inning1']['overs']
            home_wickets = i['homeScore']['innings']['inning1']['wickets']
        else:
            home_over = 0
            home_wickets = 0

        if 'innings' in i['awayScore']:
            away_over = i['awayScore']['innings']['inning1']['overs']
            away_wickets = i['awayScore']['innings']['inning1']['wickets']
        else:
            away_over = 0
            away_wickets = 0
        print('\n')
        final= league + '\n' + home_team + ' ' + str(home_score) + '/' + str(home_wickets) + ' ( ' + str(home_over) + ' overs )\n' + away_team + ' ' + str(away_score) + '/' + str(away_wickets) + ' ( ' + str(away_over) + ' overs )'
        #print(league , '\n' , home_team + ' ' , home_score , '/' , home_wickets , '(' , home_over , 'overs )\n' , away_team , ' ' , away_score , '/' , away_wickets , '(' , away_over , 'overs )' )
        finaly = finaly +'\n\n' + final
    return finaly


# for i in jsondata['events']:
#     league = i['tournament']['name']
#     home_team = i['homeTeam']['name']
#     away_team = i['awayTeam']['name']
#     home_score = i['homeScore']['current']
#     away_score = i['awayScore']['current']
#     if 'innings' in i['homeScore']:
#         home_over =i['homeScore']['innings']['inning1']['overs']
#         home_wickets = i['homeScore']['innings']['inning1']['wickets']
#     else:
#         home_over = None
#         home_wickets = None

#     if 'innings' in i['awayScore']:
#         away_over = i['awayScore']['innings']['inning1']['overs']
#         away_wickets = i['awayScore']['innings']['inning1']['wickets']
#     else:
#         away_over = None
#         away_wickets = None
#     print('\n')
#     final = league + '\n' + home_team + ' ' + str(home_score) + '/' + str(home_wickets) + ' ( ' + str(home_over) + ' overs )\n' + away_team + ' ' + str(away_score) + '/' + str(away_wickets) + ' ( ' + str(away_over) + ' overs )'
#     print(final)


