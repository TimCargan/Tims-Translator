import pickle
import os

DATA_PATH = "../data/"
trigrams = {}
bigrams = {}
unigrams = {}

#Entry point for the file
def main():
	print "Opening file..."
	rawText = open(DATA_PATH + "split.en").read()
	rawText = rawText.split("\n")

	count = 1
	length = len(rawText)
	print "File open, starting processing..."
	for line in rawText:
		preProcess(line, count, length)
		count += 1

	print "Saving Trigrams..."
	save(trigrams, "trigrams")
	print "Saving Bigrams..."
	save(bigrams, "bigrams")
	print "Saving Unigrams..."
	save(unigrams, "unigrams")


#Bigest flaw is that it trigram cant deal with less than 3 words
def preProcess(line, c, l):
	pString = line.split(" ")
	for word in range(-2, len(pString)):
		x = getFromAray(pString, word)
		y = getFromAray(pString, word + 1)
		z = getFromAray(pString, word + 2)

		trigram = join([x, y, z])
		bigram1 = join([x,y])
		bigram2 = join([y,z])
		unigram = z

		trigam = hash(trigram)
		bigram1 = hash(bigram1)
		bigram2 = hash(bigram2)
		unigram = hash(unigram)

		if trigram in  trigrams:
			trigrams[trigram] += 1
		else:
			trigrams[trigram] = 1

		if bigram1 in  bigrams:
			bigrams[bigram1] += 1
		else:
			bigrams[bigram1] = 1

		if bigram2 in  bigrams:
			bigrams[bigram2] += 1
		else:
			bigrams[bigram2] = 1

		if unigram in  unigrams:
			unigrams[unigram] += 1
		else:
			unigrams[unigram] = 1
		
	os.system('cls' if os.name=='nt' else 'clear')
	print "Processed {:d}/{:d}: {:s}".format(c, l, line)



#get element for array or reutrn "" if index is not valid
def getFromAray(aray, index):
	if index < 0 :
		return "*#es#*"
	try:
		return aray[index]
	except IndexError: 
		return "*#es#*"

#join an array of words into a string
def join(strings):
	r = ""
	for word in strings:
		r += word +  " "
	return r.strip()

def save(obj, name ):
    with open(DATA_PATH + 'obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load(name):
    with open(DATA_PATH + 'obj/' + name + '.pkl', 'r') as f:
        return pickle.load(f)

main()