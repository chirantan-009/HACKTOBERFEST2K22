# Program to display the Fibonacci sequence up to n-th term

terms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0
if terms <= 0:
    print("Please enter a positive integer")

elif terms == 1:
    print("Fibonacci sequence upto", terms, ":")
    print(n1)

else:
    print("Fibonacci sequence:")
    while count < terms:
        print(n1)
        n = n1 + n2
        # update values
        n1 = n2
        n2 = n
        count += 1