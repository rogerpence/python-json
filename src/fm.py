import frontmatter
import io
from os.path import basename, splitext
import glob

# Where are the files to modify
path = "*.md"

# Loop through all files
for fname in glob.glob(path):
    with io.open(fname, 'r') as f:
        # Parse file's front matter
        post = frontmatter.load(f)
        if post.get('Category') != None:
            print(fname)
            print(post.get('Category'))
