import io, json
import os 
import glob

def getArray():
    result = {'directories': []}
    dirs = []
    
    directory = {'name': 'root', 'files': []}
    dirs.append(directory)

    files = []
    
    afile = {'name': 'intro.md', 'order': 1000}
    files.append(afile)

    afile = {'name': 'skills.md', 'order': 1002}
    files.append(afile)


    directory = {'name': 'avr', 'files': files}
    dirs.append(directory)

    result['directories'] = dirs
    
    return result



j = json.dumps(getArray())
print(j)

with open('test.json', 'w') as outfile:
    json.dump(getArray(), outfile)



