a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
x1 = (- b + (b**2 - 4*a*c)**(1/2))/2*a
x2 = (- b - (b**2 - 4*a*c)**(1/2))/2*a
x = x1, x2
print(x)
