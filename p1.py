import sys
from file_read import file_read

if __name__=='__main__':
    '''
    THIS IS JUST COMMENTED OUT BECAUSE IM LAZY AND DONT WANT TO RUN FROM COMMAND LINE
    forward = sys.argv[1]

    try:
        input_file = open(sys.argv[2], 'r')
    except:
        print('Failed to open file\n')
        sys.exit()
    '''
    input_file = open("p1-input01.txt")
    s = []
    t = []
    instructs, all_instructs = file_read(input_file)

    print(instructs, all_instructs)
    for i in instructs:
        print(i)
