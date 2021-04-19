#Three numbers are given. Print "yes" if you can take any two of them and get the third in total.

a = 13
b = 1
c = 14

if a + b == c:
    print("yes")
elif c + b == a:
    print("yes")
elif a + c == b:
    print("yes")
else:
    print("false")
