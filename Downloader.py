from pytube import YouTube

def try_download(video):
    try:
        video.download()
    except:
        print("An error occurred in your download")
        
    print("The download was successful!")

def download_higher(link):
    video = YouTube(link)
    video = video.streams.get_highest_resolution()
    try_download(video)

def download_lowest(link):
    video = YouTube(link)
    video = video.streams.get_lowest_resolution()
    try_download(video)

def download_audio(link):
    video = YouTube(link)
    video = video.streams.get_audio_only()
    try_download(video)

def download_selection():
    options = input("How do you want to make your download?\n[1]Highest Resolution - [2]Lowest Resolution - [3]Only Audio\n->")
    if options == "1":
        download_higher(link)
    elif options == "2":
        download_lowest(link)
    elif options == "3":
        download_audio(link)
    else:
        print("You need to select of the 3 choices\n", "="*50)
        download_selection()

while True:
    link = input("Put your Youtube link Here! URL: ")
    download_selection()

    choice = input("Do you want to make another download?[y]/[n]\n->")
    if choice == "n":
        break
    elif choice != "y":
        print("Invalid Option. Closing the application")
