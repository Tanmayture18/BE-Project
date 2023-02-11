import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

if __name__=='__main__':
    df=pd.read_csv('kidney_disease.csv')

    ### We are going to take useful features only
    df=df[['age','bp','al','su','rbc','bgr','bu','ba','hemo','wc','rc','htn','cad','classification']]
    ### Null values imputation
    df['age']=df['age'].fillna(df['age'].mean())
    df['bp']=df['bp'].fillna(df['bp'].mean())
    df['al']=df['al'].fillna(df['al'].mean())
    df['su']=df['su'].fillna(df['su'].mean())
    df['bgr']=df['bgr'].fillna(df['bgr'].mean())
    df['bu']=df['bu'].fillna(df['bu'].mean())
    df['hemo']=df['hemo'].fillna(df['hemo'].mean())
    df['cad']=df['cad'].fillna(df['cad'].mode()[0])
    df['ba']=df['ba'].fillna(df['ba'].mode()[0])
    df['rbc']=df['rbc'].fillna(df['rbc'].mode()[0])
    df['wc']=df['wc'].fillna(df['wc'].mode()[0])
    df['rc']=df['rc'].fillna(df['rc'].mode()[0])
    df['htn']=df['htn'].fillna(df['htn'].mode()[0])

    df['age']=df['age'].astype(int)
    df['bp']=df['bp'].astype(int)
    df['al']=df['al'].astype(int)
    df['su']=df['su'].astype(int)
    df['bgr']=df['bgr'].astype(int)
    df['bu']=df['bu'].astype(int)
    df['hemo']=df['hemo'].astype(int)

    df=df[df.wc!='\t?']
    df['wc']=df['wc'].astype(int)

    df=df[df.rc!='\t?']
    df['rc']=df['rc'].astype('float')

    df=df[df.cad!='\tno']

    df=df[df.classification!='ckd\t']

    #### We are going to perform label encoding for categorical variables here
    from sklearn.preprocessing import LabelEncoder
    le=LabelEncoder()
    df['rbc']=le.fit_transform(df['rbc'])
    df['ba']=le.fit_transform(df['ba'])
    df['htn']=le.fit_transform(df['htn'])
    df['cad']=le.fit_transform(df['cad'])
    df['classification']=le.fit_transform(df['classification'])

    X=df.drop('classification',axis=1)
    y=df.classification

    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

    clf2=RandomForestClassifier()
    clf2.fit(X_train,y_train)

    file2=open('model2.pk1','wb')
    pickle.dump(clf2,file2)   
    file2.close() 
