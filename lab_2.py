import random
import string 
import string.ascii_letters
import string.digits
#1. Open Python in command mode and type the following 3 programs. Which of the followings work?
  #What warning messages did you get for those that didn’t work?
  print hello world
  #Output: Traceback (most recent call last):
  # File "python", line 3
  #  print hello world
  #             ^
  #SyntaxError: Missing parentheses in call to 'print'

  print "hello world"
  #Output: Traceback (most recent call last):
  #  File "python", line 9
  #   print hello world
  #              ^
  #SyntaxError: Missing parentheses in call to 'print'

  print (“hello world”)
  #Output: Traceback (most recent call last):
  #  File "python", line 16
  #    print (“hello world”)
  #                ^
  #SyntaxError: invalid character in identifier

  print(‘hello world’)
  #Output: Traceback (most recent call last):
  #  File "python", line 22
  #    print(‘hello world’)
  #               ^
  #SyntaxError: invalid character in identifier
  # print(hello world)
  #Output: Traceback (most recent call last):
  #  File "python", line 28
  #    print(hello world)
  #                    ^
  #SyntaxError: invalid syntax

  #What do these lines do?

  print(“hello world”, end=”!!!”)
  #Output: Traceback (most recent call last):
  #   File "python", line 16
  #     print(“hello world”, end=”!!!”)
  #                ^
  # SyntaxError: invalid character in identifier

  print(“hello world”,"hello world")
  #Output: Traceback (most recent call last):
  #  File "python", line 22
  #   print(“hello world”,"hello world")
  #              ^
  #SyntaxError: invalid character in identifier

  print(“hello world”,"hello world")
  #Output: Traceback (most recent call last):
  #  File "python", line 48
  #    print(“hello world”,"hello world")
  #               ^
  #SyntaxError: invalid character in identifier

  print("hello world","hello world", sep="0")
  #Prints Successfully! sep is equal to a number or character value that will determine the the character that will go in between the two "hello world" strings
  #Output: hello world0hello world
  print("hello world"+"jack")
  #Prints successfully - strings are able to concatenate without declaring variable type
  #Output: hello worldjack

  #What does + do in a print statement?
  #A + sign in a print statement concatenates strings and adds floats or integers with each other prior to printing out this value

  #What are end and sep inside a print statement?
  #- sep is equal to a number or character value that will determine the the character that will go in between two srtings
  #- end is a string value that will be appended to the end of the value to be printed

#2. A computer program has many variables. Assuming that you need to write a program to calculate the tuition fees for the semester based on the number of units taken for the semester,
  #   What is a good variable name for storing the number of credits taken in Fall 2017? 
      #   credits_number = 6
  #What is bad variable name?
  #     Anything using a space, caramel case or beginning with a number is a bad variable name. 
  #What is a good but (unfortunately)  illegal variable name?  
      #   credits number would be a 'good' illegal variable name
#Please find the exact rule of legal variables
      #    -  Variables names must start with a letter or an underscore
      #    -  The remainder of your variable name may consist of letters, numbers and underscores
      #    -  Names Are Case Sensitive
#   Conventions: Avoid using the lowercase letter ‘l’, uppercase ‘O’, and uppercase ‘I’.

#3 Create a program that randomly creates a variable with 5 characters
  # Create a variable that contains all alphanumeric characters
random_variable = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(6)])
print(random_variable)

# Create another variable that contains only letters
random_letter_variable = ''.join([random.choice(string.ascii_letters) for n in xrange(6)])
print(random_letter_variable)




