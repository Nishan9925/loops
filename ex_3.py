# Print "The number is Prime" (պարզ) if the number which saved in variable named P is  Prime and  The number is not
# Prime" not.

P = int(input("Enter the number: "))
if P > 1:
    for i in range(2, P - 1,2):
        a = P % i
        if a == 0:
            print("Your entered number",P, "is not prime")
            break
    else:
        print("Your entered number",P, "is prime")

