#~/usr/bin/python3

from bs4 import BeautifulSoup
import requests
# import json
from xml.dom import minidom
import urllib
import sys
import os

my_key = r'507ba75534b0005df0e2d15fb2901a29'
# my_secret = r'0cd20345117cf04b'


def setup(arg):
    ret = {}

    # NEXT UP: PIPING HOT TAGS FROM THE CMD!!!
    if arg is not None and len(arg) >= 2:
        ret['data_tag'] = arg[1]
        print(arg[1])
    dir = os.path.join(os.getcwd(), 'resources')
    if not os.path.exists(dir):
        os.mkdir(dir)

    return ret

def getListing(args):

    requestURL = "https://api.flickr.com/services/rest"

    headers = {
        'api_key': my_key
    }

    body = {
        'method': 'flickr.photos.search',
        'tags': ['dogs'] if args.get('data_tag') is None else args.get('data_tag'),
        'api_key': my_key
    }

    data = urllib.parse.urlencode(body)
    response = requests.get(requestURL, params=data)
    xmldoc = minidom.parseString(response.content)
    return xmldoc.getElementsByTagName('photo')


def readTags():
    

def main():
    print(sys.argv)

    setup_dict = setup(sys.argv)

    list = getListing(setup_dict)

    for x in range(0, 10):
        cur = list[x].attributes

        farm_id = cur['farm'].firstChild.data
        server_id = cur['server'].firstChild.data
        pic_id = cur['id'].firstChild.data
        pic_secret = cur['secret'].firstChild.data

        link = f'https://farm{farm_id}.staticflickr.com/{server_id}/{pic_id}_{pic_secret}.jpg'
        print(link)
        # Fix the links, some parsing isn't working on certain photos
        if farm_id is '0':
            print("wowow")
            continue

        urllib.request.urlretrieve(link, f'./resources/pic{x}.jpg')
    #    pic_file = open(f'./resources/pic{x}.jpg', 'wb')
    #    pic_data = requests.get(link).content
    #    pic_file.write(pic_data)
    #    pic_file.close()

if __name__ == "__main__":
    main()
