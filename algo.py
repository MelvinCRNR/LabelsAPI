import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from stop_words import get_stop_words
from sklearn.svm import SVC
#Si les librairies sont chargées.
print('libs load')

df=pd.read_csv('data/labels.csv')
#Si df est chargée.
print('df loaded')

#Affichage de quelque donnée de df afin de vérifier la validité de la Dataframe.
#print(df)

df['tweet']
#print(df['tweet'])


#Nettoyage des données.
df['tweet']=df['tweet'].str.lower()
df['tweet']=df['tweet'].apply(lambda x : re.sub("[^a-z\s]", "", x))
df['tweet']=df['tweet'].str.replace("#", " ")
df['tweet']=df['tweet'].apply(lambda x : ' '.join([w for w in x.split() if len(w)>2]))
stopwords=set(stopwords.words("english"))
df['tweet']=df['tweet'].apply(lambda x : " ".join(word for word in x.split() if word not in stopwords))
#Affichage des données après le nettoyage.
#print(df['tweet'])

clf=make_pipeline(
	TfidfVectorizer(stop_words=get_stop_words('en')),
	OneVsRestClassifier(SVC(kernel='linear', probability=True))
)
#Si le make_pipeline a fonctionné.
print('pipeline worked')

X = df['tweet']
y = df['class']

clf.fit(X, y)
