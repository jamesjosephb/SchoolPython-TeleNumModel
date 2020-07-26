##########################################################
#   CS217:      BillingTN
#   Assignment: Lab5
#   Author:     James Burch
#   Date:       11/29/2016
#   Filename:   telephoneNumber.py
#   Purpose:
#
##########################################################


from WorkingTN import WorkingTN

class BillingTN(WorkingTN):
    def __init__(self, inNPA = "000", inNXX = "000", inLine = "0000", inCostomer = "None", inNumWorkingTNs = 0):
        super().__init__(inNPA, inNXX, inLine, inCostomer) # call parent __init__(...)
        #self.__numWorkingTNs = inNumWorkingTNs if inNumWorkingTNs < 1 else "No Billing TN"
        self.__numWorkingTNs = 0 ; self.setBilling(inNumWorkingTNs)
        print("In BillingTN Constructor")


    def load(self):
        super().load()
        self.__numWorkingTNs = input(int("Enter the amount of telephone accounts:"))
        while int(self.__numWorkingTNs) < 1:
            self.__numWorkingTNs = input("invalid -- please re-enter: ")

    def __del__(self):
        print("In BillingTN Constructor")
        super().__del__()

    def setBilling(self, newBilling):
        self.__numWorkingTNs = newBilling if newBilling < 1 else self.__numWorkingTNs

    def getBilling(self):
        return self.__numWorkingTNs

    def __str__(self):
        return super().__str__() + "\n" + str(self.__numWorkingTNs)

    def displayPhoneNumber(self):
        super().displayPhoneNumber()
        print("Number of working Telephone numbers is:", self.__numWorkingTNs)

if __name__ == '__main__':
    myBillingTN = BillingTN()
    print(" myWorkingTN =", myBillingTN)
    myBillingTN.displayPhoneNumber()
    myBillingTN = BillingTN("719", "598", "0200", "CTU", 0)
    print(" myWorkingTN =", myBillingTN)
    myBillingTN.displayPhoneNumber()