from faker import Faker
import random
import string

fake = Faker()

# Генерация email
def create_random_email():
    cohort_number = random.randint(1, 99)  # Генерация случайного номера когорты от 1 до 99
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    domains = ['yandex.ru', 'mail.ru', 'google.com']
    random_digits = f"{random.randint(100, 999)}"
    random_domain = random.choice(domains)
    random_email = f'{first_name}_{last_name}_{cohort_number}_{random_digits}@{random_domain}'
    return random_email

# Генерация пароля
def create_random_password():
    random_letters = ''.join(random.choices(string.ascii_letters, k=2))
    random_digits = random.randint(10, 99)
    random_password = f'qwerty_{random_letters}_{random_digits}'
    return random_password

def create_email_base():
    cohort_number = random.randint(1, 99)
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    random_digits = f"{random.randint(100, 999)}"
    random_domain = random.choice(['yandex.ru', 'mail.ru', 'google.com'])
    email_base = f'{first_name}_{last_name}_{cohort_number}_{random_digits}@{random_domain}'
    return email_base