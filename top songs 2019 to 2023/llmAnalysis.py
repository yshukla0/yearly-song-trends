
import google.generativeai as genai
import os
import csv
import time

genai.configure(api_key='AIzaSyAAceK2tD3AZAO2UUzIY4R5AD3K-zKd1-4')

model = genai.GenerativeModel('gemini-1.5-flash')

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
            entityLines = eval(row[4])
            for entityType in ['brands', 'locations']:
                for entity, line in entityLines[entityType].items():
                    sentiment = analyzeSentiment(entity, line)
                    csvWriter.writerow([title, artist, year, entity, entityType, sentiment, line])

def analyzeSentiment(entity, text):
    response = model.generate_content(f"What is the sentiment (positive/negative/neutral) of the {entity} in {text} in one word. If there is not enough information, make a guess. Your answer should never be more than one word or anything other than the 3 options provided. If the statement is not appropriate, skip the evaluation, return 'skip'.")
    time.sleep(2)
    return response.text

analyzeEntitiesSentiment()

