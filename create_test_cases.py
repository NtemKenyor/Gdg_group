import random

file = open("inputs/c.in", "w")

#Create Integer only test cases
""" n = 10
for x in range(n):
    row = []
    for y in range(n):
        row.append(random.randint(1, 5))
        #row.append(random.uniform(0.1, 10))
    file.write(" ".join(map(str, row)) + "\n") """


#create integer and float mixture
n = 1000
for x in range(n):
    row = []
    for y in range(n):
        row.append( round(random.uniform(0.1, 5), 2) )
        #row.append(random.uniform(0.1, 10))
    file.write(" ".join(map(str, row)) + "\n")