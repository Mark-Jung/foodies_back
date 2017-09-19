import collections
import re
import sys
import nltk

from nltk.corpus import stopwords

url = str(sys.argv[1])

with open(url, 'r') as f:
	text = f.read()
	text = text.lower()

stop_words = set(stopwords.words('english'))

pattern = re.compile(r'\b(' + r'|'.join(stop_words) + r')\b\s*')
text = pattern.sub('', text)


word_freq = collections.Counter(text.lower().split())

tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)

text = []

for item in tagged:
	if item[1][0] == 'N':
		text.append(item[0])

text = [word.replace("'", "") for word in text]
text = str(text)

for word, freq in word_freq.most_common():
	if (freq >= 3):
		print("%-10s %d" % (word, freq))


