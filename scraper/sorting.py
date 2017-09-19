import collections
import re
import sys
import nltk
from nltk.corpus import stopwords

url = str(sys.argv[1])
with open(url, 'r') as f:
	text = f.read()
	text = text.lower()

# Removes stopwords from the text
stop_words = set(stopwords.words('english'))
pattern = re.compile(r'\b(' + r'|'.join(stop_words) + r')\b\s*')
text = pattern.sub('', text)
word_freq = collections.Counter(text.lower().split())

# tokenize the text and tag each word to its word class
tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)

# Takes the tokens and sorts
# Appends frequently used word as (word, freq) tuple to result list
text = []
result = []
for item in tagged:
	if item[1][0] == 'N':
		text.append(item[0])

text = [word.replace("'", "") for word in text]
text = str(text)

def moreThanThreementions(text):
	for word, freq in word_freq.most_common():
		if (freq >= 3):
			result.append("%s %d" % (word, freq))
	return result

moreThanThreementions(text)
