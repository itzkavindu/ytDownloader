from pytube import YouTube

link = input("Please enter the link of the YouTube video you wish to Download: ")
yt = YouTube(link)

print()
print("Title          : ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Rating of video: ", yt.rating)

ys = yt.streams.get_highest_resolution()

print()
print(yt.title, "is Now Downloading...")
ys.download()
print()
print("---Download completed---")
