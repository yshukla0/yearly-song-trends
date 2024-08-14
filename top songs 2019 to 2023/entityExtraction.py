import csv

entityFileNames = ['entities data/entities - brands.csv', 
                    'entities data/entities - locations.csv']
entities = {'brands':[], 'locations':[]}

def readEntitiesFile(fileName):
    with open(fileName, 'r') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            if 'brands' in fileName: 
                entities['brands'].append(row[0].lower())
            else:
                entities['locations'].append(row[0].lower())
    
for fileName in entityFileNames:
    readEntitiesFile(fileName)

def findEntitiesMentioned(song):
    entitiedMentioned = {'brands': [], 'locations': []}
    words = song.split() 

    for word in words:
        if word.lower() in entities['brands'] and word.lower() not in entitiedMentioned['brands']:
            if word[0].isupper():
                entitiedMentioned['brands'].append(word.lower())
        elif word.lower() in entities['locations'] and word.lower() not in entitiedMentioned['locations']:
            if word[0].isupper():
                entitiedMentioned['locations'].append(word.lower())
    
    return entitiedMentioned
