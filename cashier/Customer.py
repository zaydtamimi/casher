import enum
class CustomerTypes(enum.Enum):
    '''
    Enum class which represent the customer types
    either A or B
    '''
    A = 1
    B = 2
    


class Customer(object):
    '''
    Represent the Customer 
    '''

    def __init__(self,typeOfCustomer,arrivalTime,numberOfItems):
        '''
        parameter:
            typeOfCustomer,arrivalTime,numberOfItems
        return:
            Customer object
        '''
        self._typeOfCustomer = CustomerTypes.A if typeOfCustomer == "A" else CustomerTypes.B
        self._arrivalTime = arrivalTime
        self._numberOfItems = numberOfItems

    def getTypeOfCustomer(self):
        return self._typeOfCustomer
    def setTypeOfCustomer(self,typeOfCustomer):
        self._typeOfCustomer = typeOfCustomer

    def getArrivalTime(self):
        return self._arrivalTime
    def setArrivalTime(self,arrivalTime):
        self._arrivalTime = arrivalTime
    
    def getNumberOfItems(self):
        return self._numberOfItems
    def setNumberOfItems(self,numberOfItems):
        self._numberOfItems = numberOfItems

