import json

def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)
listOfPhotos = getJSON('./id.json').get('name',[])

