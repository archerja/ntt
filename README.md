
# ntt.py - NAME THAT TUNE

This python3 script will create a menu from a list of local songs to use in a simple "Name That Tune" game.

It works really well with compilation albums (various artists). I use it with a Raspberry Pi connected to my TV. I use a 128 GB SD card, without GUI, and a display resolution of 640x480 60Hz 4:3 (CEA Mode 1).

```
:'##::: ##::::'###::::'##::::'##:'########:::::::::::::::::::::
: ###:: ##:::'## ##::: ###::'###: ##.....::::::::::::::::::::::
: ####: ##::'##:. ##:: ####'####: ##:::::::::::::::::::::::::::
: ## ## ##:'##:::. ##: ## ### ##: ######:::::::::::::::::::::::
: ##. ####: #########: ##. #: ##: ##...::::::::::::::::::::::::
: ##:. ###: ##.... ##: ##:.:: ##: ##:::::::::::::::::::::::::::
: ##::. ##: ##:::: ##: ##:::: ##: ########:::::::::::::::::::::
:..::::..::..:::::..::..:::::..::........::::::::::::::::::::::
:::::::::'########:'##::::'##::::'###::::'########:::::::::::::
:::::::::... ##..:: ##:::: ##:::'## ##:::... ##..::::::::::::::
:::::::::::: ##:::: ##:::: ##::'##:. ##::::: ##::::::::::::::::
:::::::::::: ##:::: #########:'##:::. ##:::: ##::::::::::::::::
:::::::::::: ##:::: ##.... ##: #########:::: ##::::::::::::::::
:::::::::::: ##:::: ##:::: ##: ##.... ##:::: ##::::::::::::::::
:::::::::::: ##:::: ##:::: ##: ##:::: ##:::: ##::::::::::::::::
::::::::::::..:::::..:::::..::..:::::..:::::..:::::::::::::::::
::::::::::::::::::::'########:'##::::'##:'##::: ##:'########:::
::::::::::::::::::::... ##..:: ##:::: ##: ###:: ##: ##.....::::
::::::::::::::::::::::: ##:::: ##:::: ##: ####: ##: ##:::::::::
::::::::::::::::::::::: ##:::: ##:::: ##: ## ## ##: ######:::::
::::::::::::::::::::::: ##:::: ##:::: ##: ##. ####: ##...::::::
::::::::::::::::::::::: ##:::: ##:::: ##: ##:. ###: ##:::::::::
::::::::::::::::::::::: ##::::. #######:: ##::. ##: ########:::
:::::::::::::::::::::::..::::::.......:::..::::..::........::::
    v.0.1.3
                                  Press enter to begin...
```

## Some of the options

* Reads a file with up to 9 different music folders listed.
* Scans each folder, and it's name becomes a separate menu option.
* It is set at a 5 second audio clip, from the beginning of the song.
* It also allows for 10 extra seconds to be added.
* Can play the whole song, with or without revealing the artist and title.
* Play a random song.
* Override mode, for continuous, random play.
* Two team hide/show (with team naming and scoring).

> Note: Settings can be changed in the script itself.

## Background

MPV has a neat feature that allows you to hear a song, without showing anything on the screen. It also lets you open the audio file paused, and only play a certain number of seconds of the file. You can also read the embedded mp3 tags within the audio file.

## Installation

***This script requires:***

 -  [mpv](https://mpv.io) to play the songs, hide the artist/title, and read mp3 tags.

### Configuration

* Place ntt.py and music directory file (songs) in a folder.
* Edit the song file, (default filename is "songs"), and enter the full path to your music folders containing your songs.


## Usage example

```
$ ./ntt.py 
```

#### or

```
$ python3 ntt.py
```

#### Song selection menu
```
============================================================
Select one of the 386 following songs: 
--------------------
( a ) Folder of Rock (160 songs)
( b ) Folder of Country (86 songs)
( c ) 50s Instrumental Hits (60 songs)
( d ) Classical Music (80 songs)
----------
( r ) Random song    ( o ) Override mode    ( t ) Team menu
( ? ) help           ( q ) quit game
--------------------
Pick an option: 
['a', 'b', 'c', 'd','r','o','t','?','q']
then press enter: d
--------------------
Press spacebar to hear the song...
```

#### Optional Teams menu
```
============================================================
           Gals              vs               Guys          
            0                                  0            
============================================================
Select one of the following:
--------------------
( 1 ) change score for Gals
( 2 ) change score for Guys
 
( 3 ) change team name for Gals
( 4 ) change team name for Guys
( 5 ) show teams on menus 
 
( q ) quit menu, back to game
--------------------
Pick ['1','2','3','4','5','q']
then press enter:
```

#### Menu after audio clip is played
```
============================================================
Select one of the following:
--------------------
( a ) answer          [artist/title revealed]
( r ) replay          [first 5 seconds]
( c ) cheat           [first 15 seconds]
( w ) whole song      [press q to stop]
( p ) play song       [artist/title revealed]
( n ) next song       [return to group selection menu]
( t ) team menu       [hide/show/rename/score]
( ? ) help
( q ) quit
--------------------
Pick ['a','r','c','w','p','n','t','?','q']
then press enter:  
```

#### Selection 'a' is picked
```
============================================================
 
 menu: Classical Music
 
 title: Piano Sonata No. 8 in C minor, Op. 13

 artist: Ludwig van Beethoven

============================================================

...press enter to continue
```

#### Override mode
```
============================================================
 
 catalog: 101 One Hit Wonders
 
 listen to the whole song,
 or [space] to pause,
 or [left](rewind) / [right](forward),
 or [q]uit song, for answer
 
============================================================
```

##### Override: after "q" is pressed
```
============================================================
 
 catalog: 101 One Hit Wonders
 
 title: Baker Street

 artist: Gerry Rafferty

============================================================
 
 press enter for next song, or q to quit: 
```

#### help within the game

``` 
Help: To select a song to hear:
Help:   (a - i)    - pick a song group
Help:   (r)        - pick a random song
Help:   (o)        - override mode (continuous play)
Help:   (t)        - team menu (hide/show/rename/score)
Help: 
Help: To hear the first 5 seconds of a song:
Help:   (spacebar) - when ready, press spacebar to hear the song
Help: 
Help: After hearing the song:
Help:   (a) answer   - reveal the artist and title of a song
Help:   (r) replay   - hear the first 5 seconds of a song
Help:   (c) cheat    - hear the first 15 seconds of a song
Help:   (w) whole    - hear the whole song (artist/title are hidden)
Help:   (p) play     - hear the whole song (reveals song info)
Help:   (n) next     - go to next song group selection
Help: 
Help:   (q) quit     - quit game
 
Press enter to exit help
```

## Release History

*  0.1.3
    * added: 2 team naming and scoring option (can be hidden)
*  0.1.1
    * added: override menu option for continuous, random play
*  0.0.9
    * code cleanup
    * removed grep command dependency
*  0.0.8
    * added: replay 5 sec clip
    * added: play whole song (artist/title hidden)
    * added: play whole song (reveal artist/title)
*  0.0.7
    *  Preload answer for quicker response
*  0.0.6
    *  Code/logic cleanup
    *  Random song
*  0.0.5
    * Separate file for music directories
*  0.0.4
    * Started coding simple error checking
*  0.0.3
    * Ode to Arcade/Console game banner
*  0.0.2
    * Multiple music directories
    * Pull mp3 tag information from mpv
*  0.0.1
    *  The first release
    *  One music directory
    *  Playable as is

## Author

Joseph Archer (C) 2021


## License

The code is covered by the MIT.

