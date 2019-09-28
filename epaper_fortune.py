#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import epd7in5
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import subprocess
import string
weatherfile = '/home/pi/short_weather.txt'  

try:
    epd = epd7in5.EPD()
    epd.init()
    print("Clearing e-paper display")
    epd.Clear(0xFF)
    Himage = Image.new('1', (epd7in5.EPD_WIDTH, epd7in5.EPD_HEIGHT), 255)  # 255: clear the frame
    # Defining fonts
    font64 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf',64)
    font60 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf',60)
    font25 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf',25)
    font20 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf',20)
    draw = ImageDraw.Draw(Himage)
    currentdate = time.strftime("%d %B %Y")
    dayofweek = time.strftime("%A")
    result = os.popen('/home/pi/bin/fortune_reformatted.sh').read()

    # Date and weekday
    print(currentdate)
    draw.text((30,30), currentdate, font = font60, fill = 0)
    print(dayofweek)
    draw.text((200,100), dayofweek, font = font60, fill = 0)
    print (result)

    # fortune cookie text   
    y = 170
    linesarray = str.split(result,'\n')
    for i in range(len(linesarray)):
        print(linesarray[i])
        print('-')
        draw.text((50,y), linesarray[i], font = font25, fill = 0)
        y = y + 25

# Weather and sunrise/sunset information
    y = 300
    wf = open(weatherfile, 'r')
#    weatherinfo = wf.readline()
    weatherarray = wf.read().split('\n')
    wf.close()
#    draw.text((50,320), weatherinfo, font = font20, fill = 0)
    for i in range(len(weatherarray)):
        print(weatherarray[i])
        draw.text((50,y), weatherarray[i], font = font20, fill = 0)
        y = y + 20
   
# lines = text_file.read().split(',')

    epd.display(epd.getbuffer(Himage))
    epd.sleep()
 
except:
    print('traceback.format_exc():\n%s', traceback.format_exc())
    exit()

