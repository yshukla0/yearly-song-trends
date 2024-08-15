import csv

entityFileNames = ['entities data/entities - brands.csv', 
                    'entities data/entities - locations.csv']
entities = {'brands':[], 'locations':[]}

def readEntitiesFile(fileName):
    with open(fileName, 'r') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            if 'brands' in fileName: 
                entities['brands'].append(row[0].lower()) #handle alternate capitalizations
            else:
                entities['locations'].append(row[0].lower())
    
for fileName in entityFileNames:
    readEntitiesFile(fileName)

def findEntitiesMentioned(song):
    entitiesMentioned = {'brands': [], 'locations': []}
    words = song.split() 

    for word in words:
        word = word.replace(',','')
        wordLower = word.lower()
        wordSingular = wordLower.rstrip('s') #Find plural mentions 

        if (wordLower in entities['brands'] or 
              wordSingular in entities['brands']): #Find plural mentions 
                if word[0].isupper() and wordLower not in entitiesMentioned['brands']:
                    entitiesMentioned['brands'].append(wordLower)

        elif wordLower in entities['locations']:
            if len(word) == 2: #Find 'LA' and 'SF' etc. correctly
                if word.isupper():
                    if (wordLower in entities['locations'] and 
                        wordLower not in entitiesMentioned['locations']):
                        entitiesMentioned['locations'].append(wordLower)
            else:
                if word[0].isupper() and wordLower not in entitiesMentioned['locations']:
                    entitiesMentioned['locations'].append(wordLower)
    
    return entitiesMentioned
