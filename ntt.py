#!/usr/bin/env python3

# requires mpv, and grep

import os
import sys
import random

version = '0.0.5'

# create empty arrays
mp3s = []
patharray = []

# number of seconds to play
end = 5

# name your file of directories below
songfile = 'songs'

# create list of songs
def makelist(listnum,listpath):
        if listnum < 10:
            for root, dir, files in os.walk(listpath):
                for name in files:
                    if name[-4:].lower() == '.mp3':
                        path = os.path.join(root,name)
                        mp3s.append([listnum,path])
        if pickcount(mp3s,listnum) > 0:
            print('(' + str(pickcount(mp3s,listnum)) + ' of ' + str(len(mp3s)) + ')' + listpath)
        else:
            print('no music loaded')
        return mp3s

def getlocations():
        pathnum = 0
        if str(os.path.exists(songfile)) == 'True':
            with open(songfile) as f:
                for line in f:
                    if line[0] == '#' or line[0] == '\n':
                        continue
                    else:
                        line = line.strip('\n')
                        if line[-1:] == '/':
                            pass
                        else:
                            line = line + '/'
                        pathnum = pathnum + 1
                        patharray.append([pathnum,line])
            print('Loading music from: ')
            for k in range(0,len(patharray)):
                for q in range(0,len(patharray[k])):
                    continue
                makelist(patharray[k][0], patharray[k][1])
        else:
            print('* error: could not find file [' + songfile + ']') 
            print('* error: check current directory')
            sys.exit(0)
        return

def pickcount(songs,pick):
        num = [row[0] for row in songs]
        return num.count(pick)

# get mp3 tags with mpv
def songinfo(song,info):
        return os.system('mpv "%s" --display-tags=album,artist,title --audio=no --video=no | grep %s ' % (song, info))

# clear the screen with os call
def clearscreen():
        if os.name == "posix":
            # Linux, Unix, MacOS, Solaris
            os.system('clear')
        else:
            # Windows
            os.system('cls')

# start the game
def gamebanner():
        clearscreen()
        print(' ')
        print("::::::'##::'#######::'########:'####::'######:::::'##::: ##::::'###::::'##::::'##:'########:")
        print(":::::: ##:'##.... ##: ##.....:: ####:'##... ##:::: ###:: ##:::'## ##::: ###::'###: ##.....::")
        print(":::::: ##: ##:::: ##: ##:::::::. ##:: ##:::..::::: ####: ##::'##:. ##:: ####'####: ##:::::::")
        print(":::::: ##: ##:::: ##: ######:::'##:::. ######::::: ## ## ##:'##:::. ##: ## ### ##: ######:::")
        print(":##::: ##: ##:::: ##: ##...::::..:::::..... ##:::: ##. ####: #########: ##. #: ##: ##...::::")
        print(":##::: ##: ##:::: ##: ##:::::::::::::'##::: ##:::: ##:. ###: ##.... ##: ##:.:: ##: ##:::::::")
        print(": ######::. #######:: ########:::::::. ######::::: ##::. ##: ##:::: ##: ##:::: ##: ########:")
        print(":......::::.......:::........:::::::::......::::::..::::..::..:::::..::..:::::..::........::")
        print(":::'########:'##::::'##::::'###::::'########::::'########:'##::::'##:'##::: ##:'########::::")
        print(":::... ##..:: ##:::: ##:::'## ##:::... ##..:::::... ##..:: ##:::: ##: ###:: ##: ##.....:::::")
        print(":::::: ##:::: ##:::: ##::'##:. ##::::: ##:::::::::: ##:::: ##:::: ##: ####: ##: ##::::::::::")
        print(":::::: ##:::: #########:'##:::. ##:::: ##:::::::::: ##:::: ##:::: ##: ## ## ##: ######::::::")
        print(":::::: ##:::: ##.... ##: #########:::: ##:::::::::: ##:::: ##:::: ##: ##. ####: ##...:::::::")
        print(":::::: ##:::: ##:::: ##: ##.... ##:::: ##:::::::::: ##:::: ##:::: ##: ##:. ###: ##::::::::::")
        print(":::::: ##:::: ##:::: ##: ##:::: ##:::: ##:::::::::: ##::::. #######:: ##::. ##: ########::::")
        print("::::::..:::::..:::::..::..:::::..:::::..:::::::::::..::::::.......:::..::::..::........:::::")
        print('                                           v.' + version)
        print(' ')
        input('                                                                 Press enter to begin...')
        print(' ')

# end the game
def exitbanner():
        clearscreen()
        print(' ')
        print('****************************')
        print('*    Thanks for playing    *')
        print('****************************')
        print(' ')

def help():
        print(' ')
        print('Help: ')
        print('Help: ')
        print('Help: ')
        print('Help: ')
        print('Help: ')
        print('Help: ')
        print('Help: ')
        print('Help: ')
        print('Help: ')
        print('Help: ')
        print('Help: ')
        print('Help: ')
        print('Help: ')
        print('Help: ')
        print('Help: ')
        print(' ')

def loadgame():
        clearscreen()
        getlocations()
        if len(mp3s) == 0:
            print('* error: No songs loaded in game...')
            print('* error: Check file for correct directory paths...')
            sys.exit(0)
        print(' ')
        print('shuffling ' + str(len(mp3s)) + ' total songs...')
        random.shuffle(mp3s)
        random.shuffle(mp3s)
        random.shuffle(mp3s)
        print(' ')
        input('...press enter to begin the game!')

# let's begin
def main(mp3s):
        clearscreen()
        picklist = 0
        for j in range(0,len(mp3s)-1):
            for i in range(0,len(mp3s[j])-1):
                if picklist == 0:
                    status = True
                    while status:
                        print('-------------------------------------')
                        print('Select which song list:')
                        if pickcount(mp3s,1) > 0:
                            print('  (a) ' + patharray[0][1].split('/')[-2])
                        if pickcount(mp3s,2) > 0:
                            print('  (b) ' + patharray[1][1].split('/')[-2])
                        if pickcount(mp3s,3) > 0:
                            print('  (c) ' + patharray[2][1].split('/')[-2])
                        if pickcount(mp3s,4) > 0:
                            print('  (d) ' + patharray[3][1].split('/')[-2])
                        if pickcount(mp3s,5) > 0:
                            print('  (e) ' + patharray[4][1].split('/')[-2])
                        if pickcount(mp3s,6) > 0:
                            print('  (f) ' + patharray[5][1].split('/')[-2])
                        if pickcount(mp3s,7) > 0:
                            print('  (g) ' + patharray[6][1].split('/')[-2])
                        if pickcount(mp3s,8) > 0:
                            print('  (h) ' + patharray[7][1].split('/')[-2])
                        if pickcount(mp3s,9) > 0:
                            print('  (i) ' + patharray[8][1].split('/')[-2])
                        response = input('Pick letter, (?)help, or (q)uit, then press enter: ')
                        if 'q' in response:
                            exitbanner()
                            sys.exit(0)
                        elif '?' in response:
                            help()
                            continue
                        elif 'a' in response:
                            picklist = 1
                            if pickcount(mp3s,picklist) > 0:
                                status = False
                            else:
                                continue
                        elif 'b' in response:
                            picklist = 2
                            if pickcount(mp3s,picklist) > 0:
                                status = False
                            else:
                                continue
                        elif 'c' in response:
                            picklist = 3
                            if pickcount(mp3s,picklist) > 0:
                                status = False
                            else:
                                continue
                        elif 'd' in response:
                            picklist = 4
                            if pickcount(mp3s,picklist) > 0:
                                status = False
                            else:
                                continue
                        elif 'e' in response:
                            picklist = 5
                            if pickcount(mp3s,picklist) > 0:
                                status = False
                            else:
                                continue
                        elif 'f' in response:
                            picklist = 6
                            if pickcount(mp3s,picklist) > 0:
                                status = False
                            else:
                                continue
                        elif 'g' in response:
                            picklist = 7
                            if pickcount(mp3s,picklist) > 0:
                                status = False
                            else:
                                continue
                        elif 'h' in response:
                            picklist = 8
                            if pickcount(mp3s,picklist) > 0:
                                status = False
                            else:
                                continue
                        elif 'i' in response:
                            picklist = 9
                            if pickcount(mp3s,picklist) > 0:
                                status = False
                            else:
                                continue
                        else:
                            continue
                if mp3s[j][0] == picklist:
                    picklist = 0
                else:
                    continue
                print('----------')
                print('Press space to hear the song...')
                os.system('mpv --really-quiet --pause --start=0 --end=' + str(end + 1) + ' "' +  mp3s[j][1] + '"')
                print('----------')
                status = True
                while status:
                    print('(a)nswer, (c)heat, (w)hole song, (n)ext song, (?)help, or (q)uit')
                    response = input('[a/c/w/n/h/q] then enter: ')
                    print('----------')
                    if 'q' in response:
                        exitbanner()
                        sys.exit(0)
                    elif '?' in response:
                        help()
                        continue
                    elif 'a' in response:
                        #print(mp3s[j][1])
                        songinfo(mp3s[j][1],'title')
                        songinfo(mp3s[j][1],'artist')
                        print('----------')
                    elif 'w' in response:
                        os.system('mpv "' +  mp3s[j][1] + '"')
                    elif 'c' in response:
                        os.system('mpv --really-quiet --start=0 --end=' + str(end + 11) + ' "' +  mp3s[j][1] + '"')
                    elif 'n' in response:
                        status = False
                    else:
                        continue

if __name__ == '__main__':

        gamebanner()
        loadgame()
        main(mp3s)


