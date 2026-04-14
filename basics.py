#input statement takes string.
# ascii arts website

name = input("What is your name ? ")
print("Hello " + name)
print("length : "+ str(len(name)))

print("HELLO"[0]); 
# only prints the character at that position (string subscripting)
# -1 referes O , -2 refers L

# Integers
print(123)

# Large Integers
print(12_78_789)
# Computer will interpret as 1278789

# Float
print(56.87)

# Boolean
print(True)
print(False)

print(6/2) # is a float 2.0
print(6//2) # is a int 2
print(3**2) # 3^2 = 9

print(65.6658) # prints 65.6658
print(int(65.6658)) # prints 65
print(round(65.6658)) # prints 66

print(f"NUMBER : {56}") # f strings


# CONDITIONAL STATEMENTS
a = 56
b = 59
if (a>50 and b>50 and a!=56) :
    print("Okay 1")
    print("Okay 2")
else :
    print("Not okay")

# && is and
# || is or 
# !=
# indentation is necessary only the indented code lies under the if and else block
# if elif else 

# Changing to upper and lower cases 
name = "JAGrit"
name = name.lower()
print(name)
name = name.upper()
print(name)

# GENERATING RANDOM NUMBERS
import random
a = random.randint(1,100) # 1<= a <= 100 (integer value)
b = random.random() # 0<= b < 1 (floating value)
c = random.uniform(1,100) # 1<= a <= 100 (floating value)

# LISTS
fruits = ["apple", "banana", "orange", "mango"]
print(fruits[1]) # prints banana
fruits[0] = "grapes"
fruits.append("apple") # adds 1 item at the end of the list
fruits.extend(["watermelon", "papaya"]) # adds multiple items at the end of the list
# list.insert(i,x)
# list.remove(x)
# list.clear()
# list.pop([i])
# Lists can store multiple data types
# you can store a list inside a list

# LOOPS IN LISTS
for fruit in fruits:
    print(fruit)

# LOOPS IN RANGE
for i in range(0,10): # for(i=0 ; i<10 ; i++)
    print(i)
# for i in range(0,10,2): # for(i=0 ; i<10 ; i+=2)
#     print(i)

# FUNCTIONS
def f1():
    print("Hello")
    print("Bye")
f1()
