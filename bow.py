from sklearn.feature_extraction.text import CountVectorizer
document=["kedi evde","kedi bahçede"]
vectorizer=CountVectorizer()    #CountVectorizer sınıfından bir nesne oluşturuldu

#metini sayısal vektöre dönüştürme
X=vectorizer.fit_transform(document)

#kelime kümesi
print ("Kelime kümesi: ",vectorizer.get_feature_names_out()) #['bahçede', 'evde', 'kedi']

#vektör temsili
print("vektör temsili: ",X.toarray()) #[[0 1 1] [1 0 1]]    #1. cümlede evde ve kedi var, 2. cümlede bahçede ve kedi var
