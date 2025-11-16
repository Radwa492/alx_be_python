size = int(input("Enter a positive integer for the size of the square pattern: "))
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()