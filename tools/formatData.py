text = open("unsplit.en").read()
#noBreak = open(noB)
output = open ("split.en", "w")

def isEndOfLine(text):
	return true

def splitParagaphs():
	p = text.split("\n")
	return p

def removeNoLang(p):
	for line in p:
		if line != "":
			if line[0] == '<':
				p.remove(line)
	return p

def splitSentances(text):
	allSentacnes = []
	for p in text:
		sentances = p.split(". ")
		#need to add exeptions
		#sentances = rejoin(sentances)
		allSentacnes += sentances
	return allSentacnes

def write(p):
	for line in p:
		if line.strip() == "":
			continue
		output.write(line + "\n")

print "Running..."
p = splitParagaphs()
print "Praragaphs split..."
p = removeNoLang(p)
p = splitSentances(p)
write(p)
output.close()
print "done"
