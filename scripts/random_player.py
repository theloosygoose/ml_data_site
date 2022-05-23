import nba_players
import random as rd


def getRandomPlayer(choice = 'all'):
    player_names = nba_players.NBA_PLAYERS
    randomPlayer = rd.choice(player_names)

    if choice == 'name':
        return randomPlayer['PlayerName']
    elif choice == 'nicknames':
        return randomPlayer['nicknames']
    else:
        return [randomPlayer['PlayerName'], randomPlayer['nicknames']]
