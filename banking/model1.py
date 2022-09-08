import pandas as pd
import numpy as np
import pickle
from sklearn.pipeline import Pipeline

if __name__=='__main__':
    df=pd.read_csv('loan.csv')
    df.drop('Loan_ID',axis=1,inplace=True)

    df['Gender']=df['Gender'].fillna(df['Gender'].mode()[0])
    df['Married']=df['Married'].fillna(df['Married'].mode()[0])
    df['Dependents']=df['Dependents'].fillna(df['Dependents'].mode()[0])
    df['Self_Employed']=df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])
    df['LoanAmount']=df['LoanAmount'].fillna(df['LoanAmount'].mean())
    df['Loan_Amount_Term']=df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean())
    df['Credit_History']=df['Credit_History'].fillna(df['Credit_History'].mode()[0])

    from sklearn.preprocessing import LabelEncoder
    le=LabelEncoder()
    df['Gender']=le.fit_transform(df['Gender'])
    df['Dependents']=le.fit_transform(df['Dependents'])
    df['Married']=le.fit_transform(df['Married'])
    df['Education']=le.fit_transform(df['Education'])
    df['Self_Employed']=le.fit_transform(df['Self_Employed'])
    df['Property_Area']=le.fit_transform(df['Property_Area'])
    df['Loan_Status']=le.fit_transform(df['Loan_Status'])

    X=df.drop('Loan_Status',axis=1)
    y=df.Loan_Status

    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import SVC

    pipe1=Pipeline([('scaler',StandardScaler()),('svc',SVC(kernel='rbf'))])

    pipe1.fit(X_train,y_train)

    file1=open('model.pk2','wb')

    pickle.dump(pipe1,file1)

    file1.close()




