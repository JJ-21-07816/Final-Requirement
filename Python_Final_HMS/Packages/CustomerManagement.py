class Customer:
    def __init__(self, customerId, firstName, lastName, email, phone):
        self.customerId = customerId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
    
    def values(self):
        return ("{:<40} {:<40} {:<40} {:<40} {:<40}".format(self.customerId, self.firstName, self.lastName, self.email, self.phone))

def printCustomerMenu():
    print('[1] CREATE AN ACCOUNT FOR CUSTOMER')
    print('[2] SEARCH A CUSTOMER TO VIEW DATA')
    print('[3] UPDATE A CUSTOMER DATA')
    print('[4] DELETE A CUSTOMER ACCOUNT')
    print('[5] DISPLAY ALL CUSTOMERS DATA')
    print('[X] EXIT')

# CREATE CUSTOMER
def CreateCustomer():
    print("\n<======| CREATE ACCOUNT FOR CUSTOMER |======>")
    print("Please fill up the following credentials.")
    try:
        customerIdExists = False
        customerId = int(input('Customer ID: '))

        with open("CustomerRecord.txt", "r") as fp:
            lines = fp.readlines()
            for n in range(len(lines)):
                if str(customerId) in lines[n].split():
                    print('\n|===========> Invalid! | Customer ID already exists! <===========|\n')
                    customerIdExists = True
                    break
                
        if not customerIdExists:
            firstName = input('Firstname: ')
            lastName = input('Lastname: ')
            email = input('Email: ')
            phone = input('Phone #: ')
            customer = Customer(customerId, firstName, lastName, email, phone)
            with open("CustomerRecord.txt", "a") as myfile:
                myfile.write("\n")
                myfile.write(customer.values())

            print('\n|===========> Customer Created Successfully! <===========|\n')

    except ValueError:
        print("\nInvalid input!\nPlease Try Again!\n")


# SEARCH CUSTOMER
def SearchCustomer():
    print("\n<======| SEARCH A CUSTOMER TO VIEW DATA |======>")
    choice = input("How do you want to search a customer?\nPlease search by.\n\n[1] Lastname\n[2] Customer ID #\n\nEnter your Choice: ")
    isFound = False
    foundCustomers = [];
    if choice == '1':
        lastname = input('Enter lastname: ')
        with open("CustomerRecord.txt", "r") as fp:
            lines = fp.readlines()
            for n in range(len(lines)):
                if lastname == lines[n].split()[2]:
                    isFound = True
                    foundCustomers.append(lines[n].split())
            if isFound:
                print('\n|===========> Customer Record Found! <===========|')
                print("{:<25} {:<25} {:<25} {:<25} {:<25}".format("CUSTOMER ID", "FIRSTNAME", "LASTNAME", "EMAIL", "PHONE #"))
                for i in range(len(foundCustomers)):
                    print("{:<25} {:<25} {:<25} {:<25} {:<25}".format(foundCustomers[i][0],foundCustomers[i][1],foundCustomers[i][2],foundCustomers[i][3],foundCustomers[i][4]))
                print("")
                foundCustomers.clear()
            else:
                print("\n|===========> Customer doesn't exist! <===========|\n")

    elif choice == '2':
        customerId = input('Enter Customer ID: ')
        with open("CustomerRecord.txt", "r") as fp:
            lines = fp.readlines()
            for n in range(len(lines)):
                if customerId == lines[n].split()[0]:
                    isFound = True
                    foundCustomers.append(lines[n].split())
            if isFound:
                print('\n|===========> Customer Record Found! <===========|')
                print('Customer Record Found!\n')
                print("{:<25} {:<25} {:<25} {:<25} {:<25}".format("CUSTOMER ID", "FIRSTNAME", "LASTNAME", "EMAIL", "PHONE #"))
                for i in range(len(foundCustomers)):
                    print("{:<25} {:<25} {:<25} {:<25} {:<25}".format(foundCustomers[i][0],foundCustomers[i][1],foundCustomers[i][2],foundCustomers[i][3],foundCustomers[i][4]))
                foundCustomers.clear()
                print("")
            else:
                print("\n|===========> Customer doesn't exist! <===========|\n")
    
    else:
        print('\nInvalid input!\nPlease Try Again Later!\n')


# UPDATE CUSTOMER
def UpdateCustomer():
    print("\n<======| UPDATE A CUSTOMER DATA |======>")
    customerId = input("Enter Customer ID: ")
    isFound = False
    with open("CustomerRecord.txt", "r") as fp:
        lines = fp.readlines()
        for n in range(len(lines)):
            record = lines[n].split()
            if len(record) != 0:
                if customerId == record[0]:
                    isFound = True
                
                    while True:
                        isUnique = True
                        print('\nPlease fill up the following credentials.')
                        newCusId = input("Enter New Customer ID: ")
                        for customerRecords in lines:
                            record2 = customerRecords.split()
                            if len(record2) != 0:

                                if newCusId == customerId or newCusId == record2[0]:
                                    print('\n|===========> Customer ID already exists! Please enter a unique Customer ID! <===========|')
                                    isUnique = False
                                    break
                        if isUnique:
                            break
                    newFirstName = input("Enter New Firstname: ")
                    newLastName = input("Enter New Lastname: ")
                    newEmail = input("Enter New Email: ")
                    newPhone = input("Enter New Phone #: ")
                    newRecord = [newCusId, newFirstName, newLastName, newEmail, newPhone]                   
                    for i in range(len(newRecord)):
                        if newRecord[i] == "":
                            newRecord[i] = record[i]
                
                    customer = Customer(newRecord[0], newRecord[1], newRecord[2], newRecord[3], newRecord[4])
                    lines[n] = customer.values().strip() + "\n"
                    break

        with open("CustomerRecord.txt", "w") as fp:
            for line in lines:
                fp.write(line.lstrip())        
        fp.close

        if not isFound:
            print("\n|===========> Customer doesn't exist! <===========|\n")
        else:
            print('\n|===========> Customer Updated Successfully! <===========|\n')


# DELETE CUSTOMER


def my_sort(line):
    line_fields = line.strip().split()
    id = int(line_fields[0])
    return id

# DISPLAY ALL CUSTOMERS
def DisplayAllCustomer():
    print("\n<======| DISPLAY ALL CUSTOMER DATA |======>")
    with open("CustomerRecord.txt", "r") as fp:
        fp.readline()
        print("{:<25} {:<25} {:<25} {:<25} {:<25}".format("Customer ID", "Firstname", "Lastname", "Email", "Phone #"))
        lines = fp.readlines()
        lines.sort(key=my_sort)
        for line in lines:
            print("{:<25} {:<25} {:<25} {:<25} {:<25}".format(line.split()[0],line.split()[1],line.split()[2],line.split()[3],line.split()[4]))
        print("")
