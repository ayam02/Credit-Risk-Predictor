import pandas as pd
import numpy as np

class ChartGenerator:
    def __init__(self, filePath):
        self.filePath = filePath
         #This class is going to be staticly reading the dataset
        self.df = pd.read_csv(self.filePath)
        self.charts = []
        
        #Graphic design is my passion /j
        self.colors = [
                'rgba(204, 85, 0, 0.9)',    #orange
                'rgba(153, 51, 51, 0.9)',   #red
                'rgba(51, 102, 153, 0.9)',  #blue
                'rgba(102, 102, 51, 0.9)',  #yellow
                'rgba(102, 51, 102, 0.9)',  #purple
                'rgba(153, 102, 51, 0.9)',  #brown
                'rgba(76, 70, 50, 0.9)',    #olive
                'rgba(153, 76, 0, 0.9)'     #sienna
            ]        
        # Dark red highlight for user's value
        self.highlight_color = 'rgba(139, 0, 0, 0.9)'  # Dark red
        
        self.categorical_columns = [
            "checking_balance", "credit_history", "purpose", 
            "savings_balance", "employment_duration", "other_credit",
            "housing", "job", "phone"
        ]
        
        self.numerical_columns = [
            "months_loan_duration", "amount", "percent_of_income",
            "years_at_residence", "age", "existing_loans_count",
            "dependents"
        ]


    def generate_charts(self, user_input=None):
        
        #Generate charts with user value highlighting and indicators
        #Parameters: user_input (dict): Dictionary containing user's form input values
        #Returns: list: List of chart configurations
        
        #Create categorical charts for each column in the csv
        for column in self.categorical_columns:
            value_counts = self.df[column].value_counts()
            labels = value_counts.index.tolist()
            data = value_counts.values.tolist()
            self.colors = [self.colors[i % len(self.colors)] for i in range(len(labels))]
            
            #Track user's value for this column
            user_value = None
            if user_input and column in user_input and user_input[column] is not None:
                user_value = str(user_input[column])
                for i, label in enumerate(labels):
                    if str(label) == user_value:
                        self.colors[i] = self.highlight_color
            
            self.charts.append({
                'id': f'chart_{column}',
                'type': 'bar',
                'title': f'Distribution of {column.replace("_", " ").title()}',
                'labels': labels,
                'data': data,
                'colors': self.colors,
                'max_value': max(data) * 1.2,
                'user_value': user_value  # Include user's value in chart data
            })
            
        return self.charts
