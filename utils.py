from faker import Faker
import csv
import requests

def users(number: int = 100) -> str:
    fake = Faker()
    user_list=''
    for _ in range(number):
        user_list = user_list + fake.first_name() + ' ' + fake.free_email() + '<br>'

    return user_list