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
    
def main():
    userLink = input('Please, insert the link of the video you want to download.\nNote that you can cancel by pressing Enter.\n')
    if linkIsValid(userLink) == False:
        return
    streams = YouTube(userLink).streams
    streamType = getStreamTypeFromUser()
    if streamType == None:
        return
    source = streams.get_audio_only() if streamType == 'a' else streams.get_highest_resolution()
    print('Downloading...')
    source.download("/users/matheusss03/downloads", None, f'{streamType}_')
    print('Done.')
main()