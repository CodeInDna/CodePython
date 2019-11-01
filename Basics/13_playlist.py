playlist = {
'title': 'A day at CAFE', 
'author': 'Unknown', 
'songs' : [
		{'title': 'song1', 'artist': ['Jagjeet'], 'duration': 2.6},
		{'title': 'song2', 'artist': ['Ali', 'Badshah'], 'duration': 5.23},
		{'title': 'song3', 'artist': ['popey'], 'duration': 2.0}
	]
}
total_duration = 0
for song in playlist['songs']:
	total_duration += song['duration']
print(total_duration)