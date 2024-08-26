import os
directory_path = 'c:\\users\\yedhu\\onedrive\\desktop\\python_learning\\getting_started' 
def list_files_in_directory(directory):
        entries = os.listdir(directory)
        for entry in entries:
            full_path = os.path.join(directory, entry)
            if os.path.isfile(full_path):           
                file_stat = os.stat(full_path)
                file_length = file_stat.st_size
                Last_Modified= file_stat.st_mtime
                print(f"{entry}\t{file_length}\t{Last_Modified}")

list_files_in_directory(directory_path)

