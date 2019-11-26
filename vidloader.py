#!/usr/bin/env python
#
from __future__ import unicode_literals
import youtube_dl
import os
import sys

os.system("clear && clear && clear")

print ("""

        _________ ______   _        _______  _______  ______   _______  _______ 
|\     /|\__   __/(  __  \ ( \      (  ___  )(  ___  )(  __  \ (  ____ \(  ____ )
| )   ( |   ) (   | (  \  )| (      | (   ) || (   ) || (  \  )| (    \/| (    )|
| |   | |   | |   | |   ) || |      | |   | || (___) || |   ) || (__    | (____)|
( (   ) )   | |   | |   | || |      | |   | ||  ___  || |   | ||  __)   |     __)
 \ \_/ /    | |   | |   ) || |      | |   | || (   ) || |   ) || (      | (\ (   
  \   /  ___) (___| (__/  )| (____/\| (___) || )   ( || (__/  )| (____/\| ) \ \__
   \_/   \_______/(______/ (_______/(_______)|/     \|(______/ (_______/|/   \__/
                                                                                 
          >>>>>>>>>>>>>>>>>>>>>>>>>>>    }--{+} Coded By Prasoon {+}--{
                 >>>>>>>>>>>>>>>>>>>>>>>>>>>>   }----{+}  fb.me/prasoon0  {+}----{

     """)
       

print('Select the download option')
menu = '''\033[0m
    1.Video (Youtube,openload etc)
    2.Audio Download
    3.Audio PlayList Download

    {99}-Exit
 '''
print (menu)


def quit():
    con = input('Continue [Y/n] -> ')
    if con[0].upper() == 'N':
        exit()
    else:
        os.system("clear")
        print (menu)
        select()


def select():
    try:
        choice = input("Select~# ")
        if choice == 1:
            os.system("clear")
            print ("""
 __ __  ____  ___      ___   ___   _____
|  |  ||    ||   \    /  _] /   \ / ___/
|  |  | |  | |    \  /  [_ |     (   \_ 
|  |  | |  | |  D  ||    _]|  O  |\__  |
|  :  | |  | |     ||   [_ |     |/  \ |
 \   /  |  | |     ||     ||     |\    |
  \_/  |____||_____||_____| \___/  \___|
                                        
  
PUT URL EX: https://www.youtube.com/watch?v=KYHGFg124e
""")
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([input('URL: ')])
            print("")
            quit()
        elif choice == 2:
            os.system("clear")
            print ("""
 
  ____  __ __  ___    ____  ___  
 /    ||  |  ||   \  |    |/   \ 
|  o  ||  |  ||    \  |  ||     |
|     ||  |  ||  D  | |  ||  O  |
|  _  ||  :  ||     | |  ||     |
|  |  ||     ||     | |  ||     |
|__|__| \__,_||_____||____|\___/ 
                 

PUT URL EX: https://www.youtube.com/watch?v=KTHGFg124e
""")
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([input('URL: ')])
            quit()
        elif choice == 3:
            os.system("clear")
            print("""

 ____  _       ____  __ __  _      ____ _____ ______ 
|    \| |     /    ||  |  || |    |    / ___/|      |
|  o  ) |    |  o  ||  |  || |     |  (   \_ |      |
|   _/| |___ |     ||  ~  || |___  |  |\__  ||_|  |_|
|  |  |     ||  _  ||___, ||     | |  |/  \ |  |  |  
|  |  |     ||  |  ||     ||     | |  |\    |  |  |  
|__|  |_____||__|__||____/ |_____||____|\___|  |__|  
           

EX: https://www.youtube.com/playlist?list=PLDIoUOhQQPlXr63I_vwF9GD8sAKh77dWU
""")
            d3 = input('playlist URL: ')
            os.system("clear")
            os.system("youtube-dl -cit --extract-audio --audio-format mp3 " + d3)
            print("")
            quit()
    except(KeyboardInterrupt):
        print ("")


select()
