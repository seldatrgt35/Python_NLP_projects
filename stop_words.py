import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

#stop words listesi
stop_words=set(stopwords.words('english'))

#ornek metin
text="This is an example of removing stop words from a sentence"
filter_words=[word for word in text.split() if word.lower() not in stop_words]
print("Filtered word: ",filter_words) #['This', 'example', 'removing', 'stop', 'words', 'sentence']
