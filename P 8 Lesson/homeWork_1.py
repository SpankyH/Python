# 1. Умножить все элементы в произвольном списке написав для этого функцию .


spis = [27,8,19,88]
product = spis[0]*spis[1]*spis[2]*spis[3]
print(product)


spis1 = [27,8,19,88]
product1 = 1
for i in spis1:
    product1 *= i
print(product1)


spis2 = [27,8,19,88]
a = spis2[0]
b = spis2[1]
c = spis2[2]
d = spis2[3]
def product2(a,b,c,d):
    print(a * b * c * d)   
product2(a,b,c,d)


spis3 = [27,8,19,88]
def product3(a,b,c,d):
    print(a * b * c * d)   
product3(spis3[0],spis3[1],spis3[2],spis3[3])

