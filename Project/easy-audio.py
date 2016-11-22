import json
import urllib2
import os

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
WHITE = '\033[97m'

inputURL = ""
version = "2.0"
release_date = "July 26th, 2016"
path = "/Users/ianthompson/Music/youtube-dl/"

songs_downloaded = 0
playlists_downloaded = 0

# Configuration varibles 

text_color = str
# path = str
verbose = bool
audio_format = str
audio_quality = int
playlist_output_format = str


def playlist(url):
    print("playlist")

    requestURL = "https://www.youtube.com/oembed?url=%s&format=json" % url
    response = urllib2.urlopen(requestURL)
    data = json.loads(response.read())

    print(data["title"])



    album_name = data["title"]
    directory = path + album_name
    print(directory)

    os.mkdir(directory)

    output = "\"" + directory + "/%(playlist_index)s %(title)s.%(ext)s\""

    command = "youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 --o %s %s" % (output, url)
    os.system(command)

    # playlists_downloaded += 1    

    getinput()



def singlevideo(url):
    print("single")
    
    output = '"' + path + "%(title)s.%(ext)s\""
    command = "youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 --o %s %s" % (output, url)

    os.system(command)

    # songs_downloaded += 1

    getinput()

def checkforcommand(command):
    if command == "version":
        print("easy-audio version " + version + ".")
        print("Released " + release_date + ".")
    elif command == "ls":
        os.system("ls " + path)
        getinput()
    elif command == "pwd": 
        print(path)
        getinput()
    else:
        print(BOLD + FAIL + "[ERROR]: " + ENDC + "Command " + command + " not found. Type 'help' for help.")
        getinput()

def getinput():

    # if songs_downloaded > 0:
        # print("%i songs and %i playlists have been downloaded this session.") % (songs_downloaded, playlists_downloaded)

    inputURL = raw_input(WHITE + BOLD + "Please enter the url to your desired audio, or a command: " + ENDC)

    if "http://www.youtube.com" in inputURL or "https://www.youtube.com" in inputURL:
        if "playlist" in inputURL:
            playlist(inputURL)
        else:
            singlevideo(inputURL)
    elif inputURL == "end":
        print(WHITE + BOLD + "Thank you for using easy-audio by Nice Lion Technologies" + ENDC)
        exit()
    else:
        checkforcommand(inputURL)

def load_config():
    config = json.load(open("/Users/ianthompson/Documents/Python Projects/easy-audio/easy-audio-config.json"))
    
    text_color = config["text-color"]
    path = config["output-location"]
    verbose = config["verbose"]
    audio_format = config["audio-format"]
    audio_quality = config["audio-quality"]
    

def startprogram():
    os.system("clear")
    print(BOLD + WHITE + "Welcome to easy-audio by Nice Lion Technologies!")
    print(FAIL + BOLD + "[NOTE:]" + ENDC + " Before using easy-audio, please configure the 'easy-audio-config' file." + ENDC)
    getinput()

    

# load_config()

startprogram()


