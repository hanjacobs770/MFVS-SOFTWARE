class UserLists:
    def __init__(self):
        self.userAccouts = {}
        self.insertLists()

    # Add a new user into the accout list
    # parameter: user -> the new user class
    def addAccount(self, user):
        f = open('userList.txt','a+')
        self.userAccouts[user.getName()] = user
        userInfo = user.getName() + '|' + user.getPw() + '|' + user.getPhone() + '|' + user.getEmail() + '|' + user.getQ() + '|' + user.getA() + '|' + '\n'
        f.write(userInfo)
        f.close()
    # block a user with its name
    # parameter: userName -> the name of the user

    def blockAccount(self,userName):
        if userName in self.userAccouts:
            with open('userList.txt', 'r') as r:
                lines = r.readlines()
            with open('userList.txt', 'w') as w:
                for l in lines:
                    userInfo = l.split("|")
                    if userName != userInfo[0]:
                        w.write(l)
                    else:
                        pass
        else:
            print('Sorry, this username is invalid')

    def insertLists(self):
        f = open('userList.txt','r')
        for line in f:
            userInfo = line.split("|")
            self.userAccouts[userInfo[0]] = userInfo[1:]
        f.close()

    def modifyDetail(self, user, type, content):
        with open('userList.txt', 'r') as r:
            lines = r.readlines()
        with open('userList.txt', 'w') as w:
            for l in lines:
                userInfo = l.split("|")
                if user != userInfo[0]:
                    w.write(l)
                else:
                    userInfo[type] = content
                    words = userInfo[0] + '|' + userInfo[1] + '|' + userInfo[2] + '|' + userInfo[3] + '|' + userInfo[4] +'|' + userInfo[5] + '|' + '\n'
                    w.write(words)