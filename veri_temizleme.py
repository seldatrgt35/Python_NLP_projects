#metinlerdeki fazla boşlukları temizleme
text="Hello,   World!   2025" 
text.split() #['Hello,', 'World!', '2025']
cleande_text= " ".join(text.split())   #'Hello, World! 2025'
print(cleande_text)

#büyük harf küçük harf dönüşümü
text="Hello, World! 2025"
cleande_text=text.lower() #'hello, world! 2025'
#text.upper() #'HELLO, WORLD! 2025'
print(cleande_text)

#noktalama işaretlerini temizleme
import string
text="hello, world! 2025"
cleande_text3=text.translate(str.maketrans("","",string.punctuation)) #'hello world 2025'
print(cleande_text3)

#özel karakterleri temizleme
import re
text="hello, world! 2025"
cleaned_text4=re.sub(r"[^a-zA-Z0-9\s]","",text) #'hello  world  2025'  #özel karakterler yerine boşluk ekler
print(cleaned_text4)

#yazım hatalarını düzeltme
from textblob import TextBlob
text="helio, wirld! 2025"
text_blob_object=str(TextBlob(text).correct()) #'hello, world! 2025'
print(text_blob_object)

#html taglerini temizleme
from bs4 import BeautifulSoup
html_text="<html><h2>hello, world! 2025</h2></html>"
soup=BeautifulSoup(html_text,"html.parser").get_text() #'hello, world! 2025'
print(soup)