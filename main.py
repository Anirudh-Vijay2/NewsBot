from instabot import Bot
import time
import requests
import json
from datetime import datetime
from pytz import timezone
import textwrap
import os
import platform
from PIL import Image, ImageDraw, ImageFont
bot = Bot()
bot.login(username="thenewssage", password="u4njF!kAt4Di7SF")
key = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=8127727ffc49478ab6685dd16fadc301"
i = 0
done = []
while i != 20:
    hour = datetime.now(timezone("Asia/Kolkata")).strftime('%H')
    if int(hour) == 20 or int(hour) == 7 or int(hour) == 14:
        News = requests.get(key).json()
        Heading = News['articles'][i]["title"]
        description = News['articles'][i]['description']
        Url = "Read the complete news from here:- ",News['articles'][i]['url']
        done.append(Heading)
        textx = textwrap.fill(text=Heading, width=27.5)
        scnd = time.localtime().tm_sec
        Eimg = Image.open('MainImg.jpg') 
        d = ImageDraw.Draw(Eimg)
        style = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 34)
        d.text((50, 225), textx, font=style, fill="black")
        Eimg.save(f"{scnd}img.jpg")
        bot.upload_photo(f"{scnd}img.jpg", caption=description)
        pathName = f"{scnd}img.jpg"
        print("In Sleep will post again in 60 seconds.. Please be patient")
        if platform.system() == "Windows":
            os.system(f"del {pathName}")
        else:
            os.system(f"rm -rf {pathName}")
        print(f"Value of i is {i}")
        time.sleep(60)
        i = i+1
        if i == 20:
           i = i-20
    else:
        print("Wait time pending")
       
# os.system("rm -rf config")
print("Exited")

