#!/usr/bin/env python3

# requires mpv, and grep

import os
import sys
import random

version = '0.0.4'

# create empty array
mp3s = []

# number of seconds
end = 5

# set your music paths (with / as end of path)
mediapath1 = '/media/archerja/My Passport/backup/Music/Compilation/AM Gold 1962 - 1979/'
mediapath2 = '/media/archerja/My Passport/backup/Music/Compilation/Ultimate Seventies/'
mediapath3 = '/media/archerja/My Passport/backup/Music/Compilation/Flower Power/'
mediapath4 = '/media/archerja/My Passport/backup/Music/Compilation/Columbia Country Classics/'
mediapath5 = '/media/archerja/My Passport/backup/Music/Compilation/101 One Hit Wonders/'
mediapath6 = '' 
mediapath7 = '/media/archerja/My Passport/backup/Music/Compilation/Disco Fever/'

# create list of songs
def makelist(listnum,listpath):
        for root, dir, files in os.walk(listpath):
            for name in files:
                if name[-4:].lower() == '.mp3':
                    path = os.path.join(root,name)
                    mp3s.append([listnum,path])
        if pickcount(mp3s,listnum) > 0:
            print('(' + str(pickcount(mp3s,listnum)) + ' of ' + str(len(mp3s)) + ')' + listpath)
        return mp3s

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

def loadgame():
        clearscreen()
        print('Loading music from: ')
        print(' ')
        makelist(1,mediapath1)
        makelist(2,mediapath2)
        makelist(3,mediapath3)
        makelist(4,mediapath4)
        makelist(5,mediapath5)
        makelist(6,mediapath6)
        makelist(7,mediapath7)
        if len(mp3s) == 0:
            print('????? No songs loaded in game...')
            print('????? Check folder locations...')
            exitbanner()
            sys.exit(0)
        print(' ')
        print('shuffling ' + str(len(mp3s)) + ' total songs...')
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
                            print('  (a) ' + mediapath1.split('/')[-2])
                        if pickcount(mp3s,2) > 0:
                            print('  (b) ' + mediapath2.split('/')[-2])
                        if pickcount(mp3s,3) > 0:
                            print('  (c) ' + mediapath3.split('/')[-2])
                        if pickcount(mp3s,4) > 0:
                            print('  (d) ' + mediapath4.split('/')[-2])
                        if pickcount(mp3s,5) > 0:
                            print('  (e) ' + mediapath5.split('/')[-2])
                        if pickcount(mp3s,6) > 0:
                            print('  (f) ' + mediapath6.split('/')[-2])
                        if pickcount(mp3s,7) > 0:
                            print('  (g) ' + mediapath7.split('/')[-2])
                        response = input('Pick letter, (?)help, or (q)uit, then press enter: ')
                        #response = input('[a/b/c/d/e/f/g/?/q] enter: ')
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


