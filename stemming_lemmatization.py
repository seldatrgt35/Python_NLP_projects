import nltk
nltk.download('wordnet')    
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()

words=['run','running','ran','runs','runner','better','go','went']

[print(stemmer.stem(word)) for word in words]

from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
words=['run','running','ran','runs','runner','better','go','went']
[print(lemmatizer.lemmatize(word,pos="v")) for word in words]
# v verirsek fiil , n verirsek isim anlamına gelir

