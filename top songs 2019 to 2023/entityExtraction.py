import csv

entityFileNames = ['entities data/entities - brands.csv', 
                    'entities data/entities - locations.csv']

entities = {'brands':set(), 'locations':set()}

def readEntitiesFile(fileName):
    with open(fileName, 'r') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            if 'brands' in fileName: 
                entities['brands'].add(row[0].lower()) #handle alternate capitalizations
            else:
                entities['locations'].add(row[0].lower())
    
for fileName in entityFileNames:
    readEntitiesFile(fileName)

def identifyAndAddEntity(word, entityType, entitiesMentioned):
    wordLower = word.lower()
    wordSingular = wordLower.rstrip('s') #identify plural entities, like 'Ferraris' 

    if (wordLower in entities[entityType]) or (wordSingular in entities[entityType]):
        if word[0].isupper(): #case against words that are also brands/locations, like 'gap'
            entitiesMentioned[entityType].add(wordLower)
            return True
    return False

def findEntitiesMentioned(song):
    entitiesMentioned = {'brands': set(), 'locations': set()}
    entityLines = {'brands': {}, 'locations': {}}
    lines = song.splitlines() 
    
    for line in lines:
        words = line.split() 

        for i in range(len(words)):  
            word = words[i]
            word = word.replace(',','') #handle entities before commas and contractions, like 'prada,', or "'rari"
            word = word.replace("'", '')
            words[i] = word

        i = 0
        while i < len(words):
            if i < len(words) - 1: #handle two-worded entities, like 'Puerto Rico', 'Coca Cola'
                twoWordEntity = words[i].lower() + ' ' + words[i + 1].lower()
                if twoWordEntity in entities['brands']:
                    if words[i][0].isupper() and words[i + 1][0].isupper():
                        entitiesMentioned['brands'].add(twoWordEntity)
                        entityLines['brands'][twoWordEntity] = line
                        i += 2
                        continue
                elif twoWordEntity in entities['locations']:
                    if words[i][0].isupper() and words[i + 1][0].isupper():
                        entitiesMentioned['locations'].add(twoWordEntity)
                        entityLines['locations'][twoWordEntity] = line
                        i += 2
                        continue
            
            #handle single-worded entities, like 'Nissan', 'California'
            if 2 <= len(words[i]) <= 3:  # Check if the word is an abbreviation like 'LA'
                if words[i].isupper():
                    if identifyAndAddEntity(words[i], 'locations', entitiesMentioned):
                        entityLines['locations'][words[i].lower()] = line
            else:
                if identifyAndAddEntity(words[i], 'brands', entitiesMentioned):
                    entityLines['brands'][words[i].lower()] = line
                if identifyAndAddEntity(words[i], 'locations', entitiesMentioned):
                    entityLines['locations'][words[i].lower()] = line

            i += 1
        

    return entitiesMentioned, entityLines
