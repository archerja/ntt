#!/usr/bin/env python3

# requires mpv
# https://mpv.io

import os
import sys
import random
import configparser

version = '0.1.5'

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

def exitbanner():
    """
    end the game with a thank you
    """
    clearscreen()
    print(' ')
    print('-' * 20)
    print(' ')
    response = input('Are you sure you want to quit? (Y/y) ')
    if 'Y' in response.upper():
        clearscreen()
        print(' ')
        print('-' * 20)
        print(' Thanks for playing ')
        print('-' * 20)
        print(' ')
        sys.exit(0)

def systemshutdown():
    """
    completely shutdown the computer
    """
    clearscreen()
    print(' ')
    print('-' * 20)
    response = input('Turn the computer off? (Y/y) ')
    if 'Y' in response.upper():
        if os.name == "posix":
            # Linux, Unix, MacOS, Solaris
            os.system('shutdown -h now')
        else:
            # Windows
            os.system('shutdown /s')
        sys.exit(0)

def help():
    clearscreen()
    print(' ')
    print('Help: To select a song to hear:')
    print('Help:   (a - i)    - pick a song group')
    print('Help:   (r)        - pick a random song')
    print('Help:   (o)        - override mode (continuous play)')
    print('Help:   (s)        - re-shuffle all songs')
    print('Help:   (t)        - team menu (hide/show/rename/score)')
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
    print('Help:   (x) exit     - turn off the computer')
    print(' ')
    input('Press enter to exit help')
    clearscreen()

def checkmpv():
    """
    check that required mpv is installed
    """
    if os.name == "posix":
        # Linux, Unix, MacOS, Solaris
        chkmpv = os.system('which mpv')
    else:
        # Windows
        chkmpv = os.system('where mpv')
    if chkmpv != 0:
       print('* error: could not find mpv executable') 
       print('* error: make sure mpv is installed')
       sys.exit(0)

def loadconfig():
    """
    load variables from config file
    """
    global ini_version
    global shuffle_count
    global debug
    global song_path
    global song_ext
    global clipsec
    global cheatsec
    global teamshow
    global team1name
    global team1score
    global team2name
    global team2score

    if str(os.path.exists('ntt.ini')) == 'True':
        config = configparser.ConfigParser()
        config.read('ntt.ini')
        
        ini_version = config.get('app','ini_version')
        shuffle_count = config.getint('app','shuffle_count')
        debug = config.getboolean('app','debug')
        song_path = config.get('song','song_path')
        song_ext = config.get('song','song_ext')
        clipsec = config.getint('song','clipsec')
        cheatsec = config.getint('song','cheatsec')
    
        teamshow = config.getboolean('team','teamshow')
        team1name = config.get('team','team1name')
        team1score = config.getint('team','team1score')
        team2name = config.get('team','team2name')
        team2score = config.getint('team','team2score')

        #debug...
        if debug:
            print('debug...')
            for section_name in config.sections():
                print('Section:', section_name)
                #print('  Options:', config.options(section_name))
                for name, value in config.items(section_name):
                    print('  %s = %s' % (name, value))
            input('...debug')
        #...debug

    else:
        print('* error: could not find ntt.ini') 
        response = input('Do you want to create the config file? (Y/y) ')
        if 'Y' in response.upper():
            ini_version = version
            shuffle_count = 3
            debug = False
            song_ext = '.mp3'
            clipsec = 5
            cheatsec = 10
            song_path = 'music'
            teamshow = False
            team1name = 'Gals'
            team1score = '0'
            team2name = 'Guys'
            team2score = '0'
            saveconfig() 
        sys.exit(0)

def saveconfig():
    """
    save variables to config file
    """
    config = configparser.ConfigParser()
    config.read('ntt.ini')

    if not config.has_section('app'):
        config.add_section('app')
    if not config.has_section('song'):
        config.add_section('song')
    if not config.has_section('team'):
        config.add_section('team')

    config['app']['ini_version'] = ini_version
    config['app']['shuffle_count'] = str(shuffle_count)
    if debug:
        config['app']['debug'] = 'True'
    else:
        config['app']['debug'] = 'False'

    config['song']['song_path'] = song_path
    config['song']['song_ext'] = song_ext
    config['song']['clipsec'] = str(clipsec)
    config['song']['cheatsec'] = str(cheatsec)

    if teamshow:
       config['team']['teamshow'] = 'True'
    else:
       config['team']['teamshow'] = 'False'
    config['team']['team1name'] = team1name
    config['team']['team1score'] = str(team1score)
    config['team']['team2name'] = team2name
    config['team']['team2score'] = str(team2score)

    with open('ntt.ini', 'w') as newini:
       config.write(newini)

def teamscores():
    """
    display team names and scores
    """
    global teamshow
    if teamshow:
        print('=' * 60)
        print(team1name.center(25) + ' vs '.center(10) + team2name.center(25))
        print(str(team1score).center(25) + ' '.center(10) + str(team2score).center(25))

def teammenu():
    global teamshow
    global team1name
    global team2name
    global team1score
    global team2score
    status3 = True
    while status3:
        clearscreen()
        teamscores()
        print('=' * 60)
        print('Select one of the following:')
        print('-' * 20)
        print('( 1 ) change score for ' + team1name)
        print('( 2 ) change score for ' + team2name)
        print(' ')
        print('( 3 ) change team name for ' + team1name)
        print('( 4 ) change team name for ' + team2name)
        print('( 5 ) show/hide teams on menus ')
        print(' ')
        print('( r ) reset scores/names/hide')
        print('( s ) save, and go back to game')
        print('-' * 20)
        print("Pick ['1','2','3','4','5','r','s']")
        response = input('then press enter: ')
        if 's' in response:
            saveconfig()
            status3 = False
        elif 'r' in response:
            team1name = 'Gals'
            team1score = 0
            team2name = 'Guys'
            team2score = 0
            teamshow = False
            continue
        elif '?' in response:
            help()
            continue
        elif '1' in response:
            newscore = input('enter new score: ')
            team1score = newscore
            continue
        elif '2' in response:
            newscore = input('enter new score: ')
            team2score = newscore
            continue
        elif '3' in response:
            newname = input('enter new name: ')
            team1name = newname
            continue
        elif '4' in response:
            newname = input('enter new name: ')
            team2name = newname
            continue
        elif '5' in response:
            if teamshow:
                teamshow = False
            else:
                teamshow = True
            continue
        else:
            continue

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
    dirlist = [os.path.join(song_path, filename) for filename in os.listdir(song_path)]
    dirlist.sort()

    #debug...
    if debug:
        print('debug...')
        #cwd = os.getcwd()
        #print(cwd)
        print(dirlist)
        input('...debug')
    #...debug

    for dlist in dirlist:
        if pathnum < 10 and os.path.isdir(dlist):
            pathnum = pathnum + 1
            pathlist.append([pathnum,dlist])
            menu['menu'+ str(pathnum)] = {'pick_num': pathnum, 'song_total': 0, 'song_group': pathlist[pathnum - 1][1].split('/')[-1], 'folder_path': dlist}

    #debug...
    if debug:
        print('debug...')
        for x in range(len(pathlist)):
            print(pathlist[x])
        input('...debug')
    #...debug

    print('loading music from: ')
    print(' ')
    for k in range(0,len(pathlist)):
        makelist(pathlist[k][0], pathlist[k][1])

    #debug...
    if debug:
        print(' ')
        print('debug...')
        for key, value in menu.items():
            print(key, '::')
            for p, s in value.items():
                print(p, ' : ', s)
        input('...debug')
    #...debug

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

def override():
    for k in songs:
        if k[0] in range(1,9):
             catalog = ' catalog: ' +  k[2].split('/')[-1].split(' - ')[0]
             clearscreen()
             print('=' * 60)
             print(' ')
             print(catalog)
             print(' ')
             print(' listen to the whole song,')
             print(' or [space] to pause,')
             print(' or [left](rewind) / [right](forward),')
             print(' or [q]uit playing the song, reveal the answer')
             print(' ')
             print('=' * 60)

             #debug...
             if debug:
                 print('debug...')
                 print(k)
                 input('...debug')
             #...debug

             os.system('mpv --ao=alsa --no-audio-display --really-quiet --start=0 ' + '"' +  k[2] + '"')
             answer_title = songinfo(k[2],'title:')
             answer_artist = songinfo(k[2],'artist:')
             clearscreen()
             print('=' * 60)
             print(' ')
             print(catalog)
             print(' ')
             print(answer_title)
             print(answer_artist)
             print('=' * 60)
             print(' ')
             response = input(' press enter for the next song, or q to quit: ')
             if 'q' in response:
                 exitbanner()
             else:
                 continue
    exitbanner()

def loadmenu():
    """
    create the selection menu
    """
    clearscreen()
    teamscores()
    print('=' * 60)
    global menu_opts
    global menu_extras
    menu_opts = []
    menu_extras = ['o','s','t','?','q','x']
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
    menu_opts.append('s')
    menu_opts.append('t')
    menu_opts.append('?')
    menu_opts.append('q')
    menu_opts.append('x')
    print('-' * 10)
    print('( r ) Random song    ( o ) Override mode    ( t ) Team menu')
    print('( ? ) help           ( q ) quit game        ( x ) Shutdown')
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
    shuffle_songs()

def shuffle_songs():
    clearscreen()
    print('shuffling ' + str(len(songs)) + ' total songs...')
    for s in range(0,shuffle_count):
        print('shuffling...')
        random.shuffle(songs)
    print('... all songs are shuffled ...')
    if debug:
        input('...debug')

def main():
    """
    let's have some fun
    """
    loadconfig()
    checkmpv()
    loadgame()
    picklist = 0
    for j in range(0,len(songs)-1):
        if picklist == 0:
            status = True
            while status:
                loadmenu()
                print('Pick an option: ')
                print('  ', [item for item in menu_opts if item not in menu_extras])
                print('  ', menu_extras)
                response = input('then press enter: ')
                if response in menu_opts:
                    if 'q' in response:
                        exitbanner()
                    elif 'x' in response:
                        systemshutdown()
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
                    elif 's' in response:
                        shuffle_songs()
                        input('... press enter when ready ...')
                        status = False
                    elif 't' in response:
                        teammenu()
                        continue
                    else:
                        continue
        if songs[j][0] == picklist:
            picklist = 0
        else:
            continue

        #debug...
        if debug:
            print('debug...')
            print(j, ' - ', songs[j][2])
            input('...debug')
        #...debug

        print('-' * 20)
        print('Press spacebar to hear the song...')
        os.system('mpv --ao=alsa --no-audio-display --really-quiet --pause --start=0 --end=' + str(clipsec + 1) + ' "' +  songs[j][2] + '"')
        # load answer
        answer_title = songinfo(songs[j][2],'title:')
        answer_artist = songinfo(songs[j][2],'artist:')
        status2 = True
        while status2:
            clearscreen()
            teamscores()
            print('=' * 60)
            print('Select one of the following:')
            print('-' * 20)
            print('( a ) answer          [artist/title revealed]')
            print('( r ) replay          [first ' + str(clipsec) + ' seconds]')
            print('( c ) cheat           [first ' + str(clipsec + cheatsec) + ' seconds]')
            print('( w ) whole song      [press q to stop]')
            print('( p ) play song       [artist/title revealed]')
            print('( n ) next song       [return to group selection menu]')
            print('( t ) team menu       [hide/show/rename/score]')
            print('( ? ) help')
            print('( q ) quit')
            print('-' * 20)
            print("Pick ['a','r','c','w','p','n','t','?','q']")
            response = input('then press enter: ')
            if 'q' in response:
                exitbanner()
            elif '?' in response:
                help()
                continue
            elif 't' in response:
                teammenu()
                continue
            elif 'a' in response:
                clearscreen()
                print('=' * 60)
                print(' ')
                print(' menu:', menu['menu'+ str(songs[j][0])]['song_group'])
                print(' ')
                print(answer_title)
                print(answer_artist)
                print(' ')
                print('=' * 60)
                input('...press enter to continue')
            elif 'r' in response:
                os.system('mpv --ao=alsa --no-audio-display --really-quiet --start=0 --end=' + str(clipsec + 1) + ' "' +  songs[j][2] + '"')
            elif 'c' in response:
                os.system('mpv --ao=alsa --no-audio-display --really-quiet --start=0 --end=' + str(clipsec + cheatsec + 1) + ' "' +  songs[j][2] + '"')
            elif 'w' in response:
                os.system('mpv --ao=alsa --no-audio-display --really-quiet --start=0 ' + '"' +  songs[j][2] + '"')
            elif 'p' in response:
                os.system('mpv --ao=alsa --no-audio-display "' +  songs[j][2] + '"')
            elif 'n' in response:
                status2 = False
            else:
                continue

if __name__ == '__main__':

    main()


