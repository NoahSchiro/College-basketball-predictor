#Import statements
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split


#Grab the data from the CSV file
nba_data = pd.read_csv('nbaallelo.csv')

independent_var = nba_data.drop(['game_id', 'pts', 'elo_n', 'opp_pts', 'opp_elo_n', 'game_result'], axis=1)
dependent_var = nba_data[['pts', 'opp_pts']]

X_train, X_test, y_train, y_test = train_test_split(independent_var, dependent_var)

model = linear_model.LinearRegression()

model.fit(X_train, y_train)