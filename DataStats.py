import pandas as pd
class DataStats:
    def __init__(self):
        self.filePath = "credit.csv"
        self.categorical_columns = ["checking_balance", "months_loan_duration", 'credit_history', 'purpose', "savings_balance", 'employment_duration', 'other_credit', 'housing', 'job', 'phone' ]

    def uniqueValues(self):
        df = pd.read_csv('credit.csv')
        for col in self.categorical_columns:
            print(col, " has ", df[col].nunique(), " unique values ")
            print(df[col].unique())
    
