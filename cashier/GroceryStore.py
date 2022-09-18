

from RegisterList import RegisterList
class GroceryStore(object):
    '''
    Represent the grocery object
    '''
    def __init__(self,numberOfRegister,customerList) -> None:
        '''
        Paramter:
            numberOfRegister,customerList
        return Grocery Object
        '''
        self._numberOfRegisters = numberOfRegister
        self._customers = customerList
        self._registerList = RegisterList(numberOfRegister)
        self._totalTime = 0
    
    def _getSameTimeCustomers(self,time):
        '''
        paramter:
            time
        return:
            list of customers with same time
        '''
        sameTimeCustomers = []
        for customer in self._customers:
            if customer.getArrivalTime()==time:
                sameTimeCustomers.append(customer)
                
        return sameTimeCustomers
 
    def startSimulation(self):
        '''
        smiluate the service
        '''
        self._totalTime = 1
        while len(self._customers)!=0 or self._registerList.registersCustomerCount()!=0:
            sameTimeCustomers = self._getSameTimeCustomers(self._totalTime)
            sameTimeCustomers.sort(key=lambda customer:customer.getNumberOfItems(),reverse=False)
            self._registerList._assignCustomerToRegister(sameTimeCustomers)
            self._registerList.updateRegisterCustomers(self._customers)
            self._totalTime+=1
           

    def getTotalTime(self):
        return self._totalTime

        