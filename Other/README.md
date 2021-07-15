# College basketball predictor
---


### The Dataset
---

Taken from https://www.kaggle.com/fivethirtyeight/fivethirtyeight-nba-elo-dataset?select=README.md which used a web scraper to pull data from https://www.basketball-reference.com/ (which we will eventually do in future versions of this program so that the data is always up to date.

Header | Description
-------|------------
```gameorder``` | Play order of game in NBA history
```game_id``` | Unique ID for each game
```lg_id``` | Which league the game was played in
```_iscopy``` | Each row of data is tied to a single team for a single game, so iscopy flags if this gameid has already occured for the opposing team in the same matchup
```year_id``` | Season id, named based on year in which the season ended
```date_game``` | Game date
```is_playoffs``` | Flag for playoff games
```team_id``` | Three letter code for team name, from Basketball Reference
```fran_id``` | Franchise id. Multiple teamids can fall under the same franid due to name changes or moves. Interactive is grouped by fran_id.
```pts``` | Points scored by team
```elo_i``` | Team elo entering the game
```elo_n``` | Team elo following the game
```win_equiv``` | Equivalent number of wins in a 82-game season for a team of elo_n quality
```opp_id``` | Team id of opponent
```opp_fran``` | Franchise id of opponent
```opp_pts``` | Points scored by opponent
```opp_elo_i``` | Opponent elo entering the game
```opp_elo_n``` | Opponent elo following the game
```game_location``` | Home (H), away (A), or neutral (N)
```game_result``` | Win or loss for team in the team_id column
```forecast``` | Elo-based chances of winning for the team in the team_id column, based on elo ratings and game location

What data pointes will we train on? What data points will we try to predict? It seems most appropriate to try to guess the final score of the game for both teams. What data points will we have available to us to feed into the training model before a game beigns: gameorder, lg_id, year_id, date_game, is_playoffs, team_id, fran_id, elo_i, win_equiv, opp_id, opp_fran, opp_elo_i, game_location, forecast (??? maybe).


# Data Cleaning
---
In order to feed data into the machine learning model, all of the inputs need to be number based. For instance, team_id needs to be converted from letters to numbers. Same with lg_id, fran_id, etc. We will create here a table of the values so that we know which number represents

lg_id | Number
--------------
NBA   | 0
ABA   | 1

team_id | Number
----------------
TRH | 0
NYK | 1
CHS | 2
DTF | 3
WSC | 4
BOS | 5
PRO | 6
PIT | 7
STB | 8
CLR | 9
PHW | 10
BLB | 11
INJ | 12
FTW | 13
MNL | 14
ROC | 15
TRI | 16
DNN | 17
INO | 18
SHE | 19
WAT | 20
AND | 21
SYR | 22
MLH | 23
STL | 24
SET | 25
CIN | 26
LAL | 27
CHP | 28
CHZ | 29
SFW | 30
BAL | 31
PHI | 32
CHI | 33
SEA | 34
OAK | 35
ANA | 36
SDR | 37
KEN | 38
INA | 39
DNR | 40
DLC | 41
HSM | 42
NOB | 43
MNM | 44
NJA | 45
PTP | 46
ATL | 47
MIL | 48
PHO | 49
NYA | 50
MMF | 51
MNP | 52
LAS | 53
CAR | 54
WSA | 55
BUF | 56
CLE | 57
UTS | 58
FLO | 59
PTC | 60
POR | 61
VIR | 62
TEX | 63
MMP | 64
HOU | 65
GSW | 66
KCO | 67
MMT | 68
SDA | 69
CAP | 70
SAA | 71
NOJ | 72
DNA | 73
SSL | 74
MMS | 75
WSB | 76
KCK | 77
SDS | 78
IND | 79
NYN | 80
DEN | 81
SAS | 82
NJN | 83
SDC | 84
UTA | 85
SAL | 86
LAC | 87
SAC | 88
CHH | 89
MIA | 90
MIN | 91
ORL | 92
VAN | 93
TOR | 94
WAS | 95
MEM | 96
NOH | 97
CHA | 98
NOK | 99
OKC | 100
BRK | 101
NOP | 102
CHO | 103

fran_id | Number
----------------
Huskies | 0
Knicks | 1
Stags | 2
Falcons | 3
Capitols | 4
Celtics | 5
Steamrollers | 6
Ironmen | 7
Bombers | 8
Rebels | 9
Warriors | 10
Baltimore | 11
Jets | 12
Pistons | 13
Lakers | 14
Kings | 15
Hawks | 16
Denver | 17
Olympians | 18
Redskins | 19
Waterloo | 20
Packers | 21
Sixers | 22
Wizards | 23
Bulls | 24
Thunder | 25
Squires | 26
Stars | 27
Rockets | 28
Colonels | 29
Pacers | 30
Nuggets | 31
Spurs | 32
Spirits | 33
Sounds | 34
Floridians | 35
Nets | 36
Condors | 37
Bucks | 38
Suns | 39
Clippers | 40
Cavaliers | 41
Trailblazers | 42
Sails | 43
Jazz | 44
Mavericks | 45
Pelicans | 46
Heat | 47
Timberwolves | 48
Magic | 49
Grizzlies | 50
Raptors | 51
Hornets | 52

game_location | Number
----------------------
Home | 0
Away | 1
N/A | 2
