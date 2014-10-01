import re
import os

open('../data/split.en')

EXEPTIONS = ["mr", "dr"]
text = "this is a story about dr. tim. He is a super cool guy. He is dr dad is mr. martin. this is r. not wreal. \n\n\n \t This is in another pragraph. lol."

def splitSentances(text):
	allSentacnes = []
	for p in text:
		sentances = p.lower()
		sentances = sentances.split(". ")
		#need to add exeptions
		#the data we are processing is bad.
		allSentacnes += sentances
	return allSentacnes



def buildRegex (rules):
	regEx = ""
	for exeption in rules:
		regEx += "(?=(?<! {:s}))".format(exeption)
	#remove last char since its a |
	regEx += "\.[\s\n]*"
	print regEx
	return regEx

def readExeptions():
	prefixes = open("prefix.en").read()
	prefixes = prefixes.split("\n")
	exeptions = []
	for prefix in prefixes:
		if "#" in prefix:
			continue
		if prefix=="":
			continue
		exeptions.append(prefix.lower())
	return exeptions



readExeptions()


regEx = buildRegex(readExeptions())
prog = re.compile(regEx)

regex = r"(?=(?<!dr))(?=(?<!mr))\. "
text = [text]
print regEx
for paragraphs in text:
 	print prog.split(paragraphs)
 	print re.split(regex, paragraphs)



