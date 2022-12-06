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
