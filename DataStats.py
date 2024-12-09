import pandas as pd
import numpy as np

class DataStats:
    #Define/separate numerical and categorical columns (to prevent a typeerror)
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
    """
    Preprocess numerical and categorical columns in the dataset.

    :param pd.DataFrame df: The input dataset to preprocess
    :return: The preprocessed dataset with missing values handled
    :rtype: pd.DataFrame
    """
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
        """
        Load and preprocess the dataset from a CSV file.
    
        :return: The preprocessed dataset
        :rtype: pd.DataFrame
        """
        df = pd.read_csv("credit.csv")
        return DataStats.preprocess_data(df)

    @staticmethod
    def calculate_statistics():
        """
        Calculate stats (mean, median, mode, stdev) for numerical columns.
    
        :return: A dictionary with stats for each numerical column
        :rtype: dict
        """
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
        """
        Count loan defaults
    
        :param pd.DataFrame df: The dataset
        :param str category: (Optional) Column name for grouping default counts
        :return: A dictionary with default counts
        :rtype: dict
        """

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
        """
        Compute mean statistics for numerical columns grouped by 'default' status (yes or no).
    
        :param pd.DataFrame df: The dataset
        :return: A dictionary with demographic statistics for defaulters and non-defaulters
        :rtype: dict
        """
        
        numeric_df = df.select_dtypes(include=['number'])
        return df.groupby('default')[numeric_df.columns].mean().to_dict()

    @staticmethod
    def risk_mitigation_suggestions(profile):
        """
        Output suggestions to reduce loan default risk based on user profile...hardcoded suggestions to reduce default risk based on the profile info entered
    
        :param dict profile: User's financial and demographic details
        :return: A list of risk mitigation suggestions (suggestions to be expanded upon ideally)
        :rtype: list
        """
        
        suggestions = []
        if profile.get('savings_balance', 0) < 100:
            suggestions.append("Increase savings balance to reduce risk.")
        if profile.get('employment_duration', 'unemployed') == 'unemployed':
            suggestions.append("Consider stable employment opportunities.")
        return suggestions

    @staticmethod
    def generate_all_insights(profile=None):
        """
        Combine all insights for single output: statistics, default counts, and risk mitigation suggestions.
    
        :param dict profile: User's financial and demographic details for custom suggestions
        :return: A dictionary containing all insights
        :rtype: dict
        """

        df = DataStats.load_data()
        insights = {
            'statistics': DataStats.calculate_statistics(),
            'default_counts': DataStats.count_defaults(df),
            'demographic_stats': DataStats.demographic_statistics(df),
        }
        if profile:
            insights['risk_mitigation'] = DataStats.risk_mitigation_suggestions(profile)
        return insights
