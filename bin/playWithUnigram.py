## Opens the Uigram and prints it to screen
import pickle

def load(name ):
    with open('obj/' + name + '.pkl', 'r') as f:
        return pickle.load(f)

print "Opening file..."
unigram = load("unigrams")



print "unigrams {:d}".format(len(unigram))

text = ""
while text != "exit!":
	text = "{}".format(raw_input("Enter a sentance: "))
	search = hash(text)
	print unigram[search]

