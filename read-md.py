import frontmatter
import io
import json
#from os.path import basename, splitext
import os
import glob

# Where are the files to modify


result = {'directories' : []}

dirMask = {'name': '', 'files': []}
fileMask =  {'name': '', 'order': 0}

def readFiles():
    filelist = []
    result['directories'].append({'name': 'src', 'files': filelist})



    path = 'src'
    for root, dirs, files in os.walk(path, topdown=False):
        # for name in files:
        #     #print('name: ' + name)
        #     #print(os.path.join(root, name))
        #     fullName = os.path.join(root, name)
        #     filename, ext = os.path.splitext(fullName)
            
        #     if (ext == '.md'):

        #         print(fullName)
        #         print(ext)
        #         with io.open(fullName, 'r') as f:
        #             post = frontmatter.load(f)
        #             if post.get('Category') != None:
        #                 filelist.append( {'name': filename, 'order': (post.get('Order'))})
        #                 #print(name)
        #                 #print(post.get('Category'))
        #                 #print(post.get('Order'))

        for name in dirs:
            currentPath = os.path.join(root, name)
            print(currentPath)
            # filelist = []
            # result['directories'].append({'name': currentPath, 'files': filelist})
            
            # print('dir name-------')
            # print(os.path.join(root, name))


readFiles()
j = json.dumps(result)
print(j)


# Loop through all files
# for fname in glob.glob(path):
#     with io.open(fname, 'r') as f:
#         # Parse file's front matter
#         post = frontmatter.load(f)
#         if post.get('Category') != None:
#             print(fname)
#             print(post.get('Category'))
