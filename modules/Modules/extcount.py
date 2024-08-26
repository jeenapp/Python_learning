import os
import sys

def list_files_in_directory(directory):
        entries = os.listdir(directory)
        ext_count={}
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]
        for file in files:
            _, ext = os.path.splitext(file)
            if ext in ext_count:
                ext_count[ext] += 1
            else:
                ext_count[ext] = 1
        return ext_count
directory_path = sys.argv[1]
print(list_files_in_directory(directory_path))

