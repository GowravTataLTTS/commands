import csv
import random
import string
import datetime
import names
from random import choice

# Function to generate dummy data
def generate_dummy_data():
    # List of possible countries
    countries = ['USA', 'Canada', 'Germany', 'Mexico', 'Russia', 'France', 'Japan', 'China', 'Brazil']

    # Randomly choose a country
    country = random.choice(countries)

    # Generate a random phone number (10 digits)
    #phone_number = ''.join(random.choices(string.digits, k=10))
    phone_number = str(choice(list(range(1000000,99999999))))

    # Generate a random email address using the person's name and a random domain
    email = names.get_first_name().lower() + '.' + names.get_last_name().lower() + '@' + random.choice(
        ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com'])

    # Return a tuple with the generated data
    return (names.get_full_name(),  country, phone_number, email)


# Open a new CSV file for writing
csvfile = open('dummy_data.csv', 'w')

# Create a CSV writer object
csvwriter = csv.writer(csvfile)

# Write the first row (column headers)
csvwriter.writerow(['name', 'country', 'phone', 'email'])

# Generate 1 million dummy records and write to the file
for i in range(1000):
    data = generate_dummy_data()
    csvwriter.writerow(data)

# Close the file
csvfile.close()
