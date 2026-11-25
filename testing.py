def getData(userid):
    age = 12

    if age >= 18:
     userid = "1234"
     print("User is an adult.")
    else:
     userid = "5678"
     print("User is not an adult.") 

    return fetchUserInfo(userid)

def fetchUserInfo(user_id):
    # Simulate fetching user info from a database or API
    return {"user_id": user_id, "name": "John Doe", "email": "john.doe@example.com"}


name = "John"
age = 25
salary = 45000.50
is_active = False

print(name)
print(age)
print(salary)
print(is_active)

print(type(name))
print(type(age))
print(type(salary))
print(type(is_active))

"""""
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Your name is:", name)
print("Your age is:", age)

a = 10
b = 20

print(a == b)  # Equal
print(a != b)  # Not equal
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater or equal
print(a <= b)  # Less or equal
"""

names = ["John", "David", "Alex"]
print(len(names))
for index,name in enumerate(names):
    print(index, name)

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)


colors = ("Red", "Green", "Blue")

print(colors[0])
print(colors[1])
print(len(colors))

print(getData("1234"))