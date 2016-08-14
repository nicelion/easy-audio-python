# easy-audio-python
easy-audio rewritten in python. (Work in Progress)

## What's New? (Finished and Planned):

NOTE: easy-audio-python is a work in progress (WIP). I am rewriting easy-audio in Python from Bash. With this being said, some things are supported, and some things aren't. Please view the [original easy-audio GitHub page](https://www.github.com/nicelion/easy-audio) for more info on how easy-audio works at it's core. 

* Recognizes playlists and will create a new directory, in the name of the playlist, and export songs there.
* Reads from a configuration file (WIP)
* Text color is configurable (WIP)
* Output location can be defined (WIP)
* Verbosity can be configured (WIP)
* Audio format can be configured (WIP)
* Audio quality can be configured (WIP)
* Playlist output format can be configured (WIP)
* Single audio output can be configured (WIP)


## Description

easy-audio "piggy-backs" off of rg3's [youtube-dl.](https://github.com/rg3/youtube-dl) easy-audio makes downloading mp3s from YouTube quicker and simpler.


##  Installation

As of yet, the Python version is not yet fully supported. With this being said, an "official" installation guide has not yet been created. One will soon be created.

If you would like to test easy-audio-python anyway, you can clone this repo, and run the script:
	
	$ python /path/to/easy-audio.py

The JSON configuration is not yet supported yet either. 

## Requirements

* [youtube-dl](https://github.com/rg3/youtube-dl)
* ffmpeg or avconv and ffprobe or avprobe


## Commands

When you start easy-audio, you will be asked to provide a link or a command. Below are a list of the commands you can use to get more information about the program, or some customization options.

    end                           Ends easy-audio
    
    clear                         Clears all youtube-dl output and previous files you downloaded
   
    pwd, directory,               Outputs the current directory you are in. This is where your files will be exported
    current-directory
    
    version                       Outputs the version number of easy-audio
    
<!--     licence                       Outputs the easy-audio licence. (MIT Licence if you are wondering)
 -->    
<!--     help                          Outputs and lists some help options.
 -->    
  
#### auto-clear

Not yet supported.

<!-- By turning auto-clear on, after each file is downloaded, Terminal will clear. 

To turn on auto-clear, simply type the following when easy-audio is running:

    auto-clear

You will be promted to provide "y" or "n". "y" will turn it on and "n" will either turn it off, or just cancel. -->

#### quiet-mode

Not yet supported.

<!-- youtube-dl will not show any output when quiet-mode is on. 

To turn quiet-mode on, simply type the following when easy0audio is running:

    quiet-mode
  
  -Or-
  
    quiet
   -->
  You will be promted to provide "y" or "n". "y" will turn it on and "n" will either turn it off, or just cancel.


## Copyright

Anyone is free to use, or modify easy-audio. Do what ever you want with it. All I ask is for credit!
