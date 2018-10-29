# This is user class for recording the information of user
class User:
    def __init__(self, name, pw, em, phone, question, answer):
        self.name = str(name)
        self.password = str(pw)
        self.email = str(em)
        self.phone = str(phone)
        self.question = str(question)
        self.answer = str(answer)

    # To get the name of the user
    def getName(self):
        return self.name

    # To get the email of the user
    def getEmail(self):
        return self.email

    # To get the phone of the user
    def getPhone(self):
        return self.phone

    # To get the password of the user
    def getPw(self):
        return self.password

    def getQ(self):
        return self.question

    def getA(self):
        return self.answer

    # To change the password
    # parameter: newPw -> new password
    def changePw(self, newPw):
        self.password = newPw

    # To change the name of user
    # parameter: newN -> new name
    def changeName(self, newN):
        self.name = newN

    # To change the email
    # parameter: newE -> new email
    def changeEmail(self,newE):
        self.email = newE

    # To change the phone number
    # parameter: newP -> new phone number
    def changePhone(self, newP):
        self.phone = newP


