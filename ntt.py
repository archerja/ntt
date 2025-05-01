#!/usr/bin/env python3

# requires mpv
# https://mpv.io

import os
import sys
import random
import configparser

version = '0.1.7'

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
    print('    version: ' + version + '               Check your volume...')
    playintro()
    input('                                      Press enter to begin...')
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
    response = input('Are you sure you want to quit? (N/y) ')
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
    response = input('Turn the computer off? (N/y) ')
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
       print('* NTT error: could not find mpv executable') 
       print('* NTT error: make sure mpv is installed')
       print('* NTT error: https://mpv.io')
       sys.exit(0)

def playintro():
    """
    use mpv to play intro song to adjust volume
    """
    os.system('mpv --ao=alsa --no-audio-display --really-quiet --start=0 --end=' + str(introsec + 1) + ' "' +  intro_song + '"')
    return

# -----------------------------------------------------------

def loadconfig():
    """
    load variables from config file
    """
    global ini_version
    global debug
    global intro_song
    global introsec
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
        debug = config.getboolean('app','debug')
        intro_song = config.get('app','intro_song')
        introsec = config.getint('app','introsec')
        song_path = config.get('song','song_path')
        song_ext = config.get('song','song_ext')
        clipsec = config.getint('song','clipsec')
        cheatsec = config.getint('song','cheatsec')
    
        teamshow = config.getboolean('team','teamshow')
        team1name = config.get('team','team1name')
        team1score = config.getint('team','team1score')
        team2name = config.get('team','team2name')
        team2score = config.getint('team','team2score')

    else:
        print('* NTT error: could not find ntt.ini') 
        response = input('Do you want to create the config file? (N/y) ')
        if 'Y' in response.upper():
            ini_version = version
            debug = False
            intro_song = 'intro.mp3'
            introsec = 17
            song_ext = '.mp3'
            clipsec = 5
            cheatsec = 10
            song_path = 'music'
            teamshow = True
            team1name = 'Gals'
            team1score = '0'
            team2name = 'Guys'
            team2score = '0'
            saveconfig() 
            print('Config file created. Please restart program.')
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
    if debug:
        config['app']['debug'] = 'True'
    else:
        config['app']['debug'] = 'False'
    config['app']['intro_song'] = intro_song
    config['app']['introsec'] = str(introsec)

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

# -----------------------------------------------------------

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
            teamshow = True
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

# -----------------------------------------------------------

def getSongList():
    """
    create indexed list of songs
    """
    global menu
    menu = {}
    songIndex = 0
    indexNum = 0
    if os.path.isdir(song_path):
        dirList = [os.path.join(song_path, filename) for filename in os.listdir(song_path)]
        dirList.sort()
    else:
        print('* NTT error: music directory not found!')
        print('* NTT error: configuration file shows it as: ')
        print('* NTT error: ' + song_path)
        sys.exit(0)
    tempSongs = []
    indexed = True
    selected = False
    for dlist in dirList:
        if indexed:
            indexNum += 1
        if indexNum < 10 and os.path.isdir(dlist):
            songNum = 0
            tempSongs.clear()
            for root, dir, files in os.walk(dlist):
                dir.sort()
                for name in sorted(files):
                    if name[-4:].lower() == song_ext:
                        path = os.path.join(root,name)
                        songNum += 1
                        songIndex += 1
                        tempSongs.append([songIndex,indexNum,songNum,path,selected])
                if len(tempSongs) > 0:
                    songs.extend(tempSongs)
                    tempSongs.clear()
                    indexed = True
                    menu['menu'+ str(indexNum)] = {'indexNum': indexNum, 'songTotal': songNum, 'songGroup': dlist.split('/')[-1], 'folderPath': dlist}
                else:
                    indexed = False
    return songs

def songSelected(idx,song):
    x = [x for x in songs if x[1] == idx and x[2] == song]
    xx = x[0][0] - 1
    songs[xx][4] = True
    songsPlayed()

def songsPlayed():
    global played
    played = []
    played.clear()
    played = [x for x in songs if x[4] == True]

def songinfo(song,info):
    """
    get mp3 tag using mpv
    """
    songData = os.popen ('mpv "%s" --display-tags=album,artist,title --audio=no --video=no' % song).readlines()
    for line in songData:
        if info in line:
          return line

def override():
    overidden = True
    while overidden:
        randPick = random.randint(1,len(songs))
        picked = songs[randPick][1]
        randSong = songs[randPick][2]
        pickedSong = [x for x in songs if x[1] == picked and x[2] == randSong]
        catalog = ' catalog: ' +  pickedSong[0][3].split('/')[-1].split(' - ')[0]
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

        os.system('mpv --ao=alsa --no-audio-display --really-quiet --start=0 ' + '"' + pickedSong[0][3]  + '"')
        answerTitle = songinfo(pickedSong[0][3],'title:')
        answerArtist = songinfo(pickedSong[0][3],'artist:')
        clearscreen()
        print('=' * 60)
        print(' ')
        print(catalog)
        print(' ')
        print(answerTitle)
        print(answerArtist)
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
    menu_extras = ['o','t','?','q','x','u']
    print('Select one of the ' +  str(len(songs)) + ' following songs: ' + str(len(played)) + ' played')
    print('-' * 20)
    if menu.get('menu1'):
        if menu['menu1']['songTotal'] > 0:
            availSongs = [x for x in songs if x[1] == 1 and x[4] == False]
            print('( a )', menu['menu1']['songGroup'], '(' + str(len(availSongs)) + '/' + str(menu['menu1']['songTotal']) + ' songs)')
            if len(availSongs) > 0:
                menu_opts.append('a')
    if menu.get('menu2'):
        if menu['menu2']['songTotal'] > 0:
            availSongs = [x for x in songs if x[1] == 2 and x[4] == False]
            print('( b )', menu['menu2']['songGroup'], '(' + str(len(availSongs)) + '/' + str(menu['menu2']['songTotal']) + ' songs)')
            if len(availSongs) > 0:
                menu_opts.append('b')
    if menu.get('menu3'):
        if menu['menu3']['songTotal'] > 0:
            availSongs = [x for x in songs if x[1] == 3 and x[4] == False]
            print('( c )', menu['menu3']['songGroup'], '(' + str(len(availSongs)) + '/' + str(menu['menu3']['songTotal']) + ' songs)')
            if len(availSongs) > 0:
                menu_opts.append('c')
    if menu.get('menu4'):
        if menu['menu4']['songTotal'] > 0:
            availSongs = [x for x in songs if x[1] == 4 and x[4] == False]
            print('( d )', menu['menu4']['songGroup'], '(' + str(len(availSongs)) + '/' + str(menu['menu4']['songTotal']) + ' songs)')
            if len(availSongs) > 0:
                menu_opts.append('d')
    if menu.get('menu5'):
        if menu['menu5']['songTotal'] > 0:
            availSongs = [x for x in songs if x[1] == 5 and x[4] == False]
            print('( e )', menu['menu5']['songGroup'], '(' + str(len(availSongs)) + '/' + str(menu['menu5']['songTotal']) + ' songs)')
            if len(availSongs) > 0:
                menu_opts.append('e')
    if menu.get('menu6'):
        if menu['menu6']['songTotal'] > 0:
            availSongs = [x for x in songs if x[1] == 6 and x[4] == False]
            print('( f )', menu['menu6']['songGroup'], '(' + str(len(availSongs)) + '/' + str(menu['menu6']['songTotal']) + ' songs)')
            if len(availSongs) > 0:
                menu_opts.append('f')
    if menu.get('menu7'):
        if menu['menu7']['songTotal'] > 0:
            availSongs = [x for x in songs if x[1] == 7 and x[4] == False]
            print('( g )', menu['menu7']['songGroup'], '(' + str(len(availSongs)) + '/' + str(menu['menu7']['songTotal']) + ' songs)')
            if len(availSongs) > 0:
                menu_opts.append('g')
    if menu.get('menu8'):
        if menu['menu8']['songTotal'] > 0:
            availSongs = [x for x in songs if x[1] == 8 and x[4] == False]
            print('( h )', menu['menu8']['songGroup'], '(' + str(len(availSongs)) + '/' + str(menu['menu8']['songTotal']) + ' songs)')
            if len(availSongs) > 0:
                menu_opts.append('h')
    if menu.get('menu9'):
        if menu['menu9']['songTotal'] > 0:
            availSongs = [x for x in songs if x[1] == 9 and x[4] == False]
            print('( i )', menu['menu9']['songGroup'], '(' + str(len(availSongs)) + '/' + str(menu['menu9']['songTotal']) + ' songs)')
            if len(availSongs) > 0:
                menu_opts.append('i')
    menu_opts.append('r')
    menu_opts.append('o')
    menu_opts.append('t')
    menu_opts.append('u')
    menu_opts.append('?')
    menu_opts.append('q')
    menu_opts.append('x')
    print('-' * 10)
    print('( r ) Random song    ( o ) Override mode    ( t ) Team menu')
    print('( ? ) help           ( q ) quit game        ( x ) Shutdown')
    print('-' * 20)

def loadgame():
    """
    get the music folders, load the songs
    """
    global songs
    songs = []
    gamebanner()
    clearscreen()
    getSongList()
    if len(songs) == 0:
        print('* error: No songs loaded in game...')
        print('* error: Check for correct directory paths...')
        sys.exit(0)
    songsPlayed()

def main():
    """
    let's have some fun
    """
    checkmpv()
    loadconfig()
    loadgame()
    picked = 0
    gameOn = True
    status = True
    while gameOn:
        pickedSong = []
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
                    picked = 1
                    while not pickedSong:
                        randSong = random.randint(1,menu['menu'+ str(picked)]['songTotal'])
                        pickedSong = [x for x in songs if x[1] == picked and x[2] == randSong and x[4] == False]
                    status = False
                elif 'b' in response:
                    picked = 2
                    while not pickedSong:
                        randSong = random.randint(1,menu['menu'+ str(picked)]['songTotal'])
                        pickedSong = [x for x in songs if x[1] == picked and x[2] == randSong and x[4] == False]
                    status = False
                elif 'c' in response:
                    picked = 3
                    while not pickedSong:
                        randSong = random.randint(1,menu['menu'+ str(picked)]['songTotal'])
                        pickedSong = [x for x in songs if x[1] == picked and x[2] == randSong and x[4] == False]
                    status = False
                elif 'd' in response:
                    picked = 4
                    while not pickedSong:
                        randSong = random.randint(1,menu['menu'+ str(picked)]['songTotal'])
                        pickedSong = [x for x in songs if x[1] == picked and x[2] == randSong and x[4] == False]
                    status = False
                elif 'e' in response:
                    picked = 5
                    while not pickedSong:
                        randSong = random.randint(1,menu['menu'+ str(picked)]['songTotal'])
                        pickedSong = [x for x in songs if x[1] == picked and x[2] == randSong and x[4] == False]
                    status = False
                elif 'f' in response:
                    picked = 6
                    while not pickedSong:
                        randSong = random.randint(1,menu['menu'+ str(picked)]['songTotal'])
                        pickedSong = [x for x in songs if x[1] == picked and x[2] == randSong and x[4] == False]
                    status = False
                elif 'g' in response:
                    picked = 7
                    while not pickedSong:
                        randSong = random.randint(1,menu['menu'+ str(picked)]['songTotal'])
                        pickedSong = [x for x in songs if x[1] == picked and x[2] == randSong and x[4] == False]
                    status = False
                elif 'h' in response:
                    picked = 8
                    while not pickedSong:
                        randSong = random.randint(1,menu['menu'+ str(picked)]['songTotal'])
                        pickedSong = [x for x in songs if x[1] == picked and x[2] == randSong and x[4] == False]
                    status = False
                elif 'i' in response:
                    picked = 9
                    while not pickedSong:
                        randSong = random.randint(1,menu['menu'+ str(picked)]['songTotal'])
                        pickedSong = [x for x in songs if x[1] == picked and x[2] == randSong and x[4] == False]
                    status = False
                elif 'r' in response:
                    while not pickedSong:
                        randAllSongs = random.randint(1,len(songs)-1)
                        picked = songs[randAllSongs][1]
                        randSong = songs[randAllSongs][2]
                        pickedSong = [x for x in songs if x[1] == picked and x[2] == randSong and x[4] == False]
                    status = False
                elif 'o' in response:
                    override()
                    status = False
                elif 'u' in response:
                    for z in played:
                        print(z[3].split('/')[-1])
                    input('...')
                    continue
                elif 't' in response:
                    teammenu()
                    continue
                else:
                    continue

        print('-' * 20)
        print('Press spacebar to hear the song...')
        songSelected(picked,randSong)     
        os.system('mpv --ao=alsa --no-audio-display --really-quiet --pause --start=0 --end=' + str(clipsec + 1) + ' "' +  pickedSong[0][3] + '"')
        # load answer
        answerTitle = songinfo(pickedSong[0][3],'title:')
        answerArtist = songinfo(pickedSong[0][3],'artist:')
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
                print(' menu:', menu['menu'+ str(picked)]['songGroup'])
                print(' ')
                print(answerTitle)
                print(answerArtist)
                print(' ')
                print('=' * 60)
                input('...press enter to continue')
            elif 'r' in response:
                os.system('mpv --ao=alsa --no-audio-display --really-quiet --start=0 --end=' + str(clipsec + 1) + ' "' +  pickedSong[0][3] + '"')
            elif 'c' in response:
                os.system('mpv --ao=alsa --no-audio-display --really-quiet --start=0 --end=' + str(clipsec + cheatsec + 1) + ' "' +  pickedSong[0][3] + '"')
            elif 'w' in response:
                os.system('mpv --ao=alsa --no-audio-display --really-quiet --start=0 ' + '"' +  pickedSong[0][3] + '"')
            elif 'p' in response:
                os.system('mpv --ao=alsa --no-audio-display "' +  pickedSong[0][3] + '"')
            elif 'n' in response:
                picked = 0
                status = True
                status2 = False
            else:
                continue

if __name__ == '__main__':

    main()


