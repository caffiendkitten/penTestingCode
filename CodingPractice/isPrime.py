# !/user/bin/python3
# This program will check if a given number is prime or not and retrun "True" or "False" respectivly.

# A prime number is a natural number greater than 1, which is only divisible by 1 and itself. 
# Example prime numbers: 2 3 5 7 11 13 17 19 23

# If num % i == 0 then not a prime in range of 2 to num-1.
def isPrime(num):
    for i in range(2, num):
        if (num % i == 0):
            print("\nFalse.",i,"times",num//i,"is",num)
            return print(num, "is not a Prime Number.\n")
    return print("\nTrue.", num, "is a Prime Number.\n")



# If num is divisible by any number between 2 and n / 2, it is not prime
def isPrime2(num):
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            return print("\nFalse.", num, "is not a Prime Number.\n")
            break
    else:
        return print("\nTrue.", num, "is a Prime Number.\n")


# Optimized Method
# This is checked so that we can skip middle five numbers in below loop
def isPrime3(num):
    if (num % 2 == 0 or num % 3 == 0) : 
        return print("\nFalse.", num, "is not a Prime Number.\n")
    i = 5
    while(i * i <= num) : 
        if (num % i == 0 or num % (i + 2) == 0) : 
            return print("\nFalse.", num, "is not a Prime Number.\n")
        i = i + 6
    return print("\nTrue.", num, "is a Prime Number.\n")
 




def getRemainder(num, divisor):
    return (num - divisor * (num // divisor)) 

# Check without % operator
def isPrime4(num):
    for i in range(2, int(num/2)+1):
        if (getRemainder(num, i)) == 0:
            return print("\nFalse.", num, "is not a Prime Number.\n")
            break
    else:
        return print("\nTrue.", num, "is a Prime Number.\n")    









version = input("Please choose a persion of the prime number checker: ") 
version = int(version) # Given number



if (version == 1):
        val = input("Enter the number to check: ") 
        val = int(val) # Given number
        if (val <= 1):
            print("\nFalse. Value must be 2 or greater to be a Prime Number.\n")
        elif (val == 2):
            print("\nTrue. 2 is a Prime Number.\n")
        else:
            isPrime1(val)


elif (version == 2):
    val = input("Enter the number to check: ") 
    val = int(val) # Given number
    if (val <= 1):
        print("\nFalse. Value must be 2 or greater to be a Prime Number.\n")
    elif (val == 2):
        print("\nTrue. 2 is a Prime Number.\n")
    else:
        isPrime2(val)


elif (version == 3):
    val = input("Enter the number to check: ") 
    val = int(val) # Given number
    if (val <= 1):
        print("\nFalse. Value must be 2 or greater to be a Prime Number.\n")
    elif (val <= 3):
        print("\nTrue.", val, "is a Prime Number.\n")
    else:
        isPrime3(val)

if (version == 4):
    val = input("Enter the number to check: ") 
    val = int(val) # Given number
    if (val <= 1):
        print("\nFalse. Value must be 2 or greater to be a Prime Number.\n")
    elif (val == 2):
        print("\nTrue. 2 is a Prime Number.\n")
    else:
        isPrime4(val)

else:
    print ("error, unknown value")
print("End")