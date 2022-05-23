if __name__ == '__main__':
    import config
    import nba_players
else: 
    from scripts import config
    from scripts import nba_players

import tweepy
import random as rd
import numpy

client = tweepy.Client(bearer_token = config.BEARER_TOKEN)
player_names = nba_players.NBA_PLAYERS

def randomNBAPlayer():
    return rd.choice(player_names)

if __name__ == '__main__':
    print(randomNBAPlayer())