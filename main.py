# Command + Enter to run






































'''
Question1 - Factorial
Find the factorial of a number provided by the user.
'''

# 1. With a Loop
num = int(input("Enter a positive int: "))

factorial = 1

# check if the number is negative, positive or zero
if (num == 0):
	print ("The factorial of 0 is 1")
else:
	for i in range(1, num + 1):
		factorial = factorial * i
	print("The factorial of " + str(num) + " is " + str(factorial))

# 2. With a Recursive Function
def factorial(n):
	if (n == 0):
		return 1
	else:
		return n * factorial(n-1)

num = int(input("Enter a positive int: "))

print ("The factorial of " + str(num) + " is " + str(factorial(num)))


'''
Question2 - A Fibonacci sequence
The integer sequence of 0, 1, 1, 2, 3, 5, 8...
Program to print the fibonacci series upto n_terms
'''

# 1. With a Loop

# first two terms
n1, n2 = 0, 1
count = 0

nterms = int(input("How many terms? "))

# check if the number of terms is valid
if (nterms <= 0):
  print("Please enter a positive integer")
else:
	print("Fibonacci sequence:")

	while (count < nterms):
		print(n1)
		nth = n1 + n2

		# update values
		n1 = n2
		n2 = nth
		count += 1


# 2. With a Recursive function
def fibonacci(n):
  if (n <= 1):
    return n
  else:
    return(fibonacci(n-1) + fibonacci(n-2))

nterms = int(input("How many terms? "))

# check if the number of terms is valid
if (nterms <= 0):
  print("Please enter a positive integer")
else:
	print("Fibonacci sequence:")
	
	for i in range(nterms):
		print(fibonacci(i))



'''
def fun1(x, y) :
	if (x == 0) :
		return y
	else :
		return fun1(x - 1, x + y)

fun1(5,2) # 5 + 4 + 3 + 2 + 1 + 2 = 15 + 2 = 17
'''