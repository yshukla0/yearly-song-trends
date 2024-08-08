import spacy
nlp = spacy.load("en_core_web_sm")

def extractEntities(lyrics):
    doc = nlp(lyrics)
    entities = {'brands':[], 'celebrities':[], 'locations':[]}
    for ent in doc.ents:
        if ent.label_ == 'LOC' or ent.label_ == 'GPE':
            entities['locations'].append(ent.text)
        elif ent.label_ == 'ORG':
            entities['brands'].append(ent.text)
        elif ent.label_ == 'PERSON':
            entities['celebrities'].append(ent.text)
    return entities