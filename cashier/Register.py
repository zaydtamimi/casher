
class Register(object):
    '''
    Represent the register
    '''
    def __init__(self,registerNumber) -> None:
        '''
        Register Constructor
        Parameter:
            registerNumber
        return:
            register object
        '''
        self._registerNumber = registerNumber
        self._customerList = []
    def getRegisterTotalItems(self):
        return sum([customer.getItems() for customer in self._customerList])
    def getRegisterCustomers(self):
        return len(self._customerList)
    def addCustomer(self,customer):
        self._customerList.append(customer)
    def getLastCustomerItems(self):
        '''
        return the item of last customer 
        '''
        if len(self._customerList)==0:
            return 0
        return self._customerList[-1].getNumberOfItems()
    def getNumberOfCustomer(self):
        return len(self._customerList)
        