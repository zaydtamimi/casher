from Customer import Customer
def parseStringToCustomer(customerString):
    '''
    paramter:
        customerString
    return customerObject
        this methods covert the string of customer
        sperated by customer in to the customer object
    '''
    cust = customerString.split(' ')
    if len(cust) != 3:
        raise Exception('invalid customer!')
    try:
        cust[1] = int(cust[1])
        cust[2] = int(cust[2])
    except:
        raise Exception("invalid Customer!")
    return Customer(cust[0],cust[1],cust[2]) 

def readFileContent(fileName):
    '''
    paramter:
        fileName
    return:
        it return tuple (numberOFRegisters,list of customers)
    it read the given file and extract the useful information
    '''
    file = open(fileName)
    customers = []
    numberOfRegisters=0
    firstLineFlag = True
    for line in file:
        if firstLineFlag:
            try:
                numberOfRegisters = int(line)
                firstLineFlag = False
            except:
                raise Exception('invalid register number')
        else:
            
            customers.append(parseStringToCustomer(line))
    
    return (numberOfRegisters,customers)
