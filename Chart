import pandas as pd
import numpy as np

class ChartGenerator:
    @staticmethod
    def generate_charts(user_input=None):
        
        #Generate charts with user value highlighting and indicators
        #Parameters: user_input (dict): Dictionary containing user's form input values
        #Returns: list: List of chart configurations
        
        #This class is going to be staticly reading the dataset
        df = pd.read_csv("credit.csv")
        charts = []
        
        #Graphic design is my passion /j
        def get_default_color(index):
            colors = [
                'rgba(204, 85, 0, 0.9)',    #orange
                'rgba(153, 51, 51, 0.9)',   #red
                'rgba(51, 102, 153, 0.9)',  #blue
                'rgba(102, 102, 51, 0.9)',  #yellow
                'rgba(102, 51, 102, 0.9)',  #purple
                'rgba(153, 102, 51, 0.9)',  #brown
                'rgba(76, 70, 50, 0.9)',    #olive
                'rgba(153, 76, 0, 0.9)'     #sienna
            ]
            return colors[index % len(colors)]
        
        # Dark red highlight for user's value
        highlight_color = 'rgba(139, 0, 0, 0.9)'  # Dark red
        
        categorical_columns = [
            "checking_balance", "credit_history", "purpose", 
            "savings_balance", "employment_duration", "other_credit",
            "housing", "job", "phone"
        ]
        
        numerical_columns = [
            "months_loan_duration", "amount", "percent_of_income",
            "years_at_residence", "age", "existing_loans_count",
            "dependents"
        ]
        
        #Create categorical charts for each column in the csv
        for column in categorical_columns:
            value_counts = df[column].value_counts()
            labels = value_counts.index.tolist()
            data = value_counts.values.tolist()
            colors = [get_default_color(i) for i in range(len(labels))]
            
            #Track user's value for this column
            user_value = None
            if user_input and column in user_input and user_input[column] is not None:
                user_value = str(user_input[column])
                for i, label in enumerate(labels):
                    if str(label) == user_value:
                        colors[i] = highlight_color
            
            charts.append({
                'id': f'chart_{column}',
                'type': 'bar',
                'title': f'Distribution of {column.replace("_", " ").title()}',
                'labels': labels,
                'data': data,
                'colors': colors,
                'max_value': max(data) * 1.2,
                'user_value': user_value  # Include user's value in chart data
            })
        
        # Generate numerical charts
        for column in numerical_columns:
            hist, bins = np.histogram(df[column], bins='auto')
            bin_labels = [f'{bins[i]:.1f}-{bins[i+1]:.1f}' for i in range(len(bins)-1)]
            colors = [get_default_color(i) for i in range(len(bin_labels))]
            
            # Track user's value for this column
            user_value = None
            if user_input and column in user_input and user_input[column] is not None:
                try:
                    user_value = float(user_input[column])
                    for i in range(len(bins)-1):
                        if bins[i] <= user_value < bins[i+1]:
                            colors[i] = highlight_color
                except (ValueError, TypeError):
                    pass
            
            charts.append({
                'id': f'chart_{column}',
                'type': 'bar',
                'title': f'Distribution of {column.replace("_", " ").title()}',
                'labels': bin_labels,
                'data': hist.tolist(),
                'colors': colors,
                'max_value': max(hist) * 1.2,
                'user_value': user_value  # Include user's value in chart data
            })
            
        return charts
