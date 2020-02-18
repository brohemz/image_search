from bs4 import BeautifulSoup
import requests
import json
from lxml import etree
from xml.dom import minidom
import urllib

client_id = r'client_id'
client_secret = r'client_secret'
redirect_uri = 'https://callback'

my_key = r'507ba75534b0005df0e2d15fb2901a29'
my_secret = r'0cd20345117cf04b'



# url = 'https://www.google.com/search?hl=en&authuser=0&tbm=isch&sxsrf=ACYBGNTkdMAlsKaQGY_6nZX9PEMIrcLIAw%3A1581828961721&source=hp&biw=1680&bih=915&ei=YctIXoPQKeGxggfX_4eQBA&q=dog&oq=dog&gs_l=img.3..35i39j0l9.632.914..1041...0.0..0.137.293.2j1......0....1..gws-wiz-img.WWcj4hJhthI&ved=0ahUKEwjDhO2KpNXnAhXhmOAKHdf_AUIQ4dUDCAU&uact=5'
#
# req = requests.get(url)
#
# soup = BeautifulSoup (req.text, features='lxml')
#
#
#
# print(soup.prettify())

# source = r'https://farm66.staticflickr.com/65535/49540211346_0becbf4e7b.jpg'

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
    parser = etree.XMLParser(encoding='utf-8')

    # xml = '<a xmlns="test"><b xmlns="test"/></a>'
    # html = "<html><head><title>test</title></head></html>"
    #
    # print(etree.tostring(etree.HTML(xml), pretty_print=True))

    # return etree.XML(xml, parser=parser)

    xmldoc = minidom.parseString(response.content)
    # print(xmldoc.getElementsByTagName('photo'))

    return xmldoc.getElementsByTagName('photo')

# print(getListing()[0].attributes.keys())

cur = getListing()[0].attributes

print(getListing()[0].attributes)

farm_id = cur['farm'].firstChild.data
server_id = cur['server'].firstChild.data
pic_id = cur['id'].firstChild.data
pic_secret = cur['secret'].firstChild.data

# farm_id = r'66'
# server_id = r'65535'
# pic_id = r'49545018336'
# pic_secret = r'd9a78e052d'
#
link = f'https://farm{farm_id}.staticflickr.com/{server_id}/{pic_id}_{pic_secret}.jpg'
print(link)
