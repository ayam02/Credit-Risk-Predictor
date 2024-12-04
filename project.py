from flask import Flask, render_template, request
from Model import PredictiveModel

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    filePath = "credit.csv"
    categories=["checking_balance", "months_loan_duration",	"credit_history",	"purpose","amount",	"savings_balance","employment_duration","percent_of_income","years_at_residence","age","other_credit","housing","existing_loans_count",	"job","dependents","phone"]
    # Check if the form is submitted (POST request)
    if request.method == 'POST':
        input_dictionary = {}
        for category in categories:
            input_dictionary[category] = request.form.get(category)

        #test the model -- find the probability 
        default_probability = PredictiveModel(filePath).testRisk(input_dictionary)
          
        return render_template("results.html", default_risk = default_probability, dictionary= input_dictionary)
    # If it's a GET request, render the form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)