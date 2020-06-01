import argparse

parser = argparse.ArgumentParser(prog = 'top', description = 'Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-1', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

# python top.py --lines=5 alpha.txt beta.txt