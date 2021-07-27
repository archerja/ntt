#!/usr/bin/env python3

# requires mpv

import os
import sys
import random

version = '0.0.1'

mp3s = []
mediapath = "/home/archerja/Music/"

# number of seconds
end = 5

# create list of songs
for root, dir, files in os.walk(mediapath):
    for name in files:
        if name[-4:].lower() == '.mp3':
            path = os.path.join(root,name)
            location = path.split(path)[1]
            mp3s.append(path)
            #print(path)

# start the game
print(" ")
print("NTT, version " + version)
print(" ")
print("Music from: " + mediapath)
print(" ")
print("Loaded " + str(len(mp3s)) + " songs...")
print(" ")
print(str(end) + " seconds of audio...")
print(" ")
print("Get ready to play...")
print(" ")
print("**************************")
print("*  Joe's Name That Tune  *")
print("**************************")
print(" ")

random.shuffle(mp3s)

# let's begin
for i in range(0,len(mp3s)-1):
    print("Press space to hear the song...")
    os.system('mpv --really-quiet --pause --start=0 --end=' + str(end + 1) + ' "' +  mp3s[i] + '"')
    status = True
    while status:
        response = input("Get (a)nswer, (c)heat add 10 seconds, hear (w)hole song, (n)ext song, or (q)uit [a/c/w/n/q] enter: ")
        if "q" in response:
            print(" ")
            print("**************************")
            print("*  Thanks for playing    *")
            print("**************************")
            print(" ")
            sys.exit(0)
        elif "a" in response:
            print(mp3s[i])
        elif "w" in response:
            os.system('mpv "' +  mp3s[i] + '"')
        elif "c" in response:
            os.system('mpv --really-quiet --start=0 --end=' + str(end + 11) + ' "' +  mp3s[i] + '"')
        elif "n" in response:
            status = False
        else:
            continue

