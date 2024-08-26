import os
def list_files_in_directory(directory):
        entries = os.listdir(directory)
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]
        
        return files

directory_path = 'c:\\users\\yedhu\\onedrive\\desktop\\python_learning' 
print(list_files_in_directory(directory_path))

