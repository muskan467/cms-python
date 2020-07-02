#CMS
#BLL
class Customer:
    cus_list = []
    def __init__(self):
        self.id = 0
        self.name = ""
        self.age = 0
        self.mob = 0
        self.add = ""
    def createCust(self):
        for e in Customer.cus_list:
            if(e.id == self.id):
                return False
        Customer.cus_list.append(self)
        return True
    def modifyCust(self):
        for e in Customer.cus_list:
            if(e.id == self.id):
                e.name = self.name
                e.age = self.age
                e.mob = self.mob
                e.add = self.add
                return True
        else:
            return False
    def searchCust(self):
        for e in Customer.cus_list:
            if(e.id==self.id):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                return True
        else:
            return False
    @staticmethod
    def deleteCust(id):
        for e in Customer.cus_list:
            if(e.id == id):
                Customer.cus_list.remove(e)
                return e
        else:
            return False

#PL
def displayCust(cus):
    print(f"Customer i'd:{cus.id}\nCustomer name: {cus.name}\nCustomer age: {cus.age}")
    print(f"Customer mob no: {cus.mob}\nCustomer address: {cus.add}")
while(1):
    print("1. Add new customer\n2. Modify customer\n3. Search customer")
    print("4. Delete customer\n5. Display all customers\n6. Exit ")
    choice = input("Enter your choice:")
    if(choice =="1"):     #Addition of new customer
        cus = Customer()
        cus.id = input("Enter i'd of customer:")
        cus.name = input("Enter name of customer:")
        while (1):
            age = input("Enter Customer Age:")
            if (age.isdecimal()):
                if (10 <= int(age) <= 100):
                    cus.age = age
                    break
                else:
                    print("Enter Age in 10 to 100 years only")
            else:
                print("Enter Age in Whole Numbers Only")
        while (1):
            mob = input("Enter Customer mob no:")
            if (mob.isdecimal()):
                if (len(mob) == 10):
                    cus.mob = mob
                    break
                else:
                    print("Enter 10 digit no only")
            else:
                print("Enter Age in Whole Numbers Only")
        cus.add = input("Enter address of customer:")
        flag= cus.createCust()
        if (flag==True): #checking duplicacy of I'd
            print("Customer added successfully")
        else:
            print("I'd already exists")
    elif(choice == "2"):
        cus = Customer()
        cus.id = input("Enter i'd of customer:")
        cus.name = input("Enter updated name of customer:")
        cus.age = input("Enter updated age of customer:")
        cus.mob = input("Enter updated mobile of customer:")
        cus.add = input("Enter updated address of customer:")
        flag = cus.modifyCust()
        if(flag == True):
            print("Customer modified successfully")
        else:
            print("Customer I'd does not exist")
    elif(choice == "3"):
        cus = Customer()
        cus.id = input("Enter i'd of customer:")
        flag = cus.searchCust()
        if (flag == False):
           print("Customer I'd does not exist")
    elif(choice == "4"):
        cus = Customer()
        cus.id = input("Enter i'd of customer")
        cus.deleteCust(cus.id)
        flag = cus.searchCust()
        if (flag == False):
            print("Customer I'd does not exist")
    elif(choice == "5"):
        for e in Customer.cus_list:
            displayCust(e)
    elif(choice == "6"):
        break