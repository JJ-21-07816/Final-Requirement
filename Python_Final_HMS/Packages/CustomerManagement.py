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



# UPDATE CUSTOMER



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
