from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
count_of_passwords = int(input('Укажите количество паролей для генерации: '))
length_of_passwords = int(input('Укажите длинну пароля: '))
in_digits = input('Включать ли цифры? (да/нет): ' )
in_uppercase = input('Включать ли прописные буквы? (да/нет): ')
in_lowercase = input('Включать ли строчные буквы? (да/нет): ')
in_punctuation = input('Включать ли символы? (да/нет): ')
in_ambiguous = input('Включать ли неодносзначные символы "il1Lo0O"? (да/нет):')
if in_digits == 'да':
    chars += digits
if in_uppercase == 'да':
    chars += uppercase_letters
if in_lowercase == 'да':
    chars += lowercase_letters
if in_punctuation == 'да':
    chars += punctuation
if in_ambiguous == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += choice(chars)
    return password

for _ in range(count_of_passwords):
    print(generate_password(length_of_passwords, chars))