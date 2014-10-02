import math
import pickle

DATA_PATH = "../data/"

PXYZ = 0.475
PYZ = 0.475
PZ = 0.049
PB = 0.001

#Bigest flaw is that it trigram cant deal with less than 3 words
def calcStringP(string):
	string = formatSentance(string)
	outputString = string

	string = string.split(" ")
	stringProb = []

	for word in range(-2, len(string)):
		x = getFromAray(string, word)
		y = getFromAray(string, word + 1)
		z = getFromAray(string, word + 2)

		prob = nGram (x, y, z)
		stringProb.append(prob)

		print "b({:s}|{:s}) = {:f}".format(z, join([x,y]), prob)

	prob = multiLog(stringProb) / len(string)
	result = "P({:s}) = {:f}".format(outputString, prob)
	return result


def nGram (x, y, z):
	if((x != "") & (y != "") & (z !="")):
		return trigramS(x, y, z)
	return 1

def bigram(x,y):
	cxy = numOfAcc(join([x,y]))
	cy = numOfAcc(y)
	try:
		p1 =  (cxy / float(cy))
	except ZeroDivisionError:
		print "got 0 in b"
		p1 = 0

	return p1

def trigramS(x, y, z):
	cxyz = numOfAcc(join([x,y,z]), "t")
	cxy = numOfAcc(join([x,y]), "b")
	cyz = numOfAcc(join([y,z]), "b")
	cz = numOfAcc(join([z]), "u")

	#added try catched to handle zero exeptions
	try:
		p1 = PXYZ * (cxyz / float(cxy))
	except ZeroDivisionError:
		p1 = 0

	try:
		p2 = PYZ * (cyz / float(cz))
	except ZeroDivisionError:
		p2 = 0

	p3 = PZ * (cz / float(200400000))
	p4 = PB

	return p1 + p2 + p3 + p4


#get element for array or reutrn "" if index is not valid
def getFromAray(aray, index):
	if index < 0 :
		return "*#es#*"
	try:
		return aray[index]
	except IndexError: 
		return "*#es#*"

#return the number of accurences in the test data 
def numOfAcc(search, type):
	acc = 0
	noHash = search
	search = hash(search)

	#search the trigram file
	if type == "t":
		try:
			return trigrams[noHash]
		except KeyError:
			return 0
	#search Bigrams
	if type == "b":
		try:
			return bigrams[search]
		except KeyError:
			return 0
	#Search Unigrams (words)
	if type == "u":
		try:
			return unigrams[search]
		except KeyError:
			return 0

# return the sum of the logs of a list of numbers
def multiLog(numbers):
	total = 0
	for num in numbers:
		total += math.log(num, 2)
	return total

#join an array of words into a string
def join(strings):
	r = ""
	for word in strings:
		r += word +  " "
	return r.strip()

def load(name):
    with open(DATA_PATH + 'obj/' + name + '.pkl', 'r') as f:
        return pickle.load(f)

def formatSentance(string):
	string = string.strip()
	string = string.lower()
	return string
	
print "PXYZ {:f}".format(PXYZ)
print "PYZ {:f}".format(PYZ)

#load files
print "loading files..."
trigrams = load("trigrams")
bigrams = load("bigrams")
unigrams = load("unigrams")

testData = "The other problem relates to the immigration issue noted above. In many ways, people with STEM expertise are most needed in the developing world, where the projects they create and industries they start will have the largest impact. But the mismatches between education and industry's needs in the developed nations drives a brain drain that sucks talent from the developing world. Again, this occurs despite the fact that schools here are producing a lot of STEM graduates."
testData = testData.split(".")
testData.append("This is when we where how this isn't even english words just random text not here")
for s in testData:
	print calcStringP(s)

text = ""
while text != "exit!":
	print "\n"
	text = "{}".format(raw_input("Enter a sentance: "))
	print "=" * 50
	print calcStringP(text)



