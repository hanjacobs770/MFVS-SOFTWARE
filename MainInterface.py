import re
import sys
import time
sys.path.append('Userclasses')
sys.path.append('Products')
from UserLists import UserLists
from Customer import Customer
from Products import Products
from Shelf import Shelf
from Transaction import Transaction

class MainInterface:
    def __init__(self):
        self.acl = UserLists()
        self.pcl = Shelf()
        self.counter = 0
        self.currentUser = None
        self.trans = None

    # Register a new customer
    def register(self):
        print("Please input your username")
        name = input()
        print("Please input your password")
        #pw = input()
        while True:
            pw = input()
            # pw = raw_input("Enter a password: ")
            if len(pw) < 8:
                print("Make sure your password is at lest 8 letters")
            elif re.search('[0-9]', pw) is None:
                print("Make sure your password has a number in it")
            elif re.search('[A-Z]', pw) is None:
                print("Make sure your password has a capital letter in it")
            else:
                print("Your password seems fine")
                break
        print("Please input your email address")
        while True:
            em = input()
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", em) != None:

                print('Email Id seems fine')
                break
            else:
                print("Email ID does not follow the desired syntax, example@gmail.com")
                print('Enter your password again')


        print("Please input your phone number")
        while True:
            ph = input()
            if re.match(r'(?:\+?61)?(?:\(0\)[23478]|\(?0?[23478]\)?)\d{8}', ph)!=None:
                print('Phone number is fine')
                break
            else:
                print('Phone number is not valid, match the format 0451924979 or +61451924979')
                print("Enter your number again")
        print("Please input your security question")
        q = input()
        print("Please input your security answer")
        a = input()
        newCustomer = Customer(name, pw, em, ph, q, a)
        self.acl.addAccount(newCustomer)
        self.acl.userAccouts[name] = [pw, em, ph, q, a]
    # Login the system
    # parameter: pw -> password
    def login(self):
        print("Please input your username and password")
        username = input()
        pw = str(input())
        try:
            if self.acl.userAccouts[username][0] == pw:
                print("Succeed")
                self.currentUser = Customer(username, pw, self.acl.userAccouts[username][1],
                                            self.acl.userAccouts[username][2],
                                            self.acl.userAccouts[username][3],
                                            self.acl.userAccouts[username][4])
                if username == 'admin':
                    return self.adminOperate()
                else:
                    self.trans = Transaction(username)
                    return self.opearte()
            else:
                print("Invalid password")
                self.counter += 1
                if self.counter == 3:
                    question = self.acl.userAccouts[username][3]
                    print("Security question:" + question)
                    aw = input()
                    if aw == self.acl.userAccouts[username][4]:
                        print("Success")
                        self.currentUser = Customer(username, pw, self.acl.userAccouts[username][1],
                                                    self.acl.userAccouts[username][2],
                                                    self.acl.userAccouts[username][3],
                                                    self.acl.userAccouts[username][4])
                        self.trans = Transaction(username)
                        return self.opearte()
                else:
                    self.login()
        except:
            print("Invalid username")
            self.login()

    def purchaseProduct(self):
        if self.currentUser == None:
            print("Please login first")
        else:
            print("Please input the name of the product")
            nm = input()
            if nm not in self.pcl.getProductLists().keys():
                print("This product does not exist")
                return self.purchaseProduct()
            else:
                price = self.pcl.getProductLists()[nm][2]
                discount = self.pcl.getProductLists()[nm][3]
                quantity = self.pcl.getProductLists()[nm][4]
                onePack = self.pcl.getProductLists()[nm][5]
            print("Please press 1 for purchasing single product, 2 for purchasing by package, one pack has " + onePack + "\nThe maximum quantity is " + quantity)
            choice = input()
            if choice == '1':
                print('Ok please enter the quantity')
                qt = input()
            else:
                print('Ok please enter the number the number of packs')
                number = input()
                try:
                    number = int(number)
                    qt = int(onePack) * number
                except:
                    print("It must be an integar")
                    return self.purchaseProduct()
            try:
                while int(qt) > int(quantity):
                    print("The product number is not sufficient, the maximum number is " + quantity + ", please enter again")
                    qt = input()
                total = float(price) * int(qt) * float(discount)
                info = "The total price is " + str(total) + ', input 1 for purchase, 2 for quit'
                print(info)
                result = input()
                try:
                    result = int(result)
                    if result == 1:
                        self.currentUser.getCart().addCart(nm,str(qt),total)
                        ft = int(quantity) - int(qt)
                        self.pcl.deleteContent(nm, 5, str(ft))
                        self.currentUser.regetCart()
                        self.pcl.insertProducts()
                    if result == 2:
                        self.opearte()
                except:
                    print("An integer is needed")
                    self.purchaseProduct()
            except:
                print("Quantity needs to be a number")
                self.purchaseProduct()

    def mainChoice(self):
        if self.currentUser == None:
            print("Please input corresponding number to operate the system")
            print("1. Login")
            print("2. Register")
            print("3. Search product")
            print("4. View products")
            print("5. Purchase products")
            print("6. Quit")
        else:
            print("1. Search product")
            print("2. View products")
            print("3. Purchase products")
            print("4. View Cart")
            print("5. Modify details")
            print("6. Check my transaction")
            print("7. Log out")
            print("8. Quit")

    def adminChoice(self):
        print("Please input corresponding number to operate the system")
        print("1. Insert products")
        print("2. Block user")
        print("3. View transaction")
        print("4. Modify products")
        print("5. Quit")

    def displayProduct(self):
        aList = []
        print("To print by alphabet please input 1, by price input 2")
        a = input()
        if a == '1':
            for item, key in self.pcl.getProductLists().items():
                aList.append([item, key])
            aList.sort()
            for item in aList:
                words = "Product: " + item[0] + '\nPrice:' + item[1][2] + '\nDiscount:' + item[1][3] + '\nQuantity:'\
                        + item[1][4] +'\nOne-Pack:' + item[1][5] + '\nDescription:' + item[1][0] + '\n****************************'
                print(words)
        if a == '2':
            for item, key in self.pcl.getProductLists().items():
                aList.append([float(key[2]), item, key])
            aList.sort()
            for item in aList:
                words = "Product: " + item[1] + '\nPrice:' + item[2][2] + '\nDiscount:' + item[2][3] + '\nQuantity:' + item[2][4] + '\nOne-Pack:' + item[2][5] + \
                        '\nDescription:' + item[2][0] + '\n****************************'
                print(words)

    def opearte(self):
        self.mainChoice()
        try:
            i = int(input())
        except:
            print("you need to input an integer")
            return self.opearte()
        if self.currentUser == None and i != 6:
            if i == 1:
                return self.login()
            if i == 2:
                self.register()
            if i == 3:
                print("Please input the search phrase\nIf you would like to serch by category please type either vegetable or fruit and then the word category")
                ip = input()
                content = ip.split(' ')
                if len(content) == 1:
                    self.pcl.search(content[0], 'product')
                else:
                    self.pcl.search(content[0], content[1])
            if i == 4:
                self.displayProduct()
            if i == 5:
                self.purchaseProduct()
            return self.opearte()
        elif self.currentUser != None and i != 8:
            if i == 1:
                print("Please input the search phrase")
                r = input()
                b = r.split(' ')
                if len(b) == 1:
                    self.pcl.search(b[0], 'product')
                else:
                    self.pcl.search(b[0],b[1])
            if i == 2:
                self.displayProduct()
            if i == 3:
                self.purchaseProduct()
            if i == 4:
                gp = self.currentUser.getCart().getProductList()
                for i in gp:
                    words = "Product: " + i[0] + ", Quantity: " + i[1] + ", Price: " + i[2]
                    print(words)
                print("If you want to checkout your cart, please input 1.  2 for quit")
                i = input()
                if i == '1':
                    nowTime  = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                    for i in gp:
                        self.trans.addTrans(i[0],i[1],nowTime,i[2])
                    self.currentUser.getCart().deleteContent()
                    self.trans = Transaction(self.currentUser.getName())
                    self.currentUser.regetCart()
                if i == '2':
                    return self.opearte()
            if i == 5:
                print("Please input the type that you want to modify")
                print("1. Password")
                print("2. Email")
                print("3. Phone")
                ip = int(input())
                print("Please input the change")
                cg = input()
                self.acl.modifyDetail(self.currentUser.getName(),ip,cg)
            if i == 6:
                for i in self.trans.getTransList():
                    words = "Product: " + i[0] + ", Quantity: " + i[1] + ", Price: " + i[3] + ", Timestamp:" + i[2]
                    print(words)
            if i == 7:
                self.currentUser = None
            return self.opearte()
        else:
            pass

    def adminOperate(self):
        self.adminChoice()
        i = int(input())
        if i != 5:
            if i == 1:
                print("Please input the product name")
                nm = input()
                print("Please input the description")
                des = input()
                print("Please input the grocery")
                gc = input()
                print("Please input the price")
                pc = input()
                print("Please input the discount")
                dc = input()
                print("Please input the quantity of the product")
                qt = input()
                print("Please input the numbers for one pack")
                pk = input()
                self.pcl.addProducts(Products(nm,des,gc,pc,dc,qt,pk))
            if i == 2:
                print("Please input the block user name")
                nm = input()
                self.acl.blockAccount(nm)
            if i == 4:
                print("Please enter the name of product that needed to change")
                i = input()
                print("Please enter the attribute that needed to change:")
                print("1. Description")
                print("2. Category")
                print("3. Price")
                print("4. Discount")
                print("5. Quantity")
                print("6. Cages")
                m = int(input())
                print("Please input the content")
                c = input()
                self.pcl.deleteContent(i,m,c)
            if i == 3:
                print("Please enter the name of user")
                nm = input()
                self.trans = Transaction(nm)
                for i in self.trans.getTransList():
                    words = "Product: " + i[0] + ", Quantity: " + i[1] + ", Price: " + i[3] + ", Timestamp:" + i[2]
                    print(words)
            return self.adminOperate()

MI = MainInterface()
MI.opearte()

