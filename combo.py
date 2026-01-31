import itertools
import argparse
import math

parser = argparse.ArgumentParser(
                    prog='Combo',
                    description='generete all iteration of charset',
                    epilog='from your base you can generate all iteration of this base')
parser.add_argument("-s", "--string")
parser.add_argument("-c", "--count", default=0)
parser.add_argument("-o", "--filename")
args = parser.parse_args()

if not args.string or not args.filename:
	print("Launch --help to see arguments")
	raise

baseSplited = args.string.split(",")
count = int(args.count)
iteration = 1

def writeAndPrintAndIterate(line, file):
	global iteration
	file.write(line + '\n')
	print(line)
	iteration += 1

with open(args.filename, "w") as f:
	for base in baseSplited: 
		for combo in itertools.product(*[(c.lower(), c.upper()) for c in base]):
			word = ''.join(combo)
			writeAndPrintAndIterate(word, f)
			if count:
				for i in range(0, count + 1):
					writeAndPrintAndIterate(word + str(i), f)
					digitCount = len(str(count))
					digitI = len(str(i))
					if int(digitI) < int(digitCount):
						for digitDiff in range(int(digitI)+1, int(digitCount)+1):
							writeAndPrintAndIterate(word + str(i).zfill(digitDiff), f)

print(f"Vous avez généré {iteration} dans {args.filename}")
