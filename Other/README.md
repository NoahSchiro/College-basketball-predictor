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
