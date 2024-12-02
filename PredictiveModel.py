from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

class PredictiveModel:
    def __init__(self, filePath):
        self.filePath(filePath)
        self.categorical_columns = ["checking_balance", 'credit_history', 'purpose', 'employment_duration', 'other_credit', 'housing', 'job', 'phone', 'savings_balance' ]
        self.encoders={}

    def trainingPreprocessing(self):
        self.train_df = pd.read_csv(self.filePath)
        for column in self.categorical_columns:
            label_encoder = LabelEncoder()
            self.train_df[column] = label_encoder.fit_transform(self.train_df[column])
            self.encoders[column] = label_encoder

    def trainModel(self):
        self.preprocessData()
        X = self.train_df.drop("default", axis=1)
        Y = self.train_df["default"]
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        self.decision_tree = tree.DecisionTreeClassifier()
        self.decision_tree = self.decision_tree.fit(X_train, y_train)
        y_predicted = self.decision_tree.predict(X_test)
        # accuracy = accuracy_score(y_test, y_predicted)
        # print(accuracy)

    def createInputDictionary(self, array_input):
        self.input_dictionary = { "checking_balance":"> 200 DM",
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

    def testingPreprocessing (self):
        for category in self.categorical_columns:
            user_input= self.input_dictionary.get(category)
            self.input_dictionary[category] = self.encoders[category].transform([user_input])[0]
        test_columns = self.train_df.columns.tolist()[:-1]
        self.input_df = pd.DataFrame([self.input_dictionary.values()], columns=test_columns)

    def testRisk (self):
        default_probability = self.decision_tree.predict_proba(self.input_df)
        return default_probability[0]