size = int(input("Enter a positive integer for the size of the square pattern: "))
if size <= 0:
    print("Please enter a positive integer.")
else:
    for i in range(size):
        for j in range(size):
            print("*", end=" ")
        print()