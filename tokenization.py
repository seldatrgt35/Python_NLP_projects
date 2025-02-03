import nltk
nltk.download('punkt_tab')  

text="hello, world! 2025 How Are You"

#kelime tokenizasyonu
word_tokens=nltk.word_tokenize(text) #['hello', 'world', '2025', 'How', 'Are', 'You']   
print(word_tokens)

#sentences tokenizasyonu
sentence_tokens=nltk.sent_tokenize(text) #['hello, world! 2025 How Are You']
print(sentence_tokens)