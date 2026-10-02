from dataclasses import dataclass


@dataclass
class Person:
    full_name : str = None
    email : str = None
    current_address : str = None
    permanent_address : str = None



@dataclass
class AddPerson:
    first_name: str = None
    last_name : str = None
    email : str = None
    age: int = None
    salary: int = None
    department : str = None
    mobile : int = None
    data: int = None
    current_address : str = None
    birth_date: int = None


@dataclass
class Color:
    color_name : list = None


@dataclass
class Date:
    day : str = None
    month : str = None
    year : str = None
