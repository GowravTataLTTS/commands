import random

first_name = ['Ayan', "Brad", "Chetan", "David", "Eswar"]
last_name = ["Reddy", "Smith", "Naidu", "Abbas", "Jenkovich"]
country = ['IND', "US"]

names = []

for i in range(5):
    values = (random.choice(first_name) + " " + random.choice(last_name),
              random.choice(list(range(18, 61))),
              random.choice(country))
    names.append(values)

print(f'INSERT INTO customers  (name, age, country) VALUES {names}')
# print(names)