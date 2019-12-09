import sys

if __name__=='__main__':
    forward = sys.argv[1]

    try:
        input_file = open(sys.argv[2], 'r')
    except:
        print('Failed to open file\n')

    s = []
    t = []
    instructs = []
    # ADD FUNCTION TO PARSE INSTRUCTIONS INTO THE INSTRUCTS LIST
    # ADD FOR LOOP FOR CPU CYCLES