from Register import Register
from Customer import CustomerTypes
class RegisterList(object):
    '''
    this class repesent the list of register present in the grocery
    '''
    def __init__(self,numberOfRegister) -> None:
        '''
        paramter:
            numberOfRegister
        return RegisterList Object
        '''
        self._registersList = [Register(i) for i in range(numberOfRegister)]
        self._numberOfRegisters=numberOfRegister
    def getNumberOfRegisters(self):
        return self._numberOfRegisters
    def registersCustomerCount(self):
        '''
        return the number of customers present in all registers
        '''
        count = sum([register.getNumberOfCustomer() for register in self._registersList])
        return count
    def updateRegisterCustomers(self,_customers):
        '''
        parameter:  
            _customers
        return None
            serve all the customer 
        '''
        for i in self._registersList:
            if len(i._customerList)==0:
                continue
            customer = i._customerList[0]
            
            if (i._registerNumber!=self._numberOfRegisters-1 and customer.getNumberOfItems() == 1) or customer.getNumberOfItems() == 0.5:
                _customers.remove(customer)
                i._customerList.remove(customer)
            else:
                if i._registerNumber == self._numberOfRegisters-1:
                    customer.setNumberOfItems(customer.getNumberOfItems()-0.5)
                else:
                    customer.setNumberOfItems(customer.getNumberOfItems()-1)

    def getRegisterWithShortestLine(self):
        '''
        return:
            register with shortest number of customers
        '''
        register = self._registersList[0]
        for i in self._registersList:
            if i.getNumberOfCustomer() < register.getNumberOfCustomer():
                register = i
        return register

    def getRegisterForB(self):
        '''
        return:
            register who's last customer has smallest number of items
        '''
        register = self._registersList[0]
        for i in self._registersList:
            if i.getLastCustomerItems() < register.getLastCustomerItems():
                register = i
        return register

    def _assignCustomerToRegister(self,customers):
        '''
        paramter:  
            customer
        return None
            assign customer according to requiremnts
        '''
        if len(customers)==0:
            return
        register = self._registersList[0]
        for customer in customers:
            if customer.getTypeOfCustomer() == CustomerTypes.A:
                register = self.getRegisterWithShortestLine()
                register.addCustomer(customer)
            elif customer.getTypeOfCustomer() == CustomerTypes.B:
                register = self.getRegisterForB()
                register.addCustomer(customer)
        