
# ntt.py - NAME THAT TUNE

This python3 script will create a menu from a local directory, using up to 9 different top level directories, to create a simple "Name That Tune" game. It allows you to hear the first 5 seconds of the song, then select options until the answer is requested. You can manually keep track of team names and scores (2 teams).

It works really well with compilation albums (various artists). I use it with a Raspberry Pi connected to my TV. I use a 128 GB SD card, without a GUI, and a display resolution of 640x480 60Hz.

### NEW!
* An intro song can be added at the start banner, so that the volume can be adjusted before the game begins.
* Will now track all played songs, in each menu category, so that it can not be played again.
* If all songs in a menu category have been played, that menu can not be picked anymore.

### An ode to Arcade banner:
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
    v.0.1.7                      Check your volume...
                                      Press enter to begin...
```

## Some of the options

* Automatically creates a configuration file, if needed.
* Reads a music directory using the first 9 music sub-folders listed.
* Scans each folder, and the first level directory becomes a separate menu option.
* It is set at a 5 second audio clip, from the beginning of the song.
* It also allows for 10 extra seconds to be added. (cheat)
* Can play the whole song, with or without revealing the artist and title.
* Play a random song.
* Override mode, for continuous, random play. (speed round)
* Two team hide/show (with team naming and scoring).

#### Note:
* Settings for number of clip seconds, team names and scores, music directory, intro song, etc. can be changed in the configuration file (ntt.ini).

## Background

MPV has a neat feature that allows you to hear a song, without showing anything on the screen. It also lets you open the audio file paused, and only play a certain number of seconds of the file. You can also read the embedded mp3 tags within the audio file.

## Installation

***This script requires:***

 -  [mpv](https://mpv.io) to play the songs, hide the artist/title, and read mp3 tags.

### Quick Configuration (on desktop or existing setup)

* Place ntt.py in a folder.
* Create music directory with several sub-directories of music files.
* The first 9 sub-directories (in top music folder) will be used, and become the menu selections.
* First time run: allow ntt.py to create configuration file.
* Edit ntt.ini for music directory and intro song location.

### Example Setup on Raspberry Pi 3B+ (new Lite install)

* Download Lite 64-bit version for 3B+
* Uncompress xz image
* Flash to SD card with balenaEtcher
* Place SD card in RPi and turn on

#### at First Boot
  * Pick Keyboard: other/English(US)
  * Enter New Username (ntt)
  * Enter Password
  * Confirm Password
  * reboot and login as ntt

#### sudo raspi-config
  * Select 1 System Options, S1 Wireless Lan, enter country, ssid, pw
  * reboot and login as ntt

#### sudo raspi-config
  * Select 1 System Options, S5 Boot/Auto Login, B2 Console Autologin
  * Select 6 Advanced Options, A1 Expand Filesystem
  * Exit/Reboot Now
  * login as ntt
  * sudo apt install mpv
  * (coffee break)

#### Note:
  * RPi Lite does NOT come with any audio daemon!
  * sudo apt install pulseaudio
  * sudo raspi-config
  * select 6 Advanced Settings / Audio config / select PulseAudio
  * sudo reboot
  * sudo raspi-config
  * select System Settings / Audio / select HDMI
  * reboot and login as ntt

#### finish RPi setup
  * sudo apt update
  * sudo apt upgrade
  * (more coffee)
  * shutdown -h now
  * remove SD card and mount on desktop

#### (on desktop) within /home/ntt folder on SD card
  * go to the "rootfs" partition of the SD card
  * copy ntt.py to /home/ntt
  * make directory "music" in /home/ntt (mkdir music)
  * copy up to 9 music folders (and sub-folders) under new music directory
  * copy intro song to /home/ntt (rename intro.mp3 or edit ntt.ini later)

#### Note:
  * I made my RPi screen very small by editing the boot options manually
  * go to the "bootfs" partition of the SD card
  * edit the cmdline.txt file
  * add the following to the end of your boot string
```
 video=HDMI-A-1:640x480M@60
```

#### continue SD setup on desktop
  * unmount the SD card and remove
  * place in RPi and turn on

#### back on RPi
  * login as ntt
  * make executable with "chmod +x ntt.py" (to start using ./ntt.py) or
  * python3 ntt.py
  * allow ntt.py to create configuration file
  * python3 ntt.py

## How to Play

### Start game
```
$ ./ntt.py
```

##### or

```
$ python3 ntt.py
```

#### Song selection menu
##### Example Directory structure:
```
music
   Classical Music
   Disco Music
   Instrumentals
   Misc Country
   Misc Rock
   Songs of the 50s
      disc 1
      disc 2
   Songs of the 60s
      disc 1
      disc 2
   Songs of the 70s
      disc 1
      disc 2
   Songs of the 80s
      disc 1
      disc 2
```

##### Example Game Menu:
```
============================================================
           Gals              vs               Guys
            0                                  0
============================================================
Select one of the 1127 following songs: 0 played
--------------------
( a ) Classical Music (19/19 songs)
( b ) Disco Music (58/58 songs)
( c ) Instrumentals (466/466 songs)
( d ) Misc Country (113/113 songs)
( e ) Misc Rock  (160/160 songs)
( f ) Songs of the 50s (86/86 songs)
( g ) Songs of the 60s (58/58 songs)
( h ) Songs of the 70s (60/60 songs)
( i ) Songs of the 80s (97/97 songs)
----------
( r ) Random song    ( o ) Override mode    ( t ) Team menu
( ? ) help           ( q ) quit game        ( x ) Shutdown
--------------------
Pick an option:
   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'r']
   ['o', 't', '?', 'q', 'x']
then press enter:
```

#### Selection 'a' is picked
```
then press enter: a
--------------------
Press spacebar to hear the song...
```

#### Menu after audio clip is played
```
============================================================
           Gals              vs               Guys
            0                                  0
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

#### Note:
* Enter will return to previous menu.
* Select next song "n", to start next round.
* Menu selection "a" will now show "( a ) Classical Music (18/19 songs)"

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
( 5 ) show/hide teams on menus

( r ) reset scores/names/hide
( s ) save, and go back to game
--------------------
Pick ['1','2','3','4','5','r','s']
then press enter:
```
#### Note:
* Save 's', will save team name/score to configuration file.

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

###

 help within the game

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
Help:   (x) exit     - turn off the computer

Press enter to exit help
```

## Release History
*  0.1.7
    *  can play an intro song, to adjust volume
    *  code cleanup with better logic
    *  team scores now show on default
    *  tracks all songs played
    *  played songs can not be picked again
    *  locks menu option if all songs in menu are picked
*  0.1.6
    *  code cleanup, lots of code cleanup
    *  removed shuffle, better random generate used
*  0.1.5
    *  now works on music directory instead of directory list from a file
    *  added ability to re-shuffle
    *  added shuffle_count to configuration file
    *  fixed [mpv issue 11790](https://github.com/mpv-player/mpv/issues/11790) with work around using "--ao=alsa"
    *  removed display of song cover image using "--no-audio-display"
*  0.1.4
    *  configuration file (ntt.ini) creation and update
    *  computer shutdown option (useful for raspberry pi)
    *  more code cleanup and organization
    *  debug mode added
    *  check for installation of mpv
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


