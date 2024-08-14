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
    words = song.lower().split() 

    for word in words:
        if word in entities['brands']:
            entitiedMentioned['brands'].append(word)
        elif word in entities['locations']:
            entitiedMentioned['locations'].append(word)
    
    return entitiedMentioned


#print(entities)