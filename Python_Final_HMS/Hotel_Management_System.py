from Packages import CustomerManagement
from Packages import HotelManagement

def printManagement():
    print('[1] CUSTOMER MANAGEMENT')
    print('[2] HOTEL MANAGEMENT')
    print('[X] EXIT')

def welcome():
    print('')
    print('----------->   WELCOME   <-----------')
    print('-------    DREAM BIG HOTEL    -------')
    print('---->  Hotel Management System  <----')
    print('')

# PROGRAM START
welcome()

input('Press enter key to continue...')
print('')

select = ""
while (select != 'X' and select != 'x'):
    printManagement()
    select = input('\nEnter your choice: ')
    if select == '1':
        print('\n<=======| CUSTOMER MANAGEMENT |=======>\n')
        choice = ""
        while (choice != 'X' and choice != 'x'):
            CustomerManagement.printCustomerMenu()
            choice = input('\nEnter your choice: ')
            if choice == '1':
                CustomerManagement.CreateCustomer()
            elif choice == '2':
                CustomerManagement.SearchCustomer()
            elif choice == '3':
                CustomerManagement.UpdateCustomer()
            elif choice == '4':
                CustomerManagement.DeleteCustomer()
            elif choice == '5':
                CustomerManagement.DisplayAllCustomer()
            elif choice == 'X' or choice == 'x':
                welcome()
            else:
                print('\nInvalid input!\nPlease Try Again!\n')

    elif select == '2':
        print('\n<=======| HOTEL MANAGEMENT |=======>\n')
        choice = ""
        while (choice != 'X' and choice != 'x'):
            HotelManagement.printHotelMenu()
            choice = input('\nEnter your choice: ')
            if choice == '1':
                HotelManagement.Booking()
            elif choice == '2':
                HotelManagement.RoomInformation()
            elif choice == '3':
                HotelManagement.Restaurants()
            elif choice == '4':
                HotelManagement.Payment()
            elif choice == 'X' or choice == 'x':
                welcome()
            else:
                print('\nInvalid input!\nPlease Try Again!\n')

    elif select == 'X' or select == 'x':
        print('\n---------->   Thank You For Using Our Program!   <----------')
        print('---------------->     Have A Nice Day!     <----------------\n')
        
    else:
        print('\nInvalid input!\nPlease Try Again Later!\n')


