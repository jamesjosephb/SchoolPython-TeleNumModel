##########################################################
#   CS217:      telephoneNumber
#   Assignment: Lab5
#   Author:     James Burch
#   Date:       11/29/2016
#   Filename:   telephoneNumber.py
#   Purpose:
#
##########################################################
# python model of a basic telephone number containing area code , prefix and lone componennts
# imports

class TelephoneNumber:
    def __init__(self, inNPA = "000", inNXX = "000", inLine = "0000"):
        self.__NPA = inNPA if len(inNPA) == 3 else "000"
        self.__NXX = inNXX if len(inNXX) == 3 else "000"
        self.__Line = inLine if len(inLine) == 4 else "0000"
        print("In Telephone Constructor")


    def load(self):
        self.__NPA = input("Enter the phone numbers NPA (3 digit Area Code): ")
        while len(self.__NPA) != 3:
            self.__NPA = input("Invalid input, please enter a NPA number (3 digit Area Code): ")

        self.__NXX = input("Enter the phone numbe's 3-digit prefix")
        while len(self.__NXX) != 3:
            self.__NXX = input("Invalid input, please enter a NXX number (3 digits after area code): ")

        self.__Line = input("Enter the phone numbe's 4 digit line number")
        while len(self.__Line) != 4:
            self.__Line = input("Invalid input, please enter the 4 digit line (Last for digits of phone number): ")



    def __del__(self):
        print("In TelephoneNumber Destructor")


    def setNPA(self, newNPA):
        self.__NPA = newNPA if len(newNPA) == 3 else "000"
    def setNXX(self, newNXX):
        self.__NXX = newNXX if len(newNXX) == 3 else "000"
    def setLine(self, newLine):
        self.__Line = newLine if len(newLine) == 4 else "0000"

    def getNPA(self):
        return self.__NPA
    def getNXX(self):
        return self.__NXX
    def getLine(self):
        return self.__Line

    def __str__(self):
        return '(' + self.__NPA + ')' + self.__NXX + '-' + self.__Line

    def displayPhoneNumber(self):
        print("Telephone Number is: ",  self.__NPA + '-' + self.__NXX + '-' + self.__Line)


if __name__ == '__main__':
    myPhoneNum = TelephoneNumber()
    myPhoneNum.displayPhoneNumber()
    print("myPhoneNum =",myPhoneNum )
    myPhoneNum.load()
    print("myPhoneNum =",myPhoneNum )
    myPhoneNum = None # This is not neccassary for the use of Pycharm
