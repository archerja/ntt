#!/usr/bin/env python3

# requires mpv, and grep

import os
import sys
import random

version = '0.0.3'

# create empty array
mp3s = []

# number of seconds
end = 5

# set your music paths
mediapath1 = '/media/archerja/My Passport/backup/Music/Compilation/AM Gold 1962 - 1979/'
mediapath2 = '/media/archerja/My Passport/backup/Music/Compilation/Ultimate Seventies/'
mediapath3 = '/media/archerja/My Passport/backup/Music/Compilation/Magic 80s/'
mediapath4 = '/media/archerja/My Passport/backup/Music/Compilation/Columbia Country Classics/'
mediapath5 = '/media/archerja/My Passport/backup/Music/Compilation/160 One Hit Wonders/'

# create list of songs
def makelist(listnum,listpath):
        for root, dir, files in os.walk(listpath):
            for name in files:
                if name[-4:].lower() == '.mp3':
                    path = os.path.join(root,name)
                    #location = path.split(path)[1]
                    mp3s.append([listnum,path])
        print('(' + str(len(mp3s)) + ')' + listpath)
        #print(listpath.split('/')[-2])
        #print('Loading music from: ' + listpath)
        #print(str(len(mp3s)) + ' total songs...')
        #print(' ')
        return mp3s

# get mp3 tags with mpv
def songinfo(song,info):
        return os.system('mpv "%s" --display-tags=album,artist,title --audio=no --video=no | grep %s ' % (song, info))

# clear the screen with os call
def clearscreen():
        # Linux
        os.system('clear')
        # Windows
        # os.system('cls')

# start the game
def gamebanner():
        clearscreen()
        print(' ')
        print("::::::'##::'#######::'########:'####::'######:::::'##::: ##::::'###::::'##::::'##:'########:")
        print(":::::: ##:'##.... ##: ##.....:: ####:'##... ##:::: ###:: ##:::'## ##::: ###::'###: ##.....::")
        print(":::::: ##: ##:::: ##: ##:::::::. ##:: ##:::..::::: ####: ##::'##:. ##:: ####'####: ##:::::::")
        print(":::::: ##: ##:::: ##: ######:::'##:::. ######::::: ## ## ##:'##:::. ##: ## ### ##: ######:::")
        print("'##::: ##: ##:::: ##: ##...::::..:::::..... ##:::: ##. ####: #########: ##. #: ##: ##...::::")
        print(" ##::: ##: ##:::: ##: ##:::::::::::::'##::: ##:::: ##:. ###: ##.... ##: ##:.:: ##: ##:::::::")
        print(". ######::. #######:: ########:::::::. ######::::: ##::. ##: ##:::: ##: ##:::: ##: ########:")
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
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')

def loadgame():
        clearscreen()
        print('Loading music from: ')
        print(' ')
        makelist(1,mediapath1)
        makelist(2,mediapath2)
        makelist(3,mediapath3)
        makelist(4,mediapath4)
        makelist(5,mediapath5)
        if len(mp3s) == 0:
            print('????? No songs loaded in game...')
            print('????? Check folder locations...')
            exitbanner()
            sys.exit(0)
        print(' ')
        print('shuffling ' + str(len(mp3s)) + ' total songs...')
        random.shuffle(mp3s)
        input('...press enter to begin the game!')

# let's begin
def main(mp3s):
        picklist = 0
        for j in range(0,len(mp3s)-1):
            for i in range(0,len(mp3s[j])-1):
                if picklist == 0:
                    status = True
                    while status:
                        clearscreen()
                        print('-------------------------------------')
                        print('Select which song list:')
                        print('  (a) ' + mediapath1.split('/')[-2])
                        print('  (b) ' + mediapath2.split('/')[-2])
                        print('  (c) ' + mediapath3.split('/')[-2])
                        print('  (d) ' + mediapath4.split('/')[-2])
                        print('  (e) ' + mediapath5.split('/')[-2])
                        print('Pick a, b, c, d, e, (h)elp, or (q)uit')
                        response = input('[a/b/c/d/e/h/q] enter: ')
                        if 'q' in response:
                            exitbanner()
                            sys.exit(0)
                        elif 'h' in response:
                            help()
                            continue
                        elif 'a' in response:
                            picklist = 1
                            status = False
                        elif 'b' in response:
                            picklist = 2
                            status = False
                        elif 'c' in response:
                            picklist = 3
                            status = False
                        elif 'd' in response:
                            picklist = 4
                            status = False
                        elif 'e' in response:
                            picklist = 5
                            status = False
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
                    print('(a)nswer, (c)heat, (w)hole song, (n)ext song, (h)elp, or (q)uit')
                    response = input('[a/c/w/n/h/q] then enter: ')
                    print('----------')
                    if 'q' in response:
                        exitbanner()
                        sys.exit(0)
                    elif 'h' in response:
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

