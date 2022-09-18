
from GroceryStore import GroceryStore
from utility import readFileContent
import sys


def main():
    filename = sys.argv[1]
    numberOfRegisters, customers = readFileContent(fileName=filename)
    grocery = GroceryStore(numberOfRegister=numberOfRegisters, customerList=customers)
    grocery.startSimulation()
    print('Finished at: t='+str(grocery.getTotalTime())+' minutes')

if __name__ == "__main__":
    main()

