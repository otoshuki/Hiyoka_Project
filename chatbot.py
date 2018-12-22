import nltk
import os
import numpy as np
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt')
nltk.download('wordnet')
put = input("Enter : ")
#Pre_processing
#Conversion
# file = open('corp.txt','r',errors = 'ignore')
# put = file.read()
put = put.lower()

sent_tokens = nltk.sent_tokenize(put)
word_tokens = nltk.word_tokenize(put)
print(sent_tokens)
print("word_tokens\n")
print(word_tokens)
