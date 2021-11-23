#!/usr/bin/env python3

# requires mpv

import os
import sys
import random

version = '0.1.1'

# --------------------
# configuration start

# song format extension
song_ext = '.mp3'

# number of seconds to play
clipsec = 5
cheatsec = 10

# name your file of directories below
songfile = 'songs'

# configuration end
# --------------------

def makelist(listnum,listpath):
    """
    create indexed list of songs
    """
    songnum = 0
    for root, dir, files in os.walk(listpath):
        for name in files:
            if name[-4:].lower() == song_ext:
                path = os.path.join(root,name)
                songnum = songnum + 1
                songs.append([listnum,songnum,path])
    if pickcount(songs,listnum) > 0:
        print('  (' + str(pickcount(songs,listnum)) + ' of ' + str(len(songs)) + ')' + listpath)
        menu['menu'+ str(listnum)]['song_total'] = pickcount(songs,listnum)
    else:
        print('  *no music* ' + listpath)
    return songs

def getlocations():
    """
    create indexed list of music folders
    """
    pathlist = []
    global menu
    menu = {}
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
                    if pathnum < 10 and os.path.isdir(line):
                        pathnum = pathnum + 1
                        pathlist.append([pathnum,line])
                        menu['menu'+ str(pathnum)] = {'pick_num': pathnum, 'song_total': 0, 'song_group': pathlist[pathnum - 1][1].split('/')[-2], 'folder_path': line}
        print('loading music from: ')
        print(' ')
        for k in range(0,len(pathlist)):
            for q in range(0,len(pathlist[k])):
                continue
            makelist(pathlist[k][0], pathlist[k][1])
    else:
        print('* error: could not find file [' + songfile + ']') 
        print('* error: check current directory')
        sys.exit(0)
    return

def pickcount(songs,pick):
    """
    count number of songs in specific index
    """
    num = [row[0] for row in songs]
    return num.count(pick)

def songinfo(song,info):
    """
    get mp3 tag using mpv
    """
    songdata = os.popen ('mpv "%s" --display-tags=album,artist,title --audio=no --video=no' % song).readlines()
    for line in songdata:
        if info in line:
          return line

def clearscreen():
    """
    clear the screen with os call
    """
    if os.name == "posix":
        # Linux, Unix, MacOS, Solaris
        os.system('clear')
    else:
        # Windows
        os.system('cls')

def gamebanner():
    """
    create the game banner
    """
    clearscreen()
    print(' ')
    print(":'##::: ##::::'###::::'##::::'##:'########:::::::::::::::::::::")
    print(": ###:: ##:::'## ##::: ###::'###: ##.....::::::::::::::::::::::")
    print(": ####: ##::'##:. ##:: ####'####: ##:::::::::::::::::::::::::::")
    print(": ## ## ##:'##:::. ##: ## ### ##: ######:::::::::::::::::::::::")
    print(": ##. ####: #########: ##. #: ##: ##...::::::::::::::::::::::::")
    print(": ##:. ###: ##.... ##: ##:.:: ##: ##:::::::::::::::::::::::::::")
    print(": ##::. ##: ##:::: ##: ##:::: ##: ########:::::::::::::::::::::")
    print(":..::::..::..:::::..::..:::::..::........::::::::::::::::::::::")
    print(":::::::::'########:'##::::'##::::'###::::'########:::::::::::::")
    print(":::::::::... ##..:: ##:::: ##:::'## ##:::... ##..::::::::::::::")
    print(":::::::::::: ##:::: ##:::: ##::'##:. ##::::: ##::::::::::::::::")
    print(":::::::::::: ##:::: #########:'##:::. ##:::: ##::::::::::::::::")
    print(":::::::::::: ##:::: ##.... ##: #########:::: ##::::::::::::::::")
    print(":::::::::::: ##:::: ##:::: ##: ##.... ##:::: ##::::::::::::::::")
    print(":::::::::::: ##:::: ##:::: ##: ##:::: ##:::: ##::::::::::::::::")
    print("::::::::::::..:::::..:::::..::..:::::..:::::..:::::::::::::::::")
    print("::::::::::::::::::::'########:'##::::'##:'##::: ##:'########:::")
    print("::::::::::::::::::::... ##..:: ##:::: ##: ###:: ##: ##.....::::")
    print("::::::::::::::::::::::: ##:::: ##:::: ##: ####: ##: ##:::::::::")
    print("::::::::::::::::::::::: ##:::: ##:::: ##: ## ## ##: ######:::::")
    print("::::::::::::::::::::::: ##:::: ##:::: ##: ##. ####: ##...::::::")
    print("::::::::::::::::::::::: ##:::: ##:::: ##: ##:. ###: ##:::::::::")
    print("::::::::::::::::::::::: ##::::. #######:: ##::. ##: ########:::")
    print(":::::::::::::::::::::::..::::::.......:::..::::..::........::::")
    print('    v.' + version)
    input('                                  Press enter to begin...')
    print(' ')

def exitbanner():
    """
    end the game with a thank you
    """
    clearscreen()
    print(' ')
    print('-' * 20)
    print(' Thanks for playing ')
    print('-' * 20)
    print(' ')

def help():
    clearscreen()
    print(' ')
    print('Help: To select a song to hear:')
    print('Help:   (a - i)    - pick a song group')
    print('Help:   (r)        - pick a random song')
    print('Help:   (o)        - override mode (continuous play)')
    print('Help: ')
    print('Help: To hear the first ' + str(clipsec) + ' seconds of a song:')
    print('Help:   (spacebar) - when ready, press spacebar to hear the song')
    print('Help: ')
    print('Help: After hearing the song:')
    print('Help:   (a) answer   - reveal the artist and title of a song')
    print('Help:   (r) replay   - hear the first '+ str(clipsec) + ' seconds of a song')
    print('Help:   (c) cheat    - hear the first '+ str(clipsec + cheatsec) + ' seconds of a song')
    print('Help:   (w) whole    - hear the whole song (artist/title are hidden)')
    print('Help:   (p) play     - hear the whole song (reveals song info)')
    print('Help:   (n) next     - go to next song group selection')
    print('Help: ')
    print('Help:   (q) quit     - quit game')
    print(' ')
    input('Press enter to exit help')
    clearscreen()

def loadmenu():
    """
    create the selection menu
    """
    clearscreen()
    print('=' * 50)
    global menu_opts
    menu_opts = []
    print('Select one of the ' + str(len(songs)) + ' following songs: ')
    print('-' * 20)
    if menu.get('menu1'):
        if menu['menu1']['song_total'] > 0:
            print('( a )', menu['menu1']['song_group'], '(' + str(menu['menu1']['song_total']) + ' songs)')
            menu_opts.append('a')
    if menu.get('menu2'):
        if menu['menu2']['song_total'] > 0:
            print('( b )', menu['menu2']['song_group'], '(' + str(menu['menu2']['song_total']) + ' songs)')
            menu_opts.append('b')
    if menu.get('menu3'):
        if menu['menu3']['song_total'] > 0:
            print('( c )', menu['menu3']['song_group'], '(' + str(menu['menu3']['song_total']) + ' songs)')
            menu_opts.append('c')
    if menu.get('menu4'):
        if menu['menu4']['song_total'] > 0:
            print('( d )', menu['menu4']['song_group'], '(' + str(menu['menu4']['song_total']) + ' songs)')
            menu_opts.append('d')
    if menu.get('menu5'):
        if menu['menu5']['song_total'] > 0:
            print('( e )', menu['menu5']['song_group'], '(' + str(menu['menu5']['song_total']) + ' songs)')
            menu_opts.append('e')
    if menu.get('menu6'):
        if menu['menu6']['song_total'] > 0:
            print('( f )', menu['menu6']['song_group'], '(' + str(menu['menu6']['song_total']) + ' songs)')
            menu_opts.append('f')
    if menu.get('menu7'):
        if menu['menu7']['song_total'] > 0:
            print('( g )', menu['menu7']['song_group'], '(' + str(menu['menu7']['song_total']) + ' songs)')
            menu_opts.append('g')
    if menu.get('menu8'):
        if menu['menu8']['song_total'] > 0:
            print('( h )', menu['menu8']['song_group'], '(' + str(menu['menu8']['song_total']) + ' songs)')
            menu_opts.append('h')
    if menu.get('menu9'):
        if menu['menu9']['song_total'] > 0:
            print('( i )', menu['menu9']['song_group'], '(' + str(menu['menu9']['song_total']) + ' songs)')
            menu_opts.append('i')
    menu_opts.append('r')
    menu_opts.append('o')
    menu_opts.append('?')
    menu_opts.append('q')
    print('( r ) Random song')
    print('( o ) Override mode')
    print('( ? ) help')
    print('( q ) quit game')
    print('-' * 20)

def loadgame():
    """
    get the music folders, load the songs, then shuffle 3 times
    """
    global songs
    songs = []
    gamebanner()
    clearscreen()
    getlocations()
    if len(songs) == 0:
        print('* error: No songs loaded in game...')
        print('* error: Check file for correct directory paths...')
        sys.exit(0)
    print(' ')
    print('shuffling ' + str(len(songs)) + ' total songs...')
    random.shuffle(songs)
    random.shuffle(songs)
    random.shuffle(songs)

def override():
    for k in songs:
        if k[0] in range(1,9):
             catalog = ' catalog: ' +  k[2].split('/')[-1].split(' - ')[0]
             clearscreen()
             print('=' * 50)
             print(' ')
             print(catalog)
             print(' ')
             print(' listen to the whole song,')
             print(' or [space] to pause,')
             print(' or [left](rewind) / [right](forward),')
             print(' or [q]uit song, for answer')
             print(' ')
             print('=' * 50)
             os.system('mpv --really-quiet --start=0 ' + '"' +  k[2] + '"')
             answer_title = songinfo(k[2],'title:')
             answer_artist = songinfo(k[2],'artist:')
             clearscreen()
             print('=' * 50)
             print(' ')
             print(catalog)
             print(' ')
             print(answer_title)
             print(answer_artist)
             print('=' * 50)
             print(' ')
             response = input(' press enter for next song, or q to quit: ')
             if 'q' in response:
                 exitbanner()
                 sys.exit(0)
             else:
                 continue
    exitbanner()
    sys.exit(0)

def main():
    """
    let's have some fun
    """
    loadgame()
    picklist = 0
    for j in range(0,len(songs)-1):
        if picklist == 0:
            status = True
            while status:
                loadmenu()
                print('Pick an option: ')
                print(menu_opts)
                response = input('then press enter: ')
                if response in menu_opts:
                    if 'q' in response:
                        exitbanner()
                        sys.exit(0)
                    elif '?' in response:
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
                    elif 'f' in response:
                        picklist = 6
                        status = False
                    elif 'g' in response:
                        picklist = 7
                        status = False
                    elif 'h' in response:
                        picklist = 8
                        status = False
                    elif 'i' in response:
                        picklist = 9
                        status = False
                    elif 'r' in response:
                        picklist = random.randint(1,9)
                        while pickcount(songs,picklist) == 0:
                            picklist = random.randint(1,9)
                        status = False
                    elif 'o' in response:
                        override()
                        status = False
                    else:
                        continue
        if songs[j][0] == picklist:
            picklist = 0
        else:
            continue
        print('-' * 20)
        print('Press spacebar to hear the song...')
        os.system('mpv --really-quiet --pause --start=0 --end=' + str(clipsec + 1) + ' "' +  songs[j][2] + '"')
        # load answer
        answer_title = songinfo(songs[j][2],'title:')
        answer_artist = songinfo(songs[j][2],'artist:')
        status2 = True
        while status2:
            clearscreen()
            print('=' * 50)
            print('Select one of the following:')
            print('-' * 20)
            print('( a ) answer     [artist/title revealed]')
            print('( r ) replay     [first ' + str(clipsec) + ' seconds]')
            print('( c ) cheat      [first ' + str(clipsec + cheatsec) + ' seconds]')
            print('( w ) whole song [press q to stop]')
            print('( p ) play song  [artist/title revealed]')
            print('( n ) next song')
            print('( ? ) help')
            print('( q ) quit')
            print('-' * 20)
            print("Pick ['a','r','c','w','p','n','?','q']")
            response = input('then press enter: ')
            if 'q' in response:
                exitbanner()
                sys.exit(0)
            elif '?' in response:
                help()
                continue
            elif 'a' in response:
                clearscreen()
                print('=' * 50)
                print(' ')
                print(' menu:', menu['menu'+ str(songs[j][0])]['song_group'])
                print(' ')
                print(answer_title)
                print(answer_artist)
                print(' ')
                print('=' * 50)
                input('...press enter to continue')
            elif 'r' in response:
                os.system('mpv --really-quiet --start=0 --end=' + str(clipsec + 1) + ' "' +  songs[j][2] + '"')
            elif 'c' in response:
                os.system('mpv --really-quiet --start=0 --end=' + str(clipsec + cheatsec + 1) + ' "' +  songs[j][2] + '"')
            elif 'w' in response:
                os.system('mpv --really-quiet --start=0 ' + '"' +  songs[j][2] + '"')
            elif 'p' in response:
                os.system('mpv "' +  songs[j][2] + '"')
            elif 'n' in response:
                status2 = False
            else:
                continue

if __name__ == '__main__':

    main()

