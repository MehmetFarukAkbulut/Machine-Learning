import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler=pd.read_csv('eksikveriler.csv')
print(veriler)

#eksik veriler
#sci kit learn
from sklearn.impute import SimpleImputer
imputer= SimpleImputer(missing_values=np.nan,strategy='mean')
Yas=veriler.iloc[:,1:4].values
print(Yas)
imputer=imputer.fit(Yas[:,1:4])

Yas[:,1:4]=imputer.transform(Yas[:,1:4])
print(Yas)

ulke= veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing
le=preprocessing.LabelEncoder()

ulke[:,0]=le.fit_transform(veriler.iloc[:,0])
print(ulke)

ohe= preprocessing.OneHotEncoder()
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)

sonuc= pd.DataFrame(data=ulke,index=range(22),columns=['fr','tr','us'])
print(sonuc)