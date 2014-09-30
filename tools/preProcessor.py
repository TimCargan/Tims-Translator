import pickle

print "opening file"
<<<<<<< HEAD
rawText = open("split.en").read()
=======
rawText = open("data/testenglish.en").read()
>>>>>>> e924fe66749110950e74c37c1c7c88712e4ceb71
rawText = rawText.split("\n")

trigrams = {}
bigrams = {}
unigrams = {}

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
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load(name):
    with open('obj/' + name + '.pkl', 'r') as f:
        return pickle.load(f)

count = 1
length = len(rawText)
print "File open, starting processing..."
for line in rawText:
	preProcess(line, count, length)
	count += 1

print "Saving..."
save(trigrams, "trigrams")
print "Saving..."
save(bigrams, "bigrams")
print "Saving..."
save(unigrams, "unigrams")
