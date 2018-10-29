class Transaction:
    def __init__(self, name):
        self.name = name
        self.productList = []
        self.insertTrans(name)

    def addTrans(self, product, quantity, time, total):
        f = open('Trans.txt','a+')
        content = self.name + '|' + product + '|' + quantity + '|' + time  + '|' + total + '|' + '\n'
        f.write(content)
        f.close()

    def total(self):
        total = 0
        for v in productList.values():
            total += y[2]
        return total

    def insertTrans(self, user):
        f = open('Trans.txt','r')
        for lines in f:
            productInfo = lines.split('|')
            if productInfo[0] == user:
                self.productList.append(productInfo[1:])
        f.close()

    def getTransList(self):
        return self.productList