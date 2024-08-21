import nltk
import csv

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

songWordsFile = 'song words data/songWords.csv'
sentimentOutputFile = 'song words data/sentimentAnalysis.csv'

def readSongWordsFile(fileName):
    with open(fileName, 'r') as file:
        csvReader = csv.reader(file)
        rows = list(csvReader)[1:2]  
    return rows

def analyzeEntitiesSentiment():
    songData = readSongWordsFile(songWordsFile)

    with open(sentimentOutputFile, 'w', newline='') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow(['Title', 'Artist', 'Year', 'Entity', 'Entity Type', 'Sentiment'])
        
        for row in songData:
            title = row[0]
            artist = row[1]
            year = row[2]
            entities = eval(row[3])
            for entityType, entityList in zip(['brands', 'locations'], entities):
                for entity in entityList:
                    sentiment = analyzeSentiment(entity)
                    csvWriter.writerow([title, artist, year, entity, entityType, sentiment])

def analyzeSentiment(text):
    sentiment = sia.polarity_scores(text)
    return sentiment

analyzeEntitiesSentiment()

