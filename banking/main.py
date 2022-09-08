from flask import Flask,render_template,request
import pickle

app = Flask(__name__)
file=open('model.pk1','rb')
file1=open('model.pk2','rb')
pipe=pickle.load(file)
pipe1=pickle.load(file1)
file.close()
file1.close()

@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        mydict=request.form
        CreditScore=int(mydict['CreditScore'])
        Gender=int(mydict['Gender'])
        Age=int(mydict['Age'])
        Tenure=int(mydict['Tenure'])
        Balance=int(mydict['Balance'])
        NumOfProducts=int(mydict['NumOfProducts'])
        HasCrCard=int(mydict['HasCrCard'])
        IsActiveMember=int(mydict['IsActiveMember'])
        EstimatedSalary=int(mydict['EstimatedSalary'])

        inputfeatures=[CreditScore,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]
        
        

        pred=pipe.predict([inputfeatures])

           

        return render_template('show.html',inf=pred)
    return render_template('index.html')

@app.route("/loan",methods=["GET","POST"])
def hello_world1():
    if request.method=="POST":
        mydict1=request.form
        Gender=int(mydict1['Gender'])
        Married=int(mydict1['Married'])
        Dependents=int(mydict1['Dependents'])
        Education=int(mydict1['Education'])
        Self_Employed=int(mydict1['Self_Employed'])
        ApplicantIncome=int(mydict1['ApplicantIncome'])
        CoapplicantIncome=int(mydict1['CoapplicantIncome'])
        LoanAmount=int(mydict1['LoanAmount'])
        Loan_Amount_Term=int(mydict1['Loan_Amount_Term'])
        Credit_History=int(mydict1['Credit_History'])
        Property_Area=int(mydict1['Property_Area'])

        inputfeatures1=[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]
        
        

        pred1=pipe1.predict([inputfeatures1]) 

        return render_template('show1.html',inf1=pred1)
    return render_template('index1.html')    

if __name__=='__main__':
    app.run(debug=True)   
