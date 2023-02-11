import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

if __name__=='__main__':



    # Importing Dataset
    df=pd.read_csv('diabtesdata.csv')

    # Balancing dataset
    legit=df[df.Outcome==0]
    fraud=df[df.Outcome==1]
    legit_sample=legit.sample(n=268)
    df=pd.concat([legit_sample,fraud],axis=0)

    # Separating dependent and independent variables
    X=df.drop('Outcome',axis=1)
    y=df.Outcome

    # Performing train-test-split
    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

    # We are going to use randomforestclassifer for our project
    clf3=RandomForestClassifier()
    clf3.fit(X_train,y_train)


    # Pickling file
    file3=open('model3.pk1','wb')
    pickle.dump(clf3,file3)   
    file3.close() 