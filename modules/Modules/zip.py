import sys
import zipfile
import os
def zip(file_name,files):
    with zipfile.ZipFile(file_name, 'w') as zipf:
        for file in files:
            if os.path.isfile(file):
                zipf.write(file, os.path.basename(file))

zip_filename = sys.argv[1]
files = sys.argv[2:]
zip(zip_filename, files)