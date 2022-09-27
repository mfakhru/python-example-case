n = int(input("Enter a strictly positive integer: "))
steps = 0
while n != 1:
    if n % 2 == 0:
        n = n / 2
    elif n % 2 == 1: 
        n = (3*n) + 1
    steps += 1
    print(int(n))
    
print("steps:", steps)
