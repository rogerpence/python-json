import io, json
import os 
import glob

result = {'directories': []}


def sortObject(objArray):
    keys = []
    sortedList = []

    for a in objArray:
        j = a['order']
        keys.append(j)

    keys.sort()        

    for k in keys:
        for a in objArray:
            if a['order'] == k:
                sortedList.append(a)

    return sortedList        


def getArray():
    result = {'directories': []}
    dirs = []
    
    directory = {'name': 'root', 'files': []}
    dirs.append(directory)

    files = []
    
    afile = {'name': 'intro.md', 'order': 1004}
    files.append(afile)

    afile = {'name': 'skills.md', 'order': 1003}
    files.append(afile)

    afile = {'name': 'skills.md', 'order': 1000}
    files.append(afile)

    files = sortObject(files)

    directory = {'name': 'avr', 'files': files}
    dirs.append(directory)

    result['directories'] = dirs
    
    return result



j = json.dumps(getArray())
print(j)

with open('test.json', 'w') as outfile:
    json.dump(getArray(), outfile)



