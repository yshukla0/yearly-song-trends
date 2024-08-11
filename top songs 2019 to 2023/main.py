import csv
import lyricsgenius as lg
from entityExtraction import extractEntities


client_access_token = 'W8c9UewEKOdTJ8aJclY3vPzBLkRl1OBh_rhgJtLQ4C0oftxsY7nGOFufkVS7nAmu'
genius = lg.Genius(client_access_token)
songWords = {}
fileNames = fileNames = ['data/2019.csv']
                         #',data/2020.csv', 'data/2021.csv', 'data/2022.csv', 'data/2023.csv']

def getLyrics(title, artist):
    try:
        song = genius.search_song(title, artist)
        if song: return song.lyrics
        else: return ''
    except: 
        print(f'{title} by {artist} not found.')
        return ''

def readFile(fileName):
    with open(fileName, 'r') as file:
        csvReader = csv.reader(file)
        lines = list(csvReader)
        rows = [line[:2] for line in lines[7:8]] 
    return rows

for fileName in fileNames:
    rows = readFile(fileName)
    print(f'{fileName} songs:')
    for artist, title in rows:
        songWords[title] = {'artist': artist, 'words':[]}
        lyrics = getLyrics(title, artist)
        entities = extractEntities(lyrics) if lyrics else []
        songWords[title]['entities'] = entities
    print(lyrics)
    print(songWords)