from data.data import Person, AddPerson
from faker import Faker

faker_ru = Faker('ru_RU')
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
        department=faker_ru.job()
    )