#!/usr/bin/env python3
from sys import argv, stdout
from shutil import copy
from random import choice, randint
from sqlite3 import connect
from faker import Faker

DB_IN = '/home/pft/restapi/point-of-sale/pos_bak.db'
DB_OUT = '/home/pft/restapi/point-of-sale/pos.db'
faker = Faker(['sv_SE'])
SEX = ['male', 'female']

def generate_customer():
    'Generates a customer using faker'
    sex = choice(SEX)
    name = faker.name_male() if sex == 'male' else faker.name_female()
    firstname, lastname = name.split(' ')
    age = randint(20, 60)
    street = faker.street_name()
    zip = faker.postcode()
    city = faker.city()
    email = faker.email()

    return (
        firstname,
        lastname,
        age,
        sex,
        street,
        zip,
        city,
        email,
    )

def main():
    'CLI Entrypoint'
    try:
        count = int(argv[1])
    except ValueError:
        print('Not a valid amount of customers')
        exit(1)
    except IndexError:
        print('No customer amount provided')
        exit(1)

    # Assure we run on a fresh database
    copy(DB_IN, DB_OUT)
    db = connect(DB_OUT)

    # Fill db with users
    print('Faking users, might take a while...grab a cup of coffee')
    for i in range(count):
        customer = generate_customer()
        sql = '''INSERT INTO Customers (Firstname, Lastname, Age, Sex, Street, Zip, City, Email) VALUES (?, ?, ?, ?, ?, ?, ?, ?);'''
        db.execute(sql, customer)
        stdout.write(f'\r{i + 1} / {count}')
        stdout.flush()

    db.commit()
    db.close()
    print('\nDone')

if __name__ == '__main__':
    main()
else:
    print('Database faker needs to be run as a main script')
    exit(1)
