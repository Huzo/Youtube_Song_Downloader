from __future__ import unicode_literals
import youtube_dl
import os 
import sys
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

SONG_DIRECTORY = 'Song'


#youtube_dl download configurations 
donwload_config = {
	'format':'bestaudio/best',
	'outtmpl': '%(title)s.%(ext)s',
	'nocheckcertificate': True,
	'postprocessors':[{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}]
}


def get_SongLink(song_name):
	#get the youtube video of the song. (First video to appear when searched)
	

	query = urllib.parse.quote(song_name)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html,'html.parser')

	#get the first youtube link.
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
		url_to_download = 'https://www.youtube.com' + vid['href']
		return url_to_download



def download_song(url):
	#Download Song
	with youtube_dl.YoutubeDL(donwload_config) as dl:
		dl.download([url])


if __name__ == '__main__':
	# Song Directory
	if not os.path.exists(SONG_DIRECTORY) and os.path.curdir is not SONG_DIRECTORY:
		os.mkdir(SONG_DIRECTORY)
	else:
		os.chdir(SONG_DIRECTORY)


	while True:
		#ask for the song name
		song_name = input("Please enter a song name (ex: Metallica - Until It Sleeps):\n Or press 'q' to quit.")
		song_name = str(song_name)
		if(song_name == 'q' or song_name == 'Q'):
			print("Thank you for using Huzo's Youtube Song Downloader!")
			sys.exit()

		url_to_download = get_SongLink(song_name)
		download_song(url_to_download)

