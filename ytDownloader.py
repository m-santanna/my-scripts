from pytube import YouTube
# Note that this file will only work if you have the pytube library installed.

def linkIsValid(link):
    if link == '':
        print('Operation canceled.')
        return False
    elif link.startswith('https://www.youtube.com/watch?v=') == False:
        print('Please, insert a link that starts with: "https://www.youtube.com/watch?v=".')
        return False
    return True

def getStreamTypeFromUser():
    userInput = input('\nGreat, now insert the stream type you want to download.\n"v" for video\n"a" for audio\nNote that you can cancel by pressing Enter.\n')
    if userInput == '':
        print('Operation canceled.')
        return
    elif userInput == 'v':
        return "v"
    elif userInput == 'a':
        return "a"
    else:
        print('Please, insert a valid input.')
        return 
def getDirectoryFromUser():
    userInput = input('\nGreat, now insert the directory you want to download the file at.\n"d" to download the file in the directory this script is located\n"m" to download this file at "/Users/matheusss03/downloads"\nOr type your desired directory. Example "/Users/user123/folder1/folder2"\nNote that you can cancel by pressing Enter.\n')
    if userInput == '':
        print('Operation canceled.')
        return
    elif userInput == 'd':
        return 'd'
    elif userInput == 'm':
        return '/Users/matheusss03/downloads'
    return userInput

def main():
    userLink = input('\nPlease, insert the link of the video you want to download.\nNote that you can cancel by pressing Enter.\n')
    if linkIsValid(userLink) == False:
        return
    streams = YouTube(userLink).streams
    streamType = getStreamTypeFromUser()
    if streamType == None:
        return
    source = streams.get_audio_only() if streamType == 'a' else streams.get_highest_resolution()
    directory = getDirectoryFromUser()
    if directory == None:
        return
    print('Downloading...')
    source.download(directory if directory != "d" else None, None, f'{streamType}_')
    print('Done.')
main()