import sys
import os

def chunked_lines(filename, lines_per_chunk):
    with open(filename, 'r') as file:
        chunk = []
        for line in file:
            chunk.append(line)
            if len(chunk) == lines_per_chunk:
                yield chunk
                chunk = []
        if chunk:  
            yield chunk
def split_file(filename, lines_per_chunk):
    base_filename, ext = os.path.splitext(filename)
    chunk_number = 1    
    for chunk in chunked_lines(filename, lines_per_chunk):
        chunk_filename = f"{base_filename}_part{chunk_number}{ext}"
        with open(chunk_filename, 'w') as chunk_file:
            chunk_file.writelines(chunk)        
        print(f"Created: {chunk_filename}")
        chunk_number += 1

lines_per_chunk = int(sys.argv[1])
filename = sys.argv[2]      
split_file(filename, lines_per_chunk)

