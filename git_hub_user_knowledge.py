import json
import requests
repos_url = None
autorization_tial = '?client_id=eb2d986740eb9bb4cf4c&client_secret=f93b446152723031af092e7ac3858586b0fb733c'
BASE_API_URL = 'jso'

while True:
    name = input('Please input github username:')
    r = requests.get(BASE_API_URL + 'users/%s' % name + autorization_tial)
    if r.status_code == 200:
        break
    else:
        print("please enter again")

with open('myJson.json', 'w') as f:
    json.dump(r.json(), f)

with open('myJson.json', 'r') as f:
    user_obj = json.load(f)
    repos_url = user_obj['repos_url']
    print(repos_url)

if repos_url:
    r = requests.get(repos_url + autorization_tial)
    arr = []
    for elem in r.json():
        req = requests.get(elem['languages_url'] + autorization_tial)
        if req.status_code != 200:
            continue
        summ = sum(req.json().values())
        for element in req.json().keys():
            if req.json()[element]/summ * 100 > 40:
                arr.append(element)
    arr = set(arr)
    line = (", ").join(arr)


    with open('textbook.txt', 'w') as f:
        f.write(name + " knows " + line)
