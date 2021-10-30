# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def amountApples():
    _amountApples = input("How many apples do you want to buy?: ")
    return _amountApples

def amountOranges():
    _amountOranges = input(" How many oranges do you want to buy?: ")
    return _amountOranges
    
def priceFormula(amountApples,amountOranges):
    _priceFormula = amountApples * 20 + amountOranges * 25
    return _priceFormula

# Steps
# Ask how many apples you want to buy?
amountApples1 = amountApples()
# Ask how many oranges you want to buy?
amountOranges1 = amountOranges()
# Insert Formula for Computation
priceFormula(amountApples1,amountOranges1)
# Display