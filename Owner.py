from User import User
class Owne(User):
    def __init__(self, name, pw, em, phone = None):
        User.__init__(self, name, pw, em, phone)
