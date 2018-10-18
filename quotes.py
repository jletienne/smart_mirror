#import requests
import random
import json

import urllib, json


def request_quote2():
    url = "https://raw.githubusercontent.com/jletienne/smart_mirror/master/static/quotes.json"
    response = urllib.urlopen(url)
    data = json.load(response)
    filmNumber = random.randrange(0,len(data))
    return data[filmNumber]




def request_quote():
    try:
        r = requests.get('https://raw.githubusercontent.com/jletienne/smart_mirror/master/static/quotes.json')
        filmNumber = random.randrange(0,len(r.json()))
        return r.json()[filmNumber]
    except:
        pass
    try:
        with open('static/quotes.json') as json_data:
            r = json.load(json_data)
        filmNumber = random.randrange(0,len(r))
        return r[filmNumber]
    except:
        return {'Person': 'Jean-Luc Etienne', 'Phrase': 'Fix your code it\'s broken bro'}
'''
def search_movie(movie='Get Shorty'):
    r = requests.get('https://raw.githubusercontent.com/jletienne/jletienne.com/master/static/films.json')
    return r.json(movie)
'''

if __name__ == '__main__':
    print(request_quote())
