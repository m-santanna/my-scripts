import webbrowser
from sys import argv

def getLink():
    match argv[1].lower():
        case "gau":
            return "https://www.twitch.tv/gaules"
        case "github":
            return "https://github.com/m-santanna"
        case "anime":
            return "https://www.crunchyroll.com/pt-br"
        case default:
            return 0

def main():
    if len(argv) != 2:
        print('Please, use this program as the following: "python links.py (desired link)"')
        return
    userInput = getLink()
    if userInput == 0:
        print('Note that the only allowed inputs for now are: \n"gau"\n"github"\n"anime"\nWhere all of them are case insensitive.')
        return
    webbrowser.open(userInput)
main()