import frontmatter
import io
#from os.path import basename, splitext
import os
import glob

# Where are the files to modify
path = "src"

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        #print('name: ' + name)
        #print(os.path.join(root, name))
        fullName = os.path.join(root, name)
        filename, ext = os.path.splitext(fullName)
        
        if (ext == '.md'):
            print(fullName)
            print(ext)
            with io.open(fullName, 'r') as f:
                post = frontmatter.load(f)
                if post.get('Category') != None:
                    #print(name)
                    print(post.get('Category'))
                    print(post.get('Order'))

    # for name in dirs:
    #     print(os.path.join(root, name))


# Loop through all files
# for fname in glob.glob(path):
#     with io.open(fname, 'r') as f:
#         # Parse file's front matter
#         post = frontmatter.load(f)
#         if post.get('Category') != None:
#             print(fname)
#             print(post.get('Category'))
