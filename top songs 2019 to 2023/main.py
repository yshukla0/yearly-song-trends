import csv
import sys
import lyricsgenius as lg
from entityExtraction import findEntitiesMentioned

csv.field_size_limit(sys.maxsize)

client_access_token = 'W8c9UewEKOdTJ8aJclY3vPzBLkRl1OBh_rhgJtLQ4C0oftxsY7nGOFufkVS7nAmu'
genius = lg.Genius(client_access_token)

songWords = {}

songFileNames = ['/Users/Cameroon/yshukla0.github.io/yearly-song-trends/top songs 2019 to 2023/top songs data/2020.csv']
#songFileNames = ['top songs data/2019.csv', 'top songs data/2020.csv', 
 #                'top songs data/2021.csv', 'top songs data/2022.csv', 
 #                'top songs data/2023.csv']

lyricsFileName = '/Users/Cameroon/yshukla0.github.io/yearly-song-trends/top songs 2019 to 2023/lyrics data/lyrics.csv'
outputFileName = '/Users/Cameroon/yshukla0.github.io/yearly-song-trends/top songs 2019 to 2023/song words data/songWords.csv' 

def getLyrics(title, artist):
    lyrics = findStoredLyrics(title, artist)
    if lyrics: 
        return lyrics

    try:
        song = genius.search_song(title, artist)
        if song: 
            storeLyrics(title, artist, song.lyrics)
            return song.lyrics
        else: 
            return ''
    except: 
        print(f'{title} by {artist} not found.')
        return ''

def readSongFile(fileName):
    with open(fileName, 'r') as file:
        csvReader = csv.reader(file)
        lines = list(csvReader)
        rows = [line[:2] for line in lines[1:2]] 
    return rows

def storeLyrics(title, artist, lyrics):
    with open(lyricsFileName, 'a', newline='') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow([title, artist, lyrics])

def findStoredLyrics(title, artist):
    with open(lyricsFileName, 'r') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            if row[0] == title and row[1] == artist: 
                return row[2]
    return None

def saveSongWords(songWords, fileName):
    with open(fileName, 'a', newline='') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow(['Title', 'Artist', 'Year', 'Entities', 'Entity Lines']) 
        for title, data in songWords.items():
            artist = data['artist']
            year = data['year']
            entities = [data['entities']['brands'], data['entities']['locations']]
            entityLines = data['entity lines']
            csvWriter.writerow([title, artist, year, entities, entityLines])

for fileName in songFileNames:
    year = fileName[15:20]
    rows = readSongFile(fileName)
    
    print(f'{fileName} songs:')
    for artist, title in rows:
        lyrics = getLyrics(title, artist)
        if lyrics:
            songWords[title] = {'artist': artist, 'year': year}
            firstLine = lyrics.find('\n')
            entities, entityLines = (findEntitiesMentioned(lyrics[firstLine:]))[0], (findEntitiesMentioned(lyrics[firstLine:]))[1]  #skip title line
            songWords[title]['entities'] = entities
            songWords[title]['entity lines'] = entityLines
saveSongWords(songWords, outputFileName)