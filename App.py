print("Hello Word")

if 5 > 2:
    print("Five is greater than two")
if 6 < 10:
 print("six is less ten")

 x = 5
 y = ("hello word")
#  print (x)
#  print (y)


x = 5
y = ("hello woeld")
print(x)
print(y)


x = 5
y = "john"
print (type(x))
print(type(y))

x = "awesome"

def myfunc():
    print("python is " + x)

myfunc ()

x = "awesome"

def myfunc():
    x = "fantastic"
    print("python is " + x)

# myfunc()
print("python is " + x)


course = "python programming"
print(len(course))
print(course[1])


fisrt = "olarewaju"
last = "olalekan"
full = fisrt + " " + last
print(full)

course = "python programming"
print(course.upper())
print(course.lower())
print(course.title())

def my_area(l, b):
    # # global x
    # x = "Good morning everyone. Python language is sweet"
    # print(x)

    area = l * b
    # print(area)
    return area
# area()

def volume():
    h = 3
    area = my_area(5, 8)
    volume = area * h
    return volume

def basket_volume():
    h = 3
    area = my_area(4, 2)
    volume = area * h
    return volume
print(volume())
print(basket_volume())
# print("python is " + x)


fisrt = "olarewaju"
last = "olalekan"
full = fisrt + " " + last
print(full)

fisrt = "olarewaju"
last = "olalekan"
full = f"{fisrt} {last}"
print(full)


course = "python programming"
print(course.upper())
print(course.lower())

course = "python programming"
print(len(course))
print(course[0])

temperture = 25
if temperture > 30:
    print("it hot")
    print("it cold")
print("done")


age = 17
message = "eligible" if age >= 18 else "not eligible"
print(message)


age = 22
if age >= 15:
    message = "eligible"
else:
    message = "not eligible"
print(message)


age = 12
message ="eligible" if age >=15 else "not eligible"
print(message)

high_income = True
good_create =True
if high_income and good_create:
    print("eligible")

high_income = False
good_create =True
if high_income and good_create:
    print("eligible")
else:
    print("not eligible") 


age = 36
txt = "my name is ola, i am " + age 
print(txt)

age = 36
txt = f"my name is ola i am {36}"
print(txt)


price = 59
txt = f"the price is {price: .2f} dollars"
print(txt)

print(10 > 9)

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")


class myclass():
    def __len__(self):
     return 0
myobj = myclass
print(bool(myobj))


def myfunction():
   return True
print(myfunction())

today_practic:

def myfunction():
    print("myfunction")
myfunction()


def myfunction():
    print("myfunction")
myfunction()
myfunction()
myfunction()

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)



def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))


def get_greeting():
    return("hello from a functon")

message = get_greeting()
print(message)

def my_function(fname):
    print(fname + " refsnes")

my_function("Email")
my_function("tobias")
my_function("linus")

def my_function(name):
    print("hello" , name)
my_function("Email")   


def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Email", "refsnes")    











