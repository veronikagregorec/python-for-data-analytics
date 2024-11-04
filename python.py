# Data Types
x = True # or False

multiline = """
                lorem
                ipsum
                whatever
            """
print(multiline)

a = 'Hello world'
print(a[6])
print(a[2:5])
print(a[:])

ice_cream = ['a', 'b', 'c']
ice_cream.append('d')
ice_cream[0] = 'value'

x,y,z,f = ice_cream
print(x)
print(y)
print(z)
print(f)

nest_list = ['Vanilla', 3, ['Spoon', 'Fork'], True]
print(nest_list[2][1])

tuple = (1,2,3,2,1) # immutable
print(tuple[4])

set = {1,2,2,3,3,2,1}
print(set)

dictionary = {"firstname": "John",
              "lastname": "Doe",
              "age": 24,
              "fav ice cream" : ['vanilla', 'apple']
              }

dictionary['firstname'] = 'Anna'
print(dictionary)
print(dictionary['firstname'])
print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())
del dictionary['lastname']

scoopes = [1,2,3,4,5]
print(2 in scoopes)
print(6 not in scoopes)

# If Statement
if (25 < 10) or (1 < 3):
    print("Yes")
    if 10 > 5:
        print("Nestead if")
elif 25 < 30:
    print("Elif")
else:
    print("Not wok")

# For Loop
int = [1,2,3,4,5]

for i in int:
    if i <= 3:
        print(i + i)

ice_cream_dic = {"name":"Alex", "age": 35, "fav ice cream": ["Vanilla", "Choco"]}

for item in ice_cream_dic.values():
    print(item)

for key, value in ice_cream_dic.items():
    print(key, "->",  value)

flavors = ["Vanilla", "Choco", "Cookie"]
toppings = ["Hot Fudge", "Oreos", "Marshmellows"]

for one in flavors:
    for two in toppings:
        print(one, two)

# While Loop
number = 1
while number < 10:
    print(number)
    if number == 5:
        break
    number = number + 1

number = 0
while number < 5:
    print(number)
    if number == 6:
        break
    number = number + 1
else:
    print("No loneger")

# Functions
def my_func(a,b):
    return a**b

print(my_func(8,2))

def number_arg(*args):
    return args

print(number_arg(9,8,7))

def number_kwarg(**kwarg):
    return kwarg

print(number_kwarg(integer =2039, number = 1050))

# Converting Data Types
num_str = '7'
print(type(num_str))

num_str_conv = int(num_str)
print(type(num_str_conv))

list_type = [1,2,3,3]
print(type(list_type))

print(tuple(list_type))
print(set(list_type))

long_str = "I like to learning"
print(list(long_str))

dict_type = {"name": "John", "age": "35"}
print(list(dict_type.values()))
print(list(dict_type.keys()))

# Input
weight = int(input("Enter your weight: "))
print(weight)
height = int(input("Enter your height: "))
print(height)

# Web Scraping
from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')
print(soup)

soup.find_all('div')[0]
soup.find('p', class_ ='lead').text.strip() #strip = no spaces