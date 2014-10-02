import math
import pickle

DATA_PATH = "../data/"

PXYZ = 0.475
PYZ = 0.475
PZ = 0.049
PB = 0.001

#Bigest flaw is that it trigram cant deal with less than 3 words
def calcStringP(pString):
	pString = pString.split(" ")
	stringProb = []
	for word in range(0, len(pString)):
		x = getFromAray(pString, word)
		y = getFromAray(pString, word + 1)
		z = getFromAray(pString, word + 2)

		prob = trigramS(x, y, z)
		stringProb.append(prob)

		print "b({:s}|{:s}) = {:f}".format(z, join([x,y]), prob)

	result = "{:f}".format(prob)
	return result


def trigramS(x, y, z):
	cxyz = numOfAcc(join([x,y,z]), "t")
	print "cxyz: {:d}".format(cxyz)
	return cxyz

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
	search = search
	#search the trigram file

	try:
		return trigrams[search]
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

	
print "PXYZ {:f}".format(PXYZ)
print "PYZ {:f}".format(PYZ)

#load files
print "loading files..."
trigrams = load("trigrams")

print calcStringP("member states were")



