import pickle
from flask import Flask,render_template,request

app = Flask(__name__,template_folder='templates')
model = pickle.load(open('rent_model.pkl','rb'))

@app.route('/')
def index():
    return render_template('rent.html')

@app.route('/predict',methods={'GET','POST'})
def predict():
    prediction = model.predict([[request.form.get('area','bedrooms','bathrooms','stories','mainroad','guestroom','basement','hotwaterheating','airconditioning','parking','prefarea','furnishingstatus')]])
    output = round(prediction[0],2)
    return render_template('rent.html',prediction_text=f'Price {output}/-')

if __name__ == '__main__':
    app.run(debug=True)
