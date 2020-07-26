##########################################################
#   CS217:      Lab5
#   Assignment: Lab5
#   Author:     James Burch
#   Date:       11/29/2016
#   Filename:   telephoneNumber.py
#   Purpose:
#
##########################################################

#python model of a basic telephone number containing area code , prefix and lone componennts
from telephoneNumber import *
from WorkingTN import *
from BillingTN import *

def main():

    TestNumber = TelephoneNumber("719","590","6768")
    Paul = TelephoneNumber("719","590","6729")
    Bob = TelephoneNumber("719","590","6729")
    CSStaff1 = WorkingTN("719","590","6732","Book Store")
    CSStaff2 = WorkingTN("212","371","6940","Borland C++ Guru")
    CSStaff3 = WorkingTN("405","612","3433","Visual C++ Export")
    CSDept = BillingTN("719","590","6850","Dean of CS")
    Library = BillingTN("719","598","6708","Librarian")
    ReceptionDesk = BillingTN("719","598","0200","Reception",35)
    print("The Telephone numbers are: \n")
    TestNumber.displayPhoneNumber()
    Paul.displayPhoneNumber()
    Bob.displayPhoneNumber()
    print("\The Working Telephone numbers are: \n")
    CSStaff1.displayPhoneNumber()
    CSStaff2.displayPhoneNumber()
    CSStaff3.displayPhoneNumber()
    print("\nThe Billing Telephone numbers are: \n")
    CSDept.displayPhoneNumber()
    Library.displayPhoneNumber()
    ReceptionDesk.displayPhoneNumber()
    print("\nEnd of test of Telephone number hierarchy!")
    print("\nAttempting to force destructors to be executed")
    TestNumber = None
    Paul = None
    Bob = None
    CSStaff1= None
    CSStaff2 = None
    CSStaff3 = None
    CSDept= None
    Library= None
    ReceptionDesk= None

main()


'''
C:\Anaconda3\python.exe "E:/school/Python 3/Labs/Lab 5/Lab 5.py"
In Telephone Constructor
In Telephone Constructor
In Telephone Constructor
In Telephone Constructor
In WorkingTN Constructor
In Telephone Constructor
In WorkingTN Constructor
In Telephone Constructor
In WorkingTN Constructor
In Telephone Constructor
In WorkingTN Constructor
In BillingTN Constructor
In Telephone Constructor
In WorkingTN Constructor
In BillingTN Constructor
In Telephone Constructor
In WorkingTN Constructor
In BillingTN Constructor
The Telephone numbers are:

Telephone Number is:  719-590-6768
Telephone Number is:  719-590-6729
Telephone Number is:  719-590-6729
\The Working Telephone numbers are:

Telephone Number is:  719-590-6732
Customer is: Book Store
Telephone Number is:  212-371-6940
Customer is: Borland C++ Guru
Telephone Number is:  405-612-3433
Customer is: Visual C++ Export

The Billing Telephone numbers are:

Telephone Number is:  719-590-6850
Customer is: Dean of CS
Number of working Telephone numbers is: 0
Telephone Number is:  719-598-6708
Customer is: Librarian
Number of working Telephone numbers is: 0
Telephone Number is:  719-598-0200
Customer is: Reception
Number of working Telephone numbers is: 0

End of test of Telephone number hierarchy!

Attempting to force destructors to be executed
In TelephoneNumber Destructor
In TelephoneNumber Destructor
In TelephoneNumber Destructor
In WorkingTN Destructor
In TelephoneNumber Destructor
In WorkingTN Destructor
In TelephoneNumber Destructor
In WorkingTN Destructor
In TelephoneNumber Destructor
In BillingTN Constructor
In WorkingTN Destructor
In TelephoneNumber Destructor
In BillingTN Constructor
In WorkingTN Destructor
In TelephoneNumber Destructor
In BillingTN Constructor
In WorkingTN Destructor
In TelephoneNumber Destructor

Process finished with exit code 0
'''


