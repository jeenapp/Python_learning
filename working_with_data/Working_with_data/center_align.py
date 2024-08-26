import sys
filename = sys.argv[1]
def center_align_file(filename):
        lines=open(filename).readlines()
        with open(filename, 'w') as file:
      
                for line in lines:
                        line = line.strip()
                        centered_line = line.center(10)
                        file.write(centered_line + '\n')
                   
center_align_file(filename)
