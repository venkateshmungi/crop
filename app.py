from flask import Flask,render_template,url_for,request,redirect
import numpy as np
import pandas as pd
import joblib
import pickle

app = Flask(__name__)

model = joblib.load('regressor.pkl')

@app.route('/')
@app.route('/main')
def main():
	return render_template('main.html')

@app.route('/predict',methods = ['POST'])

def predict(): 
	int_features = [[features for features in request.form.values()]]
	c = ['Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity', 'pH','Rainfall']
	df = pd.DataFrame(int_features,columns=c)
	final = df
	result=model.predict(final)
	print('The suitable crop is : ', result)

	print(int_features)
   
	return render_template("main.html",prediction_text="The suitable crop is : {}".format(result))

if __name__ == "__main__":
	app.debug=True
	app.run()