from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('credit.csv')
print(df.columns)
print()
print(df.describe())

categorical_columns = ["checking_balance", 'credit_history', 'purpose', 'employment_duration', 'other_credit', 'housing', 'job', 'phone', 'savings_balance' ]

encoders={}

for column in categorical_columns:
    label_encoder = LabelEncoder()
    df[column] = label_encoder.fit_transform(df[column])
    encoders[column] = label_encoder

X = df.drop("default", axis=1)
Y = df["default"]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

decision_tree = tree.DecisionTreeClassifier()
decision_tree = decision_tree.fit(X_train, y_train)
y_predicted = decision_tree.predict(X_test)
accuracy = accuracy_score(y_test, y_predicted)
print(accuracy)

#test a sample
# input_dictionary = [{ "checking_balance":"< 0 DM"}, {"months_loan_duration":48}, {"credit_history":"good"}, {"purpose":"furniture/appliances"}, {"amount":2096}, {"savings_balance":"100 - 500 DM"},{"employment_duration": "unemployed"}, {"percent_of_income":2}, {"years_at_residence":4}, {"age":50}, {"other_credit":"none"}, {"housing":"own"}, {"existing_loans_count":1}, {"job":"skilled"}, {"dependents":2}, {"phone":"yes"} ]
# input_dictionary = { "checking_balance":"< 0 DM",
#                     "months_loan_duration":48, 
#                     "credit_history":"good",
#                     "purpose":"furniture/appliances",
#                     "amount":2096,
#                     "savings_balance":"100 - 500 DM",
#                     "employment_duration": "unemployed",
#                     "percent_of_income":2,
#                     "years_at_residence":4,
#                     "age":50,
#                     "other_credit":"none",
#                     "housing":"own",
#                     "existing_loans_count":1,
#                     "job":"skilled",
#                     "dependents":2,
#                     "phone":"yes" }

input_dictionary = { "checking_balance":"> 200 DM",
                    "months_loan_duration":10, 
                    "credit_history":"good",
                    "purpose":"furniture/appliances",
                    "amount":1000,
                    "savings_balance":"100 - 500 DM",
                    "employment_duration": "unemployed",
                    "percent_of_income":1,
                    "years_at_residence":4,
                    "age":30,
                    "other_credit":"none",
                    "housing":"own",
                    "existing_loans_count":1,
                    "job":"skilled",
                    "dependents":2,
                    "phone":"yes" }


for category in categorical_columns:
    user_input= input_dictionary.get(category)
    input_dictionary[category] = encoders[category].transform([user_input])[0]
    # print(category ,"  " , input_dictionary[category])

print(list(input_dictionary.values()))
test_columns = df.columns.tolist()[:-1]
print(test_columns)

input_df = pd.DataFrame([input_dictionary.values()], columns=test_columns)

print(input_df)

print(decision_tree.classes_)

default_probability = decision_tree.predict_proba(input_df)
print(default_probability)