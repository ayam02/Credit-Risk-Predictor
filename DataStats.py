import pandas as pd
import numpy as np

class DataStats:
    #Define/separate numerical and categorical columns (so i don't get a typeerror)
    numerical_columns = [
        'months_loan_duration', 'amount', 
        'percent_of_income', 'years_at_residence', 
        'age', 'existing_loans_count', 'dependents'
    ]
    categorical_columns = ['checking_balance', 'credit_history', 'purpose', 
                           'savings_balance', 'employment_duration', 'savings_balance',
                           'other_credit', 'housing', 'job', 'phone']

    @staticmethod
    def preprocess_data(df):
        #Preprocess numerical and categorical columns to ensure data ->casting numerical columns
        
        # Process numerical columns
        for column in DataStats.numerical_columns:
            if column in df.columns:
                try:
                    df[column] = pd.to_numeric(df[column], errors='coerce')  # Convert to numeric
                except Exception as e:
                    print(f"Could not convert column {column} to numeric. Error: {e}")
        df[DataStats.numerical_columns] = df[DataStats.numerical_columns].fillna(0)  # Fill NaNs

        # Process categorical columns
        for column in DataStats.categorical_columns:
            if column in df.columns:
                df[column] = df[column].fillna("unknown")  # Fill missing with 'unknown'

        return df

    @staticmethod
    def load_data():
        #Load and preprocess the dataset... can't resuse prev fn unfortunately
        df = pd.read_csv("credit.csv")
        return DataStats.preprocess_data(df)

    @staticmethod
    def calculate_statistics():
        
        #Calculate mean, median, mode, and stdev for numerical columns.
        
        df = DataStats.load_data()
        stats = {}
        
        for column in DataStats.numerical_columns:
            if column in df.columns:
                stats[column] = {
                    'mean': df[column].mean(),
                    'median': df[column].median(),
                    'mode': df[column].mode()[0] if not df[column].mode().empty else None,
                    'stdev': df[column].std()
                }
        return stats

    @staticmethod
    def count_defaults(df, category=None):
        #Counts the number of people likely to default - expand to be grouped by a category.
        
        if category:
            if category in df.columns:
                #Group by the specified category and count occurrences of 'yes' in 'default'
                return df.groupby(category)['default'].apply(lambda x: (x == 'yes').sum()).to_dict()
            else:
                print(f"Category '{category}' not found in data.")
                return {}
        #Count occurrences of 'yes' and 'no' in the default column
        return df['default'].value_counts().to_dict()

    @staticmethod
    def demographic_statistics(df):
        #Generate statistics for demographics to identify groups most likely to default.
        #Aggregates only numeric columns for mean calculation.
        
        numeric_df = df.select_dtypes(include=['number'])
        return df.groupby('default')[numeric_df.columns].mean().to_dict()

    @staticmethod
    def risk_mitigation_suggestions(profile):
        #lowkey frivolous...hardcoded suggestions to reduce default risk based on the profile info entered.
        
        suggestions = []
        if profile.get('savings_balance', 0) < 100:
            suggestions.append("Increase savings balance to reduce risk.")
        if profile.get('employment_duration', 'unemployed') == 'unemployed':
            suggestions.append("Consider stable employment opportunities.")
        return suggestions

    @staticmethod
    def generate_all_insights(profile=None):
        #Combine all insights into a single output structure to display in resuats.
        df = DataStats.load_data()
        insights = {
            'statistics': DataStats.calculate_statistics(),
            'default_counts': DataStats.count_defaults(df),
            'demographic_stats': DataStats.demographic_statistics(df),
        }
        if profile:
            insights['risk_mitigation'] = DataStats.risk_mitigation_suggestions(profile)
        return insights
