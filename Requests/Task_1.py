import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
comparison_list = ['Hulk', 'Captain America', 'Thanos']
char_list = []
if 200 <= response.status_code < 300:
    all_info = response.json()
    for super_h in all_info:
        if super_h['name'] in comparison_list:
            char_list.append((super_h['name'], super_h['powerstats']['intelligence']))
    char_list = sorted(char_list, key=lambda couple: couple[1])
    print(char_list[-1][0])