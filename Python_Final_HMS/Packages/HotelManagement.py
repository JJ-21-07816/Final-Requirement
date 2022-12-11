class BookingClass:
    def __init__(self, customerId, bookingId, room, checkin, checkout):
        self.customerId = customerId
        self.bookingId = bookingId
        self.room = room
        self.checkin = checkin
        self.checkout = checkout
    
    def values(self):
        return ("{:<40} {:<40} {:<40} {:<40} {:<40}".format(self.customerId, self.bookingId, self.room, self.checkin, self.checkout))

class PaymentClass:
    def __init__(self, paymentId, bookingId, amount, pay, change):
        self.paymentId = paymentId
        self.bookingId = bookingId
        self.amount = amount
        self.pay = pay
        self.change = change
    
    def values(self):
        return ("{:<40} {:<40} {:<40} {:<40} {:<40}".format(self.paymentId, self.bookingId, self.amount, self.pay, self.change))

def printHotelMenu():
    print('[1] BOOKING')
    print('[2] ROOMS INFORMATION')
    print('[3] PAYMENT')
    print('[X] EXIT')

# BOOKING
def Booking():
    print("\n<======| BOOKING |======>")
    print("Please fill up the neccessary information.")
    try:
        bookingIdExists = False
        bookingId = int(input('Booking ID: '))
        with open("BookingRecord.txt", "r") as fp:
            lines = fp.readlines()
            for n in range(len(lines)):
                if str(bookingId) in lines[n].split():
                    bookingIdExists = True
                    break
                else:
                    bookingIdExists = False

        if bookingIdExists:
            print('\n|===========> Invalid! | Booking ID already exists! <===========|')
            Booking()
        
        isFound = False
        customerId = input('Customer ID: ')
        with open("CustomerRecord.txt", "r") as fp:
            lines = fp.readlines()
            for n in range(len(lines)):
                if customerId == lines[n].split()[0]:
                    isFound = True
                    break
                else:
                    isFound = False
        
        if not isFound:
            print("\n|===========> Customer doesn't exist! <===========|")
            Booking()


        if isFound and not bookingIdExists:
            print("\n|===> PLEASE SELECT ROOM <===|")
            print("[1] STANDARD")
            print("[2] ELITE")
            print("[3] MANAGERIAL")
            print("[4] VIP")
            print("[5] SUITE\n")
            c = input('Room: ')
            if(c == "1"):
                room = "STANDARD"
            elif(c == "2"):
                room = "ELITE"
            elif(c == "3"):
                room = "MANGERIAL"
            elif(c == "4"):
                room = "VIP"
            elif(c == "5"):
                room = "SUITE"
            else:
                print('\nInvalid input!\nPlease Try Again!\n')

            print("\n|===> PLEASE SELECT DATE FOR CHECK IN <===|")
            dayIn = int(input('Day: '))
            monthIn = int(input('Month: '))
            yearIn = int(input('Year: '))

            if(dayIn <= 31 and monthIn <= 12 and yearIn >= 2022):
                checkin = ("{}{}{}{}{}".format(dayIn, "/", monthIn, "/", yearIn))
            else:
                print("|===> Error, maybe because of one or more of this following situation! <===|")
                print("> Day should not be greater than 31.")
                print("> Month should not be greater than 12.")
                print("> Year should not be greater than 2022.\n")
                input('Press enter key to continue...')
                print('')
                Booking()


            print("\n|===> PLEASE SELECT DATE FOR CHECK OUT <===|")
            print("{}{}".format('Checked In Date: ', checkin, '\n'))
            dayOut = int(input('Day: '))
            monthOut = int(input('Month: '))
            yearOut = int(input('Year: '))

            if(dayOut <= 31 and monthOut <= 12 and yearOut >= 2022):
                if(dayOut > dayIn and monthOut >= monthIn and yearOut >= yearIn):
                    checkout = ("{}{}{}{}{}".format(dayOut, "/", monthOut, "/", yearOut))
                else:
                    print("|===> Check Out Date doesn't have to be Less than or Equal to Check In Date! <===|\n")
                    input('Press enter key to continue...')
                    print('')
                    Booking()
            else:
                print("|===> Error, maybe because of one or more of this following situation! <===|")
                print("> Day should not be greater than 31.")
                print("> Month should not be greater than 12.")
                print("> Year should not be less than 2022.\n")
                input('Press enter key to continue...')
                print('')
                Booking()

            booking = BookingClass(customerId, bookingId, room, checkin, checkout)
            with open("BookingRecord.txt", "a") as myfile:
                myfile.write("\n")
                myfile.write(booking.values())

            print('\n|===========> Booked Successfully! <===========|\n')

    except ValueError:
        print("\nInvalid input!\nPlease Try Again!\n")

# ROOM INFORMATION
def RoomInformation():
    print("\n<======| ROOMS INFORMATION |======>")
    print("")
    print("|===> STANDARD <===|")
    print("-----------------------------------------------------------------")
    print("ROOM AMENITIES INCLUDES: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water.")
    print("-----------------------------------------------------------------\n")

    print("|===> ELITE <===|")
    print("-----------------------------------------------------------------")
    print("ROOM AMENITIES INCLUDES: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water + Window/Split AC.")
    print("-----------------------------------------------------------------\n")

    print("|===> MANAGERIAL <===|")
    print("-----------------------------------------------------------------")
    print("ROOM AMENITIES INCLUDES: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water.")
    print("-----------------------------------------------------------------\n")

    print("|===> VIP <===|")
    print("-----------------------------------------------------------------")
    print("ROOM AMENITIES INCLUDES: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.")
    print("-----------------------------------------------------------------\n")

    print("|===> SUITE <===|")
    print("-----------------------------------------------------------------")
    print("ROOM AMENITIES INCLUDES: 2 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.")
    print("-----------------------------------------------------------------\n")


# PAYMENT
def Payment():
    print("\n<======| PAYMENT |======>")
    print("Payment Center.")
    try:
        paymentIdExists = False
        paymentId = int(input('Payment ID: '))
        with open("PaymentRecord.txt", "r") as fp:
            lines = fp.readlines()
            for n in range(len(lines)):
                if str(paymentId) in lines[n].split():
                    paymentIdExists = True
                    break
                else:
                    paymentIdExists = False

        if paymentIdExists:
            print('\n|===========> Invalid! | Payment ID already exists! <===========|')
            Payment()
        
        isFound = False
        bookingId = input('Booking ID: ')
        with open("BookingRecord.txt", "r") as fp:
            lines = fp.readlines()
            for n in range(len(lines)):
                if bookingId == lines[n].split()[1]:
                    isFound = True
                    break
                else:
                    isFound = False
        
        if not isFound:
            print("\n|===========> Booking doesn't exist! <===========|")
            Payment()


        if isFound and not paymentIdExists:
            print("\n|===> PLEASE SELECT ROOM YOU CHECKED IN <===|")
            print("[1] STANDARD ------ 2000")
            print("[2] ELITE --------- 3000")
            print("[3] MANAGERIAL ---- 4000")
            print("[4] VIP ----------- 6000")
            print("[5] SUITE --------- 8000\n")
            c = input('Room: ')
            if(c == "1"):
                amount = 2000
            elif(c == "2"):
                amount = 2000
            elif(c == "3"):
                amount = 4000
            elif(c == "4"):
                amount = 6000
            elif(c == "5"):
                amount = 8000
            else:
                print('\nInvalid input!\nPlease Try Again!\n')

            print("|===> PAYMENT CENTER <===|")
            pay = int(input('Enter Your Payment: '))

            if(amount > pay):
                print("\n|===> Sorry you do not have enough balance. <===|")
                print("|===> Please try again later. <===|\n")
                Payment()
            else:
                change = pay - amount
                print("{}{}".format('Updated Balance: ', change))

            payment = BookingClass(paymentId, bookingId, amount, pay, change)
            with open("PaymentRecord.txt", "a") as myfile:
                myfile.write("\n")
                myfile.write(payment.values())

            print('\n|===========> Payment Successfull! <===========|\n')

    except ValueError:
        print("\nInvalid input!\nPlease Try Again!\n")



















