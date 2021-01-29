# dvdCollection = []
# print(dvdCollection)


# avengersDVD = ['The Avengers', 2012, 'Joss Whedon']
# dvdCollection.append(avengersDVD)

# incrediblesDVD = ['The Incredibales', 2004, 'Brad Bird']
# findingDoryDVD = ['Finding Dory', 2016, 'Andrew Stanton']
# lionKingDVD = ['The Lion King', 2019, 'Jon Favreau']

# dvdCollection.append(incrediblesDVD)
# dvdCollection.append(findingDoryDVD)
# dvdCollection.append(lionKingDVD)

# print(dvdCollection[0])
# print(dvdCollection[1])
# print(dvdCollection[2])
# print(dvdCollection[3])

# dvdCollection[3] = ['Star Wars', 1977, 'George Lucas']

# print(dvdCollection[3])

# squareNumbers = []
# a = 1

# while a < 20:
#     square = a * a 
#     a += 1
#     squareNumbers.append(square)


# for i in range(10):
#     print(squareNumbers[i]
################################################

#pre-alllocation 
import random

x = random.randint(1,100)

b = random.randint(1,x)

squareNumbers = [None] * x

array = 0
squareint = 1
i = 1
while i < b:
    squareint = i*i
    i += 1
    squareNumbers[i-2] = squareint


for a in squareNumbers:
    if a != None:
        array += 1

capacity = len(squareNumbers)
print('The capacity of this list is : ' + str(capacity))
print(f'There are {array} numbers in the list !') 






