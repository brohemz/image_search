from bs4 import BeautifulSoup
import requests
import json
from xml.dom import minidom
import urllib

my_key = r'507ba75534b0005df0e2d15fb2901a29'
# my_secret = r'0cd20345117cf04b'

def getListing():
    requestURL = "https://api.flickr.com/services/rest"

    headers = {
        'api_key': my_key
    }

    body = {
        'method': 'flickr.photos.search',
        'tags': 'dog',
        'api_key': my_key
    }

    data = urllib.parse.urlencode(body)
    response = requests.get(requestURL, params=data)
    xmldoc = minidom.parseString(response.content)

    return xmldoc.getElementsByTagName('photo')


cur = getListing()[0].attributes
print(cur)

farm_id = cur['farm'].firstChild.data
server_id = cur['server'].firstChild.data
pic_id = cur['id'].firstChild.data
pic_secret = cur['secret'].firstChild.data

link = f'https://farm{farm_id}.staticflickr.com/{server_id}/{pic_id}_{pic_secret}.jpg'
print(link)
