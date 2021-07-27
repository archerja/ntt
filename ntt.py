#!/usr/bin/env python3

# requires mpv, and grep

import os
import sys
import random

version = '0.0.1'

mp3s = []
mediapath = "/home/archerja/Music/"

# number of seconds
end = 5

# create list of songs
def makelist(listnum,listpath):
        for root, dir, files in os.walk(listpath):
            for name in files:
                if name[-4:].lower() == '.mp3':
                    path = os.path.join(root,name)
                    location = path.split(path)[1]
                    mp3s.append([listnum,path])
        print("Music from: " + listpath)
        print("Loaded " + str(len(mp3s)) + " total songs...")
        print(" ")
        random.shuffle(mp3s)
        return mp3s

def songinfo(song,info):
        return os.system('mpv "%s" --display-tags=album,artist,title --audio=no --video=no | grep %s ' % (song, info))

# start the game
def gamebanner():
        print(" ")
        print("Get ready to play...")
        print(" ")
        print("****************************")
        print("    Joe's Name That Tune    ")  
        print("          v." + version)
        print("****************************")
        print(" ")
        input("Press enter to begin...")

# end the game
def exitbanner():
        print(" ")
        print("**************************")
        print("*  Thanks for playing    *")
        print("**************************")
        print(" ")

# let's begin
def main(mp3s):
        picklist = 0
        for j in range(0,len(mp3s)-1):
            for i in range(0,len(mp3s[j])-1):
                if picklist == 0:
                    status = True
                    while status:
                        print("-------------------------------------")
                        print("Select which audio list")
                        print("(a) " + mediapath1)
                        print("(b) " + mediapath2)
                        print("(c) " + mediapath3)
                        print("(d) " + mediapath4)
                        print("(e) " + mediapath5)
                        response = input("Pick a, b, c, d, e, or (q)uit, then press enter: ")
                        if "q" in response:
                            exitbanner()
                            sys.exit(0)
                        elif "a" in response:
                            picklist = 1
                            status = False
                        elif "b" in response:
                            picklist = 2
                            status = False
                        elif "c" in response:
                            picklist = 3
                            status = False
                        elif "d" in response:
                            picklist = 4
                            status = False
                        elif "e" in response:
                            picklist = 5
                            status = False
                        else:
                            continue
                if mp3s[j][0] == picklist:
                    picklist = 0
                else:
                    continue
                print("----------")
                print("Press space to hear the song...")
                os.system('mpv --really-quiet --pause --start=0 --end=' + str(end + 1) + ' "' +  mp3s[j][1] + '"')
                status = True
                while status:
                    response = input("Get (a)nswer, (c)heat add 10 seconds, hear (w)hole song, (n)ext song, or (q)uit [a/c/w/n/q] enter: ")
                    print("----------")
                    if "q" in response:
                        exitbanner()
                        sys.exit(0)
                    elif "a" in response:
                        #print(mp3s[j][1])
                        songinfo(mp3s[j][1],'artist')
                        songinfo(mp3s[j][1],'title')
                        print("----------")
                    elif "w" in response:
                        os.system('mpv "' +  mp3s[j][1] + '"')
                    elif "c" in response:
                        os.system('mpv --really-quiet --start=0 --end=' + str(end + 11) + ' "' +  mp3s[j][1] + '"')
                    elif "n" in response:
                        status = False
                    else:
                        continue

if __name__ == '__main__':

        gamebanner()
        makelist(1,mediapath1)
        makelist(2,mediapath2)
        makelist(3,mediapath3)
        makelist(4,mediapath4)
        makelist(5,mediapath5)
        main(mp3s)

