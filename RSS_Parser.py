from io import BytesIO
from tkinter import *
from urllib.request import Request, urlopen

import feedparser
import requests
from PIL import Image, ImageTk


class Film:
	def __init__(self):
		self._nom = "nul"
		self._lien = "https://127.0.0.1"
		self._note = "0/0"
		self._genre = "nul/nul"
		self._size = "0.0GB"
		self._duree = "0hr0"
		self._miniature = 0

	def _get_nom(self):
		return self._nom
	def _set_nom(self, s):
		self._nom = s
	
	def _get_lien(self):
		return self._lien
	def _set_lien(self, s):
		self._lien = s

	def _get_note(self):
		return self._note
	def _set_note(self, s):
		self._note = s

	def _get_genre(self):
		return self._genre
	def _set_genre(self, s):
		self._genre = s

	def _get_size(self):
		return self._size
	def _set_size(self, s):
		self._size = s

	def _get_duree(self):
		return self._duree
	def _set_duree(self, s):
		self._duree = s

	def _get_miniature(self):
		return self._miniature
	def _set_miniature(self, s):
		self._miniature = s
	
	nom=property(_get_nom, _set_nom)
	lien=property(_get_lien, _set_lien)
	note=property(_get_note, _set_note)
	genre=property(_get_genre, _set_genre)
	size=property(_get_size, _set_size)
	duree=property(_get_duree, _set_duree)
	miniature=property(_get_miniature, _set_miniature)
		
class RSSFeed:
	def __init__(self):
		self._rss_url = "https://127.0.0.1"
		self._nom = "rss_feed"

	def _get_feed(self):
		return feedparser.parse(self._rss_url)
	def _set_feed(self, s):
		self._rss_url = s

	def _get_nom(self):
		return self._nom
	def _set_nom(self, s):
		self._nom = s

	nom=property(_get_nom, _set_nom)
	feed=property(_get_feed, _set_feed)

class Fenetre:
	def __init__(self):
		self.window = Tk()
		self.window.title("RSS Feed Analyzer")
		self.window.geometry('1650x350')
		self.window.mainloop()


if __name__ == "__main__":
	
	python_wiki_rss_url = "https://yts.am/rss/0/1080p/all/0"
	feed = feedparser.parse( python_wiki_rss_url )
	x = 0
	tabImages = []

	for film in feed.entries:
		print(film.title)
		print(film.link)
		tab = film.summary.split('>')
		genre = ""
		
		for token in tab:
			if "IMDB" in token:
				data = token.split('<')[0].split(' ')
				imdb = data[2]
				print(imdb)
			if "Genre" in token:
				data = token.split('<')[0].split(' ')
				for i in range(1, len(data)) :
					genre += data[i]    
				print(genre)
			if "Size" in token:
				data = token.split('<')[0].split(' ')
				size = data[1]+data[2]
				print(size)
			if "Runtime" in token:
				data = token.split('<')[0].split(' ')
				duree = data[1]+data[2]
				print(duree)
			if "img" in token:
				data = token.split('"')
				img = data[1]

		req = Request(img, headers={'User-Agent': 'Mozilla/5.0'})
		fd = urlopen(req)
		imgFile = BytesIO(fd.read())
		tabImages.append(ImageTk.PhotoImage(Image.open(imgFile)))
		Button(window, image=tabImages[x]).grid(column=x, row=0)
		x = x+1

	
