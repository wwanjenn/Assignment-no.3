# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

def totalAmount():
    _totalAmount = int(input("How much money do you have?: "))
    return _totalAmount
 
def priceApple():
    _priceApple = int(input("How much is an apple?: "))
    return _priceApple

def formulaTotalapple(totalCash1,costApple1):
    _totalApple = totalCash1 // costApple1
    return _totalApple

def formulaTotalchange(totalCash2,costApple2):
    _totalChange = totalCash2 % costApple2
    return _totalChange

def display(totalAppleD,totalChangeD):
    print(f'You can buy {totalAppleD} apples and your change is {totalChangeD} pesos.')
# Steps
#1 Input amount of money
totalCash = totalAmount()
#2 Input price of apple
costApple = priceApple()
#3 Formula for Total amount of apples
totalApple = formulaTotalapple(totalCash,costApple)
#4 Formula for Change
totalChange = formulaTotalchange(totalCash,costApple)
#5 Display
display(totalApple,totalChange)