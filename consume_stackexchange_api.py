#!/usr/bin/env /usr/local/bin/python3 

import requests
import json

get_response = requests.get('http://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow')
# print(get_response.json()['items'])

#Getting questions without answers
for question in get_response.json()['items']:
    if question['answer_count'] == 0:
        print(question['title'])
        print(question['link'])
    else:
        #printing the word "skipped" for questions having at least 1 answer.
        print("skipped")
    print("")