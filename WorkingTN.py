##########################################################
#   CS217:      WorkingTN
#   Assignment: Lab5
#   Author:     James Burch
#   Date:       11/29/2016
#   Filename:   telephoneNumber.py
#   Purpose:
#
##########################################################

from telephoneNumber import TelephoneNumber

class WorkingTN(TelephoneNumber):
    def __init__(self, inNPA = "000", inNXX = "000", inLine = "0000", inCostomer = "None"):
        super().__init__(inNPA, inNXX, inLine) # call parent __init__(...)
        #self.__costumer = inCostomer if len(inCostomer) > 0 else "No Name" #Guards against an empty string
        self.__costumer = "None" ; self.setCostumer(inCostomer) #This line of code does the same as above but uses the set fuction to Guards against an empty string
        print("In WorkingTN Constructor")


    def load(self):
        super().load()
        self.__customer = input("Enter customer's name:")
        while len(self.__customer) == 0:
            self.__customer = input("Empyt name -- please re-enter: ")


    def __del__(self):
        print("In WorkingTN Destructor")
        super().__del__()


    def setCostumer(self, newCostomer):
        self.__customer = newCostomer if len(newCostomer) > 0 else self.__costumer

    def getCostumer(self):
        return self.__customer

    def __str__(self):
        return super().__str__() + "\n" + self.__customer


    def displayPhoneNumber(self):
        super().displayPhoneNumber()
        print("Customer is:", self.__customer)


if __name__ == '__main__':
    myWorkingTN = WorkingTN()
    print(" myWorkingTN =", myWorkingTN)
    myWorkingTN.displayPhoneNumber()
    myWorkingTN = WorkingTN("719", "598" , "0200" , "CTU")
    print(" myWorkingTN =", myWorkingTN)
    myWorkingTN.displayPhoneNumber()