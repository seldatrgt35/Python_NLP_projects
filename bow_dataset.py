import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import re
from collections import Counter
df=pd.read_csv("IMDB Dataset.csv")
df2=df.head(100)
print(df2)

#metin verilerini alalım
documents=df2["review"]
labels=df2["sentiment"]

#metin verilerini temizleme fonksiyonu
def clean_text(text):
    text=text.lower()
    #rakamları temizleme
    text=re.sub(r"\d+","",text)
    #özel karakterleri temizleme    
    text=re.sub(r"[^\w\s]","",text)
    #kısa kelimeleri temizleme
    text=" ".join([word for word in text.split() if len(word)>2])   
    return text

#metin verilerini temizleme
cleaned_documents=[clean_text(doc) for doc in documents]

#bow
vectorizer=CountVectorizer()
#metni sayısal vektöre dönüştürme
X=vectorizer.fit_transform(cleaned_documents[:100])
#kelime kümesi
print("Kelime kümesi: ",vectorizer.get_feature_names_out())
#vektör temsili
print("Vektör temsili: ",X.toarray()[:2])

#vektör temsili dataframe
#df3=pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names_out())
#print(df3)

#kelime frekansları
word_counts=X.sum(axis=0).A1
word_counts=Counter(dict(zip(vectorizer.get_feature_names_out(),word_counts)))  #kelime frekanslarını hesaplama
print("Kelime frekansları: ",word_counts)