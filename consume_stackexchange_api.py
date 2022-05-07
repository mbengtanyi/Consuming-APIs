#!/usr/bin/env /usr/local/bin/python3 

import requests
import json

get_response = requests.get('http://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow')
print(get_response.json())