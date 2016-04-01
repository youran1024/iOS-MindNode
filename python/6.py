#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

import urllib.request
import urllib
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen


array = []
def getAllImageLink(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    imageEntityArray = soup.findAll('img')
    for image in imageEntityArray:
        link = image.get('src')
        imageName = image.get('src')
        imageName = imageName.split('/')
        imageName = imageName[-1]
        filesavepath = '/Users/MrYang/Desktop/123/%s' % imageName 
        urllib.request.urlretrieve(link,filesavepath)
        print(filesavepath)

    array.append(url)

    herfArray = soup.findAll('a', attrs={'target':'_blank'})
    print(herfArray)
    for herfSign in herfArray:
        herf = herfSign.get('href')
        print(herf)
        if herf in array:
            print('herfBreak:', herf)
            continue
        
        if 'wmpic' in herf:
            getAllImageLink(herf)


if __name__ == '__main__':

    getAllImageLink('http://www.wmpic.me/meinv')
