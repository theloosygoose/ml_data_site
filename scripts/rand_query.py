from scripts import random_player
import random as rd
import numpy
import re


# Get Random Query
def parseName(name):
    name = re.split('\s', name)
    return name

def generateRandomQuery():
    playerNameFull = random_player.getRandomPlayer()

    playerFirstName = re.split('\s', playerNameFull[0])[0]
    playerLastName = re.split('\s', playerNameFull[0])[1]

    playerNicknames = playerNameFull[1]
    query = '' + playerLastName + ' lang:en OR ' + playerFirstName + ' ' + playerLastName + ' lang:en'

    if (playerNicknames[0] != 'NULL'):
        for i in playerNicknames:
            query += ' OR ' + i + ' lang:en'
    else:
        print('No Nicknames')

    #return "" + playerLastName + ' OR ' + playerNameFull 
    return query 


if __name__ == '__main__':
    print(generateRandomQuery())