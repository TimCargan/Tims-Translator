## Opens the Uigram and prints it to screen
import pickle

def load(name ):
    with open('obj/' + name + '.pkl', 'r') as f:
        return pickle.load(f)

unigram = load("unigrams")

wordCount = 0
for word in unigram:
	wordCount += unigram[word]

print unigram
print "unigrams {:d}".format(len(unigram))
print "Number of words {:d}".format(wordCount)