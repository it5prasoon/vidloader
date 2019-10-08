#!/usr/bin/env python
#
from __future__ import unicode_literals
import youtube_dl
import os
import sys

os.system("clear && clear && clear")
logo = '''
 _  _  ____  ____  __    _____    __    ____  ____  ____ 
( \/ )(_  _)(  _ \(  )  (  _  )  /__\  (  _ \( ___)(  _ \
 \  /  _)(_  )(_) ))(__  )(_)(  /(__)\  )(_) ))__)  )   /
  \/  (____)(____/(____)(_____)(__)(__)(____/(____)(_)\_)
                                                                                       
   >>>>>>>>>>>>>>>>>>>>>>>>>>>    }--{+} Coded By Prasoon {+}--{
         >>>>>>>>>>>>>>>>>>>>>>>>>>>>   }----{+}  fb.me/prasoon0  {+}----{
'''

print ('Select the download option')
menu = '''\033[0m
    1.Video (Youtube,openload etc)
    2.Audio Download
    3.Audio PlayList Download

    {99}-Exit
 '''
print logo
print menu


def quit():
    con = raw_input('Continue [Y/n] -> ')
    if con[0].upper() == 'N':
        exit()
    else:
        os.system("clear")
        print logo
        print menu
        select()


def select():
    try:
        choice = input("SnapTub~# ")
        if choice == 1:
            os.system("clear")
            print """
 __ __  ____  ___      ___   ___   _____
|  |  ||    ||   \    /  _] /   \ / ___/
|  |  | |  | |    \  /  [_ |     (   \_ 
|  |  | |  | |  D  ||    _]|  O  |\__  |
|  :  | |  | |     ||   [_ |     |/  \ |
 \   /  |  | |     ||     ||     |\    |
  \_/  |____||_____||_____| \___/  \___|
                                        
  
PUT URL EX: https://www.youtube.com/watch?v=KYHGFg124e
"""
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([raw_input('URL: ')])
            print("")
            quit()
        elif choice == 2:
            os.system("clear")
            print """
 
  ____  __ __  ___    ____  ___  
 /    ||  |  ||   \  |    |/   \ 
|  o  ||  |  ||    \  |  ||     |
|     ||  |  ||  D  | |  ||  O  |
|  _  ||  :  ||     | |  ||     |
|  |  ||     ||     | |  ||     |
|__|__| \__,_||_____||____|\___/ 
                 

PUT URL EX: https://www.youtube.com/watch?v=KTHGFg124e
"""
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([raw_input('URL: ')])
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
            d3 = raw_input('playlist URL: ')
            os.system("clear")
            os.system("youtube-dl -cit --extract-audio --audio-format mp3 " + d3)
            print("")
            quit()
    except(KeyboardInterrupt):
        print ""


select()
