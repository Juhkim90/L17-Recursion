## Function

### Recursion
A defined function can call itself. It is a common mathematical and programming concept.
Every recursive function requires to have a parameter and a base condition.

### Formula:
```python
def functionName(parameter):
	if ():					# base condition
		return something
	else:
		return something
```

### Where can we apply?
Things that have many possible branches and are too complex for an iterative approach.
Recursion works well for searching through types of structure (data structure) because it can search multiple branching paths without having many checks/conditions.


## The main() Function
Many programming languages have a special function that is automatically executed when an operating system starts to run a program, usually called main().

Python interpreter executes script starting at the top of the file, and there is no specific function that python automatically executes.
____name____ is one such special variable. If the source file is executed as the main program, the interpreter sets the ____name____ variable to have a value ____main____

Even though it is not mandatory to use this function, it is a good practice to use this function as it improves the logical structure of the code.

### Formula
```
def main():
	BODY

if __name__ == "__main__":
	main()
```


### Example
```python
print ("Good Afternoon")

def add(n1,n2):
	return n1 + n2

def main():
	print ("Hello Python")
	print (add(3,4))


if __name__ == "__main__":
	main()

>>
Good Afternoon
Hello Python
7