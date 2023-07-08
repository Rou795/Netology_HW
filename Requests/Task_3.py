import requests

import json
url = 'https://api.stackexchange.com/2.3/questions'
params = {'fromdate': '1688601600',
          'todate': '1688774400',
          'order': 'asc',
          'sort': 'activity',
          'tagged': 'python',
          'site': 'stackoverflow'}
response = requests.get(url, params=params)
if 200 <= response.status_code < 300:
    data = response.json()
    print(len(data['items']))