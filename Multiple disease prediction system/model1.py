import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

if __name__=='__main__':
    df=pd.read_csv('heart.csv')
    X=df.drop('target',axis=1)
    y=df.target
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    clf1=RandomForestClassifier()
    clf1.fit(X_train,y_train)
    file=open('model1.pk1','wb')
    pickle.dump(clf1,file)   
    file.close() 