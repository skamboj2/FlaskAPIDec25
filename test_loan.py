import pytest
from loan import app

@pytest.fixture
def client():
    return app.test_client()
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.text == '<h1>Loan Prediction API</h1>'
def test_predict(client):
    data={
        "Gender": "Male",
        "Married": "No",
        "ApplicantIncome": 5000,
        "LoanAmount": 20,
        "CreditHistory": 1
    }
    response = client.post('/predict', json=data)
    assert response.status_code == 200
    assert response.json == {"loan_approval_status": "Approved"}

