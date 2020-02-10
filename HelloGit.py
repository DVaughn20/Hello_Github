# comment
print("Hello World!")
a = 6
b = 4
print(a+b)

#how to make a list
myList = [1, 2, 3]

#how to access elements of a list
print(myList[1])

d = 2
while d < 20:
  print(d)
  d += 2


#how to create a function
def sumFunction(a,b):
	return a + b

print(sumFunction(2, 20))

print("hello world")


#dictionary
#lookup{}



#three datatypes at input

#float
someFloat = float(input("Enter a float: "))
print("You entered float: " + str(someFloat))
print(f"you entered float: {someFloat}" )
#string
phrase = input ("Enter a String: ")
print("you said " + phrase)
print(f"you said {phrase}")
#int
someInt = float(input("Enter an int: "))
print("You entered int: " + str(someInt))
print(f"you entered int: {someInt}" )

print(f"Do Python inline, like this: {someFloat} * {someInt} = {someFloat} * {someInt}")