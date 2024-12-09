from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

#Our predictive model class!
class PredictiveModel:
    def __init__(self, filePath):
        self.filePath= filePath
        self.categorical_columns = ["checking_balance", 'credit_history', 'purpose', 'employment_duration', 'other_credit', 'housing', 'job', 'phone', 'savings_balance' ]
        self.encoders={}
        self.trainingPreprocessing()
        self.trainModel()


    def trainingPreprocessing(self):
        """
        Preprocess the training dataset by encoding categorical columns.
        Updates the dataset and saves label encoders for later use.
        """
        self.train_df = pd.read_csv(self.filePath)
        for column in self.categorical_columns:
            label_encoder = LabelEncoder()
            self.train_df[column] = label_encoder.fit_transform(self.train_df[column])
            self.encoders[column] = label_encoder

    def trainModel(self):
        """
        Train a decision tree model using the preprocessed dataset.
        Splits the data into training and testing sets and evaluates the model accuracy.
        """
        X = self.train_df.drop("default", axis=1)
        Y = self.train_df["default"]
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        self.decision_tree = tree.DecisionTreeClassifier()
        self.decision_tree = self.decision_tree.fit(X_train, y_train)
        y_predicted = self.decision_tree.predict(X_test)
        # accuracy = accuracy_score(y_test, y_predicted)
        # print(accuracy)

    def testingPreprocessing (self, input_dictionary):
        """
        Preprocess user input by encoding categorical values and aligning with training data schema.
        :param dict input_dictionary: User input values to preprocess
        """
        for category in self.categorical_columns:
            user_input= input_dictionary.get(category)
            input_dictionary[category] = self.encoders[category].transform([user_input])[0]
        test_columns = self.train_df.columns.tolist()[:-1]
        self.input_df = pd.DataFrame([input_dictionary.values()], columns=test_columns)

    def testRisk (self, input_dictionary):
        """
        Predict the probability of loan default based on user input.
    
        :param dict input_dictionary: User-provided values for prediction
        :return: Predicted probabilities of default risk
        :rtype: list
        """
        self.testingPreprocessing(input_dictionary)
        default_probability = self.decision_tree.predict_proba(self.input_df)
        return default_probability
