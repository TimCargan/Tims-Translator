import re

DATA_PATH = "../data/"
#Entry point for the file
def main():
	text =  open("../data/raw.en").read()
	print "Running..."
	#Convert Case
	print "Converting Case..."
	text = text.lower()
	print "split pragraphs"
	text = text.split("\n")
	print "Splitting..."
	regEx = buildRegex()
	text = splitPara(text, regEx)
	#write output
	print "Writing output..."
	write(text)
	print "done"

def write(data):
	name = "split.en"
	outputFileName = DATA_PATH  + name
	output = open (outputFileName , "w")
	for line in data:
		if line.strip() != "":
			output.write(line.strip() + "\n")
	output.close()

def splitPara(p, regEx):
	allLines = []
	i = len(p)
	for pragraph in p:
		allLines += regEx.split(pragraph)
		print i
		i -= 1
	return allLines
#Build and compile the regEx that splits the sentances
def buildRegex():
	rules = readExeptions()
	regEx = ""
	for exeption in rules:
		regEx += "(?=(?<! {:s}))".format(exeption)
	regEx += "\.[\s\\n]*"
	return re.compile(regEx)
#Read the No Breake expetions from file and format them so the regex can be built
def readExeptions():
	prefixes = open(DATA_PATH + "nb/prefix.en").read()
	prefixes = prefixes.split("\n")
	exeptions = []
	for prefix in prefixes:
		if "#" in prefix:
			continue
		if prefix=="":
			continue
		exeptions.append(prefix.lower())
	return exeptions
#remove any lines from the data that are inalid. Not Used
def removeNoLang(p):
	for line in p:
		if line != "":
			if line[0] == '<':
				p.remove(line)
	return p

## Run main (entry point)
main()