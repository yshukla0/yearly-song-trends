import csv
import lyricsgenius as lg
from entityExtraction import findEntitiesMentioned


client_access_token = 'W8c9UewEKOdTJ8aJclY3vPzBLkRl1OBh_rhgJtLQ4C0oftxsY7nGOFufkVS7nAmu'
genius = lg.Genius(client_access_token)
songWords = {}
songFileNames =['top songs data/2019.csv']
                         #, 'top songs data/2020.csv', 'top songs data/2021.csv', 
                         # 'top songs data/2022.csv', 'top songs data/2023.csv']

def getLyrics(title, artist):
    try:
        song = genius.search_song(title, artist)
        if song: return song.lyrics
        else: return ''
    except: 
        print(f'{title} by {artist} not found.')
        return ''

def readSongFile(fileName):
    with open(fileName, 'r') as file:
        csvReader = csv.reader(file)
        lines = list(csvReader)
        rows = [line[:2] for line in lines[3:4]] 
    return rows

for fileName in songFileNames:
    rows = readSongFile(fileName)
    print(f'{fileName} songs:')
    for artist, title in rows:
        songWords[title] = {'artist': artist, 'words':[]}

        lyrics = getLyrics(title, artist)
        entities = findEntitiesMentioned(lyrics) if lyrics else []
        songWords[title]['entities'] = entities

    print(songWords)