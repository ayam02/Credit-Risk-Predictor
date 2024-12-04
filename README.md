# Pre-requisites

- run the following command <br/>
  `pip install Flask`
  <br/><br/><br/>

# Running the Program

- navigate to the main folder of the project
- run the following command <br/>
  `python project.py runserver --d`
  <br/><br/><br/>

# Tech Stack

- Flask is the framework used
- Python is used for backend
- HTML, CSS are used for frontend
- Bootstrap is used for styling
  <br/><br/><br/>

# Program Design and Architecture

## project.py

This is the main script that initializes the Flask application and renders the necessary templates.

## index.html

This template displays a form for users to input data and allows them to submit the form.

## results.html

This template shows the results, indicating whether the user is likely to default on a loan. Dashboards and some statistics will also be displayed

## Model.py

This file contains a class that handles the pre-processing of data for training, trains a decision tree model, processes input data from users, tests the model, and provides the probability of a user defaulting on a loan.

## credit.csv

This CSV file contains the dataset used for training the model.
