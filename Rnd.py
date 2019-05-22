import numpy

List = []
Order = []

for i in range(1,151):
    List.append(i)

up = 150
while List:
    Order.append(List.pop(numpy.random.randint(0,up)))
    up -= 1

f = open("Order.txt","w")
f.write(str(Order))
f.close()
