from flask import Flask,render_template,request
import pickle

app = Flask(__name__)
file1=open('model1.pk1','rb')
clf1=pickle.load(file1)
file1.close()

file2=open('model2.pk1','rb')
clf2=pickle.load(file2)
file2.close()

file3=open('model3.pk1','rb')
clf3=pickle.load(file3)
file3.close()

@app.route("/",methods=["GET","POST"])
def hello_world():
    return render_template('index.html')


@app.route("/heart",methods=["GET","POST"])
def hello_world1():
    if request.method=="POST":
        mydict1=request.form
        age=int(mydict1['age']) 
        sex=int(mydict1['sex'])
        cp=int(mydict1['cp'])
        trestbps=int(mydict1['trestbps'])
        chol=int(mydict1['chol'])
        fbs=int(mydict1['fbs'])
        restecg=int(mydict1['restecg'])
        thalach=int(mydict1['thalach'])
        exang=int(mydict1['exang'])
        oldpeak=int(mydict1['oldpeak'])
        slope=int(mydict1['slope'])
        ca=int(mydict1['ca'])
        thal=int(mydict1['thal'])

        inputfeatures1=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]

        pred1=clf1.predict([inputfeatures1])


        return render_template('show1a.html',inf1=pred1)
    return render_template('index1ab.html')  


@app.route("/kidney",methods=["GET","POST"])
def hello_world2():

    if request.method=="POST":
        mydict2=request.form
        age=int(mydict2['age'])
        bp=int(mydict2['bp'])
        al=int(mydict2['al'])
        su=int(mydict2['su'])
        rbc=int(mydict2['rbc'])
        bgr=int(mydict2['bgr'])
        bu=int(mydict2['bu'])
        ba=int(mydict2['ba'])
        hemo=int(mydict2['hemo'])
        wc=int(mydict2['wc'])
        rc=int(mydict2['rc'])
        htn=int(mydict2['htn'])
        cad=int(mydict2['cad'])

        inputfeatures2=[age,bp,al,su,rbc,bgr,bu,ba,hemo,wc,rc,htn,cad]

        pred2=clf2.predict([inputfeatures2])

        return render_template('show2.html',inf2=pred2)
    return render_template('index2b.html')  


@app.route("/diabetes",methods=["GET","POST"])
def hello_world3():
    if request.method=="POST":
        mydict3=request.form
        Glucose=int(mydict3['Glucose']) 
        BloodPressure=int(mydict3['BloodPressure'])
        SkinThickness=int(mydict3['SkinThickness'])
        Insulin=int(mydict3['Insulin'])
        BMI=int(mydict3['BMI'])
        DiabetesPedigreeFunction=float(mydict3['DiabetesPedigreeFunction'])
        Age=int(mydict3['Age'])
        

        inputfeatures3=[Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]

        pred3=clf3.predict([inputfeatures3])

        return render_template('show3.html',inf3=pred3)

    return render_template('index3.html')










    


if __name__=='__main__':
    app.run(debug=True)