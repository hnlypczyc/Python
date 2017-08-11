#!/usr/bin/python
import re

import urllib.request as ur

def getHtml(url):
    page = ur.urlopen(url)
    html = page.read()
    return html
    ##return 'src="http://tse1.mm.bing.net/th?id=OET.7d34bce1208547d1a45611db2930c7bd&amp;w=135&amp;h=135&amp;c=7&amp;rs=1&amp;qlt=90&amp;o=4&amp;pid=1.9" alt'

##src="http://tse1.mm.bing.net/th?id=OET.7d34bce1208547d1a45611db2930c7bd&amp;w=135&amp;h=135&amp;c=7&amp;rs=1&amp;qlt=90&amp;o=4&amp;pid=1.9" alt

def getImage(html):
    '''
    r = r'src="tse1\.mm\.bing\.net\/th.*?pid=1\.9" alt='
    '''
    r = r'src="(http://tse1\.mm\.bing\.net/th.*?pid=1\.9)"'
    ImageRe  = re.compile(r)
    ImageList = re.findall(ImageRe,html)
    print('----------------- START ---------------')
    print(len(ImageList))
    x = 0
    for image in ImageList:
        print(image)
        ur.urlretrieve(image,"%s.jpg" %x)
        x = x + 1
    
##print(getHtml("http://www.bing.com"))
url="http://cn.bing.com/images/trending?form=Z9LH"
pageSource = getHtml(url)
pageSourceStr = str(pageSource)
getImage(pageSourceStr)
