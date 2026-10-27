
import random
from datetime import time

from data.data import Person, AddPerson, Color, Date, SelectValue, SelectOne, FourColor
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('EN')
Faker.seed()

def generated_person():
    yield Person (
        full_name= faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email= faker_ru.email(),
        current_address= faker_ru.address(),
        permanent_address= faker_ru.address()
    )

def generator_new_person():
    yield AddPerson(
        first_name= faker_ru.first_name(),
        last_name= faker_ru.last_name(),
        email = faker_ru.email(),
        age = faker_ru.random_int(min=1, max=90),
        salary = faker_ru.random_int(min=1000),
        department=faker_ru.job(),
        mobile = faker_ru.random_int(min=1111111111, max=9999999999),
        current_address= faker_ru.address(),
    )

def generated_file():
    path = rf'C:\Users\belmas\PycharmProjects\automation_qa_course\filetest{random.randint(10, 100)}.txt'
    file = open(path, 'w+')
    file.write(f'Hellow, hi, привет {random.randint(1, 10000)}')
    file.close()
    return file.name, path



def generated_color():
    yield Color(
        color_name = ["Red","Blue","Green","Yellow","Purple","Black","White","Voilet","Indigo","Magenta","Aqua"]
    )


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month(),
        day=faker_en.day_of_month()

    )

def generated_time():
    steps_per_day = 24 * 4
    step = random.randint(0, steps_per_day - 1)
    total_minutes = step * 15
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours:02d}:{minutes:02d}"


def generated_value():
    yield SelectValue(
        value = ["Group 1, option 1", "Group 1, option 2", "Group 2, option 1", "Group 2, option 2", "A root option", "Another root option"]
    )


def generated_one_value():
    yield SelectOne(
        one_value= ["Dr.", "Mr.", "Mrs.", "Ms.", "Prof.", "Other"]
    )


def generated_four_color():
    yield FourColor(
        color_name=["Red","Blue","Green", "Black"]
    )