from pytube import YouTube

url = "https://youtu.be/bF_jYaSNFV8"
video = YouTube(url)

print("Title:", video.title)
print("Description:", video.description)
print("Thumbnail URL:", video.thumbnail_url)
print("Downloading")

#streams = video.streams.all()
#stream = video.streams.get_highest_resolution()
stream = video.streams.filter(file_extension='mp4').get_highest_resolution()

stream.download()


