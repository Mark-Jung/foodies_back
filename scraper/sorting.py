import collections
import re
import sys
import nltk
from nltk.corpus import stopwords

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
    result = []
    for item in tagged:
        if item[1] == 'NN':
            text.append(item[0])

    text = str(text)
    word_freq = collections.Counter(text.split())
    result = ''
    for word, freq in word_freq.most_common():
        if (freq >= 3):
            # store format: 
            # {"word":"placeholder","freq": 22},
            result += ('"word"'+':'+word+'"freq"'+':'+str(freq)+ "\n")
            #result += (str(freq) + ' ' + word.strip("'").strip("',") + "\n")
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
    result = []
    for item in tagged:
        if item[1] == 'NN':
            text.append(item[0])

    text = str(text)
    word_freq = collections.Counter(text.split())
    for word, freq in word_freq.most_common():
        if (freq >= 2):
            result.append("%s %d" % (word, freq))
    return result

   
