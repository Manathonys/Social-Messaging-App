from DAO.gUsers import *
from flask import *


class gUsersHandler:

    def buildgUserDict(self, row):
      users = {}
      users['uID'] = row[0]
      users['Name'] = row[1] +" "+ row[2]
      return users

    def buildGroupDict(self, row):
        groups = {}
        groups['gID'] = row[0]
        groups['gName'] = row[1]
        groups['gOwner'] = row[2]
        return groups

    #returns all users in specified group
    def getGroupUsers(self, gid):
        dao = gUsersDAO()
        users = dao.getUsersInGroup(gid)
        users_list = []
        for row in users:
            users_list.append(self.buildgUserDict(row))

        return jsonify(Users=users_list)

    #searches for groups specified user is in
    def getGroupsWithUser(self, uid):
        dao = gUsersDAO()
        groups = dao.getUserGroups(uid)
        groups_list = []
        for row in groups:
            groups_list.append(self.buildGroupDict(row))

        return jsonify(Groups=groups_list)

    #guser registration
    def addGroupUser(self, form):
        if len(form) != 2:
            return jsonify(Error = "Malformed post request") , 400
        else:
            gid = form.get("gID")
            uid = form.get("uID")
            if gid and uid:
                dao = gUsersDAO()
                if dao.getUidInGroup(uid, gid) != []:
                    return jsonify(Error="User already exists in group"), 400
                else:
                    uid = dao.addGroupUser(gid, uid)
                    return self.getGroupUsers(gid)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400