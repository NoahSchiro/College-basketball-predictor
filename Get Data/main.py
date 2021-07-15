import csv

#Appends data to our csv file containing historical data for basketball games
def add_data(data):
    
    #Open csv file in append mode
    with open('data.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')

        #Determine whether or not the home team won
        if data[3] > data[4]:
            home_win = 1
        else:
            home_win = 0
        
        #Write data
        #data[0] = date, data[1] = home_team, data[2] = away_team
        #data[3] = home_score, data[4] = away_score
        writer.writerow(data + [home_win])
