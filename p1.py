import sys
from file_read import file_read

if __name__=='__main__':
    forward = sys.argv[1]

    try:
        input_file = open(sys.argv[2], 'r')
    except:
        print('Failed to open file\n')
        sys.exit()
    
    s = []
    t = []
    # all_instructs is just list of strings of the file per line, mainly just for Randy/Branching, feel free to modify it how you see fit
    instructs, all_instructs = file_read(input_file)

    print(instructs, all_instructs)
    for i in instructs:
        print(i)
