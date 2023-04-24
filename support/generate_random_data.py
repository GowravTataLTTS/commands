import random
import sys


first_name = ['Ayan', "Brad", "Chetan", "David", "Eswar"]
last_name = ["Reddy", "Smith", "Naidu", "Abbas", "Jenkovich"]
country = ['I', "U", "E", "F", "G"]
number = list(range(100000, 999999))

names = []

value = int(sys.argv[1])
for i in range(value):
    values = (random.choice(first_name) + " " + random.choice(last_name),
              random.choice(list(range(18, 61))),
              random.choice(country),
              random.choice(number),
              "Pending")

    names.append(values)

new = f'INSERT INTO public.customer_data  (name, age, country,number,status) VALUES {names};'
news = new.replace('[', '')
news = news.replace(']', '')
print(news)
