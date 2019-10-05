import sqlite3

import scraper
from espnCricinfoStatsDownloader import StatsDownloader
from persistDatabase import PersistDatabase

def getPlayers():
    return scraper.listOfPlayers()

if __name__ == '__main__':
    # # rohit_sharma = "Rohit Sharma"
    # link = "http://www.espncricinfo.com/india/content/player/34102.html"
    connection = sqlite3.connect('Hello.db')
    playersMap = getPlayers()
    for playerName, PlayerLink in playersMap.items():
        statsDownloader = StatsDownloader(PlayerLink,playerName)
        battingStats = statsDownloader.downloadBattingStats()
        p = PersistDatabase(playerName,connection)
        playerId = p.createPlayerID()
        p.persistData(battingStats,playerId)
        print("-----")
    connection.close()


