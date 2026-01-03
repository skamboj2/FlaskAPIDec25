from flask import Flask,request
import pickle

app = Flask(__name__)

with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return '<h1>Loan Prediction API</h1>'

@app.route('/predict')
def predict():
    return 'I will predict for loan approval'
@app.route('/predict',methods=['POST'])
def predict_loan():
    loan_req = request.get_json()
    
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "No":
        Married = 0
    else:
        Married = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    CreditHistory = loan_req['CreditHistory']
    LoanAmount = loan_req['LoanAmount']

    input_data = [Gender, Married, ApplicantIncome, LoanAmount, CreditHistory]

    pred = model.predict([input_data])

    print(pred)


    if pred[0] == 1:
        pred = "Approved"
    else:
        pred = "Rejected"


    return {"loan_approval_status": pred}
if __name__ == '__main__':
    app.run(debug=True)
# To run the application, use the command: python loan.py
