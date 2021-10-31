# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .

def insert(sample):
    _store = input(f'{sample}: ')
    return _store

def display(nameD,ageD,addressD):
    print(f'Hi, my name is {nameD}. I am {ageD} years old and I live in {addressD}.')

# Steps
#1 Input name
name = insert('Name')
#2 Input age
age = insert('Age')
#3 Input address
address = insert('Address')
#4 Display
display(name,age,address)







