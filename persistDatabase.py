import sqlite3
import sys

from espnCricinfoStatsDownloader import StatsDownloader


class PersistDatabase:

    def __init__(self,playerName,connection):
        self.playerName = playerName
        self.databseConnection = connection

    def createPlayerID(self):
        cursor = self.databseConnection.cursor()
        cursor.execute("SELECT * FROM Players WHERE Player_Name=?", (self.playerName,))
        rows = cursor.fetchall()
        if (len(rows) != 0):
            print("Player already exists")
            self.databseConnection.close()
            sys.exit(0)
        else:
            cursor.execute('INSERT INTO Players (Player_Name) VALUES (?)',
                           (self.playerName,))
            player_Id = cursor.lastrowid
            # self.databseConnection.commit()
            # self.databseConnection.close()
            print("Player ID Created, player id is ",player_Id)
            return player_Id

    def persistData(self,data,player_id):
        print("Persisting data for player Name "+self.playerName)
        cursor = self.databseConnection.cursor()
        for index, row in data.iterrows():
            query = """INSERT INTO `{}`
                                  ('Player_ID','Mat', 'Inns', 'NO', 'Runs', 'HS', 'Ave', 'BF', 'SR', '100', '50', '4s', '6s', 'Ct', 'St') 
                                  VALUES (?, ?, ?, ?,?,?, ?, ?,?,?, ?, ?,?,?,?);""".format(index)
            values = list(row)
            values.insert(0, player_id)
            # print((values))
            cursor.execute(query, values)
        print("Data Persist Successfull")
        self.databseConnection.commit()
        # self.databseConnection.close()



