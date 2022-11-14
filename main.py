import json
from pprint import pprint

def get_allusername(data):
    answer = []
    for user in data['results']:

        first = user['name']['first']
        last = user['name']['last']
        title = user['name']['title']

        fullname = f'{title} {first} {last}'
        answer.append(fullname)
    return answer

f = open('randomuser_data.json').read()
data = json.loads(f)
pprint(get_allusername(data))


