if __name__ == '__main__':
    import config
    import random_player
else: 
    from scripts import config
    from scripts import random_player

import tweepy
import random as rd
import numpy
import re

client = tweepy.Client(bearer_token = config.BEARER_TOKEN)

# Get Random Query
def parseName(name):
    name = re.split('\s', name)
    return name

def generateRandomQuery():
    playerNameFull = random_player.getRandomPlayer('name')
    playerNicknames = random_player.getRandomPlayer('nicknames')
    
    playerFirstName = re.split('\s', playerNameFull)[0]
    playerLastName = re.split('\s', playerNameFull)[1]

    query = "" + playerLastName + ' OR ' + playerNameFull + ' OR '

if __name__ == '__main__':
    print(generateRandomQuery())
    print(random_player.getRandomPlayer('nicknames'))