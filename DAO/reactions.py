from dbconfig import dbconfig
import psycopg2

class reactionsDAO:
    def __init__(self):
        curl = "dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                     dbconfig['user'],
                                                     dbconfig['password'])
        self.connection = psycopg2._connect(curl)

    #Get all messages user has reacted to, 0 for dislike, 1 for like
    def getUserReactions(self, uid):
        cursor = self.connection.cursor()
        query = "select * from Reactions where uid = %s;"
        cursor.execute(query,(uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get reactions to a message
    def getReactions(self, mid):
        cursor = self.connection.cursor()
        query = "select reactions.mid,likeValue,count(likeValue) as num from " \
                "reactions " \
                "where reactions.mid = %s group by(reactions.mid,likeValue);" \


        cursor.execute(query,(mid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    #Get reactions to a message
    def getMessageLikes(self,mid):
        likeValue =1
        cursor = self.connection.cursor()
        query = "select ufirstname,ulastname as num from " \
                "reactions inner join users on reactions.uid = users.uid " \
                "where reactions.mid = %s and likeValue = %s;"
        cursor.execute(query, (mid, likeValue,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageDislikes(self, mid,):
        likeValue = -1
        cursor = self.connection.cursor()
        query = "select * from Reactions where mid = %s and likeValue = %s;"
        cursor.execute(query, (mid, likeValue,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Get reactions with rID
    def getReactionsId(self, rid):
        cursor = self.connection.cursor()
        query = "select * from Reactions where rid = %s;"
        cursor.execute(query,(rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
