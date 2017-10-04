import os
import collections
import re
import sys
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords

# Create NLTK data directory
NLTK_DATA_DIR = './nltk_data'
if not os.path.exists(NLTK_DATA_DIR):
        os.makedirs(NLTK_DATA_DIR)

nltk.data.path.append(NLTK_DATA_DIR)

# Removes stopwords from the text
stop_words = set(stopwords.words('english'))
stop_words.add("comments")
stop_words.add("'")
pattern = re.compile(r'\b(' + r'|'.join(stop_words) + r')\b\s*')

def moreThanThreeMentions(text):
    text = text.lower()
    text = pattern.sub('', text)

    # tokenize the text and tag each word to its word class
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    # Takes the tokens and sorts
    # Appends frequently used words as (word, freq) tuple to result list
    text = []
    for item in tagged:
        if item[1] == 'NN':
            text.append(item[0])
    text = str(text)
    word_freq = collections.Counter(text.split())
    result = ''
    for word, freq in word_freq.most_common():
        if (freq >= 3):
            result = result + (str(freq) + ' ' + word.strip("'").strip("',") + ' ')
    return result

def moreThanTwoMentions(text):
    text = text.lower()
    text = pattern.sub('', text)

    # tokenize the text and tag each word to its word class
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    # Takes the tokens and sorts
    # Appends frequently used words as (word, freq) tuple to result list
    text = []
    for item in tagged:
        if item[1] == 'NN':
            text.append(item[0])
    text = str(text)
    word_freq = collections.Counter(text.split())
    result = ''
    for word, freq in word_freq.most_common():
        if (freq >= 2):
            result = result + (str(freq) + ' ' + word.strip("'").strip("',") + ", ")
    return result
