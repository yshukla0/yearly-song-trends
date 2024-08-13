import csv

entityFileNames = ['entities data/entities - brands.csv', 
                    'entities data/entities - locations.csv']
entities = {'brands':[], 'locations':[]}

def readEntitiesFile(fileName):
    with open(fileName, 'r') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            if 'brands' in fileName: 
                entities['brands'].append(row[0])
            else:
                entities['locations'].append(row[0])
    
for fileName in entityFileNames:
    readEntitiesFile(fileName)

def findEntitiesMentioned(song):


print(entities)