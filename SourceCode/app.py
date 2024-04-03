from flask import Flask,render_template
from flask import request
import pickle
import numpy as np
import joblib



app=Flask(__name__)

@app.route('/')
def home():
    return render_template('./home.html')

@app.route('/predict',methods=['POST'])
# def predict():
#     # Get form data and perform prediction
#     # ...
#     return render_template('results.html', result=my_prediction)
def predict():
    if request.method=='POST':
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        on_thyroxine = float(request.form['on_thyroxine'])
        on_antithyroid_medication = float(request.form['on_antithyroid_medication'])
        hypopituitary = float(request.form['hypopituitary'])
        psych = float(request.form['psych'])
        goitre = float(request.form['goitre'])
        TSH =float(request.form['TSH'])
        T3_measured=float(request.form['T3_measured'])
        TT4 = float(request.form['TT4'])
        referral_source =float(request.form['referral_source'])
        FTI = float(request.form['FTI'])


        # Make a prediction
        l=[]
        for i in [age, sex, TSH, TT4, FTI, on_thyroxine,  on_antithyroid_medication,goitre, hypopituitary,psych, T3_measured, referral_source]:
            l.append(float(i))
        data= np.array([l])
        print(data)
        my_prediction=classifier.predict(data)

    return render_template('result.html',prediction=my_prediction)
if __name__=='__main__':
    classifier=joblib.load('final.pkl')
    app.run(debug=True)
