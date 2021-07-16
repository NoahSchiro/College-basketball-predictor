#Import statements
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

from encodings import *

#Grab the data from the CSV file
nba_data = pd.read_csv('nbaallelo.csv')

#This leaves gameorder, lg_id, _iscopy, year_id, date_game, seasongame, is_playoff, team_id, fran_id, 
#elo_i, win_equiv, opp_id, opp_fran, opp_elo_i, game_location, forecast
independent_var = nba_data.drop(['game_id', 'pts', 'elo_n', 'opp_pts', 'opp_elo_n', 'game_result'], axis=1)

#This is simply pts and opp_pts in an array (what we are trying to predict)
dependent_var = nba_data[['pts', 'opp_pts']]

X_train, X_test, y_train, y_test = train_test_split(independent_var, dependent_var, train_size=0.8)

model = linear_model.LinearRegression()

model.fit(X_train, y_train)

print(model.score(X_test, y_test))