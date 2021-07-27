
# ntt.py - NAME THAT TUNE

This python3 script will create a list of local songs to use in a simple "Name That Tune" game.

It is set at a 5 second audio clip. It can be changed in the script itself.

You have multiple options after the clip plays.

```
::::::'##::'#######::'########:'####::'######:::::'##::: ##::::'###::::'##::::'##:'########:
:::::: ##:'##.... ##: ##.....:: ####:'##... ##:::: ###:: ##:::'## ##::: ###::'###: ##.....::
:::::: ##: ##:::: ##: ##:::::::. ##:: ##:::..::::: ####: ##::'##:. ##:: ####'####: ##:::::::
:::::: ##: ##:::: ##: ######:::'##:::. ######::::: ## ## ##:'##:::. ##: ## ### ##: ######:::
:##::: ##: ##:::: ##: ##...::::..:::::..... ##:::: ##. ####: #########: ##. #: ##: ##...::::
:##::: ##: ##:::: ##: ##:::::::::::::'##::: ##:::: ##:. ###: ##.... ##: ##:.:: ##: ##:::::::
: ######::. #######:: ########:::::::. ######::::: ##::. ##: ##:::: ##: ##:::: ##: ########:
:......::::.......:::........:::::::::......::::::..::::..::..:::::..::..:::::..::........::
:::'########:'##::::'##::::'###::::'########::::'########:'##::::'##:'##::: ##:'########::::
:::... ##..:: ##:::: ##:::'## ##:::... ##..:::::... ##..:: ##:::: ##: ###:: ##: ##.....:::::
:::::: ##:::: ##:::: ##::'##:. ##::::: ##:::::::::: ##:::: ##:::: ##: ####: ##: ##::::::::::
:::::: ##:::: #########:'##:::. ##:::: ##:::::::::: ##:::: ##:::: ##: ## ## ##: ######::::::
:::::: ##:::: ##.... ##: #########:::: ##:::::::::: ##:::: ##:::: ##: ##. ####: ##...:::::::
:::::: ##:::: ##:::: ##: ##.... ##:::: ##:::::::::: ##:::: ##:::: ##: ##:. ###: ##::::::::::
:::::: ##:::: ##:::: ##: ##:::: ##:::: ##:::::::::: ##::::. #######:: ##::. ##: ########::::
::::::..:::::..:::::..::..:::::..:::::..:::::::::::..::::::.......:::..::::..::........:::::
                                           v.0.0.6
 
                                                                 Press enter to begin...
```

## Background

MPV has a neat feature that allows you to hear a song, without showing anything on the screen. It also lets you open the audio file paused, and only play a certain number of seconds of the file. You can also read the embedded mp3 tags within the audio file.

## Installation

This script requires:

 -  [mpv](https://mpv.io) to play the songs, hide the artist/title, and read mp3 tags.
 -  [grep](https://www.gnu.org/software/grep) to search within mpv mp3 tags.


## Usage example

```
$ ./ntt.py 
```

#### or

```
$ python3 ntt.py
```

#### help within the game

``` 
Help: To select a song to hear:
Help:   (a - i)    - pick a song group
Help:   (r)        - pick a random song
Help: 
Help: To hear the first 5 seconds of a song:
Help:   (spacebar) - when ready, press spacebar to hear the song
Help: 
Help: After hearing the song:
Help:   (a)nswer   - reveal the artist and title of a song
Help:   (c)heat    - hear the first 15 seconds of a song
Help:   (w)hole    - hear the whole song (reveals song info)
Help:   (n)ext     - go to next song selection
Help: 
Help:   (q)uit     - quit game
 
Press enter to exit help
```

## Release History

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
