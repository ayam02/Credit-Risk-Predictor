from flask import Flask, render_template, request
from Model import PredictiveModel
from Chart import ChartGenerator
from DataStats import DataStats
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
        #Generate charts with user comparison
        charts = ChartGenerator().generate_charts(user_input=input_dictionary)
        profile = {
            "savings_balance": request.form.get('savings_balance', 0, type=int),
            "employment_duration": request.form.get('employment_duration', 'unemployed')
        }
        
        #Get all insights
        insights = DataStats().generate_all_insights(profile)

        #Pass insights to the results page
        return render_template("results.html", default_risk=default_probability, charts=charts, insights=insights)
          
        #return render_template("results.html", default_risk = default_probability, dictionary= input_dictionary)
    # If it's a GET request, render the form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
