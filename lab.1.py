n = int(input("Enter the number: "))
if n%2 == 0:
    r = 0
    t = n
    while t != 0:
        d = t%10
        r = d + r*10
        t //= 10
    if r == n:
        print("Number is Palindrome")
    else:
        print("Not a Palindrome")
else:
    f = 1
    for i in range(n,0,-1):
        f = f * i
    t = f
    c = 0
    while t != 0:
        c += 1
        t //= 10
    print("Number of digits in Factorial {} of a number {}".format(f,c))
    
