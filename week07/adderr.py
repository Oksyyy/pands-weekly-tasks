import sys
try: 
    filename = sys.argv[1]

    def find_e(filename, char):
        with open(filename, 'rt') as f:
            total_count = 0
            for l in f:
                count_e = l.count(char)
                total_count = total_count + count_e
        return total_count

    char = 'e'
    how_many_e = find_e(filename, char)
    print(how_many_e)
except FileNotFoundError as nf:
    print(f"file {filename} not found, please enter a valid filename that exists")
except IndexError as ie:
    print(f"list index out of range - please enter the filename as an argument")