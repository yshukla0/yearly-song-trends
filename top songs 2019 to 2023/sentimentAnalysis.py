import nltk
import csv

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

songWordsFile = 'song words data/songWords.csv'
sentimentOutputFile = 'song words data/sentimentAnalysis.csv'

def readSongWordsFile(fileName):
    with open(fileName, 'r') as file:
        csvReader = csv.reader(file)
        rows = list(csvReader)[1:]  
    return rows

def analyzeEntitiesSentiment():
    songData = readSongWordsFile(songWordsFile)

    with open(sentimentOutputFile, 'w', newline='') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow(['Title', 'Artist', 'Year', 'Entity','Entity Type', 'Sentiment'])
        
        for row in songData:
            print(row)
            title = row[0]
            artist = row[1]
            year = row[2]
            entities = eval(row[3])
            entityLines = eval(row[4])
            for entityType in ['brands', 'locations']:
                for entity, line in entityLines[entityType].items():
                    sentiment = analyzeSentiment(line)
                    csvWriter.writerow([title, artist, year, entity, entityType, sentiment, line])

def analyzeSentiment(text):
    print(text)
    sentiment = sia.polarity_scores(text)
    print(sentiment)
    return sentiment

analyzeEntitiesSentiment()

